pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
c = 0
while 'cat' in pets:
    pets.remove('cat')
    c += 1

print(pets)
print(c)
