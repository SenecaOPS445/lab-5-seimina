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

    with open(file_name, 'r') as f:
        return [line.strip() for line in f.readlines()]
        f.close()

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    
    with open(file_name, 'a') as f:
        f.write(string_of_lines)
        f.close()

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    
    with open(file_name, 'w') as f:
        for line in list_of_lines:
            f.write(line + '\n')
        f.close() 

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file

    with open(file_name_read, 'r') as file_read:
        lines = file_read.readlines()
        file_read.close()

    with open(file_name_write, 'w') as file_write:
        for i, line in enumerate(lines, 1):
            file_write.write(f"{i}:{line}")
        file_write.close()
  

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
