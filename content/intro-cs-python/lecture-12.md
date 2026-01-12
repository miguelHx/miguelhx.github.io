Title: Intro to CS: Lecture 12 - List comprehension, functions as objects, testing, debugging
Date: 2026-01-01 10:00
Category: Intro to CS using Python
Tags: computer-science,python

Topics: More Functions as Objects, Keyword Arguments, Default Arguments, Debugging: glass box/black box testing, examples


List comprehensions are review for me.  Default parameters are also review.

Functions can return another function.  Why bother returning functions?

* Code can be rewritten without returning function objects
* Good software design
    * Embracing ideas of decomposition, abstraction
    * Another tool to structure code
* Interrupting execution
    * Example of control flow
    * A way to achieve partial execution and use result somewhere else before finishing the full evaluation


Going over testing and debugging.

### Testing

Break up code into modules that can be tested and debugged individually. Document constraints on modules.  What do you expect input/output to be?
Document assumptions behind code design.

When are you ready to test?

* Ensure code runs
    * Remove syntax errors
    * Remove static semantic errors
    * Python interpreter can usually find these for you
* Have a set of expected results
    * An input set
    * For each input, the expected output

Classes of tests

* Unit testing
    * Validate each piece of program
    * Testing each function separately
* Regression testing
    * Add test for bugs as you find them
    * Catch reintroduced errors that were previously fixed
* Integration testing
    * Does overall program work?
    * Tend to rush to do this

These testing concepts definitely come up in the real world on the job, so this is a good review for me.

Testing approaches

* Intuition about natural boundaries to the problem
    * Mathematical functions usually make this easy
    * Can you come up with some natural partitions?
* If no natural partitions, might do random testing
    * Probability that code is correct increases with more tests
    * Better options below
* Black box testing
    * Explore paths through specification
    * Designed _without looking_ at the code
    * Can be done by someone other than the implementer to avoid some implementer _biases_
    * Testing can be __reused__ if implementation changes
    * __Paths__ through specification
        * Build test cases in different natural space partitions
        * Also consider boundary conditions (empty lists, singleton list, large numbers, small numbers)
* Glass box testing
    * Explore paths through code
    * __Use code__ directly to guide design of test cases
    * Called __path-complete__ if every potential path through code is tested at least once
    * What are some __drawbacks__ to this type of testing?
        * Can go through loops arbitrarily many times
        * Missing paths
    * Guidelines
        * Branches
            * Exercise all parts of a conditional
        * For loops
            * Loop not entered
            * Body of loop executed exactly once
            * Body of loop executed more than once
        * While loops
            * Same as for loops, cases that catch all ways to exit loop
    * Path complete test suite could still __miss a bug__
        * Should still test boundary cases

### Debugging

* Once you have discovered that your code does not run properly, you want to:
    * Isolate the bug(s)
    * Eradicate the bug(s)
    * Retest until code runs correctly for all cases
    * Steep learning curve
* Goal is to have a bug free program
* Tools
    * __Built in__ to IDLE and Anaconda
    * __Python tutor__
    * __Print__ statement 
    * Use your brain, be __systematic__ in your hunt

Error messages - Easy

Logic errors - hard

* __think__ before writing new code
* __draw__ picture, take a break
* __explain__ the code to 
    * Someone else
    * A rubber ducky

### Debugging steps

* __Study__ program code
    * Don’t ask what is wrong
    * Ask how did I get the unexpected result
    * Is it part of a family
* __Scientific Method__
    * Study available data
    * Form hypothesis
    * Repeatable experiments
    * Pick simplest input to test with

Print statements are a good way to test hypothesis
