import re

directory = './'
filename = 'bibliography.bib'

file = open(directory + filename, 'r')
file_content = file.read()
file_list = file_content.split('\n')

tags_list = []

for item in file_list:

    match = re.search(r'@.*\{(.*),', item)

    if match is not None:

        tag = match.group(1)
        tags_list.append(tag)

file.close()

unique_tags = list(set(tags_list))

bib_items = file_content.split('@')[1::]
bib_items = ['@' + item for item in bib_items]

new_file = open(directory + 'unique-bibliography.bib', 'w')

for item in bib_items:

    match = re.search(r'@.*\{(.*),', item)

    if match is not None:

        tag = match.group(1)

    if tag in unique_tags:

        new_file.write(item)

        unique_tags.remove(tag)

new_file.close()
