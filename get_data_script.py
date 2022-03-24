import clipboard
import sys

# 3 different allowed commands
if len(sys.argv) == 2:
    command = sys.argv[1] #the command passed in after the script name, use it to do different things
    if command == 'save':
        pass
    elif command == 'load':
        pass
    elif command == 'items':
        pass
    else:
        print('Invalid command')
else:
    print('Invalid number of arguments')


ls = []
if clipboard.paste() != clipboard.paste():
    ls.append(clipboard.paste())
data_dictionary = {}
data_dictionary[len(data_dictionary)] = clipboard.paste()
print(data_dictionary)
print(sys.argv)