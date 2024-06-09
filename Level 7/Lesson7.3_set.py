list1 = [1, 1, 2, 3, 4]
list2 = [1, 2, 3, 4]

set1 = set(list1)

print(set1)

set1.add(5)
set1.add(1)

print(set1)

print(set1.difference(list2))

print(set1.intersection(list2))

print(set1.pop())

print(set1)

print(set1.union(list2))

storm_troopers_group1 = ['trooper_1', 'trooper_2', 'trooper_3', 'trooper_4']

storm_troopers_group2 = ['trooper_5', 'trooper_2', 'trooper_34', 'trooper_46']

print(set(storm_troopers_group1).intersection(set(storm_troopers_group2)))
