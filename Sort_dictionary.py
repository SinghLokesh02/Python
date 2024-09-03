import operator
# Sorting a Dictionary

mydict = {"India":900, "Japan":100, "South Africa": 400, "China":400, "UK":676}

# Sorting by Key in descending order
print("Sorting by Key in descending order")
ans = sorted(mydict.items())
print(ans)

# Sorting by Key in Ascending order
print("Sorting by Key in Ascending order")
ans = sorted(mydict.items(),reverse=True)
print(ans)


# Sortby Value in Ascending order
print("Sort by Value in Ascending order")
sorted_by_values = dict(sorted(mydict.items(), key=operator.itemgetter(1)))
print(sorted_by_values)

# Sortby Value in Descending order
print("Sorting by Value in Descending order")
sorted_by_values = dict(sorted(mydict.items(), key=operator.itemgetter(1), reverse=True))
print(sorted_by_values)