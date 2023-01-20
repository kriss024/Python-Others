# First-In, First-Out
# Last-In, First-Out

import queue as que
from itertools import permutations, combinations, combinations_with_replacement 

q1 = que.Queue()

# Add and item in a FIFOqueue
for i in range(20):
    q1.put(i) # this will additem from 0 to 20 to the queue

# Remove an item from the FIFOqueue
print("Number of items in the queue: ", q1.qsize())
while not q1.empty():
    print("The value is ", q1.get()) # get() will remove the item from the queue.

print(20*'-')

# Add and item in a LIFOqueue
q2 = que.LifoQueue()
for i in range(20):
    q2.put(i) # this will additem from 0 to 20 to the queue

# Remove an item from the LIFOqueue
print("Number of items in the queue: ", q2.qsize())
while not q2.empty():
    print("The value is ", q2.get()) # get() will remove the item from the queue.

print(20*'-')

# Get all permutations of [1, 2, 3] 
perm = permutations([1, 2, 3]) 
  
# Print the obtained permutations 
for i in list(perm): 
    print(i)

print(20*'-')
# Get all permutations of length 2 
# and length 2 
perm = permutations([1, 2, 3], 2) 
  
# Print the obtained permutations 
for i in list(perm): 
    print(i)

print(20*'-')
# Get all combinations of [1, 2, 3]
# and length 2
comb = combinations([1, 2, 3], 2)
  
# Print the obtained combinations
for i in list(comb):
    print(i)

print(20*'-')
# Get all combinations of [1, 2, 3] and length 2 
comb = combinations_with_replacement([1, 2, 3], 2) 
  
# Print the obtained combinations 
for i in list(comb): 
    print(i)  