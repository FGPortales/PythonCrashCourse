user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
align_major = len(max(user_0))

print(user_0.items())

for k, v in user_0.items():
    print("{} : {}".format(k.ljust(align_major), v))
