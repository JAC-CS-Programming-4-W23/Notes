# 🚏 Queues

## 🎯 Objectives

- **Explain** the queue data structure.
- **Design** a queue data structure.
- **Solve** a problem using a queue.
- **Implement** a queue data structure in Java.

## ↪️ First in, First out

[![Bus Stop](./images/1-Bus-Stop.gif "The word 'queue' in the UK refers to what we call a 'line'.")](https://dribbble.com/shots/6290600-We-are-heroes)

A queue is a *collection* of data, just like a stack, only with a different set of rules. And like a stack, we refer to individual data items in the collection as *elements*.

A queue is a **FIFO** collection: the *first* element added to the queue is the *first* element to leave.

?> Recall that a *stack* is **LIFO**: last in, first out. Imagine a world where all our line-ups were LIFO instead of FIFO!

Let's draw a queue like this:

![Queue diagram](images/queue1.png)

- **front:** the element at the first position in the queue.
- **rear:** the element in the last position in the queue.
- **empty:** where there are no elements in the queue.
- **capacity:** the maximum number of elements in the queue.

## 📐 Queue Design

For every operation we design we will consider:

1. A description of what the operation accomplishes.
2. What the operation is called, what are it's inputs and outputs. This is called the *signature*.
3. What are the operation's *preconditions*, that is, what condition is required to be met in order to call the method.
4. What are the operation's *postconditions*, that is, what are the expected changes  the object when the operation is called.

### ▶️ Exercise 4.1 - Queue Design

Again, lets only consider a collection `int` for now to keep it simple.

A *enqueue* operation adds an element to the rear of the queue.

![Enqueue](images/queue2.png)

A *dequeue* operation removes an element from the front of the queue.

![Dequeue](images/queue3.png)

What is a possible problem: queue *underflow*.

![Queue underflow](images/queue4.png)

What is a possible problem: queue *overflow*.

![Queue overflow](images/queue5.png)

| `enqueue()`  |                                          |
| ------------ | ---------------------------------------- |
| Description  | Add an element to the rear of the queue. |
| Signature    | `void enqueue(int element)`              |
| Precondition | queue is not full.                       |
| Mutator      | Yes                                      |
| Returns      | `element` is the new rear of queue.      |

| `dequeue()`  |                                        |
| ------------ | -------------------------------------- |
| Description  | Remove an element from the queue.      |
| Signature    | `int dequeue()`                        |
| Precondition | queue is not empty.                    |
| Mutator      | Yes                                    |
| Returns      | the element is removed from the queue. |

| `front()`    |                                                           |
| ------------ | --------------------------------------------------------- |
| Description  | Get the front element of the queue.                       |
| Signature    | `int front()`                                             |
| Precondition | Queue is not empty.                                       |
| Mutator      | No                                                        |
| Returns      | The front element is returned and the queue is unchanged. |

| `isEmpty()`  |                                                                                  |
| ------------ | -------------------------------------------------------------------------------- |
| Description  | Check if the queue is empty.                                                     |
| Signature    | `boolean isEmpty()`                                                              |
| Precondition | None.                                                                            |
| Mutator      | No                                                                               |
| Returns      | Returns `true` if the queue is empty, `false` otherwise. The queue is unchanged. |

| `isFull()`   |                                                                                 |
| ------------ | ------------------------------------------------------------------------------- |
| Description  | Check if the queue is full.                                                     |
| Signature    | `boolean isFull()`                                                              |
| Precondition | None.                                                                           |
| Mutator      | No                                                                              |
| Returns      | Returns `true` if the queue is full, `false` otherwise. The queue is unchanged. |

!> "Queue exists" precondition: the existence of the object is required for all operations so we will omit it as a precondition. It will be considered incorrect on test.

### ▶️ Exercise 4.2 - Queue Implementation

Please click [here](https://github.com/JAC-CS-Programming-4-W23/E4.2-Queue-Array) to do the exercise.

## ⭕️ Circular Queue

How do we *not* run out of space at the end of the array? Where is there space to be *had*? What if we could reclaim the lost space in the lower portion of the array?

- **Idea 1**: How about when we hit the end, we shift everything back down to the lower portion of the array. Moving back to the original space.
- **Idea 2**: How about we let the queue "wrap" around the edges of the array. It would be as if the array we're a circle.

The first idea seems easy enough to code. We will sometimes have a costly `enqueue` operation. The second idea can be confusing at first, but has the potential to be efficient for all operations!

Here is an example of a "circular" array with **idea 1** in purple and **idea 2** in blue and green:

![Circular Queue](./images/Circular-Queue.mp4 ':include :type=video controls width=100%')

?> An array is never really circular. We will code our use of array indices to treat the boundary between the `0` index array and the `capacity - 1`.

### ％ Modulus

A standard way to implement the circular array is to use the modulus operation `%`. To see this, take a look at this sequence of expressions using the `%` operator, imagining that we have an array of length 4:

```text
0 % 4 = 0
1 % 4 = 1
2 % 4 = 2
3 % 4 = 3
4 % 4 = 0
5 % 4 = 1
6 % 4 = 2
... and so on ...
```

What we see is that any positive number `x` could be "flattened" into an array position between `0` and `length - 1`. We can now use this for our `enqueue()` and `dequeue()` methods!

### ▶️ Exercise 4.3 - Circular Queue

Please click [here](https://github.com/JAC-CS-Programming-4-W23/E4.3-Circular-Queue) to do the exercise.

## 📚 References

- [Application Programming Interface](https://en.wikipedia.org/wiki/API)
