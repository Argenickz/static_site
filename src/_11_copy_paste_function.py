import os
import shutil
"""
! Copy Static
We've written a lot of unit tests, it's time to start pulling all the pieces together into a static site generator. Let's work on that main.py that we've been neglecting.

! Assignment. 
1. Add the files in the lesson to a static directory in the root of the project:
    . static/ images/tolkien.png
    . static/index.css

2. Write a recursive function that copies all the contents from a source directory to a destination directory (in our case, static to public)
    . It should first delete all the content of the destination directory (public) to ensure tha the copy is clean.

    . It should copy all files and subdirectories, nested files, etc.

    . I recommend logging the path of each file you copy, so you can see what's happening
     as you run and debug your code.

Study these standard library docs, they might be helpful
! os.path.exists
This is used to check wether the specified path exists or not. This method can also be used to check wether the given path refers to an open file descriptor or not.
Returns True if path exists.

! os.listdir
This method is used to get the list of all files and directories in the specified directory. If we don't specify any directory, then a list of files and directories in the current working directory will be returned.

! os.path.join
This is a function in the os module that joins one or more paths components intelligently. It construct a full path by concatenating various components while automatically inserting the appropriate path separator (/ for unix based systems and '\' for Windows) Example:
` path = os.path.join("/home", "user", "documents", "/etc", "config.txt")
`print(path)
`/etc/config.txt

! os.path.isfile
This method is used to check if a path refers to a regular file (not a directory or any other type of file system object.) This method can be particularly useful when you need to validate file paths before performing file operations like reading, writing, or modifying files. It returns a boolean value.
    . True if the path refers to a file that exists.
    . False if the path does not exists or is not a regular file.

! os.mkdir
In Python this is used to create a directory, or create a directory with Python named path with the specified numeric mode. This method raised FileExistsError if the directory to be created already exists.
` Syntax: os.mkdir

! shutil.copy
This method in Python is used to copy the content of source file to destination file or directory. It also preserves the file's permission mode but other metadata of the file's creation and modification times is not preserved. 
Source must represent a file but destination can be a file or directory. If the destination is not a directory then the file will be copied into destination using the base filename from source. 
Also destination must be writable. 
If destination is a file and already exists then it will be replaced with the source file otherwise a new file will be created.

! shutil.rmtree
This is used to remove an entire directory tree, path must point to a directory (but not a symbolic link to a directory).

3. Hook the function up to your main function and test it out. I didn't use a unit test for this because it interacts with the file system, I just tested manually.

4. Add the 'public/' directory to your '.gitignore' file. This is where the generated site will live. As a general rule, it's bad to commit generated stuff, specially if it can be regenerated easily.

5. Ensure that running 'main.sh' generates the public directory and all the copied content correctly.

Run and submit the CLI tests from the root of the project.
"""

# # Let's create a simple function that copies a file from a directory into another directory and deletes the file from the previous directory
# def copy_and_delete(from_here, to_there):
#     # First, let's check if the file exists
#     if os.path.exists(from_here):
#         shutil.copy(from_here, to_there)
#         # shutil.rmtree is used to remove entire directories, for single files, is better to use os.remove(file)
#         os.remove(from_here)
#         print('success')      
# origin = "./static/this.txt"
# destination = "./public"
# copy_and_delete(origin, destination)
# Todo the function above is just practice, Let's take a look at a function that we created a while back, that recursively goes into a list of lists, it checks if the item is a list, if it is a list it goes deeper into it (by calling itself recursively) if its a file (or a number) it adds it to a list


def copy_content(source, destination):
    # First, delete all the content from the destination directory (public) to ensure a clean copy
    # Before that, let's list all of the items inside the public directory
    public_directory_list = os.listdir(destination)
    # The code above returns a list, loop though every item in the list, if the item is a file, delete it using os.remove, otherwise is a directory, delete it using shutil.rmtree()
    # Todo what happens if the list is empty after a recursive call??
    print(public_directory_list)
    for item in public_directory_list:
        path = os.path.join(destination, item)
        if os.path.isdir(path):
            shutil.rmtree(destination, item)
            print('deleted the dir')
        print(path)


origin = "./static"
destination = "./public"

copy_content(origin, destination)
# Todo Deleted the whole public dir, reinstate it and try again.