import os
import argparse

def rename_files(directory: str, extension: str = None):
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        
        if extension:
            files = [f for f in files if f.endswith(f'.{extension}')]
        
        files.sort()
        
        for index, file in enumerate(files, start=1):
            file_ext = os.path.splitext(file)[1]  # Obtener la extensión original
            new_name = f"{index}{file_ext}"
            
            old_path = os.path.join(directory, file)
            new_path = os.path.join(directory, new_name)
            
            os.rename(old_path, new_path)
            print(f"Renamed: {file} -> {new_name}")
        
        print("Renaming completed successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rename files in a directory with a numerical sequence.")
    parser.add_argument("directory", type=str, help="Directory to scan")
    parser.add_argument("--extension", type=str, help="Filter by file extension (without dot)", default=None)
    
    args = parser.parse_args()
    rename_files(args.directory, args.extension)
