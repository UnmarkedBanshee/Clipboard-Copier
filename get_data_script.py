import clipboard
import sys
import json #learn the in's an out's of json


SAVED_DATA = 'clipboard_data.json'
#print(sys.argv[1:]) #this is everyhting after calling the python file in terminal like python filename {run} argv == run now becsue we cvalled run
# 3 different allowed commands

def save_items(filepath, data):
    with open (filepath, 'w') as f: #f is file name
        json.dump(data,f) #dump is command to add data to a json file (aruments are data and file name)

def load_json(filepath):
    try: #try catch block to run otherwise if error occurs we can return empty dict
        with open(filepath,'r') as f:
            data = json.load(f)
            return data
    except:
        return {}

if len(sys.argv) == 2:
    command = sys.argv[1] #the command passed in after the script name, use it to do different things
    data = load_json(SAVED_DATA)

    if command == 'save':
        key = input('Enter a key: ')
        if key in data:
            existance_key = input('That key already exists, if you continue the data there will be overridden:')
            if existance_key.upper() or existance_key.lower == 'yes' or 'YES':
                data[key] = clipboard.paste()
                save_items(SAVED_DATA, data) #calling the save function and passing in the arguments
                print('Data saved succesfully')
            else:
                print('{}')
        else:
            data[key] = clipboard.paste()
            save_items(SAVED_DATA, data) #calling the save function and passing in the arguments
            print('Data saved succesfully')
        
    elif command == 'load':
        key = input('What key would you like to \n access data from: ')
        if key in data:
            clipboard.copy(data[key])
            print('Data accessed succesfully')
            #print('{1} copied to clipboard'.format((str(data[key])))) figure out why its not printing the loaded data
        else:
            print('Key doesnt exist! ')
            #load that key from the json dict
            #print the value of that key if it is in the dict and save it to the clipboard as the 'current copied' item
    elif command == 'items':
        print(data)
        #return all items saved in the dictionary as a dictionry
    elif command == 'delete':
        key = input('What key would you like to delete: ')
        if key in data:
            del data[key]
            save_items(SAVED_DATA, data)
        #we could add functionlaity as practcie, but since saving the data to a preexisitng key already overwrites it, there is no point
    else:
        print('Invalid command')
else:
    print('Invalid number of arguments')

