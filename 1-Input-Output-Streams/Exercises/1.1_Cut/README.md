# Create an Equivalent of Linux `cut` Command

## Learning Objectives:

* Reading and Writing to Files
* Parsing Inputs

## Description

### What Does the Linux `cut` Command Do?

The linux `cut` command is a very useful tool that will parse an input stream and extract
information about a specified column (or columns) based on a specific deliminator.

Some of the options to `cut` are:
* `-d` define a single character deliminator
* `-c` define which columns to cut
* `-f` if you specify a deliminator, which fields do you want

Again, examples are better than words.

The following is what Ian and Sandy did to kill all the processes by a student who accidentally(?) started an infinite
loop of processes: (output always uses the same columns, so it is ok to hard-code)

Output from the `ps -ef` command
```text
sandy     467259  467258  0 12:15 pts/0    00:00:00 -bash
sandy     467402  467259  0 12:24 pts/0    00:00:00 ps -ef
sandy     467403  467259  0 12:24 pts/0    00:00:00 grep --color=auto sandy
```
bash code
```bash
for pid in $(ps -ef | grep $student | cut -c10-16) 
do 
  echo $pid  # verify that its working before you actually try to kill process!
  # kill -9 $pid  # don't do this if you don't know what you are doing
done
```

Getting the name and comment field of all users from the `/etc/passwd` file

Input
```text
sandy:x:1001:1001:Sandy Bultena:/home/sandy:/bin/bash
chris:x:1002:1002:Chris Chadillon:/home/chris:/bin/bash
```
Code
```bash
cut -d ":" -f 1,5 /etc/passwd
```

## Challenge 1 

Create a python script that will read in a file and print the output of the specified columns.

* Create a file, and write some stuff to it.
* Finish the following code

```python
def main():
    filename: str = input("Enter filename to read: ")
    column_start: int = int(input("First column: "))
    column_end: int = int(input("Last column: "))
    cut(filename, column_start, column_end)
    
def cut(filename: str, column_start: int = 0, column_end: int = -1):
    '''
    Reads a file, and prints only the characters that appear in the specified column
    '''

if __name__ == "__main__":
    main()
```

## Challenge 2 

Create a python script that will read a file, and print a specific field for
each line in the file, given a specific deliminator

* Create a file, and write some stuff to it.
* Finish the following code

```python
def main():
    filename: str = input("Enter filename to read: ")
    field_num: int = int(input("Which field do you want to read?" ))
    deliminator: int = input("Specify the deliminator to use: ")
    cut(filename, field_num, deliminator)
    
def cut(filename: str, field_num: int, deliminator: str):
    '''
    Reads a file, ...
    '''

if __name__ == "__main__":
    main()
```

