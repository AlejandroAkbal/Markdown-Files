from pathlib import Path
from MarkdownPP import MarkdownPP

modules = ['include']

current_dir_utility = Path('.')

list_of_files_that_match = current_dir_utility.rglob('*.mdpp')

for file in list_of_files_that_match:
    input_file = Path.absolute(file)
    input_file_data = open(input_file, 'r')

    output_file = f'dist/{input_file.stem}.processed.md'
    output_file_data = open(output_file, 'w')

    print(f'File: {file}')
    # print(f'Absolute path: {input_file}')

    MarkdownPP(input=input_file_data, output=output_file_data, modules=modules)

    input_file_data.close()
    output_file_data.close()
