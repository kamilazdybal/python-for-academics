from os import listdir
from os.path import isfile
import nbformat

directory = './'

files = [i for i in listdir(directory) if isfile(directory + i)]

README_file = open(directory + 'README.md', 'w')

README_file.write('# Available code\n\n')

for file in files:

    file_list = file.split('.')

    if file_list[-1] == 'ipynb':

        notebook = nbformat.read(directory + file, as_version=4)

        README_file.write('##' + notebook['cells'][0]['source'].split('\n\n')[0] + '\n\n')

        README_file.write('- [Jupyter notebook: `' + file + '`](' + file + ')\n\n')

        README_file.write('> ' + notebook['cells'][1]['source'] + '\n\n')

README_file.close()

print('\nREADME.md file generated in:\n' + directory + '\n')
