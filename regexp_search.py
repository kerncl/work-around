import os
import re

def get_file_type_regex_syntax(file_type):
    file_to_search = get_regex(file_type)
    if not file_to_search.endswith('$'): file_to_search += '$'
    if not file_to_search.startswith(r'\b'): file_to_search = r'\b{}'.format(file_to_search)
    return file_to_search


def get_regex(filename):
    '''
    Function to correctly escape '.' and '*' in file names.
    '''
    filename = str(filename) # handle case of getting unicode.

    # handle python special characters for regex
    if '.' in filename:
        filename = filename.replace('.','\.')
    if '*' in filename:
        filename = filename.replace('*','.*')
    return filename


if __name__ == '__main__':
    files = {'C:\\quark_execrise\\quark_sample_2\\quark_sample_2\\test.log' : '2ad7c043',
             'C:\\quark_execrise\\quark_sample_2\\quark_sample_2\\test2.log' : 'e2c6b77a'}
    basename = os.path.basename('C:\\quark_execrise\\quark_sample_2\\quark_sample_2\\test2.log')
    file_search = get_file_type_regex_syntax(basename)
    for file in files:
        match = re.search(file_search, file, re.IGNORECASE)
        if match != None:
            print(match.string)
