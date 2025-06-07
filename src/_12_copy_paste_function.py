import os
import shutil
from _11_block_to_html import markdown_to_html_node

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

def copy_content(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
   
    public_directory_list = os.listdir(destination)
    for item in public_directory_list:
        path = os.path.join(destination, item)
        if os.path.isdir(path):
            shutil.rmtree(path)
        if os.path.isfile(path):
            os.remove(path)
    
    static_folder = os.listdir(source)
    for item in static_folder:
        path = os.path.join(source, item)
        if os.path.isdir(path):
            new_path = os.path.join(destination, item)
            os.mkdir(new_path)
            copy_content(path, new_path)

        if os.path.isfile(path):
            shutil.copy(path, destination)
# ========================================================================================

"""
! Assignment
1. Create an 'extract title(markdown) function.
    . It should pull the h1 header from the markdown file and return it.
    . If there is no h1 header, raise an exception.
    . 'extract_title(# Hello) should return 'Hello' (strip the # and any leading or trailing whitespaces)
    . Write some unit tests for it.
"""

def extract_title(markdown):
    parts = markdown.split("\n")
    title = []
    for line in parts:
        if line.startswith("# "):
            title.append(line)
    if len(title) < 1:
        raise Exception("There is not a title in this HTML page.")
    return title[0].lstrip("# ").rstrip(" ")
# ========================================================================================

"""
Create a generate_page(from_path, template_path, dest_path) function. It should:
    1. Print a message like 'Generating page from {from_path} to {dest_path} using {template_path}.

    2. Read the markdown file at 'from_path' and store the contents in a variable.

    3. Read the template file at 'template_path' and store the contents in a variable

    4. Use your 'markdown_to_html_node' function and '.to_html()' method to convert the markdown file to an HTML string.

    .5 Use the extract_title to grab the title of the page.

    6. Replace the {title} and {content} placeholders in the template with the HTML and title you generated.

    7. Write the new full HTML page to a file at 'dest_path'. Be sure to create any necessary directories if they don't exist.
"""

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    # We'll assume for now, that there is only one HTML file inside the 'from path' directory, if this changes we can then maybe run a loop for every HTML file inside 'from 'path' directory
    md_file = os.listdir(from_path)[0]
    path = os.path.join(from_path, md_file)
    with open(path, 'r') as file:
        md_content = file.read()
    
    with open(template_path, 'r') as file:
        template_file = file.read()

    html_String = markdown_to_html_node(md_content).to_html()
    title = extract_title(md_content)

    full_html = template_file.replace("{{ Title }}", f"{title}", 1).replace("{{ Content }}", f"{html_String}", 1)
    
    # Todo, Theres this part of the course that says 'be sure to create any necessary directories if they dont exist. but the public directory in which we're writing the html index to already exists, keep an eye on this, just in case they need to be created. we might need to use os.mkdirs().
    file_name = "index.html"
    try:
        new_directory = os.makedirs(dest_path)
        file_path = os.path.join(new_directory, file_name)
        created_html_file = open(file_path, "w")
        created_html_file.write(full_html)
        created_html_file.close()
    except OSError as error:
        file_path = os.path.join(dest_path, file_name)
        created_html_file = open(file_path, "w")
        created_html_file.write(full_html)
        created_html_file.close()

# ========================================================================================
"""
! Assignment
1. Create a 'generate_pages_recursively(dir_path_content, template_path, dest_dir_path) function. It should:
    1. Crawl every entry in the content directory
    2. For each markdown file found, generate a new .html file using the same template.html. The generated files should be written to the public directory in the same directory structure.

2. Change your main function to use 'generate_pages_recursive' instead of 'generate_page'. You should generate a page for every markdown file in the content directory and write the  results to the public directory.

3. Run the new program and ensure that both pages on the site are generated correctly and you can navigate between them.
"""

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    # 1. list all the items in the content directory
    items = os.listdir(dir_path_content)
    # Run a loop for every item in the list
    for item in items:
        # create a path with the 'dir_path_content' and the 'item'
        path = os.path.join(dir_path_content, item)

        if os.path.isfile(path):

            with open(template_path, "r") as temp:
                template_file = temp.read()
 
            with open(path, "r") as file:
                md_content = file.read()

            html_string = markdown_to_html_node(md_content).to_html()
            title = extract_title(md_content)
            full_html = template_file.replace("{{ Title }}", title, 1).replace("{{ Content }}", html_string).replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
            file_path = os.path.join(dest_dir_path, "index.html")
            created_html = open(file_path, "w")
            created_html.write(full_html)
            created_html.close()
            

        # check if the path is a directory
        if os.path.isdir(path):
            # create a new path with the 'dest_dir_path' and the item
            new_path = os.path.join(dest_dir_path, item)
            # create a directory on that new path
            os.mkdir(new_path)
            # call this function recursively to create directories inside directories if necessary
            generate_pages_recursive(path, template_path, new_path, basepath)
            
            


    






    
    
    





