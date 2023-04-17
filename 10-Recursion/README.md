# 🔄 Recursion

```text
A child couldn't sleep, so her mother told her a story about a little frog,
    who couldn't sleep, so the frog's mother told her a story about a little bear,
         who couldn't sleep, so the bear's mother told her a story about a little weasel...
            who fell asleep.
         ... and the little bear fell asleep;
    ... and the little frog fell asleep;
... and the child fell asleep.
```

A little recursive story. [^1]

[^1]: https://stackoverflow.com/a/2767157

## ▶️ Exercise 10.1 - Simple Recursion

To follow along with the examples below, be sure to download this starter first!

Please click [here](https://github.com/JAC-CS-Programming-4-W23/10.1-Simple-Recursion) to do the exercise.

## ❗️ Factorial

In mathematics, the factorial of a number $n$ is the product of all the numbers from $1$ to $n$:

$$
n! = 1 * 2 * ... * n
$$

For example, the factorial of $5$ is

$$
5! = 5 * 4 * 3 * 2 * 1 = 120
$$

Another way to think about $5!$ is

$$
5! = 5 * 4 * 3 * 2 * 1
$$

$$
5! = 5 * (4 * 3 * 2 * 1)
$$

$$
5! = 5 * 4!
$$

This gives us a "recursive" definition for factorial:

$$
n! = n * (n - 1)!
$$

Code a **recursive** method that implements factorial:

### First Attempt

```java
public static int factorial(int n) {
    return n * factorial(n - 1);
}
```

We will refer to function calls like `factorial(n - 1)` as **recursive** calls.

Do you see any problem with this function?

Let's race the execution of `factorial(5)`:

```text
fact(5) = 5 * fact(4)
              v--------v
              4 * fact(3)
                  v---------v
                  3 * fact(2)
                      v--------v
                      2 * fact(1)
                          v---------v
                          1 * fact(0)
                              v-----v
                              1
                          1 * 1
                          v---v
                      2 * 1
                      v---v
                 3 * 2
                 v---v
             4 * 6
             v---v
         5 * 24
         v----v
         120
```

### Second Attempt

We are missing an important piece of information. The factorial of $0$ is defined to be $1$:

```java
public static int factorial(int n) {
    if (n == 0) {
        return 1;
    }
    else {
        return n * factorial(n - 1);
    }
}
```

Better? There is now an execution path that will **not** make a recursive call. We refer to this as a **base** case.

### Ingredients of Recursion

A call to **itself** makes a function **recursive** and a **base case** is what makes it **stop**!

A recursive call without a base case will result in "infinite" recursion; a recursive function that will repeat "forever". Since we don't have infinite computing resources, we will run out of call stack space and a `StackOverflowException` will be thrown.

There is an important rule about recursive calls:

!> Every recursive call must **approach** the base case.

For example, the call `factorial(-1)` will not terminate in the above function, since each subsequent call will be a negative number.

## 🔢 Evens and Odds

Does the following recursive function lead to infinite recursion?

```java
public static boolean isEven(int n) {
    if (n == 0) {
        return true;
    }
    else {
        return isEven(n - 2);
    }
}
```

If it does, can you fix this method?

!> Please, please, don't use `isEven(n)` in a real program. In fact, most of the things we do in this part of the course is to learn recursion from examples we know we can do non-recursively. Later, we will see some interesting recursion examples and talk about when recursion is the right programming technique to use.

### More Evens and Odds

```java
public static boolean isEven(int n) {
    if (n == 0) {
        return true;
    }

    return isOdd(n - 1);
}

public static boolean isOdd(int n) {
    if (n == 0) {
        return false;
    }

    return isEven(n - 1);
}
```

## 📐 Designing Recursive Functions

### Exercise: Recursive `sum()`

Lets design a recursive function that will compute the sum of an array.

1. We start with an idea for a method. We will design our function with a parameter `index`:

    ```java
    public static int sum(int[] numbers, int index) { ... }
    ```

    Here is a description of what the `sum(numbers, index)` computes: it returns the sum of the elements in `numbers` from `index` to `length - 1`.

2. From this description, we can think of our recursive call as adding the value at `numbers[index]` to the sum of the remaining elements in the array, i.e.: `numbers[index + 1] + numbers[index + 2] + ... + numbers[numbers.length - 1]`.

    ```java
    public static int sum(int[] numbers, int index) {
        return numbers[index] + sum(numbers, index + 1);
    }
    ```

3. This is obviously infinite recursion, so let's add a base case. Aside from needing to stop recursion

    ```java
    public static int sum(int[] numbers, int index) {
        if (index == numbers.length) {
            return 0;
        }
        else {
            return numbers[index] + sum(numbers, index + 1);
        }
    }
    ```

4. Reasoning about termination: each recursive call increases the `index` by $1$ which steps closer and closer to the length of the array at which point we hit the base case.

Since calling the method `sum()` is awkward with the second argument we can restructure like this:

```java
public static int sum(int[] numbers) {
    return sum(numbers, 0);
}

private static int sum(int[] numbers, int index) {
    if (index == numbers.length) {
        return 0;
    }
    else {
        return numbers[index] + sum(numbers, index + 1);
    }
}
```

### Exercise: Recursive `max()`

```java
public static int max(int[] numbers, int index) {
    if (index == numbers.length) {
        return 0;
    }

    int max = max(numbers, index + 1);

    return numbers[index] > max ? numbers[index] : max;
}
```
