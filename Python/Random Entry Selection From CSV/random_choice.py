import os
import csv
import random
import string

currentdirpath = os.getcwd()
filename = 'choices.csv'

#filepath to open
file_path = os.path.join(os.getcwd(), filename)

def get_file_path(filename):
    currentdirpath = os.getcwd()
    file_path = os.path.join(os.getcwd(), filename)
    print file_path
    return file_path

get_file_path('choices.csv')
