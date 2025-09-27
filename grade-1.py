import os
import shutil
import requests
import subprocess

# A dictionary mapping the desired filename to its download URL
BOOKS_TO_DOWNLOAD = {
    "Amharic.pdf": "http://213.55.101.25/images/new_book/grade1/am/AMARIC_G1.pdf",
    "English.pdf": "http://213.55.101.25/images/new_book/grade1/English_grade_1_final_july_23_2022_kilole_Compressed.pdf",
    "Mathematics.pdf": "http://213.55.101.25/images/new_book/grade1/am/Maths_Grade_1Amaharic_compressed.pdf",
    "Environmental Science.pdf": "http://213.55.101.25/images/new_book/grade1/am/1__merged_Compressed.pdf",
    "Arts and Physical Education.pdf": "http://213.55.101.25/images/new_book/grade1/am/PVA_Amharic_version_Grade_1_Augest_14_2022__compressed.pdf"
}

# The target directory structure
TARGET_DIR = "resource/grade_1"

def download_file(url, filename):
    """Downloads a file from a URL and saves it locally."""
    print(f"  -> Downloading {filename} from {url}...")
    try:
        response = requests.get(url, stream=True, timeout=60)
        # Raise an exception for bad status codes (4xx or 5xx)
        response.raise_for_status()
        
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"  -> Successfully downloaded {filename}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"  -> ERROR: Failed to download {filename}. Reason: {e}")
        return False

def setup_directories():
    """Creates the necessary directory structure."""
    print(f"\n[Step 3 & 4] Creating directory: {TARGET_DIR}")
    # The exist_ok=True argument prevents an error if the directory already exists
    os.makedirs(TARGET_DIR, exist_ok=True)
    print("  -> Directory structure is ready.")

def run_git_commands():
    """Runs git add, commit, and push commands."""
    print("\n[Step 6] Running Git commands...")
    
    commands = [
        "git add .",
        'git commit -m "commit g1_books"',
        "git push origin main"
    ]
    
    for command in commands:
        try:
            print(f"  -> Executing: {command}")
            # We use check=True to raise an error if the command fails
            # Using capture_output to hide the command's stdout unless there's an error
            result = subprocess.run(
                command, 
                shell=True, 
                check=True, 
                capture_output=True, 
                text=True
            )
            print(f"  -> Success.")
        except subprocess.CalledProcessError as e:
            print(f"  -> ERROR: Command failed: {command}")
            print(f"  -> Stderr: {e.stderr}")
            print("  -> Aborting Git operations.")
            return False
            
    print("\n  -> All Git operations completed successfully!")
    return True

def main():
    """Main function to orchestrate all tasks."""
    print("Starting the process to download and commit Grade 1 books.")

    # Step 3 & 4: Create directory structure
    setup_directories()

    # Step 1, 2 & 5: Download, name, and move files
    print("\n[Step 1, 2 & 5] Downloading and moving books...")
    all_downloads_successful = True
    
    for filename, url in BOOKS_TO_DOWNLOAD.items():
        # 1. Download the file (it will be saved with a temporary name in the current dir)
        if download_file(url, filename):
            # 5. Move the downloaded file to the target directory
            try:
                destination_path = os.path.join(TARGET_DIR, filename)
                shutil.move(filename, destination_path)
                print(f"  -> Moved {filename} to {TARGET_DIR}/\n")
            except Exception as e:
                print(f"  -> ERROR: Could not move {filename}. Reason: {e}\n")
                all_downloads_successful = False
        else:
            all_downloads_successful = False

    if not all_downloads_successful:
        print("\nOne or more downloads failed. Skipping Git commands.")
        return

    # Step 6: Run Git commands
    run_git_commands()
    
    print("\n✅ All tasks completed.")

if __name__ == "__main__":
    main()

