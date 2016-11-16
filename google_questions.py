'''
Given the file structure shown below, return the sum of the number of characters
it takes to make all absolute paths to all .img and .jpg files.
'''

def total_characters_for_absolute_img_paths(root):
    directory_array = root.split('\n')
    sum_of_characters = 0
    current_path = '/'
    slash = '/'
    previous_indent = 0
    extensions = ['.img', '.jpg', '.jpeg', '.png']

    for line in directory_array:
        is_a_directory = is_directory(line)
        current_indent = get_spaces_in_front_of_element(line)
        if is_a_directory:
            directory = trim_spaces(line, current_indent)
            #  if the current_indent is larger than the previous indent
            #  we need to add it to the path and increment the indent
            if current_indent > previous_indent:
                current_path += directory + slash
                previous_indent += 1
            #  if indent is less than the previous indent
            #  we need to keep going up a directory until previous indent matches current indent
            if current_indent < previous_indent:
                while current_indent < previous_indent:
                    current_path = go_up_a_directory(current_path)
                    previous_indent -= 1
                current_path += directory + slash
                previous_indent += 1

        else:#  it's a file so...
            potential_image = trim_spaces(line, current_indent)
            extension = get_extension(potential_image)
            if extension in extensions:
                print('{} = {}'.format(current_path + potential_image + slash, str(len(current_path + potential_image + slash))))
                sum_of_characters += len(current_path + potential_image + slash)

    return sum_of_characters

def go_up_a_directory(current_path):
    num_till_a_slash = 1
    for character in current_path[-2::-1]:  # we start at neg two since current_path already ends in a slash
        if character is '/':
            break
        num_till_a_slash += 1
    return current_path[:-num_till_a_slash]

def trim_spaces(element, spaces):
    return element[spaces:]

def is_directory(element):
    ''' We assume directories CANNOT have a dot in their name! '''
    if '.' in element:
        return False
    else:
        return True

def sum_characters_in_path(path_so_far, image):
    slash = 1
    return len(path_so_far) + slash + len(image) # the one represents the needed backslash

def get_spaces_in_front_of_element(element):
    spaces = 0
    for letter in element:
        if letter is not ' ':
            break
        spaces += 1
    return spaces

def get_extension(element):
    extension = ""
    dot_found = False
    for character in element:
        if character is '.':
            dot_found = True
        if dot_found:
            extension += character
    return extension

# hierarchy = '''\
# dir1
#  dir11
#  dir12
#   picture.jpeg
#   dir121
#   file.txt
# dir2
#  file2.img
# '''

hierarchy = '''\
dir1
 dir11
  dir12
   picture.jpg
   picture2.png
  dir121
  file.txt
dir2
 file2.png
 dir21
  dir211
   file3.img
'''

print(total_characters_for_absolute_img_paths(hierarchy))