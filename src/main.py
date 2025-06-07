from _12_copy_paste_function import copy_content, generate_page, generate_pages_recursive

origin = "./static"
destination = "./public"
content = "./content"
template = "./template.html"

copy_content(origin, destination)
# generate_page(content, template, destination)
generate_pages_recursive(content, template, destination)



# def generate_page(from_path, template_path, dest_path):
#     print(f"Generating page from {from_path} to {dest_path} using {template_path}")
#     # We'll assume for now, that there is only one HTML file inside the 'from path' directory, if this changes we can then maybe run a loop for every HTML file inside 'from 'path' directory
#     md_file = os.listdir(from_path)[0]
#     path = os.path.join(from_path, md_file)
#     with open(path, 'r') as file:
#         md_content = file.read()
    
#     with open(template_path, 'r') as file:
#         template_file = file.read()

#     html_String = markdown_to_html_node(md_content).to_html()
#     title = extract_title(md_content)

#     full_html = template_file.replace("{{ Title }}", f"{title}", 1).replace("{{ Content }}", f"{html_String}", 1)
    
#     # Todo, Theres this part of the course that says 'be sure to create any necessary directories if they dont exist. but the public directory in which we're writing the html index to already exists, keep an eye on this, just in case they need to be created. we might need to use os.mkdirs().
#     file_name = "index.html"
#     try:
#         new_directory = os.makedirs(dest_path)
#         file_path = os.path.join(new_directory, file_name)
#         created_html_file = open(file_path, "w")
#         created_html_file.write(full_html)
#         created_html_file.close()
#     except OSError as error:
#         file_path = os.path.join(dest_path, file_name)
#         created_html_file = open(file_path, "w")
#         created_html_file.write(full_html)
#         created_html_file.close()

# Todo Recursive copy content for reference.
# def copy_content(source, destination):
#     if not os.path.exists(destination):
#         os.mkdir(destination)
   
#     public_directory_list = os.listdir(destination)
#     for item in public_directory_list:
#         path = os.path.join(destination, item)
#         if os.path.isdir(path):
#             shutil.rmtree(path)
#         if os.path.isfile(path):
#             os.remove(path)
    
#     static_folder = os.listdir(source)
#     for item in static_folder:
#         path = os.path.join(source, item)
#         if os.path.isdir(path):
#             new_path = os.path.join(destination, item)
#             os.mkdir(new_path)
#             copy_content(path, new_path)

#         if os.path.isfile(path):
#             shutil.copy(path, destination)