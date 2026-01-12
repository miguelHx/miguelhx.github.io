Title: Intro to CS: Lecture 11 - Aliasing, Cloning
Date: 2025-12-31 19:37
Category: Intro to CS using Python
Tags: computer-science,python

Topics:  Aliasing and cloning

Going over some operations on lists, including .clear(), .pop(), del() and .remove().

Iterating over a list as you are mutating the list can lead to unpredictable behavior.
Takeaway here is to be careful when mutating a list while iterating over it.  Consider using a copy.

= sign on mutable object creates an alias, not a clone.

Big idea:  When you pass a list as a parameter to a function, you are making an alias.

Shallow copy vs. deep copy.
