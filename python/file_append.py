import datetime

f = open('file_append.txt', 'a')

f.write('This line appended on ' + datetime.datetime.now().isoformat() + '\n')
f.close()

print(f) # will print the file reference object

# This is another way to do this
with open('file_append.txt', 'a') as f:
    f.write('This line appended on ' + datetime.datetime.now().isoformat() + '\n')

# running inside the 'with' block will automatically close the file once done
# will need to reopen the file for any further actions

print(f)