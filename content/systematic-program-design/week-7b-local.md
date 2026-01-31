Title: Systematic Program Design: Week 7b - Local
Date: 2025-12-28 19:54
Category: Systematic Program Design
Tags: computer-science,racket

> In this module we look at a new technique for improving the structure of code. Most of the problems in this module involve refactoring existing programs -- so there's relatively little new coding to do. But that doesn't mean you won't be designing programs! One of the things that separates good programmers from the other kind is taking the time to improve the structure of their code once it is written. This material is super important, and... it is really important to practice doing it!

> We'll learn local expressions which are a new kind of expression in the Intermediate Student Language (ISL) that makes it possible to write definitions (constants, functions and structures) that are only visible within the local expression. We will see how to use local expressions to encapsulate "private" helper functions. We will also use local to avoid redundant computation.
Working through the videos, practice materials and the design quiz for this module should take approximately 8-10 hours of dedicated time to complete.

> Learning Goals

> * Be able to write well-formed local expressions.
* Be able to diagram lexical scoping on top of expressions using local.
* Be able to hand-evaluate local expressions.
* Be able to use local to encapsulate function definitions.
* Be able to use local to avoid redundant computation.


### Intro

We're going to look at two important ways to use local.  One has to do with organizing programs that are large or written by more than one person. Another has to do with dealing with important performance problems that come up when we can't use local.

I like that they’re going over Lexical Scope.  This concept definitely applies to all programming languages, and is one of the fundamentals.

Also went over the local construct.  This allows for local variables inside a function in Racket.

Next up is the concept of encapsulation, which the instructor states is one of the most fundamental concepts in software engineering.  It lets us take each part of our program and make it into a “capsule”, a little package that has a bunch of internal functions and constants and structures, and only a small number of external functions and constants and structures.

We practice this concept by taking mutually referencing functions and putting them in a local under a unified function name.  This is basically a refactor.  The instructor gives us the definition of refactor:  changing a programs code/structure without changing the program’s behavior.  I’ve done this before in a professional setting so this isn’t new to me.

I want to take all of these important concepts and list them when I write the review of this course.

Idea:  take 2 or more functions, hide all the helpers inside a capsule, so that the rest of the world only sees the functions that are appropriate for them to call.

Avoiding recomputation - so far in this course, we avoided talking about performance or program efficiency. This was on purpose because it’s easy for programmers to worry too much about efficiency, too soon, or reason incorrectly about it.

As a general rule, it’s better to design a simple program that’s easy to understand/change, and then worry about the efficiency later, once the program is running.  You can run the program against a sample data set and measure the performance and see where the real performance problems are.

You might be surprised.  Some things you think might be performance problems turn out to be handled by the programming language.  Other things you thought turn out not to be.  Then there’s things you didn’t think would be performance problems but turn out to be.

That said, there’s one category of performance problems that you need to fix as part of the design.  That is, exponential growth.

We are given the example of performing a find on a skinny tree that duplicates the procedure find element in its code and replace that duplication with computing once in a local and referencing that result instead.