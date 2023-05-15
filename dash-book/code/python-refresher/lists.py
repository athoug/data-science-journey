# Lists are mutable, meaning you can modify them after they’ve been created.
# creating a list and displaying length
lst = [1, 2, 3, 4]
print(len(lst))


# Adding elements to a list
# 1. append (adding element to the end)
lst.append(5)
print(lst)

# 2. insert (adding an element to a specific location and shifting the rest to the right)
lst.insert(2, 0)
print(lst)

# 3. concatenation (+) -  creates a new list
lst = lst + [6, 7]
print(lst)

# 4. extend (to append multiple values)
lst.extend([8, 9])
print(lst)


# Removing elements from a list -  modifies the list
lst.remove(1)
print(lst)

# Reversing a list - modifies the list
lst.reverse()
print(lst)


# Sorting a list
lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

lust = [2, 1, 4, 2]
lust.sort(key=lambda x: -x)
print(lust)


# Indexing list elements
print([2, 2, 4].index(2))  # get index of element
# get index of element prints the index of the first occurrence of the value 2 but starts the search from index 1.
print([2, 2, 4].index(2, 1))
