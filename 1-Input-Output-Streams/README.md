# 🌊 Input/Output Streams

## 🎯 Objectives

- **Read** input from the user or a file.
- **Write** output to the console or a file.

## Writing to the Console

syntax: `print (arg1, arg2, ...)`

The `print` command will convert any object into its `str` version.

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
  * `r+` openf file for reading *and* writing
* `encoding` - how to interpret the characters that you are reading
  * If encoding is not specified, the default is platform dependent 
    * Because UTF-8 is the modern de-facto standard, encoding="utf-8" is recommended unless you know that you need to use a different encoding

```python
file_obj = open("./some_file.txt","r",locale="utf-8")
```
### Read from a File

Once a file has been opened for reading, you can 
* read the whole file into one string (`read()`),
* read the whole file into a list of lines (`readlines()`)
* read one line (`readline()`) or 
* loop over the file object (`for line in file_obj:`).

`read()` **always** returns a string that *includes* the new-line character!

```python
# read everything in the file
file_obj = open("./some_file.txt","r",locale="utf-8")
entire_file: str = file_obj.read()
```

```python
# read only the first 10 bytes in the file
file_obj = open("./some_file.txt","r",locale="utf-8")
entire_file: str = file_obj.read(10)
```

```python
# read first two lines of the file
file_obj = open("./some_file.txt","r",locale="utf-8")
lines: list[str] = file_obj.readlines()
```

```python
# read first two lines of the file
file_obj = open("./some_file.txt","r",locale="utf-8")
line1: str = file_obj.readline()
line2: str = file_obj.readline()
```

```python
# read everything line by line
file_obj = open("./some_file.txt","r",locale="utf-8")
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
file_obj = open("./some_file.txt","w",locale="utf-8")
x = 15
file_obj.write(str(x))  # file has 2 bytes

file_obj = open("./some_other_file.txt","w",locale="utf-8")
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

If a program exits *properly*, all files will be closed automatically.

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

### Copy v1: The Basic Way

Read all characters from an input file to an output file, i.e.: file copy.

```java
public static void copy(String inFileName, String outFileName) {
    FileReader reader = new FileReader(inFileName);
    FileWriter writer = new FileWriter(outFileName);
    int c = reader.read();

    while(c != -1) {
        writer.write(c);
        c = reader.read();
    }

    reader.close();
    writer.close();
}
```

### Copy v2: The More Efficient Way

We will revisit combining streams later in the course!

```java
public static void copy(String inFileName, String outFileName) {
    BufferedReader reader = new BufferedReader(new FileReader(inFileName), 1024);
    BufferedWriter writer = new BufferedWriter(new FileWriter(outFileName), 1024);
    int c = reader.read();

    while(c != -1) {
        writer.write(c);
        c = reader.read();
    }

    reader.close();
    writer.close();
}
```

According to [the Java docs](https://docs.oracle.com/javase/7/docs/api/java/io/BufferedReader.html), the above is more efficient because:

> [`BufferedReader`] will buffer the input from the specified file. Without buffering, each invocation of `read()` or `readLine()` could cause bytes to be read from the file, converted into characters, and then returned, which can be very inefficient.

### Copy v3: The Scanner and PrintWriter Way

To read more than just single characters, we can attach a [_scanner_](https://docs.oracle.com/javase/7/docs/api/java/util/Scanner.html) to an input stream:

![Input Scanner](./images/4-Input-Scanner.png)

- The `Scanner` class has two major kinds of methods: `hasNext()` and `next()`.

To write more than just single characters, we can attach a [_print writer_](https://docs.oracle.com/javase/7/docs/api/java/io/PrintWriter.html) to an output stream:

![Output Print Writer](./images/5-Output-Print-Writer.png)

- The `PrintWriter` class has many overloads to `print()` and `println()`. Above copy example, but now line by line:

```java
public static void copy(String inFileName, String outFileName) {
    Scanner scanner = new Scanner(new FileReader(inFileName));
    PrintWriter writer = new PrintWriter(new FileWriter(outFileName));

    while(scanner.hasNextLine()) {
        writer.println(scanner.nextLine());
    }

    scanner.close(); // Closes the file reader.
    writer.close();
}
```

### Scanner Functions

Consider a text file (or any stream) with numbers and words:

```text
-1 123
abc
3.1415
223372036854775807

----------------------------------------
|-1 123\nabc\n3.1415\n223372036854775807|
----------------------------------------
```

```java
FileReader reader = new FileReader("input.txt");
Scanner scanner = new Scanner(reader);

int x = scanner.nextInt();       // -1
int y = scanner.nextInt();       // 123
String s = scanner.next();       // "abc"
double d = scanner.nextDouble(); // 3.1415
long l = scanner.nextLong();     // 223372036854775807

scanner.close();
```

What happens when the "cursor" sees one thing and we expect another?

We can interpret the content of the file as Java primitives. Ex: summing a file of integers:

```java
public static int sum(String inFileName) {
    Scanner scanner = new Scanner(new FileReader(inFileName));
    int sum = 0;

    while(scanner.hasNextInt()) {
        sum += scanner.nextInt();
    }

    // At this point, we're confident that the next chunk of data is not a int.

    if (scanner.hasNext()) {
        // If we're here, there's still stuff to be read, but it's not a int.
        throw new RuntimeException("Bad input, I need a file that only has ints!");
    }

    scanner.close(); // Closes the file reader.

    return sum;
}
```

`Scanner` reads input by tokens delimited by whitespace by default (regex: `[ \n\t]+`), so the above works for input like this:

```text
736   284
32 409          5432
```

We can use `Scanner` to count the lines and words in a given file:

```java
public static void countLinesAndWords(String inFileName) {
    Scanner scanner = new Scanner(new FileReader(inFileName));
    int lines = 0;
    int words = 0;

    while (scanner.hasNextLine()) {
        lines++;

        while (scanner.hasNext()) {
            words++;
        }
    }

    scanner.close(); // Closes the file reader.

    System.out.printf("%d lines and %d words.", lines, words);
}
```

## ▶️ Exercise 1.1 - Cut

Please click [here](https://github.com/JAC-CS-Programming-4-W23/E1.1-Cut) to do the exercise.

## 📚 References

- [BufferedReader](https://docs.oracle.com/javase/7/docs/api/java/io/BufferedReader.html)
- [Scanner](https://docs.oracle.com/javase/7/docs/api/java/util/Scanner.html)
- [PrintWriter](https://docs.oracle.com/javase/7/docs/api/java/io/PrintWriter.html)


# Advanced Fun Stuff

## Save output to a clipboard

Context: Day 20 of Advent of Code of 2023 was very challenging for me to figure out what was
going on.  I needed to use `graphiz` to graph the data, *repeatedly*.  

To simplify my work flow, I write the output directly the clipboard, and thus I can just paste
what I need into the `graphiz` program.

```python
import pyperclip as pc

class MyGraphiz:
    def __init__(self, machines: list[Machine]):
        self.machines: list[Machine] = machines

        # Create a low-level file
        self.file = StringIO()

    def draw_graph(self):
      
        # print to my low-level file using print (not write)
        # although maybe (write) would work.  ??
        print("digraph G {", file=self.file)
        print("}", file=self.file)

        # go back to the beginning of the file
        self.file.seek(0)
        
        # save the contents of the file into a string
        s=self.file.read()
        
        # copy this string to the clipboard
        pc.copy(s)

```