# ✈️ Traversals

## 🎯 Objectives

- **Explain** what problems a traversable interface solves.
- **Design** a traversable interface API.
- **Implement** a traversable queue in Java.

## 🐒 From One to the Next

![Traversing](./Tarzan-Traversal.gif)

Question: you are storing integer values in a stack. You want to know something about the data, for example "what is the largest (or smallest) value?", or "is 123 somewhere in the stack", or maybe you just want to output the current stack values.

Options:

1. Pop the elements of the stack and perform the check. Problem: the stack is empty at the end of this, what if we still needed those values in stack. Pushing them back will invert the order unless we are careful.

2. We can add `min`, `max`, `find`, etc... to the `Stack<T>` class.

   !> Problem: most of these operations are type-dependant, for example `min` and `max` only exists for `Comparable` types.

3. Write a "getter" for the array `elements`.

   !> Problem: direct access to the array might mean the caller breaks LIFO.

4. Write a `toArray` that will return a copy of the current array elements.

   !> Problem: allocating an array takes time and memory.

5. Add methods to the `Stack<T>` class that return each element in the stack, one by one.

We can think of a traversal as "scanning" a collection.

## 📐 Traversal Design

<!-- tabs:start -->

### **reset**

| Signature    | `void reset()`                                                                                                                                            |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Description  | Initialize a traversal. If there are elements, the traversal cursor is positioned on the first element. Otherwise, the traversal is complete (trivially). |
| Precondition | None.                                                                                                                                                     |
| Mutator      | Yes, but only the traversal portion.                                                                                                                      |
| Returns      | None.                                                                                                                                                     |

### **hasNext**

| Signature    | `boolean hasNext()`                                                    |
| ------------ | ---------------------------------------------------------------------- |
| Description  | Determine if a traversal can continue.                                 |
| Precondition | The traversal has been initialized.                                    |
| Mutator      | No.                                                                    |
| Returns      | `true` is there are elements left in the traversal, `false` otherwise. |

### **next**

| Signature    | `T next()`                                                                                                                                                                         |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Description  | If there is a next element, the traversal cursor has advanced to it and it is returned. At the end of the traversal, it is *undefined*, meaning it no longer refers to an element. |
| Precondition | The traversal has been initialized. The traversal still has at least one element left.                                                                                             |
| Mutator      | Yes, but only the traversal portion.                                                                                                                                               |
| Returns      | The current element in the traversal, and then advance the traversal cursor to the next element.                                                                                   |

<!-- tabs:end -->

!> Note: these are slightly simpler than the version in A2. They don't have preconditions relating to mutation during traversal.

## ▶️ Exercises

### Printing

Here is how we might use a traversal to "print" a traversable collection:

```java
public static <T> void print(Traversable<T> traversal) {
    traversal.reset();

    while(traversal.hasNext()) {
       System.out.println(traversal.next());
    }
}
```

### Range

```java
public class Range implements Traversable<Integer> {

    private int lower;
    private int upper;

    public Range(int upper) {
        this(0, upper);
    }

    public Range(int lower, int upper) {
        if(lower > upper)
            throw new RuntimeException("Impossible range.");
        this.lower = lower;
        this.upper = upper;
    }

    ...

    @Override
    public String toString() {
        return "[" + lower + ".." + upper + "[";
    }
}
```

What does this output:

```java
Range r = new Range(2, 6);
int sum = 0;

r.reset();

while(r.hasNext()) {
   sum += r.next();
}

System.out.println(sum);
```

### ▶️ Exercise 6.1 - Traversable Queue

Please click [here](https://github.com/JAC-CS-Programming-4-W23/E6.1-Traversable-Queue) to do the exercise.
