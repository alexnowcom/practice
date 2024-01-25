import csv

#with open('10_02_us.csv', 'r') as f:

    ## This could be used to load each and every component
    # reader = csv.reader(f, delimiter='\t')
    ## and this could be use to skip a header row
    # next(reader)
    ## Also could turn it into a list
    # reader = list(csv.reader(f, delimiter='\t'))
    # And use slicing 
    #  for row in reader[1:]:

    # Going to use the DictReader functionality instead so that we can use the headers
#    reader = csv.DictReader(f, delimiter='\t')

    # This to write it all to terminal
#    for row in reader:
#        print(row)

    # Let's do *something* with it
    # Example for filtering data

# Let's load it again, the way we need it
with open('10_02_us.csv', 'r') as f:
    data = list(csv.DictReader(f, delimiter='\t'))

# Function to create a list of prime numbers 
primes = []
for number in range(2,99999):
    for factor in range(2, int(number**0.5)):
        if number % factor == 0:
            break
    else:
        primes.append(number)

data = [row for row in data if int(row['postal code']) in primes and row['state code'] == 'WA']
print(len(data))

with open('file_zips_prime_generated.csv', 'w') as f:
    writer = csv.writer(f, delimiter='\t') # defaults to comma (,)
    for row in data:
        writer.writerow([row['place name'], row['county']])