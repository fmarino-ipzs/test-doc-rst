# Script to clean up old PR directories in the gh-pages branch.
# This script:
# 1. Gets a list of active (open) PRs using GitHub CLI
# 2. Scans the 'prs' directory for PR directories
# 3. Removes directories for PRs that are no longer active (closed/merged)


import os
import re
#import sys
import json
import shutil
import subprocess
from pathlib import Path


def run_command(command):
    """Run a shell command and return the output."""
    try:
        result = subprocess.run(
            command, 
            shell=True, 
            check=True, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE,
            universal_newlines=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error message: {e.stderr}")
        return None


def get_active_pr_numbers(repo=None):
    """Get list of active (open) PR numbers using GitHub CLI."""
    repo_option = f"--repo {repo}" if repo else ""
    command = f"gh pr list --state open --json number {repo_option}"
    
    output = run_command(command)
    if not output:
        print("Failed to get list of PRs. Make sure GitHub CLI is installed and authenticated.")
        return []
    
    try:
        prs_data = json.loads(output)
        return [pr['number'] for pr in prs_data]
    except json.JSONDecodeError:
        print(f"Failed to parse JSON output: {output}")
        return []


def extract_pr_number(pr_dir):
    """Extract PR number from directory name (e.g., 'pr12' -> 12)."""
    match = re.search(r'pr(\d+)', pr_dir)
    if match:
        return int(match.group(1))
    return None


def clean_old_pr_directories():
    """Main function to clean up old PR directories."""
    prs_dir = "prs"
    
    # Check if prs directory exists
    if not os.path.isdir(prs_dir):
        print(f"The '{prs_dir}' directory does not exist. Nothing to clean.")
        return
    
    # Get the GitHub repository from environment variable
    repo = os.environ.get('GITHUB_REPOSITORY')
    
    # Get list of active PR numbers
    print("Getting list of active PRs...")
    active_pr_numbers = get_active_pr_numbers(repo)
    print(f"Active PR numbers: {active_pr_numbers}")
    
    # Initialize counter for removed directories
    removed_count = 0
    
    # Check each PR directory
    try:
        pr_dirs = [d for d in os.listdir(prs_dir) if os.path.isdir(os.path.join(prs_dir, d))]
    except Exception as e:
        print(f"Error accessing {prs_dir} directory: {e}")
        return
    
    for pr_dir_name in pr_dirs:
        pr_full_path = os.path.join(prs_dir, pr_dir_name)
        
        # Skip if not a PR directory pattern
        if not pr_dir_name.startswith('pr'):
            continue
        
        # Extract PR number
        pr_num = extract_pr_number(pr_dir_name)
        if pr_num is None:
            print(f"Could not extract PR number from directory: {pr_dir_name}")
            continue
        
        # Check if PR is active
        if pr_num not in active_pr_numbers:
            print(f"PR #{pr_num} is not active, removing directory {pr_full_path}")
            
            try:
                # First try to delete any files to handle potential permission issues
                for root, dirs, files in os.walk(pr_full_path, topdown=False):
                    for file in files:
                        try:
                            os.remove(os.path.join(root, file))
                        except Exception as e:
                            print(f"Warning: Could not remove file {file}: {e}")
                
                # Then remove the directory
                shutil.rmtree(pr_full_path)
                
                # Verify removal
                if not os.path.exists(pr_full_path):
                    print(f"Successfully removed directory {pr_full_path}")
                    removed_count += 1
                else:
                    print(f"WARNING: Directory {pr_full_path} still exists after removal attempt!")
            except Exception as e:
                print(f"Error removing {pr_full_path}: {e}")
    
    print(f"Removed {removed_count} PR directories that were no longer active.")


if __name__ == "__main__":
    clean_old_pr_directories()