Title: Intro to CS: Lecture 16 - Recursion on Non-Numerics
Date: 2026-01-09 10:00
Category: Intro to CS using Python
Tags: computer-science,python

Topics: Recursion: Fibonacci, Fibonacci with a dict, recursion on non-numerics, recursion on lists, Towers of Hanoi (extra)

We start by reviewing fibonacci and tracing through the function call graph.  Recursion in general is review for me, I still think this lecture is good for me to digest.

After doing another recursion example of basketball scores, we apply the idea of recursion to lists.   The first example is sum all elements in a list.

The idea is similar to how we would sum elements in a list in the Systematic Program Design course.  The instructor states that we need to trust that the recursive calls do the right thing.  The instructor from SPD says the same thing !  Trust the natural recursion.

Why use recursion?  Some problems are very difficult to solve with iteration.

Intuition for when to use recursion:

* In the list examples so far, we knew how many levels we needed to iterate
    * Either look at elements directly or one level down
* But lists can have elements that are lists, which can in turn have elements that are lists, which can in turn have elements that are lists, etc.
* How can we use iteration to do these checks? It’s hard

Problems that are naturally recursive:

* A file system
* Order of operations in a calculator

I like the example they gave of reverse a list of elements, all sub-elements get reversed too, leaving the code here for reference:

```python
def deep_rev(L):
    if L == []:
        Return []
    elif type(L[0]) != list:
        Return deep_rev(L[1:]) + [L[0]]
    else:
        Return deep_rev(L[1:]) + [deep_rev(L[0])]
```

I also like the finger exercise for flattening an arbitrarily-nested list, so I will include code here for reference:

```python
def flatten(L):
    result = []
    for i in L:
        if type(i) == list:
            result.extend(flatten(i))
        else:
            result.append(i)
    return result
```