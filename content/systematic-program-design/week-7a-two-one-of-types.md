Title: Systematic Program Design: Week 7a - Two One-of Types
Date: 2025-12-28 19:50
Category: Systematic Program Design
Tags: computer-science,racket

Module Overview

> Two One-Of Types
In this module we will learn to design functions consuming two arguments that have one-of types. In order to do this, we will develop a new model of our code, the cross product of the types comment table.
The cross product of the types comment table first provides us with a way to clearly think of all possible test cases. We will then find it helps us get a good idea of what our function's body will look like -- and even allow us to simplify it -- before we start coding. In this sense, it plays a role similar to the role of type comments and templates -- and in fact extends our idea of templating from simply what we copy from the types comments to what it really is; a method of knowing a great deal about what code will look like before we start coding details.
Working through the videos and practice materials for this module should take approximately 3-5 hours of dedicated time to complete.

> Learning Goals

> * Be able to produce the cross-product of type templates table for a function operating on two values with one-of types.
* Be able to use the table to generate examples and a template.
* Be able to use the table to simplify the function when there are equal answers in some cells.


I can see how using the cross product of type comments table can apply to the real world.  In the real world, we want our tests to be robust. This is a lesson to keep in mind when writing test cases where the arguments can both be of “one-of” type.  That is, we come up with a table enumerating all possible combinations of the arguments and seeing if we can simplify them.

After I finish this course and get back to using Python, I’m looking forward to see how Systematic Program Design thinking influences the way I write code.  Now that I’m remembering my experiences writing Python code, I’ve dealt with multiple cases before in a similar way to a cond in Racket.  I’m wondering if I had drawn out a table and tried to spot ways to simplify it, would that have resulted in better code?  I guess moving forward I’ll keep this idea in mind.

The instructor states this is a huge idea in all kinds of science and engineering and certainly in software development.
That is, the idea “simplifying at the model level”.  People who say “wait a minute, I can think about that without having to look at the details of the code” or “I can simplify this program before I even type any of the code”, those people are software designers, as opposed to people who just type and pray.  And you want to be those type of people, those who can reason at the model level.
