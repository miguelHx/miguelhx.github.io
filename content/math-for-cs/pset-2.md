Title: Math for CS: Problem Set 2 Thoughts
Date: 2025-12-19 13:58
Category: Math for Computer Science
Tags: computer-science,math,discrete-math

For problem 1, I follow the description’s equivalence formula of set theory.  But for part (a) when it asks to write a formula Members(p, a, b) of set theory that means p = {a, b} I am lost.  This must be something from the text book that was not in this course’s readings.  Not sure.

Part 1(a) says that we can represent (a, b) as pair(a, b) ::= {a, {a, b}}.  I don’t know why this is the case.  Going to ask chatgpt to explain this.  Chatgpt says we can make this representation because this set uniquely determines which element is first and which is second, allowing order to be encoded using only set membership.  That makes more sense.  And now that I remember, it looks like the problem we did this proof for in the in-class problems for this week.

I don’t get how to approach parts (b) and (c) of question 1. So I will look at the solution for these later.

Problem 2 is straightforward, it’s just using algebra and substitutions to get from LHS to RHS.

Problem 3 I follow until we get to the definition of S*.  Based on its description, I just wonder if I’m picturing it correctly in my head.  I guess it makes sense thinking more about the examples now.  Yes, I understand now.

Part 3(a) not sure how I would “show” this other than using the definition of concatenation-definable and some logic to show that the intersection of R and S is c-d because it’s finite because R and S each are finite.  But I just found out shortly after that the set B of all binary words is c-d, even though it’s an infinite set.

Part 3(b) not sure right away how 0*B*1 is c-d.  But now that I think about it, we can apply a finite number of unions each B in order to get a variation of 0*B*1.  Not sure if that observation is enough to answer the question.

Parts 3(c)/(d) I have some intuition as to why these may be the case, but not sure how I would “show”.

3(e) {00}^\* is not boring because the intersection of {00}^\* and 0^\* is not finite.  Idk what the complement of {00}^\* looks like, maybe any word except even number of 0s.  You still have odd number of 0s in the set, going on to infinity, therefore the intersection of the complement of {00}^* and 0^* is still not finite.  Therefore {00}^\* is not boring.

Similar reasonings can be applied to the remaining problems.

I spent 1 hr 30 min on this, the course states that these should take no more than 3 hours.  I think that’s a fair amount of time, spending more time thinking through might yield the remaining results, but I’m trying to balance time and efficiency here.  I gave each problem an honest attempt, even if that means not knowing how to proceed at all.  Okay, going to look up the solutions now!  I won’t be updating the above text, so if you want to see the solutions, they are linked [here](https://github.com/spamegg1/Math-for-CS-solutions/blob/master/psets/MIT6_042JS15_ps2_solutions.pdf).

After reading the solutions I realized that my answers weren’t explicit enough for the proofs.  I need to actually show the finite steps of concatenation, union, or complement that lead to the desired result.  Writing proofs is not easy!  Neither is discrete math but I appreciate the course so far nonetheless.