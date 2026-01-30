Title: Systematic Program Design: TA Solver Project
Date: 2026-01-26 10:20
Category: Systematic Program Design
Tags: computer-science,spd,racket

Problem 1 was straight-forward, since it's basically the same problem as `max-exits-to` from the problem bank that I already solved.

Going through the 5 step recipe to try and solve Problem 2 of the ta-solver file.

1. Signature, purpose and stub.
2. Define examples, wrap each in check-expect.
3. Template and inventory.
4. Code the function body.
5. Test and debug until correct

Steps 1-2 are done for us already, I am working to do steps 3-5.  I’m using the function parameters to help come up with a template.  For one, we will be using all selectors of the ta data structure.

Naively, we can say that there is a structural recursion on one of the parameters because it’s a list.  But due to the actual steps taken to solve this, it might be a search problem on an arbitrary-arity tree.

It might also be generative recursion, but I need to solve a few examples, examine the steps taken, then use that information to come up with the model-level template description before writing the actual template.

Here is the model-level template description that I wrote:
```racket
;; template: all selectors for ta, mutual recursion for arbitary-arity tree for multiple potential slots to take,
;; backtracking search when potential slot doesn't work out, accumulator for solution so far,
;; generative recursion - stop trivial case where slots is empty
```

After writing a model-level template description, I took the template from sudoku solver because it closely resembles the structure we are looking for.  Now making tweaks to it.

I got the structure in place, arbitrary-arity tree mixed with backtracking search mixed with generative recursion.  Coded up all of it except the (next-states s) part, which is the most complicated procedure.  I’m spending some time thinking about how it could be done.  I have some ideas, but not sure yet how to translate into code.  Need to look at the parameter data as well as the desired output and somehow put them together.

Got it!  I built out the solution in iterations.  Helper functions came up, and I made them along with their signature and purposes.  I spend a lot of time up front thinking about the solution, how it would work, what the code would need to do, etc.

Then I started coding.  The way it works is we first find the next open slots and build a list of these possible states, while updating the ta lists to reflect taking up a slot, and also updating the slots list to begin looking for the next slot when we look at the next states.

Then, we keep trying to find next open slot, producing new states until we reach a solved state, which happens when the slots list is empty and so we return the result so far that we built up while making the new states.

Going to create some more tests as a sanity check.  Then I’m done with this course !

All done !