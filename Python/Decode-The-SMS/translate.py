 
def createDictionary():

    file_data = open("abbreviations.txt").read()
    key_value = {}
    data_list = file_data.split("\n")
    del data_list[-1]

    for data in data_list:
        key_val = data.split("-")
        key = key_val[0].strip()
        value = key_val[1].strip()
        key_value[key] = value

    return key_value

def main():
    message = raw_input("Enter the message to be translated. \n")
    
    key_value = createDictionary()

main()
