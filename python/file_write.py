f = open('file_output.txt', 'w')

f.write('Don\'t ')
f.write('Stop ')
f.write('Believin\'')

f.close()
# Have to close the file to write what's in the buffer
# Running this script will overwrite the file