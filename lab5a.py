#!/usr/bin/env python3
# Author ID: [Imina Samuel]

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r')
    return f.read()
    f.close()

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters

    with open(file_name, 'r') as file:
        return [line.strip() for line in file.readlines()]
        f.close()

if __name__ == '__main__':

    file_name = 'data.txt'

    print(read_file_string(file_name))

    print(read_file_list(file_name))
