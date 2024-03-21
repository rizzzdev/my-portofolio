# map()
arr = [1,1,2,3]
squared_arr = list(map(lambda x : x**2, arr))
print(squared_arr)

# filter()
arr = [1,1,2,3]
odd = list(filter(lambda x : x % 2 == 1, arr))
print(odd)

# zip()
arr = [1,1,2,3]
arr_id_zip = list(zip(arr, arr))
print(arr_id_zip)

# enumerate()
arr = [1,1,2,3]
arr_enum = list(enumerate(arr, 2))
print(arr_enum)

# format()
print('Halo {age: .4f}, namaku'.format(age = 5))

# enmunerate