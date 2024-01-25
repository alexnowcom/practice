fizz = 'Monty'
buzz = 'Python'
fizzbuzz = fizz + ' ' + buzz
limit = 10

print([fizzbuzz if n % 6 == 0 else buzz if n % 3 == 0 else fizz if n % 2 == 0 else n for n in range(1, limit)])