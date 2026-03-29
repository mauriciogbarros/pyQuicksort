def quick_sort(ints):
	if len(ints) == 0:
		return []
	
	# Considering pivot as the first element of the list.
	sorted_ints = []
	lower_ints = []
	equal_ints = []
	higher_ints = []
	for i in ints:
		if i < ints[0]:
			lower_ints.append(i)
		elif i == ints[0]:
			equal_ints.append(i)
		else:
			higher_ints.append(i)

	lower_ints = quick_sort(lower_ints)
	higher_ints = quick_sort(higher_ints)

	sorted_ints += lower_ints
	sorted_ints += equal_ints
	sorted_ints += higher_ints

	return sorted_ints

print(quick_sort([20, 3, 14, 1, 5]))
print(quick_sort([83, 4, 24, 2]))
print(quick_sort([4, 42, 16, 23, 15, 8]))
print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))