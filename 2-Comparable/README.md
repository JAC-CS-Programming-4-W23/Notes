# ⚖️ Comparable

## 🎯 Objectives

- **Create** a class whose objects can be compared (`<`, `<=`, `==`, etc)
- **Sort** a collection of `Comparable` objects.
- **Trace** the binary search algorithm.
- **Find** a particular object in collection of `Comparable` objects using binary search.

## 🔢 The Natural Order

While having different meanings in [philosophy](https://en.wikipedia.org/wiki/Natural_order_(philosophy)) and [biology](https://en.wikipedia.org/wiki/Ordo_naturalis), the "natural order" of things in computer science usually refers to the way strings and numbers are ordered in a list.

[![Lemon Lime](./images/1-Lemon-Lime.gif "Does lemon come before lime? Or vice versa? They're both citruses, after all!")](https://medium.com/@aubreysinden/compare-and-contrast-bridge-lightroom-3a4adb038f15)

This should make sense when it comes to strings and numbers, but how do you order a list of objects? What's the criteria that makes one object greater/less than another object of the same type?

## ⚖️ Comparing Objects in Python

Reference: [Basic Customization](https://docs.python.org/3/reference/datamodel.html#basic-customization)

When python compares objects, it uses pre-defined methods on those objects.

For two objects to be comparable, they must have a subset of the following methods:

```python
def __lt__(self, other): pass
def __le__(self, other): pass
def __eq__(self, other): pass
def __ne__(self, other): pass
def __gt__(self, other): pass
def __ge__(self, other): pass
```

Certain built-in functions in python require some, but typically not all, of these methods
for comparing two objects.

### Example:
```python
from typing import Protocol


class Month:
    def __init__(self, month: str, index: int):
        '''
        Inputs: month - a string representing the name of the month
                index - Which month of the year?  i.e. May is the 5th month of the year
        '''
        self.month: str = month.upper()
        self.index: int = index

    def __eq__(self, other) -> bool:
        return self.index == other.index

    def __lt__(self, other) -> bool:
        return self.index < other.index

    def __str__(self):
        return self.month


m1 = Month("april", 4)
m2 = Month("JAN", 1)

if m2 < m1: print(m1, m2)  # prints: April Jan

# even though '__gt__' was not defined, it can be inferred from __lt__ and __eq__
if m1 > m2: print(m1, m2)  # prints: April Jan

if m1 < m2: print(m1, m2)  # prints nothing

if m1 != m2: print(m1, m2)  # prints: April Jan

if m1 == m2: print(m1, m2)  # prints nothing


# ================================================================
# Using a protocol via duck typing
# ================================================================
class LessThanProtocol(Protocol):
    def __lt__(self, other) -> bool: pass


# Define a function that requires the protocol
def earliest(arg1: LessThanProtocol, arg2: LessThanProtocol):
    if arg1 < arg2:
        print(arg1, "is the earliest")
    else:
        print(arg2, "is the earliest")


# Works for months, and integers (`int` is a class, which implements `__lt__`)
x = 3
y = 7
earliest(m1, m2)
earliest(x, y)
```

## ▶️ Exercise 2.1 - Comparable

Please click [here](./Exercises/2_1_Comparable/README.md) to do the exercise.

## 🔍 Sorting & Searching


[![Quick Sort](./images/2-Quick-Sort.gif "A visualization of the quick sort algorithm.")](https://lamfo-unb.github.io/2019/04/21/Sorting-algorithms/)

If you keep a sorted collection of objects, then you can use the built-in python sort methods, 
as long as the objects in the collection implement `__lt__`! 

### Binary Search

As you should already know, searching becomes trivial if our data is already sorted:

[![Binary Search](./images/3-Binary-Search.gif "Binary search vs linear/sequential search.")](https://blog.penjee.com/binary-vs-linear-search-animated-gifs/)

In most cases, binary search will trounce linear sort.

### Python Implementation For Integers

```python
from typing import Optional

def binary_search_find_index_of_value(data: list[int], value: int) -> Optional[int]:
    low: int  = 0
    high: int = len(data) - 1
    mid: int = (low + high) // 2   # // is integer division
    
    while low <= high:              
        if data[mid] < value:           # value would be on the right side
            low = mid + 1
        elif value < data[mid] :         # value would be on the left side
            high = mid - 1
        elif data[mid] == value:        # have we found it?
            return mid                  # return the index
        
        mid = (low + high) // 2         # recalculate the mid-point
    
    return None                         # we've looked everywhere and we can't find it
```

## ▶️ Exercise 2.2 - Sort & Search

Please click [here](./Exercises/2_1_Comparable/README.md) to do the exercise.

## 📚 References

- [Binary vs. linear search](https://blog.penjee.com/binary-vs-linear-search-animated-gifs/)


# Copyright Notice

All notes in this package are copyrighted under the Creative Commons License CC BY-NC

This license enables reusers to distribute, remix, adapt, and build upon 
the material in any medium or format for noncommercial purposes only, and only 
so long as attribution is given to the creator. 

CC BY-NC includes the following elements:

 BY: credit must be given to the creator.
 NC: Only noncommercial uses of the work are permitted.

Notes originated from Ian Clement, and modified by Vikram Singh.  
They have been subsequently modified by Ian Clement and Sandy Bultena.

All rights reserved (c) 2024
