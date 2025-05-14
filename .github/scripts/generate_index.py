import os
import re
from pathlib import Path
from datetime import datetime

def scan_directory(base_path='.'):
    """Scan the current directory structure and return a dictionary with the structure."""
    structure = {
        'versione-corrente': {
            'exists': False,
            'languages': {'it': False, 'en': False}
        },
        'prs': {},
        'releases': {}
    }
    
    # Check versione-corrente
    versione_corrente_path = os.path.join(base_path, "versione-corrente")
    if os.path.exists(versione_corrente_path):
        structure['versione-corrente']['exists'] = True
        
        # Check languages
        for lang in ['it', 'en']:
            lang_path = os.path.join(versione_corrente_path, lang)
            index_path = os.path.join(lang_path, "index.html")
            structure['versione-corrente']['languages'][lang] = os.path.exists(index_path)
    
    # Check PRs
    prs_path = os.path.join(base_path, "prs")
    if os.path.exists(prs_path):
        # Get all directories in prs_path
        try:
            pr_dirs = [d for d in os.listdir(prs_path) if os.path.isdir(os.path.join(prs_path, d))]
            
            for pr_dir in pr_dirs:
                pr_full_path = os.path.join(prs_path, pr_dir)
                languages = {}
                
                # Check languages
                for lang in ['it', 'en']:
                    lang_path = os.path.join(pr_full_path, lang)
                    index_path = os.path.join(lang_path, "index.html")
                    languages[lang] = os.path.exists(index_path)
                    
                # Only add to structure if at least one language has an index.html
                if languages['it'] or languages['en']:
                    structure['prs'][pr_dir] = {
                        'languages': languages
                    }
        except Exception as e:
            print(f"Error scanning PRs: {e}")
    
    # Check Releases
    releases_path = os.path.join(base_path, "releases")
    if os.path.exists(releases_path):
        # Get all directories in releases_path
        try:
            release_dirs = [d for d in os.listdir(releases_path) if os.path.isdir(os.path.join(releases_path, d))]
            
            for release_dir in release_dirs:
                release_full_path = os.path.join(releases_path, release_dir)
                languages = {}
                
                # Check languages
                for lang in ['it', 'en']:
                    lang_path = os.path.join(release_full_path, lang)
                    index_path = os.path.join(lang_path, "index.html")
                    languages[lang] = os.path.exists(index_path)
                    
                # Only add to structure if at least one language has an index.html
                if languages['it'] or languages['en']:
                    structure['releases'][release_dir] = {
                        'languages': languages
                    }
        except Exception as e:
            print(f"Error scanning releases: {e}")
    
    return structure

def generate_html(structure):
    """Generate HTML content based on the structure."""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Project Documentation</title>
<style>
    body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    }}
    h1 {{
    border-bottom: 1px solid #eaecef;
    padding-bottom: 10px;
    }}
    h2 {{
    margin-top: 24px;
    margin-bottom: 16px;
    font-size: 1.5em;
    }}
    .section {{
    margin-bottom: 30px;
    }}
    .language-link {{
    display: inline-block;
    margin-right: 15px;
    padding: 5px 10px;
    background: #f1f8ff;
    border-radius: 3px;
    text-decoration: none;
    color: #0366d6;
    }}
    .language-link:hover {{
    background: #ddeeff;
    }}
    .item {{
    margin: 10px 0;
    padding: 10px;
    background: #f6f8fa;
    border-radius: 3px;
    }}
    .item-title {{
    font-weight: bold;
    margin-bottom: 10px;
    }}
    .no-item {{
    color: #666;
    font-style: italic;
    }}
</style>
</head>
<body>
<h1>Project Documentation</h1>

<div class="section">
    <h2>Current Version</h2>
"""

    # Current Version section
    if structure['versione-corrente']['exists']:
        languages = structure['versione-corrente']['languages']
        if languages['it'] or languages['en']:
            html += '    <div class="item">\n'
            if languages['it']:
                html += '      <a class="language-link" href="versione-corrente/it/index.html">Italiano</a>\n'
            if languages['en']:
                html += '      <a class="language-link" href="versione-corrente/en/index.html">English</a>\n'
            html += '    </div>\n'
        else:
            html += '    <p class="no-item">No current version available</p>\n'
    else:
        html += '    <p class="no-item">No current version available</p>\n'

    # Releases section
    html += '''
</div>

<div class="section">
    <h2>Releases</h2>
'''
    if structure['releases']:
        
        releases = structure['releases'].keys()
        
        for release in releases:
            languages = structure['releases'][release]['languages']
            html += f'    <div class="item">\n'
            html += f'      <div class="item-title">{release}</div>\n'
            if languages['it']:
                html += f'      <a class="language-link" href="releases/{release}/it/index.html">Italiano</a>\n'
            if languages['en']:
                html += f'      <a class="language-link" href="releases/{release}/en/index.html">English</a>\n'
            html += '    </div>\n'
    else:
        html += '    <p class="no-item">No releases available</p>\n'

    # PRs section
    html += '''
</div>

<div class="section">
    <h2>Pull Requests</h2>
'''
    if structure['prs']:
        
        prs = structure['prs'].keys()
        
        for pr in prs:
            languages = structure['prs'][pr]['languages']
            html += f'    <div class="item">\n'
            html += f'      <div class="item-title">{pr}</div>\n'
            if languages['it']:
                html += f'      <a class="language-link" href="prs/{pr}/it/index.html">Italiano</a>\n'
            if languages['en']:
                html += f'      <a class="language-link" href="prs/{pr}/en/index.html">English</a>\n'
            html += '    </div>\n'
    else:
        html += '    <p class="no-item">No pull requests available</p>\n'

    # Footer
    current_date = datetime.now().strftime("%Y-%m-%d")
    html += f'''
</div>

<footer style="margin-top: 50px; color: #666; font-size: 0.9em; text-align: center; border-top: 1px solid #eaecef; padding-top: 20px;">
    Generated on {current_date} by automatic directory scan
</footer>
</body>
</html>
'''
    return html

def main():
    # Scan the current directory (we're in the root of gh-pages)
    structure = scan_directory()
    print("Directory structure found:")
    print(f"versione-corrente: {structure['versione-corrente']}")
    print(f"PRs: {len(structure['prs'])} found")
    print(f"Releases: {len(structure['releases'])} found")
    
    html_content = generate_html(structure)
    
    # Write the HTML to index.html
    with open("index.html", "w") as f:
        f.write(html_content)
    
    print("Generated index.html successfully!")

if __name__ == "__main__":
    main()