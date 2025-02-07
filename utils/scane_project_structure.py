import os
import argparse
from pathlib import Path

def parse_gitignore(root_dir):
    gitignore_path = Path(root_dir) / '.gitignore'
    ignored_patterns = {'.git/'}  # Siempre ignorar .git
    
    if gitignore_path.exists():
        with open(gitignore_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    ignored_patterns.add(line)
    
    return ignored_patterns

def is_ignored(path, ignored_patterns, root_dir):
    rel_path = os.path.relpath(path, root_dir)
    
    for pattern in ignored_patterns:
        if pattern.endswith('/'):
            if rel_path.startswith(pattern.rstrip('/')):
                return True
        elif Path(rel_path).match(pattern):
            return True
    
    return False

def generate_tree(root_dir, ignored_patterns, prefix=""):
    entries = sorted(os.listdir(root_dir))
    entries = [e for e in entries if not is_ignored(os.path.join(root_dir, e), ignored_patterns, root_dir)]
    
    for index, entry in enumerate(entries):
        path = os.path.join(root_dir, entry)
        connector = "├── " if index < len(entries) - 1 else "└── "
        print(prefix + connector + entry)
        
        if os.path.isdir(path):
            new_prefix = prefix + ("│   " if index < len(entries) - 1 else "    ")
            generate_tree(path, ignored_patterns, new_prefix)

def main():
    parser = argparse.ArgumentParser(description="Escanea un proyecto y muestra su estructura ignorando .gitignore.")
    parser.add_argument('--root', type=str, required=True, help="Directorio raíz del proyecto")
    args = parser.parse_args()
    
    root_dir = os.path.abspath(args.root)
    ignored_patterns = parse_gitignore(root_dir)
    
    print(os.path.basename(root_dir) + '/')
    generate_tree(root_dir, ignored_patterns)

main()
