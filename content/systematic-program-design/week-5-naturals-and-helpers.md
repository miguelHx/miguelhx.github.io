Title: Systematic Program Design: Week 5 - Naturals and Helpers
Date: 2025-12-07 23:03
Category: Systematic Program Design
Tags: computer-science,spd,racket

This is my brain dump of week 5 of SPD. I might not go into too much detail and to understand some of it you might need to be familiar with the Racket language and have completed weeks 1-4. I haven't created blog posts about weeks 1-4 yet because I just spun up my blog at the beginning of week 5. I do plan on going back and creating blog posts for those weeks.

### Week 5a - Naturals and 5b - Helpers

For operating on natural numbers, the structure is similar to operating on lists. To process or traverse all elements from 0 to n, we recursively reduce n until we get to the base case 0, applying any operations in between.

Importantly, know that when we design programs, we come up with data definitions that represent information, and we can take any data to represent any information we want.  The example from the video was that we used a list of strings to represent natural numbers.  Now of course, the underlying hardware makes some primitive data faster than other primitive data.

The good news is that while the problems get larger, the work to do at any moment in time does not get harder. Most of the work is HtDD (How to Design Data) and HtDF (How to Design Functions) work I already know how to do (from previous weeks). That's the contribution of the design method, to reduce ever more complex problems to smaller pieces I know how to solve.

Big design problems need to be broken into smaller pieces in order to be tractable.

A function should be split into a function composition when it performs two or more distinct operations on the consumed data.

For example, here we have a function that does two distinct operations:
```racket
;; ListOfImage -> Image
;; lay out images left to right in increasing order of size
;; sort images in increasing order of size and then lay them out left to right
```

That is, lays out images, and sorts images.

We can say, “first sort the images, then layout the sorted list”

Instead of trying to do both operations in this function, we can utilize helper functions so it looks like this:

```racket
(define (arrange-images loi)
  (layout-images (sort-images loi)))
```

The tests would be different, for arrange-images we need to test that the combination works, while the other two test their respective operation.

When you start to get into bigger programs, lots of programmers actually keep a pad of paper by their desk, to kinda keep track of where they are in something. TODOs are good for that, but pen and paper is too.

When we shift knowledge domain, we should use a helper function.

Helper function rules summarized:

__Function composition rule:__  a function should be split into a function composition when it performs two or more distinct operations on the consumed data
For example (same as above):
```racket
(define (arrange-images loi)
  (layout-images (sort-images loi)))
```

__Operate on arbitrarily sized data rule:__  When an expression must operate on a list -- and go arbitrarily far into that list -- then it must call a helper function to do that.
Example:
```racket
(define (sort-images loi)
  (cond [(empty? loi) empty]
        [else
          (insert (first loi)
                  (sort-images (rest loi)))])) ;result of natural recursion will be sorted
```
The helper function we are calling here is insert.

__Knowledge domain shift:__  When we shift knowledge domain, we should use a helper function.
Example:
```racket
(define (insert img loi)
  (cond [(empty? loi) (cons img empty)]
        [else
          (if (larger? img (first loi))
             (cons (first loi) (insert img (rest loi)))
             (cons img loi)))])
```
The domain-shift helper function call here is larger?
However, if larger? Was a built-in helper function that we could use, then we wouldn’t need to create our own separate helper function. Just use the built-in one.

when we design more complicated functions,
we end up having to design a bunch of helper functions
as we use different helper rules to split the work of the main function out.

Whenever you're designing functions-- the rest of this course and in the rest of your life-- keep these helper rules in mind.
They're good guidelines for where to put in a helper function.
Some programmers will adopt their own style for using rules in other places, but these are good general principles for where to put helper functions.

Also learned how to sort in racket this week.