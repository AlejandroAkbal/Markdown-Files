import os
from pathlib import Path
from MarkdownPP import MarkdownPP


def remove_md_files_from_dir(directory):
    dir_utility = Path(directory)

    list_of_files_that_match = dir_utility.rglob('*.md')

    for file in list_of_files_that_match:
        if os.path.exists(file):
            print(f'Removing file: {file}')

            os.remove(file)


def process_mdpp_files_from_dir(input_dir, output_dir):
    dir_utility = Path(input_dir)

    list_of_files_that_match = dir_utility.rglob('*.mdpp')

    for file in list_of_files_that_match:
        input_file = Path.absolute(file)
        input_file_data = open(input_file, 'r')

        output_file = f'{output_dir}/{input_file.stem}.processed.md'
        output_file_data = open(output_file, 'w')

        print(f'Processing file: {file}')
        # print(f'Absolute path: {input_file}')

        MarkdownPP(input=input_file_data,
                   output=output_file_data, modules=modules)

        input_file_data.close()
        output_file_data.close()


modules = ['Include', 'IncludeCode', 'Reference',
           'TableOfContents', 'YoutubeEmbed']
input_directory = './src'
output_directory = './dist'

remove_md_files_from_dir(output_directory)

print('\n---\n')

process_mdpp_files_from_dir(input_directory, output_directory)
