# 🌊 Input/Output Streams

## 🎯 Objectives

- **Read** input from the user or a file.
- **Write** output to the console or a file.
- **Parse** information from a string.

## Writing to the Console

syntax: `print (arg1, arg2, ...)`

The `print` command will convert any object into a string via the `str()` function.
When printing, all arguments will be separated by a space.

### Formatting (`fstring`)

Reference: [Formatted String Literals](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)

Python has a special type of string (`fstring`) which allows the user to insert the
contents of variables into the string, _and_ the ability to format the output if desired.

Syntax: `f" some string stuff {variable: formatting string} more stuff"`

* Note that the `: format string` is optional.

### Examples

The following shows examples for `int`s and `str`ings.  See 
[documentation](https://docs.python.org/3/library/string.html#formatspec) if you wish to learn
how to format `float`s.

```python
# string alignment
name = "Sandy"
print( f"You are: {name}")           # no special alignment
print( f"You are: {name : >20}")     # right aligned
print( f"You are: {name : <20}")     # left aligned

# integers
i = 301
print( f"{i}")              # no special formatting
print( f"{i:b}")            # print binary
print( f"{i:o}")            # print octal
print( f"{i:5d}")           # right align, reserving 5 spaces for the string
print( f"{i:05d}")          # right align, add leading zeros

```

## Reading From the Console

Reference: [Input](https://docs.python.org/3/library/functions.html#input)

Syntax: `variable: str = input("prompt")`

* `prompt` is optional.
* `input()` returns a string

Example:
```python
name = input("Enter your name: ")
age = input("Enter your age: ")
print ( f"{name} you are {age} years old")
age += 1 #### ERROR, age is a string, not a number!
```

### Reading in Passwords

For security reasons, a user should be able to type in a password without it being seen on the screen
by anyone else.

```python
import getpass
passwd = getpass.getpass("Enter Password: ")
```

## 📖 Files

Reference [Reading and Writing Files](https://www.geeksforgeeks.org/how-to-read-from-a-file-in-python/)

### Open a File

Syntax: `open(filename: str, mode: str, encoding: Optional[str] = None)`

* `filename` is the name of the file that is to be read or written to
* `mode`
  * `r` open file for reading
  * `w` open file for writing
  * `a` open file for appending
  * `r+` open file for reading *and* writing
* `encoding` - how to interpret the characters that you are reading
  * If encoding is not specified, the default is platform dependent 
    * Because UTF-8 is the modern de-facto standard, `encoding="utf-8"` is recommended unless you know that you need to use a different encoding

```python
file_obj = open("./some_file.txt","r",encoding="utf-8")
```
### Read from a File

Once a file has been opened for reading, you can 
* read the whole file into one string (`read()`),
* read the whole file into a list of lines (`readlines()`)
* read one line (`readline()`) or 
* loop over the file object (`for line in file_obj:`).

All the above methods returns string(s) that ***include*** the new-line character!

```python
# read everything in the file
file_obj = open("./some_file.txt","r",encoding="utf-8")
entire_file: str = file_obj.read()
```

```python
# read only the first 10 bytes in the file
file_obj = open("./some_file.txt","r",encoding="utf-8")
entire_file: str = file_obj.read(10)
```

```python
# read first two lines of the file
file_obj = open("./some_file.txt","r",encoding="utf-8")
lines: list[str] = file_obj.readlines()
```

```python
# read first two lines of the file
file_obj = open("./some_file.txt","r",encoding="utf-8")
line1: str = file_obj.readline()
line2: str = file_obj.readline()
```

```python
# read everything line by line
file_obj = open("./some_file.txt","r",encoding="utf-8")
for line in file_obj:
    print(line)
```

### Write to a File

Syntax: `file_obj.write( string )`

Syntax: `print(arg1, arg2, file=file_obj)`

* You must pass a string value to the `write` function.  
  * Any non-string must be converted to a string first!
* `write` does not write the newline character.  You must add that explicitly
* `print` automatically adds the newline character

```python
file_obj = open("./some_file.txt","w",encoding="utf-8")
x = 15
file_obj.write(str(x))  # file has 2 bytes

file_obj = open("./some_other_file.txt","w",encoding="utf-8")
x = 15
print(x, file=file_obj) # on mac or linux, file has 3 bytes (`1`,`2`,`\n`)
```

#### Suffering From Buffering.

Because it is inefficient to constantly read or write to the hard-drive, the OS typically
stores the data in a memory buffer until it is full, and then reads or writes to the hard-drive 
as necessary.

**Try this:**

* Open two terminal windows
* In one window, open a `python` or `ipython` interactive shell.
* Type the following in the `python` shell:
```python
file = open("huh.txt","w")
print("hello sandy",file=file)
```
* Go to the second window and check the contents of the file
  * Mac/linux: `cat huh.txt`
  * Windows: `type huh.txt`
* *There's nothing in it!!!* 

Why?  Because the OS has not written anything to the hard-drive yet, as the buffer would not be full.

So, what do we need to do?

Close the file.

* Go back to the `python` interactive shell
* Type:
```python
file.close()
```
* Now check the contents of your file.  You should be good.

### Closing a File

Syntax: `file_obj.close()`

If a program exits *properly*, all currently open files will be closed automatically.

## File Context Manager

As the above example showed, if your file is not closed properly, you may end up losing data.

The best way to avoid this, is to use the `with` command.  The `with` command creates a `context
manager`. 

A context manager created for a file will
* close the file as soon as the `with` block execution is finished.
* the file will be closed even if an `exception` is thrown while executing the code within the `with` block

```python
with open("some_file.txt","w") as file_obj:     # opens file and creates a context manager
    print("hello sandy", file=file_obj)         # writes to the file
                                                # once the 'with' block is complete, the file ...
                                                # ... will be closed
print("All done")                           
```





## 🐑 Copy a File

### Copy: Small Files Only

```python
def copy(in_file: str, out_file: str):
    '''
    Copy one file to another
    - Not good for large files because we save the contents of the file into memory!
    '''
    with open(in_file, "r") as file:
        file_contents = file.read()
    with open(out_file, "w") as file:
        file.write(file_contents)
```

### Copy: Any Sized File

```python
def copy(in_file: str, out_file: str):
    ''' 
    Copy one file to another
    - behind the scenes, the OS will buffer the data in the most efficient manner
    so no worries about sucking up too much memory
    '''

    with open(in_file,"r") as file_in:
        with open(out_file,"w") as file_out:
            for line in file_in:
                file_out.write(line)
```

## Parsing Input

It's all well and good to read a line from a file, or input from a user, but unless we can
glean information from the data, it won't have much value.

Most of the parsing is done with methods can be applied to strings, for the most obvious reason
that the return value of reading data is always a string.

Reference: [Python Docs](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)

### Substring

To get the *nth* character from a string:

```python
s = input("Enter a string: ")
print (s[3], "is the fourth character in the string")

if len(s) > 10:
    print(s[10], "is the 11th character in the string")

print (s[-1], "is the last character in the string")
```

To get a range of characters (i.e. a substring).  

```python
s = input("Enter a string: ")
print(s[3:5], "are the 4th and 5th characters of the string")
```

Notice that the range does not include the last character specified in the range

`s[i:j]` includes `s[i]`, `s[i+1]`, ... , `s[j-1]`


### Character by Character

Python `str` is an iterable (that means you can loop over its contents), so you
can process one character at a time.

```python
s = "Hello"
for c in s:
    print(c)
```
```text
H
e
l
l
o
```

### Split

Syntax: `str.split(sep=None, maxsplit = -1)`

Returns a list of strings where `sep` defines the deliminator.
* `sep` is a ***single*** character, unless
  * If `sep` is None, the deliminator defaults to any white space
* If `maxsplit` is a positive integer, all splits will occur.

Examples of `split` may be more effective than words, so here are a lot of examples.

```python
a: str = "hello Sandy, how       are you?"
x: list[str] = a.split()
print (x)
```
```text
['hello', 'Sandy,', 'how', 'are', 'you?']
```

```python
a: str = "hello Sandy, how       are you?"
x: list[str] = a.split(maxsplit=2)
print (x)
```
```text
['hello', 'Sandy,', 'how         are you?']
```

```python
a: str = "hello Sandy, how        are you?"
x: list[str] = a.split(",")
print (x)
```
```text
['hello Sandy', ' how         are you?']
```

### Use case

Day 24 of 2023 Advent of Code has input that looks like:
```text
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
```
where the first three integers are `(x,y,z)` coordinates, and the last three integers are
the speed in each of the various directions `(vx,vy,vz)`

So, how to parse the data?
* Read one line at a time (obviously)
* split the string on the `@` symbol to divide the coordinates from the speeds
* split coordinate strings on the ","
* split the speed string on the ","

At this point, we still have strings, not integers, but we will deal with that in the
next section

```python
    with open("input.txt","r") as file:
        for line in file:
            coordinates, speeds = line.split("@")
            x,y,z = coordinates.split(",")
            vx,vy,vz = speeds.split(",")
```

## Converting Strings to Native Types

Everything in python is an object, include `float` and `int`.

```python
s: str = "35"
a: int = int(s)
b: float = float(s)
print(a, b)
```
```text
35 35.0
```

But what if we cannot properly do the conversion?
```python
s: str = "35b"
a: int = int(s)
print(a)
```
```text
ValueError: invalid literal for int() with base 10: '35b'
```

Hmm, how about this not very elegant solution?
```python
s: str = "35b"
succeeded = True
try:
    a: int = int(s)
except ValueError:
    a = 0
    succeeded = False
    
print(succeeded, a)
```

The above is 'sucky'.  Here's a better idea
```python
s: str = "35b"
if not s.isdigit():
    print ("Bad person!")
else:
    print(int(s))
```

`str` class has many methods to determine the contents of the string, so one can check
if the string would be convertible before actually trying to convert it.


## ▶️ Exercise 1.2 - Find Specific Characters in a String

Please click [here](./Exercises/1.2_Find_digits_in_string/REAMDME.md) to do the exercise.

# Advanced

## Redirection (like Bash)

```python
import sys

# reading from a file instead of stdin
with open("inputs.txt", "r") as file:
    sys.stdin = file
    while True:
        x = input()
        try:
            x = input()
            print(x)
        except EOFError:
            break
sys.stdin = sys.__stdin__

input("press enter to continue")

# writing to a file instead of console
with open("outputs.txt","w") as file:
    sys.stdout = file
    print("Hello There")
sys.stdout = sys.__stdout__

print ("All done")
```

## Read and Write to a String

You can create an internal buffer that acts just like a file.

[Python Documentation](https://docs.python.org/3/library/io.html#io.StringIO)

```python
import io

inputs = io.StringIO()
while True:
    s = input("Enter Message: ")
    if s == "END":
        break
    elif "sandy" not in s:  
        print(s, file=inputs)

inputs.seek(0)
msg = inputs.read()
# do stuff with msg?

inputs.close()
```

## Save output to a clipboard

Context: Day 20 of Advent of Code of 2023 was very challenging for me to figure out what was
going on.  I needed to use `graphiz` to graph the data, *repeatedly*.  

To simplify my work flow, I write the output directly to the clipboard, and thus I can just paste
what I need into the `graphiz` program.

```python
from io import StringIO
import pyperclip as pc

class MyGraphiz:
    def __init__(self, machines: list[Machine]):
        self.machines: list[Machine] = machines

        # Create a low-level file
        self.file: StringIO = StringIO()

    def draw_graph(self):
      
        # print to my internal buffer
        print("digraph G {", file=self.file)
        # ... other stuff
        print("}", file=self.file)

        # go back to the beginning of the file
        self.file.seek(0)
        
        # save the contents of the file into a string
        s: str = self.file.read()
        
        # copy this string to the clipboard
        pc.copy(s)

```

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

