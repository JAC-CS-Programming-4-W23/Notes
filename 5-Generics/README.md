# 🎭 Generics

## 🎯 Objectives

- **Explain** generic types in Java.
- **Write** utility functions that use generics to make them type agnostic.

## 🐺 The Shapeshifter

We know when declaring a variable in Java, we must specify a type:

```java
class Foo {
    private int element;
}
```

This helps us know what type the value inside the variable is. However, sometimes we want to write a class whose variable types will be determined by the person who instantiates the class. Enter, the generic type.

![Encanto](./Encanto.gif "Generics can transform into any data type!")

```java
class Foo<T> {
    private T element;
}
```

You can think of the generic type `T` as shapeshifter - it can take on any form! In the first example, `element` was forced to be of type `int`. Now that it is generic, it can be any type the user deems it to be:

```java
class Foo<T> {
    private T element;
}

Foo<Integer> foo1 = new Foo();
Foo<String> foo2 = new Foo();
Foo<Boolean> foo3 = new Foo();
Foo<Pokemon> foo4 = new Foo();
```

At runtime, all of the instances of `T` will turn into the type that was specified when the object was instantiated.

## ▶️ Exercises

### `swap()`

Recall in sorting we used the idea of a "swap":

```java
 public static void swap(int[] arr, int i, int j) {
        int holder = arr[j];
        arr[j] = arr[i];
        arr[i] = holder;
    }
```

Issue: if we want to swap double or strings we would require `swap(..)` overloads:

```java
 public static void swap(double[] arr, int i, int j) {
        double holder = arr[j];
        arr[j] = arr[i];
        arr[i] = holder;
    }
```

and

```java
 public static void swap(String[] arr, int i, int j) {
        Strinv holder = arr[j];
        arr[j] = arr[i];
        arr[i] = holder;
    }
```

How about a *generic* method:

```java
 public static <T> void swap(T[] arr, int i, int j) {
        T holder = arr[j];
        arr[j] = arr[i];
        arr[i] = holder;
    }
```

### `count()`

Code a generic method `count` that takes an array and a value and returns the number of times that value occurs withing the array.

Are there any method preconditions?

### `Pair`

We'll fill this one in together as a class:

```java
public class Pair<T> {
    private T first;
    private T second;

    public Pair(T first, T second) {
        this.first = first;
        this.second = second;
    }
}
```

### `Tuple`

Write a generic class with two components that can be of different datatypes.

Hint: a tuple containing a `String` and an `int` would be created with:

```java
Tuple<String, Integer> tuple = new Tuple<>("abc", 123);
```

### `splitAt()`

Code a generic method `splitAt` that take in an array and position `pos` and returns a pair of arrays. The first component of the pair is the array values from indices $[0, pos-1]$ and the second component is $[pos, length-1]$.

Are there any method preconditions?

### `zip()`

Code a generic method `zip` that takes in two arrays and returns a single array with the elements at each indice "paired". For example:

```text
zip([a,b,c,d], [e,f,g,h]) = [(a,e), (b,f), (c,g), (d,h)]
```

Are there any method preconditions?

### Generic Stack

We'll fill this one in together as a class:

```java
public class Stack<T> {
    T[] elements;
}
```

### Identifying Type Variables

Type-level variables are "assigned" type-level values (i.e.: types) during compilation.

What is the type variables (`???`) in the follow code snippet:

```java
String input = "and now for something completely different";
String[] words = input.split(" ");

Utility.swap(words, 0, words.length-1);   // T = ???

Integer[] counts = new Integer[words.length];
Integer[] firsts = new Integer[words.length];

for(int i = 0; i < words.length; i++) {
    counts[i] = Utility.count(words, words[i]);  // T = ???
    firsts[i] = Utility.find(words, words[i]);   // T = ???
}

Pair<???>[] tmp = Utility.zip(counts, firsts);  // T = ???
Tuple<???, ???>[] stats = Utility.zipT(words, tmp); // T = ???, S = ???

System.out.println(Arrays.toString(stats));
```

## ⚖️ Generic Interfaces

Remember `Comparable`?

```java
public interface Comparable<T> {
    int compareTo(T rhs);
}
```

Why is there a type variable here?

Think about what happens when we call `compareTo(..)`:

```java
int comparison = bulbasaur.compareTo(charmander);
```

We want to compare our pokemon (`bulbasaur`) to a `rhs` that is also a pokemon (`charmander`).

It really doesn't make much sense to compare pokemon to anything else:

```java
int comparison = bulbasaur.compareTo(scanner);
int comparison = bulbasaur.compareTo(stack);
int comparison = bulbasaur.compareTo(team); // team is Pokemon[]
```

Java's type rules can enforce this by adding a type argument to the `implements` statement:

```java
public class Pokemon implements Comparable<Pokemon> {

    ...

    public int compareTo(Pokemon rhs) {
       ...
    }
}
```

## 🔬 Observations

### Type Erasure

- Type variables are for type-checking only.
- Types are erased after checking so that's why we have the funny cast

| Pros                          | Cons                                                                                                                      |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| reusable code!                | limited to methods that are available to all objects (without type variable bounds). Ex: .equals(..), .toString(), ... to |
| bad programs don't compile    | might be less efficient for primitives (wrapper classes)                                                                  |
| type checking works perfectly |                                                                                                                           |
| no need to cast return values |                                                                                                                           |
