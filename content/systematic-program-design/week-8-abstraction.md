Title: Systematic Program Design: Week 8 - Abstraction
Date: 2025-12-31 12:00
Category: Systematic Program Design
Tags: computer-science,racket

> ### Abstraction Module
In this module we look another techniques for improving the structure of code. Most of the problems in this module involve refactoring existing programs -- so there's relatively little new coding to do. But that doesn't mean you won't be designing programs! One of the things that separates good programmers from the other kind is taking the time to improve the structure of their code once it is written. This material is super important, and... it is really important to practice doing it!

> This module covers abstraction which is a technique for taking highly repetitive code and refactoring out the identical parts to leave behind a shared helper and just the different parts of the original code. The shared helper is called an abstract function because it is more general, or less detailed, than the original code.

> Abstraction is a crucial technique for managing complexity in programs. One aspect of this is that it can make programs smaller if the abstract functions are used by many other functions in the system. Another aspect is that it helps separate knowledge domains more clearly in code. All the work you've done understanding templates is about to give you a nice surprise.
Working through the videos and practice materials for this module will take approximately 7-12 hours of dedicated time to complete.

> ### Learning Goals

> * Be able to identify 2 or more functions that are candidates for abstraction.
* Be able to design an abstract function starting with 2 or more highly repetitive functions (or expressions).
* Be able to design an abstract fold function from a template.
* Be able to write signatures for abstract functions.
* Be able to write signatures that use type parameters.
* Be able to identify a function which would benefit from using a built-in abstract function
* Be able to use built-in abstract functions

A new technique for managing complexity is to reduce redundancy in programs using abstraction.

A higher order function can
* Consume one or more functions
* Produce a function

I’ve come across higher order functions before but don’t remember their exact definition so this is a good review.

Next we learn how to abstract a function.  This is useful in the real world.
How to abstract:
Identify two highly repetitive expressions. Introduce a new function

* Around one copy of repetitive code
* With a more general name
* Add a parameter for varying position

Replace specific expressions

* With calls to abstract function
* Pass varying value


We are introduced to the idea that functions can consume other functions as arguments.  This is covered early on in the Intro to CS course from MIT.

We go over some built-in abstract functions such as map and filter.  These are also used in languages such as python and javascript.  

Next up (still in week 8) is closures, another important concept in programming.

We are walked through the implementation of foldr abstract function to build understanding.

We are introduced to using built-in abstract functions such as map and filter.

The example with the element directory structure seems to be Racket specific, I don’t anticipate it being used outside of this course.
But the concept of using built-ins and referencing their documentation will definitely apply outside of this course.