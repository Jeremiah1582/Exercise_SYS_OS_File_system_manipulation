# advanced_file_process.py

import os
import sys
import shutil

# Task 1: Create Directory Structure
project_directory = "my_project"
subdirectories = ["src", "data", "logs"]

if not os.path.exists(project_directory):
    os.makedirs(project_directory)
    for subdir in subdirectories:
        os.makedirs(os.path.join(project_directory, subdir))
    print("Created Directory Structure:", project_directory)
else:
    print("Directory already exists. Skipping creation.")
print()

# Task 2: Copy Files
txt_files = [file for file in os.listdir() if file.endswith(".txt")]
data_directory = os.path.join(project_directory, "data")

for txt_file in txt_files:
    shutil.copy(txt_file, data_directory)
print("Copied .txt files to:", data_directory)
print()

# Task 3: List and Filter Files
data_files = [file for file in os.listdir(data_directory) if file.startswith("file_") and os.path.getsize(os.path.join(data_directory, file)) > 1000]
print("Filtered Files in 'data' directory:", data_files)
print()

# Task 4: Process Execution
if len(sys.argv) == 2:
    file_to_print = sys.argv[1]
    os.system(f"cat {os.path.join(data_directory, file_to_print)}")
else:
    print("Usage: python advanced_file_process.py <file_name>")
print()

# Task 5: Cleanup
shutil.rmtree(project_directory)
print("Cleanup completed.")
