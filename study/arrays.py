import array as arr

# Array com ints
ints = [1, 2, 3, 4, 5, 6]
print('Array com inteiros: ', ints)

# Printa uma posição no array
print('Uma posição no array: ', ints[1])

# Array com strings
cars = ["Ford", "Volvo", "BMW"]
print('Array com strings: ', cars)

# Adiciona itens no fim do array
cars.append("Honda")
print('Adiciona um item no fim do array: ', cars)

# Retira item no fim do array
cars.pop()
print('Retira um item no fim do array: ', cars)

# Retira item em uma posição no array
cars.pop(1)
print('Retira um item específico no array: ', cars)

# Remove um item do array
carros = ["Ford", "Volvo", "BMW"]
carros.remove("Ford")
print('Remove um item do array com remove(): ', carros)

# Limpa todos os dados do array
cars.clear()
print('Limpa todos os itens do array: ', cars)

# printa cada valor
a = arr.array('i', [1, 2, 3, 4, 5])
for i in (a): 
    print ('Printa cada valor do array: ', i, end =" ") 
print()

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list