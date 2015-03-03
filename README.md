
# Implementation of Searching and Sorting Algorithms in Python

### Searching Algorithms

##### Sequential Search
- Search items in sequence.
- Complexity of the sequential search, is O(n).  
- Sequential search can be improved by ordering the list in the case when the searched item is absent.
    - seq_search.py

##### Binary Search
- Take greater advantage of the ordered list.
- Complexity of the sequential search, is O(nlogn)
- A great example of a divide and conquer strategy
    - bin_search.py

##### Hashing
- Hash table is a collection of items and aach position of the hash table, often called a slot.
- The mapping between an item and the slot where that item belongs in the hash table is called the hash function.  
- Hash function formation methods include folding method, mid-square method, linear probing, quadratic probing etc
- Complexity of the sequential search, is O(1)
    - hashing.py

### Sorting Algorithms

##### Bubble Sort
- Compares adjacent items and exchanges those that are out of order
- Complexity is O(n^2)
	- bubble_sort.py
	
##### Selection Sort
- Makes only one exchange for every pass through the list.
- Complexity is O(n^2)
	- selection_sort.py


