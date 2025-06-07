from _12_copy_paste_function import copy_content, generate_page, generate_pages_recursive

origin = "./static"
destination = "./public"
content = "./content"
template = "./template.html"

copy_content(origin, destination)
# generate_page(content, template, destination)
generate_pages_recursive(content, template, destination)


