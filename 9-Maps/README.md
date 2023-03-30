# 🗺️ Maps

What is a map? A map is an collection of values indexed by keys. Values are accessible by their key, and the map can expand or contract as key-value pairs are added or removed.

In Java, maps are implemented in different ways, which we'll see later. These classes all implement the interface: `Map<K, V>`. The first type parameter is the type of the keys, the second is the type of the values. So a `Map<String, Integer>` has keys of type `String` and values of type `Integer`.

Other names for maps: _dictionaries_, _associative arrays_, _hashes_, etc. The name "map" come from the relationship with mathematical functions. If it helps, you can think of a map as very simple in memory database with a primary key.

Maps are very versatile and can be used to store many things. Here are some examples.

## Student grades

Student grades stored by the student's ID:

```text
{
    1442343 => 72.4,
    1542345 => 94.3,
    1654452 => 83.2,
}
```

What is the datatype of this map?

## Character counts

The count of each character in the word "aardvark".

```text
{
    'a' => 3,
    'r' => 2,
    'v' => 1,
    'd' => 1,
    'k' => 1,
}
```

What is the datatype of this map?

## Animal classification

Animal species with their "class":

```text
{
    "aardvark" => Class.Mammal,
    "aardwolf" => Class.Mammal,
    "albatross" => Class.Avian,
}
```

What is the datatype of this map?

## Coloring in DFS/BFS

In A3 the `Search` class used a map to store colors:

```text
{
    (0, 1) => Color.Black,
    (4, 5) => Color.Grey,
    (0, 0) => Color.Black,
    (2, 0) => Color.White,
}
```

What is the datatype of this map?

## Maps are collections of "entries"

An "entry" is a pair that associates a key with a value, denoted:

```text
key => value
```

Entries will be stores as `Entry<K, V>` objects. The first generic parameter `K` for key datatype and the second generic parameter `V` for value datatypes.

```java
/**
 * Stores an key-value entry in the map.
 */
public class Entry<K, V> {

    private K key;
    private V value;

    /**
     * Create an entry with a key only.
     * @param key
     */
    public Entry(K key) {
        this.key = key;
    }

    /**
     * Create an entry with a key and value.
     * @param key
     * @param value
     */
    public Entry(K key, V value) {
        this.key = key;
        this.value = value;
    }

    /**
     * Get key.
     * @return
     */
    public K getKey() {
        return key;
    }

    /**
     * Get value.
     * @return
     */
    public V getValue() {
        return value;
    }

    /**
     * Set value.
     * @param value
     */
    public void setValue(V value) {
        this.value = value;
    }

    @Override
    public String toString() {
        return String.format("%s => %s", key, value);
    }
}
```

### Rules

- Keys are _unique_, so no duplicates, which just means there is a single entry for each key in the map. The values of the map can be duplicates.
- A key object should not change after being put in the map. Frequently keys are _immutable_ datatypes, ex: `String`. The values can be changed, no problem.
- Keys are not necessarily sorted inside the structure and traversals usually will _not_ return sorted entries.

## Map API

### Put

| Signature    | `void put(K key, V value)`                                                                                                                                                               |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Description  | Associates the specified `value` with the specified key in this map. If the map previously contained a entry for key (`containsKey(key) == true`), the old value is replaced by `value`. |
| Precondition | None                                                                                                                                                                                     |
| Mutator      | Yes                                                                                                                                                                                      |
| Returns      | None                                                                                                                                                                                     |

The put operation has two functions: making a new entry or association, or modifying an association.

### Adding a new entry

```text
{
    a => v1,
    c => v2,
    d => v3,
}
```

and `put(b, v4)` results in:

```text
{
    a => v1,
    c => v2,
    d => v3,
    b => v4,
}
```

### Replacing a value

```text
{
    a => v1,
    c => v2,
    d => v3,
}
```

and `put(c, v4)` results in:

```text
{
    a => v1,
    c => v4,
    d => v3,
}
```

## Get

| Signature    | `V get(K key)`                                     |
| ------------ | -------------------------------------------------- |
| Description  | Retrieve the value mapped to by the specified key. |
| Precondition | The map contains a entry for key.                  |
| Mutator      | No                                                 |
| Returns      | the value to which the specified key is mapped.    |

```text
{
    a => v1,
    c => v2,
    d => v3,
}
```

and `get(c)` results in:

```text
v2
```

## Remove

| Signature    | `V remove(K key)`                                                        |
| ------------ | ------------------------------------------------------------------------ |
| Description  | From this map, remove the entry for the specified key, if it is present. |
| Precondition | None                                                                     |
| Mutator      | Yes                                                                      |
| Returns      | The removed value.                                                       |

```text
{
    a => v1,
    c => v2,
    d => v3,
}
```

and `remove(c)` results in:

```text
{
    a => v1,
    d => v3,
}
```

## Keys

| Signature    | `Set<K> keys()`                          |
| ------------ | ---------------------------------------- |
| Description  | Get all the keys contained in this map.  |
| Precondition | None                                     |
| Mutator      | No                                       |
| Returns      | A set of the keys contained in this map. |

Here the `Set` is the same API as in Assignment 2.

```text
{ a, d, c }
```

## Remaining operations

| Signature    | `void clear()`                            |
| ------------ | ----------------------------------------- |
| Description  | Removes all of the entries from this map. |
| Precondition | None                                      |
| Mutator      | Yes                                       |
| Returns      | None                                      |

| Signature    | `boolean containsKey(K key)`                                              |
| ------------ | ------------------------------------------------------------------------- |
| Description  | Determine is a map contains a entry for the specified key.                |
| Precondition | None                                                                      |
| Mutator      | No                                                                        |
| Returns      | true if this map contains a entry for the specified key, false otherwise. |

| Signature    | `boolean isEmpty()`                                              |
| ------------ | ---------------------------------------------------------------- |
| Description  | Determine if the map is empty: it contains no key-value entries. |
| Precondition | None                                                             |
| Mutator      | No                                                               |
| Returns      | true if this map contains no key-value entries, false otherwise. |

| Signature    | `int size()`                                           |
| ------------ | ------------------------------------------------------ |
| Description  | Determine the number of key-value entries in this map. |
| Precondition | None                                                   |
| Mutator      | No                                                     |
| Returns      | the number of key-value entries in this map.           |

### ▶️ Exercise 9.1 - Maps

Please click [here](https://github.com/JAC-CS-Programming-4-W23/E9.1-Maps) to do the exercise.
