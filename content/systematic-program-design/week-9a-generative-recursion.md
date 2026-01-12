Title: Systematic Program Design: Week 9a - Generative Recursion
Date: 2026-01-04 13:00
Category: Systematic Program Design
Tags: computer-science,spd,racket

> ### Generative Recursion Module
Generative recursion is in many ways similar to structural recursion: a function calls itself recursively (or several functions call themselves in mutual recursion). For the recursion to terminate, each recursive call must receive an argument that is in some way "closer to the base case". That is what guarantees the recursion will eventually terminate.

> In the structural recursion we have already seen, the nature of the data definitions and the template rules provide us the guarantee that we will reach the base case. But in generative recursion we have to develop that proof for each function we write.

> In this module, we will design functions to produce fractal images. We'll explore other uses of Generative Recursion in the Search Module.

> Working through the videos and practice materials for this module should take approximately 5-6 hours of dedicated time to complete.

> ### Learning Goals
> * Be able to identify whether a recursive function (or a set of mutually recursive functions) uses structural or generative recursion.
* Be able to formulate a termination argument for a recursive function (or a set of mutually recursive functions).
* Be able to design functions that use generative recursion (algorithms).

### Structural recursion vs. generative recursion

__Structural__ - start with a piece of data, and at each recursive call they take some sub-piece of that data as the argument to the next recursive call.

__Generative__ - at each recursive call, we generate entirely new data to operate on in the recursive call.

We are given a template for gen recursion functions, and do some examples generating fractal images.

Here is the template:
```racket
(define (genrec-fn d)
  (cond [(trivial? d) (trivial-answer d)]
        [else
         (... d 
              (genrec-fn (next-problem d)))]))
```

Then we go over termination arguments. A termination argument consists of 3 parts:  base case, reduction step, and argument that repeated application of reduction step will eventually reach the base case.

These are to be included in a comment near the implementation of our generative recursive function implementations.

Termination arguments are not always simple. We are given the case of the hailstone function, which is a trick problem because there exists no proof yet for it reaching its base case.

The practice problems were not easy.  I had to look up the solutions after struggling for a bit.

Overall, I feel like this module strengthened my understanding of recursion.