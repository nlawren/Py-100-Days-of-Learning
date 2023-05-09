import os

root_path = './src'
directory_prefix = 'day'
days = 100
# directory digit padding for days 1-100
padding = '03'

readme_filename = "README.md"
readme_contents = f'''
# DAY 

## Description

Python version: 

## Dependencies

## How to run this day's lesson
```

## Sample output
```
'''


def create_directory(dir):
    if not os.path.isdir(dir):
        os.mkdir(dir)


def create_file(filename, contents):
    if not os.path.isfile(filename):
        mode = 'w+'
    else:
        mode = 'w'

    with open(filename, mode) as file:
        file.write(contents)


def build_structure():
    create_directory(root_path)

    for day in range(1, days+1):
        padded_day = f'{day:{padding}}'
        directory = f'{root_path}/{directory_prefix}{padded_day}'
        create_directory(directory)

        filename = f'{directory}/{readme_filename}'
        create_file(filename, readme_contents.format(day))

if __name__ == '__main__':
    build_structure()
