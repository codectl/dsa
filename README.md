# Data Structures and Algorithms

Contains tips, suggestions and code snippets for different DSA problems.

## Time & space complexity

Table on time & space complexity on different operations over different data structures.

| Operation               | Array / List | String (immutable) |
|:------------------------|:------------:|:------------------:|
| append                  |     O(1)     |        O(n)        |
| pop                     |     O(1)     |        O(n)        |
| insert, not from end    |     O(n)     |        O(n)        |
| update element          |     O(1)     |        O(n)        |
| get                     |     O(1)     |        O(1)        |
| check if element exists |     O(n)     |        O(n)        |

## Patterns

Different patterns solve different problems. See below common patterns:

* [2 pointers, 1 input](src/two_pointers_one_input.py)
* [2 pointers, 2 inputs](src/two_pointers_two_inputs.py)
* [sliding window](src/sliding_window.py)
* [prefix sum](src/prefix_sum.py)

### When to use which?

Each pattern is useful to solve common problems.

#### 2 pointers: 1 input

* is string *s* a palindrome?
* does it exist a pair of numbers on **sorted** array *arr* that meets target?

#### 2 pointers: 2 inputs

* merge sorted arrays
* is string *s1* a substring of string *s2*?
