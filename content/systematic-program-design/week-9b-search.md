Title: Systematic Program Design: Week 9b - Search
Date: 2026-01-08 13:00
Category: Systematic Program Design
Tags: computer-science,racket

> ### Search Module
In this module, we will expand on generative recursion and work on search problems, which are a category of problem solving that can be solved by generating the space of all possible paths from a given state and traversing that space until a solution is found. We will see that it is quite easy to solve Sudoku puzzles this way.

> The Sudoku solver and similar search functions end up having a number of helper functions. So the material in this module will take longer than most previous modules- working through the videos and practice materials for this module should take approximately 8-9 hours of dedicated time to complete.
> ### Learning Goals

> * Be able to identify whether a function should be designed using domain knowledge, structural recursion, built-in abstract list functions or generative recursion.
* Be able to design a backtracking generative search.

I like how the instructor reassures us that it’s okay to not be able to come up with the data definitions on our own.  He admits that he didn’t come up with it right away on his own.  He came up with some data definitions, then worked on the design, then went back and changed the definitions to make it less cumbersome.  He says that remember if you work systematically, what that does is take advantage of good decisions and makes it easy to go back and change bad decisions.

Problem solving by searching a generated tree.

3 aspects to the core structure of our function:

* We are __generating__
* An __arbitrary-arity tree__
* And doing __backtracking search__ over it

We’re going to use a technique called template blending to put these 3 aspects together.  Although this is a little different than what we’re used to with template, the underlying fundamental idea won’t change.  That is, templates are the answer to an important question:  

_Given what I know about what this function consumes and what it produces and basically what it does, how much do I know about the form of the function before I start on the details_. 

In other words, a template is:  What we know about the body of the function, based on what it consumes and its basic behavior, before we get to the details.
Templates have always been that — the outliner, the backbone, the sketch of the function.

Did the exercise where i had to implement solved? and next-boards without watching the next video. It took me about 2 hours to implement and get all tests passing. Didn't one-shot it though, had a few bugs where i used position instead of value at position, and using the wrong formula for calculating box number.  Luckily I wrote a check-expect for invalid box + valid row/col to catch this.

I implemented it differently than the instructor.  The instructor used function composition for next-boards which I did not.  The function composition looks more readable and cleaner than mine.  I was thinking along similar lines at first, thought about using filter and building a list of new boards 1-9 to pass into filter.  Was thinking about the position of the first empty square, but ended up doing it all through helper functions.

I started with finding the first empty square, then passing that position to another function to produce next boards, which its structure had it looping through values 1-9, creating a new board for each, and appending it to return list if it was valid, which was another helper function.

So his was like this:  find position -> generate boards with 1-9 at position -> filter these boards for only valid ones.  All done through separate function call stacks via composition.
Mine was like this:  find position, for each list of boards with 1-9 at position, append to output only if valid.

The call stack of mine is deeper because it goes from next-boards -> produce next boards -> valid board -> valid board helper, that’s 3 layers deep after next-boards.  Meanwhile, the instructor’s function composition goes next-boards -> find position, back to next-boards -> produce 1-9 boards at position, go back again to next-boards -> filter valid boards only -> helper function for valid, so the call stack is at most 2.

I guess the function composition saves some stack space, in addition to being more readable.

So I kinda infused valid check within build list of boards with 1-9 at position, instead of separating the 1-9 board generation and filtering.
I can see how this can be harder to maintain and harder for someone else reading my code to follow.  I guess the takeaway here is I should be thinking what are the operations needed and how can I separate them, then combine them?  Maybe this is functional programming vs. procedural?

Not sure why I didn’t have that intuition.  I did use function composition for the space invaders project.  It made it a lot easier to implement.  Will keep this idea in mind going forward.

The instructor used function composition again for valid-board? Function.  I did not think of this.  I did it all manually and sequentially.

The instructor says not to worry if we didn’t come to the solution as fast or as accurately as he did.  What he would like for us to do is to see how all he did to produce it was to follow the design recipes we’ve used in this course.  He notes that we might not have templated based on and map right away and instead based on list of units.  We would still have gotten the same answer either way.  

He also says we might not have templated according to a 3 function composition right away (whew).  He says that would have caused us a bit more trouble but we could have still arrived at a working solution.

What he needs us to be able to do is go back through his solution and see that this was a reasonable scenario, and see why he made each choice he made at each point.

The key point is that the method we’ve been learning helped him get there.
I went back and did this.  Now I understand the why behind each line of code.

I think the topic of function composition will be revisited in the Programming Languages course, which I will take next after this one, in parallel with class-based program design.


For the maze problem in the problem bank, I was able to solve it on my own.  I used the generative recursion template to start out, but tweaked it in my own way.  I leaned on my own knowledge of implementing recursive functions from outside this course.  After looking at the solution, I saw how closely his code looked to the templates compared to mine.  I initially knew I was to use backtracking and gen recursion template and combine them somehow, but I veered off into my own path of solving it recursively.


I was able to solve the n-queens as well.  Looking at the solution, they used lambda functions.  Going to watch the YouTube video in extras playlist about lambda functions in racket before trying further to understand the given solution.  Lambdas are anonymous functions that allow for writing code in a more concise way.

```racket
;; My solution:
> (time (nqueens 11))
cpu time: 4009 real time: 4504 gc time: 53
(list 119 106 93 80 67 65 52 39 26 13 0)
> (time (nqueens 12))
cpu time: 588392 real time: 646935 gc time: 12288
(list 135 128 114 97 94 77 71 57 43 28 14 0)

;; After I apply an optimization:
> (time (nqueens 11))
cpu time: 3551 real time: 3909 gc time: 188
(list 119 106 93 80 67 65 52 39 26 13 0)
> (time (nqueens 12))
cpu time: 362869 real time: 409218 gc time: 9427
(list 135 128 114 97 94 77 71 57 43 28 14 0)
> (time (nqueens 13))
cpu time: 143030 real time: 160496 gc time: 3006
(list 162 153 137 122 107 103 87 76 60 40 30 15 0)

;; Their solution:
> (time (nqueens 11))
cpu time: 5236 real time: 5929 gc time: 297
(list 119 106 93 80 67 65 52 39 26 13 0)
> (time (nqueens 12))
cpu time: 845447 real time: 939276 gc time: 17233
(list 135 128 114 97 94 77 71 57 43 28 14 0)
> (time (nqueens 13))
cpu time: 209128 real time: 236267 gc time: 4192
(list 162 153 137 122 107 103 87 76 60 40 30 15 0)
```

Big jump in time from N=11 to 12, but less on 13.  N=14 was taking way too long so I stopped it.

The triangle solitaire, after looking understanding what was being asked and reading the code from the partial solutions, I solved it starting at V3 file.

Now I just have the quiz left, and then I’m done with week 9b!

This week has been the hardest so far.  It uses most if not all previously learned concepts.  If you paid attention and took your time learning everything leading up to now, then you’d be in good shape to complete most if not all of these exercises.

I was OK with using some of the starter files for some of the problems.  It’s OK to do, after attempting from scratch for a bit, in my opinion.

Only thing I didn’t do was go over the sudoku optimization file called sudoku-constraint, because it uses accumulators.  That’s next week’s topic, so I’ll revisit this after next week.
