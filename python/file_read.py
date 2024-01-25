f = open('zen.txt', 'r')

for line in f.readlines():
    print(line.strip())