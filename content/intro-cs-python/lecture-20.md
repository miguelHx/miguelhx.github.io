Title: Intro to CS: Lecture 20 - Fitness Tracker OOP Example
Date: 2026-01-15 10:00
Category: Intro to CS using Python
Tags: computer-science,python

Topics:  Inheritance: more examples

Reinforcing same concept as previous lectures but with a more involved example.
I learned something new.  You can get the class state by doing something like this:  SimpleWorkout.\__dict__.keys()
You can do the same on an instance variable.

Most of this was review for me, again.  I’ll keep mentioning that.

### Object Oriented Design: More Art than Science

* OOP is a powerful tool for __modularizing__ your code and grouping state and functions together
* BUT
* It is __possible to overdo__ it (aka over-engineering)
    * New OOP programmers often create elaborate class hierarchies
    * Not necessarily a good idea
    * Think about the users of your code
        * Will your decomposition make sense to them?
    * Because the function that is invoked is implicit in the class hierarchy, it can sometimes be difficult to reason about control flow

