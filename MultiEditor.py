#!/usr/bin/env python3
import fileinput


class MultiEditor:

    def read_data(files, text_to_search, replacement_text):
        for file in files:
            with fileinput.FileInput(file, inplace=True, backup='.bak') as file:
                for line in file:
                    print(line.replace(text_to_search, replacement_text), end='')

        print("Its done ... yipeee... ")


obj = MultiEditor()
print("--------------MultiEditor---------------", '\n')
num_of_files = int(input("Please enter the number of files in which you want to do the replacement.\n"))
all_files = []
for i in range(1, num_of_files + 1):
    path = input("Input the file {} path \n".format(i))
    all_files.append(path)
search = input("Enter the text you are searching to replace(Incorrect word).\n")
replacement_word = input("Enter the text you want to replace with (Corrected word)\n")
obj.read_data(all_files, search, replacement_word)
