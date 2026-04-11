import json
import subprocess
import sys
from pathlib import Path

def add_submodules():
    """
    Reads a JSON file with repository information and adds them as Git submodules.
    Supports optional 'ref' field to checkout specific branches/tags after adding.
    
    Example repos.json:
    {
        "repositories": [
            {
                "url": "https://github.com/django/django.git",
                "path": "data/repos/django-old",
                "ref": "v1.11"  # Optional: checkout this tag/branch
            }
        ]
    }
    """
    # The script is in 'scripts/', so the root is one level up.
    repo_root = Path(__file__).resolve().parents[1]
    repos_file = repo_root / "data" / "repos.json"

    if not repos_file.exists():
        print(f"Error: Repositories file not found at {repos_file}")
        sys.exit(1)

    with open(repos_file, 'r') as f:
        data = json.load(f)

    for repo in data.get("repositories", []):
        url = repo.get("url")
        path = repo.get("path")
        ref = repo.get("ref")  # Optional: branch/tag to checkout

        if not url or not path:
            print(f"Skipping invalid repository entry: {repo}")
            continue

        # Construct the full path for the submodule relative to the repo root
        submodule_path = repo_root / path
        
        # Check if the submodule is already added
        gitmodules_path = repo_root / ".gitmodules"
        already_added = False
        if gitmodules_path.exists():
            with open(gitmodules_path, 'r') as gm_file:
                if path in gm_file.read():
                    print(f"Submodule for path '{path}' already exists. Skipping add.")
                    already_added = True

        if not already_added:
            print(f"Adding submodule: {url} to {path}")
            try:
                # Run the command from the repository root
                subprocess.run(
                    ["git", "submodule", "add", "--force", url, path],
                    check=True,
                    cwd=repo_root
                )
            except subprocess.CalledProcessError as e:
                print(f"Failed to add submodule {url}. Error: {e}")
            except FileNotFoundError:
                print("Error: 'git' command not found. Is Git installed and in your PATH?")
                sys.exit(1)
        
        # Checkout specific ref (branch/tag) if provided
        if ref:
            print(f"Checking out {ref} in {path}...")
            try:
                subprocess.run(
                    ["git", "checkout", ref],
                    check=True,
                    cwd=submodule_path
                )
                print(f"✓ Checked out {ref}")
            except subprocess.CalledProcessError as e:
                print(f"Warning: Failed to checkout {ref} in {path}. Error: {e}")
            except FileNotFoundError:
                print("Error: 'git' command not found.")
                sys.exit(1)
    
    print("\n✓ Setup complete! Submodules ready.")
    print("Note: Changes are NOT automatically committed. Use 'git status' to see dirty state.")

if __name__ == "__main__":
    add_submodules()
