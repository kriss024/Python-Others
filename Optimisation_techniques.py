# The intersection of two arrays/lists

import numpy as np

list1 = [1, 2, 3, 4, 4, 4, 5]
list2 = [4, 5, 5, 6, 7, 8]

intersec = np.intersect1d(list1, list2).tolist()
print(intersec)

#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
# Variable Packing

import struct

# Packing two integers into a binary format
packed_data = struct.pack('ii', 10, 20)

# Unpacking the packed binary data
a, b = struct.unpack('ii', packed_data)
print(a)
print(b)

#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
# Memory-mapped file

import mmap

# write a simple example file
with open("hello.txt", "wb") as f:
    f.write(b"Hello Python!\n")

with open("hello.txt", "r+b") as f:
    # memory-map the file, size 0 means whole file
    mm = mmap.mmap(f.fileno(), 0)
    # read content via standard file methods
    print(mm.readline())  # prints b"Hello Python!\n"
    # read content via slice notation
    print(mm[:5])  # prints b"Hello"
    # update content using slice notation;
    # note that new content must have same size
    mm[6:] = b" world!\n"
    # ... and read again using standard file methods
    mm.seek(0)
    print(mm.readline())  # prints b"Hello  world!\n"
    # close the map
    mm.close()

#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
# Fixed-Length vs. Variable-Length Variables

import array

# Using fixed-length array for performance
fixed_array = array.array('i', [1, 2, 3, 4, 5])

# Dynamic list (variable-length)
dynamic_list = [1, 2, 3, 4, 5]

#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
# Internal vs. Public Functions

def _private_function(data):
  # Optimized for internal use, with minimal error handling
  return data ** 2

def public_function(data):
  # Includes additional checks for external use
  if isinstance(data, int):
      return _private_function(data)
  raise ValueError("Input must be an integer")

#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
# Function Modifiers

# Using lru_cache as a decorator caches the results of expensive function calls, improving performance by avoiding redundant computations.

from functools import lru_cache

@lru_cache(maxsize=100)
def compute_heavy_function(x):
    # A computationally expensive operation
    return x ** x

#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
# Short-Circuiting Conditionals

def complex_condition(x, y):
    return x != 0 and y / x > 2  # Stops evaluation if x is 0

#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
# Free Up Memory

import gc

# Manual garbage collection to free up memory
large_data = [i for i in range(1000000)]
del large_data
gc.collect()  # Forces garbage collection

#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
# Short Error Messages

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Err: Div/0")  # Short, concise error message

#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
# Optimize Loops

import numpy as np

# Vectorised operation with NumPy
array = np.array([1, 2, 3, 4, 5])

# Instead of looping through elements
result = array * 2  # Efficient, vectorised operation

values = ["a", "b", "c"]
for count, value in enumerate(values, start = 1):
    print(count, value)

#~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.~.
# List comprehension

prefix = 'abc_'
postfix = '_xyz'

filtered_features = [item for item in values if item.startswith(prefix) and item.endswith(postfix)]

postfix = '_xyz'
new_postfix = ''
features = [item.replace(postfix, new_postfix) for item in values]

postfix = '_xyz'
features = [item + postfix for item in values]

postfix = '_xyz'
col = 'abc'
filtered_features = [item for item in values if item.endswith(postfix) or item == col]
