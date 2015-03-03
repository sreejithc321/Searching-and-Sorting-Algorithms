
def selection_sort (num_list):
	for items in range(len(num_list)-1,0,-1):
		max_pos = 0
		for item in range(1,items+1):
			if num_list[max_pos] < num_list[item]:
				max_pos = item
		temp = num_list[max_pos]
		num_list[max_pos] = num_list[item]
		num_list[item] = temp
	return num_list
	
print selection_sort([54,26,93,17,77,31,44,55,20])
