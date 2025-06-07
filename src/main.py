from _12_copy_paste_function import copy_content, generate_page, generate_pages_recursive
import sys
import shutil
import os
origin = "./static"
destination = "./docs"
content = "./content"
template = "./template.html"
default_basepath = "/"

# Right now our site always assumes that / is the root path of the site (e.g. http://localhost:8888/). Make if configurable by:

# In main.py use the sys.argv to grab the first CLI argument to the program. Save it as the basepath. If one isn't provided, default to '/'. 
def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

        print(f"this is the basepath: {basepath}")

        if os.path.exists(destination):
            shutil.rmtree(destination)

    copy_content(origin, destination)
    generate_pages_recursive(content, template, destination, basepath)


main()