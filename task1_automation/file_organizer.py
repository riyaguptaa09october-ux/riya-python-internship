"""
File Organizer & Cleaner - Automation Script
Internship Task 1: Python Automation Script

Goal:
    Automatically organize a folder by sorting files into subfolders
    based on their file type (extension), renaming duplicate files
    safely, and removing empty leftover folders.

Features:
    - Uses the `os` module for all file operations
    - Full exception handling (missing folder, permission errors, etc.)
    - Generates a timestamped log file for every operation performed
    - Takes user input for the folder path to organize

Author: Riya Gupta
"""

import os
import shutil
import logging
from datetime import datetime

# ---------------------------------------------------------
# 1. LOGGING SETUP
# ---------------------------------------------------------
LOG_FILE = "file_organizer_log.txt"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def log_and_print(message, level="info"):
    """Print a message to the console AND write it to the log file."""
    print(message)
    if level == "info":
        logging.info(message)
    elif level == "error":
        logging.error(message)
    elif level == "warning":
        logging.warning(message)


# ---------------------------------------------------------
# 2. FILE TYPE CATEGORIES
# ---------------------------------------------------------
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".java", ".js", ".html", ".css", ".cpp", ".c"],
}


def get_category(extension):
    """Return the category name for a given file extension."""
    extension = extension.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    return "Others"


# ---------------------------------------------------------
# 3. CORE FUNCTIONS
# ---------------------------------------------------------
def get_unique_filename(destination_folder, filename):
    """
    If a file with the same name already exists in the destination,
    generate a new unique name like file(1).txt, file(2).txt, etc.
    """
    base, extension = os.path.splitext(filename)
    counter = 1
    new_filename = filename

    while os.path.exists(os.path.join(destination_folder, new_filename)):
        new_filename = f"{base}({counter}){extension}"
        counter += 1

    return new_filename


def organize_folder(target_folder):
    """
    Organize all files inside target_folder into category subfolders.
    Returns a summary dictionary with counts of moved/skipped/error files.
    """
    summary = {"moved": 0, "skipped": 0, "errors": 0}

    try:
        if not os.path.exists(target_folder):
            raise FileNotFoundError(f"The folder '{target_folder}' does not exist.")

        if not os.path.isdir(target_folder):
            raise NotADirectoryError(f"'{target_folder}' is not a directory.")

        entries = os.listdir(target_folder)

        if not entries:
            log_and_print(f"The folder '{target_folder}' is empty. Nothing to organize.")
            return summary

        log_and_print(f"Starting organization of: {target_folder}")

        for item in entries:
            item_path = os.path.join(target_folder, item)

            # Skip subfolders and the log file itself
            if os.path.isdir(item_path):
                continue
            if item == LOG_FILE:
                continue

            try:
                _, extension = os.path.splitext(item)

                if extension == "":
                    category = "Others"
                else:
                    category = get_category(extension)

                category_path = os.path.join(target_folder, category)

                # Create category folder if it doesn't exist
                if not os.path.exists(category_path):
                    os.makedirs(category_path)
                    log_and_print(f"Created folder: {category_path}")

                # Handle duplicate filenames safely
                safe_name = get_unique_filename(category_path, item)
                destination_path = os.path.join(category_path, safe_name)

                shutil.move(item_path, destination_path)
                log_and_print(f"Moved: '{item}' -> '{category}/{safe_name}'")
                summary["moved"] += 1

            except PermissionError as pe:
                log_and_print(f"Permission denied for '{item}': {pe}", level="error")
                summary["errors"] += 1

            except Exception as e:
                log_and_print(f"Could not move '{item}': {e}", level="error")
                summary["errors"] += 1

        log_and_print(
            f"Organization complete. Moved: {summary['moved']}, "
            f"Errors: {summary['errors']}"
        )

    except FileNotFoundError as fnf:
        log_and_print(str(fnf), level="error")
    except NotADirectoryError as nde:
        log_and_print(str(nde), level="error")
    except Exception as e:
        log_and_print(f"Unexpected error: {e}", level="error")

    return summary


def clean_empty_folders(target_folder):
    """Remove any empty subfolders left inside the target folder."""
    removed = 0
    try:
        for root, dirs, files in os.walk(target_folder, topdown=False):
            for d in dirs:
                dir_path = os.path.join(root, d)
                try:
                    if not os.listdir(dir_path):
                        os.rmdir(dir_path)
                        log_and_print(f"Removed empty folder: {dir_path}")
                        removed += 1
                except Exception as e:
                    log_and_print(f"Could not remove '{dir_path}': {e}", level="warning")
    except Exception as e:
        log_and_print(f"Error while cleaning empty folders: {e}", level="error")
    return removed


# ---------------------------------------------------------
# 4. MAIN PROGRAM (USER INPUT)
# ---------------------------------------------------------
def main():
    print("=" * 55)
    print(" FILE ORGANIZER & CLEANER - Automation Script")
    print("=" * 55)

    folder_path = input("Enter the full path of the folder to organize: ").strip()

    if not folder_path:
        log_and_print("No folder path entered. Exiting program.", level="error")
        return

    log_and_print(f"Run started at {datetime.now()}")

    summary = organize_folder(folder_path)
    clean_empty_folders(folder_path)

    print("-" * 55)
    print(f"Files moved : {summary['moved']}")
    print(f"Errors      : {summary['errors']}")
    print(f"Log saved to: {os.path.abspath(LOG_FILE)}")
    print("-" * 55)


if __name__ == "__main__":
    main()
