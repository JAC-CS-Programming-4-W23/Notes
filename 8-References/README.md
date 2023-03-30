# 🔗 References

> I'm still working on polishing these notes so they're a little hard to read, so please bear with me! Thanks :)

## Memory - Call Stack

The call stack is a stack data structure that stores information about the active subroutines of a computer program. This kind of stack is also known as an execution stack, control stack, run-time stack, or machine stack, (wikipedia)

### Exercise: draw the call stack

```java
public static void main(String[] args) {
    int x = 123;
    int y = 124;
    int z = min(x, y);

    System.out.println(z);
}

public static int min(int x, int y) {
    if (x < y) {
        return x;
    }
    else {
        return y;
    }
}
```

Include "return address" (location of statement where this method was called)

```java
public static int min(int x, int y, int z) {
    int m = min(x, y);

    return min(m, z);
}
```

## Reference Types

To study reference types, we will use a simple class whose fields are primitives:

```java
public class Point {
    private int x;
    private int y;

    // constructor, getters and setters, toString

    public double getDistance(Point p) {...} // computes the distance between two points

    public boolean equals(Point rhs) {
        return this.x == rhs.x && this.y == rhs.y;
    }
}
```

```java
int x = 123;
Point p = new Point(1, 2);
```

### Variables for reference types are references

```text
x: [value]           <- primitive type (value)
r: [o]->[object]     <- reference type (object)
```

```java
int x = 42;
int y;
y = x; // draw memory

Point p = new Point(1, 2);
Point q;
q = p; // draw memory
       // called an "alias"

q.setX(3);

System.out.println(p)
```

- draw: including frame

```java
void f() {
    int x = 1;
    int y = 2;
    Point p = new Point(x, x+1);
    Point q = new Point(p.getX(), y);
    Point r = p;

    r.setY(4);
}
```

## Reference Comparison

- `==` is the same for non-primitives, except it compares addresses not the objects!

- `p == q` is true if `p` and `q` refer to the same object, `p != q` otherwise.

```java
Point p = new Point(0, 0);
Point q = p;
Point r = q;
// r == p ?
q = new Point(1, 1);
// q == p ?
// r == p ?
p = new Point(1,1);
// p == q ?
//p.equals(q) ?
```

- object identity vs. equality:

### Example continues

```java
double getPerimeter(Scanner scanner) {
    Point current = readPoint(scanner);
    Point first = current;
    double perimeter = 0.0;

    while (scanner.hasNext()) {
        Point next = readPoint(scanner);
        perimeter += current.getDistance(next); // Returns a double
        current = next;
    }

    if (current == first) {
        throw new RuntimeException();
    }

    perimeter += current.getDistance(first);

    return perimeter;
}

Point readPoint(Scanner scanner) {
    int x;
    int y;

    if (!scanner.hasNextInt()) {
         throw new Exception();
    }

    x = scanner.nextInt();

    if (!scanner.hasNextInt()) {
        throw new Exception();
    }

    y = scanner.nextInt();

    return new Point(x, y);
}
```

### Dynamic Allocation

- New objects (created with `new`) are dynamically allocate by the OS, in a region of memory called the "heap".

```
Point p = new Point(0,0);

        Point
p[0]->[x=0,y=0]
```

- students: draw the following:

- V1: no error handling

```java
    public double perimeter(Scanner s) {
          Point first = read(s);
          Point current = first;
          double p = 0.0;
          while(s.hasNext()) {
              Point next = read(s);
              p += current.dist(next);
              current = next;
          }
          if(current == first)
              throw new RuntimeException("Single point in file.");

          p += first.dist(current);
          return p;
      }
```

## Review of references (first class)

- primitives vs. non-primitives (reference types)
- address of object
- drawing
- aliases
- dereferencing

## Dynamic store, aka "heap"

- new objects created in the heap and exist beyond th

- heap memory is finite! object must eventually be removed: object are deallocated (memory
    "recycled") automatically in Java

- The "garbage collector" executes are intervals and removes all dynamic memory that no longer has
    references.

- ex: above example with collecting, including frame pop

## null

- absence of an object. implemeneted as a bad address.
- drawn as a slash
- Point p;    p<code>[/]</code>

- you can intentionally null a reference

```
        Point p = new Point(0,0);
        p = null;
```

- you can test that a reference is null

```
    if(p == null)
      ...
```

- Ex:

- What happens if you dereference a null ?

```
Point p; // eq: Point p = null;
p.setX(2); -> throws NullPointerException
```

- Do we check for null for each call? No.
    -> programmer uses logic to check null only if necessary.
    -> be aware of techniques that use null.

### ▶️ Exercise 8.1 - Linked List

Please click [here](https://github.com/JAC-CS-Programming-4-W23/E8.1-Linked-List) to do the exercise.

### ▶️ Exercise 8.2 - Array List

Please click [here](https://github.com/JAC-CS-Programming-4-W23/E8.2-Array-List) to do the exercise.
