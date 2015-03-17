import os
import csv
import random
import string

def get_file_path(filename):
    currentdirpath = os.getcwd()
    file_path = os.path.join(os.getcwd(), filename)
    print file_path
    return file_path

def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not 'Email Address' in row:
                print row[0], row[1], row[2]

currentdirpath = os.getcwd()
filename = 'choices.csv'

#filepath to open
file_path = os.path.join(os.getcwd(), filename)

get_file_path('choices.csv')
read_csv(path)
