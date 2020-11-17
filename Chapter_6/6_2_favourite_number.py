favourite_numbers = {
    'maria': 3,
    'roberto': 5,
    'juan': 7,
    'manuel': 9,
    'mario': 1
}
align_major = len(max(favourite_numbers))
for v in favourite_numbers:
    print("{} : {}".format(v.ljust(align_major), favourite_numbers[v]))
