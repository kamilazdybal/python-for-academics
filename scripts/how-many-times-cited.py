import re

directory = '../tutorials/'

file = open(directory + 'unique-bibliography.bib', 'r')

file_content = file.read()

file_list = file_content.split('\n')

tags_list = []

for item in file_list:
    
    match = re.search(r'@.*\{(.*),', item)
    
    if match is not None:
        
        tag = match.group(1)
        tags_list.append(tag)

file.close()

latex_source_file = open(directory + 'latex-source.tex', 'r').read()

citation_pattern = re.compile(r'\\cite[p]*\{([^\}]*)\}')

citations = []

for match in re.findall(citation_pattern, latex_source_file):

    for tag in match.split(','):

        citation = tag.strip()

        citations.append(citation)

citations_dictionary = {}

for tag in tags_list:
    citations_dictionary[tag] = citations.count(tag)

sorted_citations_dictionary = {key: value for key, value in sorted(citations_dictionary.items(), key=lambda item: item[1], reverse=True)}

for item, value in sorted_citations_dictionary.items():
    print('%35s%i' % (item + ': ', value))
