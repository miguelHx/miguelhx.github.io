Title: Systematic Program Design: Week 6b - Mutual Reference
Date: 2025-12-19 13:26
Category: Systematic Program Design
Tags: computer-science,spd,racket

We are presented with a new data structure for arbitrarily wide and arbitrarily deep tree structures.  The example given is a file system.  This structure reminds me of the Trie data structure implementation in Python, because of the list of nodes data referencing itself. In this course’s terms, it’s also a mutual reference since we consider ListOfNodes to be a different data structure, that mutually references back to Node.

We then go on to write functions that use the data structure and its templates. This part is more straightforward.  What’s different now is that when designing the function, we must also design the functions of its types, they are grouped together.

The code for summing up values of the tree makes sense.  However, I struggled to come up with solution to a function that consumes Element and produces a list of the names of all the elements in the tree. So I watched the next lecture video solution and saw where my line of thinking was flawed.  I was constructing the lists correctly but I wasn’t combining sublists together. So I had to use the append keyword.

It takes a bit to wrap your brain around this algorithm and visualize how it works.  After spending several minutes I was able to visualize its process.  A downside of this course is that the instructor doesn’t teach you to do that.  He simply states that you have to “trust” the recursion.  Luckily I have experience with recursion already so I know how it works procedurally.

Next up is backtracking. It makes sense, the instructor showed us visually what is going on.

The Harry Potter exercise was good to learn from.  Then there’s a quiz and week 6b is complete.
