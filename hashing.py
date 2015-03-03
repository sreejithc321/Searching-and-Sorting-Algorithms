
class HashTable:
	
	def __init__(self):
		# Size holds the hash table size, slots will hold the key items and data will hold the data values 
		# Size should a prime number so that the collision resolution algorithm can be as efficient as possible.
		self.size = 11
		self.slots = [None] * self.size
		self.data = [None] * self.size
	
	def hash_function(self,key,size):
		# Return remainder 
		return key%size
	
	def rehash(self,old_hash,size):
		# Linear probing with a +1
		return (old_hash+1)%size
	
	def put(self,key,data):
		# Find hash value
		hash_value = self.hash_function(key,len(self.slots))	
		if self.slots[hash_value] == None:
			self.slots[hash_value] = key
			self.data[hash_value] = data
		else:
			if self.slots[hash_value] == key:
				# replace
				self.data[hash_value] = data  
			else:
				next_slot = self.rehash(hash_value,len(self.slots))
				# Iterates the rehash function until an empty slot occurs
				while self.slots[next_slot] != None and self.slots[next_slot] != key:
					next_slot = self.rehash(next_slot,len(self.slots))	
				if self.slots[next_slot] == None:
					self.slots[next_slot]=key
					self.data[next_slot]=data
				else:
					self.data[next_slot] = data 
			
	def get(self,key):
		start_slot = self.hash_function(key,len(self.slots))
		data = None
		stop = False
		found = False
		position = start_slot
		while self.slots[position] != None and not found and not stop:
			if self.slots[position] == key:
				found = True
				data = self.data[position]
			else:
				# Read rehash function to get next slot
				position=self.rehash(position,len(self.slots))
				if position == start_slot:
					stop = True
		return data
	

# Testing    
H = HashTable()
H.put(11,"a")
H.put(22,"b")
H.put(24,"c")
H.put(32,"d")
H.put(52,"e")
H.put(43,"f")
print H.get(22)
print H.data
print H.slots
