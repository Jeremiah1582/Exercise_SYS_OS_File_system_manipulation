-----------**File and Process Manipulation**-----------
# Backstory:
You are developing a utility script that needs to perform more advanced tasks, including creating a directory structure, copying files, and executing external commands. Your goal is to use the os and sys modules to accomplish these tasks efficiently.

# Objective:
Create a Python script that performs various advanced file and process manipulation tasks using the os and sys modules.

# Tasks:
1) Create Directory Structure:

Import the os module.
Create a directory named "my_project" with subdirectories: "src," "data," and "logs."

2) Copy Files:

Use the os module to copy all .txt files from the current working directory to the "data" directory.

3) List and Filter Files:

List all files in the "data" directory.
Filter the list to include only files with names starting with "file_" and having a size greater than 1000 bytes.

4) Process Execution:

Import the sys module.
Use the sys.argv list to accept a command-line argument specifying a file name.
Use the os.system() function to execute a command that prints the content of the specified file.

5) Cleanup:

Delete the "my_project" directory and its contents.

# Requirements:
Intermediate understanding of Python.
Python installed on your system.

# Test Case:
Run the script and verify the creation of the "my_project" directory structure.
Check if the .txt files are successfully copied to the "data" directory.
Verify the listing and filtering of files in the "data" directory.
Execute the script with a command-line argument specifying a file name to ensure the content is printed.
Confirm that th


*Remember:*
- Use os.makedirs() to create nested directories.
- Copy files using shutil.copy().
- List and filter files with list - comprehensions and os.path functions.
-Accept command-line arguments using sys.argv.
- Execute external commands with os.system().
- Cleanup directories and files with shutil.rmtree().