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

    emails = {}
    i=0
    with open(filepath, 'rU') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not 'Email Address' in row:
                email,domain = row[1].split('@')
                # print email,domain
                fake_email = email[:4] + get_random_string()
                # print fake_email
                emails[i] = fake_email
                i+=1
    # print emails
    return emails

def get_random_string():

    rnstring = ''
    for i in range(4):
        rnstring+=random.choice(string.ascii_letters)
    return rnstring

def get_winner():
    path = get_file_path('choices.csv')
    emails = read_csv(path)
    # print len(emails)

    ran_num = random.randint(0, len(emails)-1)
    winner = emails[ran_num]
    print "And the winner is %s" %winner

def main():
    currentdirpath = os.getcwd()
    filename = 'choices.csv'

    #filepath to open
    file_path = os.path.join(os.getcwd(), filename)
    get_winner()

main()
