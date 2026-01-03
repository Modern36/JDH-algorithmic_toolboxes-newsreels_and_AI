#!/usr/bin/env python3
"""
Fix jupyterlab-citation-manager metadata in Jupyter notebooks.

This script processes a Jupyter notebook and updates the cell-level citation metadata
to match the citation tags in the markdown source. This is needed when the
jupyterlab-citation-manager plugin breaks and citations don't get proper metadata.

Usage:
    python fix_citations.py <notebook_path>
    python fix_citations.py article.ipynb

After running this script:
1. Open the notebook in JupyterLab
2. Use the citation-manager plugin to REFRESH the bibliography
3. This will sync the notebook-level Zotero items from your Zotero library
"""

import json
import re
import sys
from urllib.parse import unquote
from pathlib import Path
from subprocess import run


def fix_citation_metadata(notebook_path):
    """
    Fix citation metadata in a Jupyter notebook.

    Args:
        notebook_path: Path to the .ipynb file to fix

    Returns:
        Number of citations updated
    """
    notebook_path = Path(notebook_path)

    if not notebook_path.exists():
        print(f"Error: File not found: {notebook_path}")
        return 0

    # Read the notebook
    print(f"Reading notebook: {notebook_path}")
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # Track statistics
    cells_updated = 0
    citations_updated = 0

    # Process each cell
    for i, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'markdown':
            source = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']

            # Find all cite tags with their IDs and hrefs
            # Pattern matches: <cite id="xyz"><a href="#zotero%7C...">
            # Using \s+ to handle whitespace/newlines between <a and href
            cite_pattern = r'<cite id="([^"]+)"><a\s+href="#([^"]+)">'
            matches = re.findall(cite_pattern, source, re.DOTALL)

            if matches:
                cell_updated = False

                # Ensure metadata structure exists
                if 'metadata' not in cell:
                    cell['metadata'] = {}
                if 'citation-manager' not in cell['metadata']:
                    cell['metadata']['citation-manager'] = {}
                if 'citations' not in cell['metadata']['citation-manager']:
                    cell['metadata']['citation-manager']['citations'] = {}

                citations = cell['metadata']['citation-manager']['citations']

                # Process each citation found in the cell
                for cite_id, href in matches:
                    # Decode the URL-encoded Zotero ID
                    # Format: zotero%7C22783102%2FERJVIH9J
                    # Decodes to: zotero|22783102/ERJVIH9J
                    decoded_href = unquote(href)

                    # Extract the Zotero ID (part after 'zotero|')
                    if 'zotero|' in decoded_href:
                        zotero_id = decoded_href.split('zotero|')[1]

                        # Check if we need to update this citation
                        if cite_id not in citations or citations[cite_id] == []:
                            # Update the citation metadata
                            citations[cite_id] = [
                                {
                                    "id": zotero_id,
                                    "source": "zotero"
                                }
                            ]
                            citations_updated += 1
                            cell_updated = True
                            print(f"  Cell {i}: Fixed citation '{cite_id}' -> {zotero_id}")

                if cell_updated:
                    cells_updated += 1

    # Write the updated notebook
    print(f"\nWriting updated notebook...")
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)

    print(f"\n{'='*60}")
    print(f"✓ Successfully updated {notebook_path}")
    print(f"  - Cells updated: {cells_updated}")
    print(f"  - Citations fixed: {citations_updated}")
    print(f"{'='*60}")

    return citations_updated


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        print("\nError: Please provide a notebook path")
        print("Usage: python fix_citations.py <notebook_path>")
        sys.exit(1)

    notebook_path = sys.argv[1]
    citations_updated = fix_citation_metadata(notebook_path)

    if citations_updated > 0:
        print("\n" + "="*60)
        print("NEXT STEPS:")
        print("="*60)
        print("1. Open the notebook in JupyterLab")
        print("2. Use the citation-manager plugin to REFRESH/SYNC")
        print("3. This will update the bibliography with Zotero data")
        print("="*60)
    else:
        print("\nNo citations needed fixing - all metadata is already correct!")

    run([
        'jupyter', 'nbconvert', '--ClearMetadataPreprocessor.enabled=True', '--inplace', notebook_path])

if __name__ == '__main__':
    main()
