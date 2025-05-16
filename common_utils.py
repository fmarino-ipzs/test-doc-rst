"""
Common utilities for GitHub documentation scripts.
"""
import os
import subprocess
import json


def run_command(command):
    """Run a shell command and return the output.
    
    Args:
        command (str): Command to execute
        
    Returns:
        str or None: Command output if successful, None otherwise
    """
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


def get_github_repo():
    """Get the GitHub repository from environment variable.
    
    Returns:
        str or None: Repository name in format 'owner/repo' or None
    """
    return os.environ.get('GITHUB_REPOSITORY')


def get_pr_info(pr_num, fields="number,title", repo=None):
    """Get information about a specific PR.
    
    Args:
        pr_num (int or str): PR number
        fields (str): Comma-separated list of fields to retrieve
        repo (str, optional): Repository in format 'owner/repo'
        
    Returns:
        dict or None: PR information or None if retrieval failed
    """
    repo_option = f"--repo {repo}" if repo else ""
    command = f"gh pr view {pr_num} --json {fields} {repo_option}"
    
    output = run_command(command)
    if not output:
        return None
    
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        print(f"Failed to parse JSON output: {output}")
        return None


def get_active_pr_numbers(repo=None):
    """Get list of active (open) PR numbers using GitHub CLI.
    
    Args:
        repo (str, optional): Repository in format 'owner/repo'
        
    Returns:
        list: List of open PR numbers
    """
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
