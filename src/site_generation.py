import os
import shutil

from split_markdown import markdown_to_html_node, extract_title

def copy_static(fpath):

    source = os.path.join(fpath,"static")
    destination = os.path.join("public")

    #remove the destination folder, if it already exists
    if os.path.exists(destination):
        shutil.rmtree(destination)

    #initialise the destination folder
    os.mkdir(destination)

    #Debugging
    # print("source contents")
    # print(os.listdir(source))

    # print("current destination contents")
    # print(os.listdir(destination))

    recursively_copy(source, destination)
    #Debugging
    # print("complete")
    # print("final destination contents")
    # print(os.listdir(destination))


def recursively_copy(source_path, destination_path):
    for item in os.listdir(source_path):
        item_source_path = os.path.join(source_path,item)
        item_destination_path = os.path.join(destination_path, item)

        if os.path.isfile(item_source_path):
            # print(f"Processing file {item}")
            # print()
            shutil.copy(item_source_path, destination_path)
        
        elif os.path.isdir(item_source_path):
            # print(f"Processing directory {item}")
            # print()
            os.mkdir(item_destination_path)
            recursively_copy(os.path.join(item_source_path), item_destination_path)

        else:    
            raise Exception("item attempted to copy is neither file nor directory")

def generate_page(from_path, template_path, destination_path, file_name):

    print(f"Generating page from {from_path} to {destination_path} using {template_path}")

    with open(from_path, 'r') as f:
        source_markdown = f.read()

    html_content = markdown_to_html_node(source_markdown).to_html()
    html_title = extract_title(source_markdown)

    with open(template_path, 'r') as g:
        html_template = g.read()

    new_file = html_template.replace("{{ Title }}", html_title)
    new_file = new_file.replace("{{ Content }}", html_content)

    if not os.path.exists(destination_path):
        os.makedirs(destination_path)

    with open(os.path.join(destination_path, file_name), 'w') as d:
        d.write(new_file)

    print(f"Completed generation, page now saved at {os.path.join(destination_path, file_name)}")

def generate_pages_recursively(dir_path_content, template_path, dir_path_destination):

    #remove the destination folder, if it already exists
    if not os.path.exists(dir_path_destination):
        raise Exception("Destination directory does not exist")

    # print(os.listdir(dir_path_content))

    for item in os.listdir(dir_path_content):

        item_path_source = os.path.join(dir_path_content, item)
        item_path_destination = dir_path_destination
        if os.path.isfile(item_path_source):
            # print(f"Processing file {item}")
            # print()
            generate_page(item_path_source, template_path, item_path_destination, f"{os.path.splitext(item)[0]}.html")
        elif os.path.isdir(item_path_source):
            # print(f"Processing directory {item}")
            # print()
            new_item_path_destination = os.path.join(item_path_destination, item)
            os.mkdir(new_item_path_destination)

            # print()
            # print("recursively calling fn")
            # print(item_path_source)
            # print(template_path)
            # print(item_path_destination)
            # print(item)
            # print()
            generate_pages_recursively(item_path_source, template_path, new_item_path_destination)

        else:
            raise Exception("Item attempting to generate a page based on is neither a file nor a directory")