from _12_copy_paste_function import copy_content, generate_page, generate_pages_recursive
import sys
origin = "./static"
destination = "./docs"
content = "./content"
template = "./template.html"

# Right now our site always assumes that / is the root path of the site (e.g. http://localhost:8888/). Make if configurable by:

# In main.py use the sys.argv to grab the first CLI argument to the program. Save it as the basepath. If one isn't provided, default to '/'. 
basepath = sys.argv[0]
print(basepath)


copy_content(origin, destination)
# generate_page(content, template, destination)
generate_pages_recursive(content, template, destination, basepath)

