import os
import csv
import random
import string

def get_file_path(filename):
    currentdirpath = os.getcwd()
    file_path = os.path.join(os.getcwd(), filename)
    # print file_path
    return file_path

def read_csv(filepath):
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not 'Email Address' in row:
                email,domain = row[1].split('@')
                print email,domain

currentdirpath = os.getcwd()
filename = 'choices.csv'

#filepath to open
file_path = os.path.join(os.getcwd(), filename)

path = get_file_path('choices.csv')
read_csv(path)
