import os
import shutil
import time
import win32file
import win32con

# Path to the directory where you want to copy the PowerPoint files
destination_directory = "E:/data/lokesh"

def copy_ppt_files(source_directory):
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            if file.lower().endswith(".ppt") or file.lower().endswith(".pptx"):
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_directory, file)
                shutil.copy2(source_path, destination_path)
                print(f"Copied: {source_path} -> {destination_path}")

def watch_for_pendrive():
    drive_to_watch = "E:\\"  # Change this to the drive letter of your pendrive

    while True:
        try:
            drive_type = win32file.GetDriveType(drive_to_watch)
            if drive_type == win32file.DRIVE_REMOVABLE:
                print("Pendrive inserted.")
                copy_ppt_files(drive_to_watch)
                print("Copying completed.")
                time.sleep(5)  # Wait for a few seconds before checking again
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)
    watch_for_pendrive()
