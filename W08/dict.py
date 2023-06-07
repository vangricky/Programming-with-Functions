bad_guys = {
    'daredevil': 'kingpin',
    'x-men': 'apocalypse',
    'batman': 'bane'
}
# print(bad_guys)

print(bad_guys['daredevil'])
print(bad_guys['x-men'])
print(bad_guys['batman'])

bad_guys['deadpool'] = 'evil deadpool'
print(bad_guys)

bad_guys['x-men'] = 'juggernaut'
print(bad_guys)

del bad_guys['x-men']
print(bad_guys)

d = {
    0: "plane",
    1: "train"
}
d[0]