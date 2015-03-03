
def merge_sort(num_list):

    if len(num_list)>1:
		
		# Split
        mid = len(num_list)//2
        left_half = num_list[:mid]
        right_half = num_list[mid:]  
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge
        i=0
        j=0
        k=0
        
        while i<len(left_half) and j<len(right_half):
            if left_half[i]<right_half[j]:
                num_list[k]=left_half[i]
                i=i+1
            else:
                num_list[k]=right_half[j]
                j=j+1
            k=k+1

        while i<len(left_half):
            num_list[k]=left_half[i]
            i=i+1
            k=k+1

        while j<len(right_half):
            num_list[k]=right_half[j]
            j=j+1
            k=k+1
    
    return num_list

print merge_sort([54,26,93,17,77,31,44,55,20])


