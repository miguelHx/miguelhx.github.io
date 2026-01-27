Title: Intro to CS: Lecture 21 - Timing Programs, Counting Operations
Date: 2026-01-19 10:00
Category: Intro to CS using Python
Tags: computer-science,python

Topics:  Complexity: measuring efficiency, timing programs, counting operations

Efficiency is important.

* Separate time and space efficiency of a program
* Tradeoff between them:  can use a bit more memory to store values for quicker lookup later
    * Think fibonacci recursive vs. fibonacci with memoization
* Challenges in understanding efficiency
    * A program can be implemented in many different ways
    * You can solve a problem using only a handful of different algorithms
* Want to separate choice of implementation from choice of more abstract algorithm

Introduced to python’s time module, which will help time programs.

Timing programs is inconsistent.  So we count operations as an attempt to get a more consistent evaluation.
