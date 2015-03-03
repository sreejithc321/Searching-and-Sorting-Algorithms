
def seq_search(search_list,item):
	pos = 0
	found = False
	
	while(pos<len(search_list) and not found):
		if search_list[pos] == item:
			found = True
		pos = pos +1
	
	return found

print bin_search([1,2,3,5,8],6)
print bin_search([1,2,3,5,8],5)

