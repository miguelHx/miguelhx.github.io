Title: Intro to CS: Lecture 5 - Floats and Approximation Methods
Date: 2025-12-19 13:51
Category: Intro to CS using Python
Tags: computer-science,python

Topics: Simple Algorithms: approximation method, floats

One thing I observed so far is that this course is not teaching a systematic way on how to come up with algorithms.  By coming up with algos, I mean the process of taking a well-defined problem, its steps, and translating it into code.  The instructor mentions that it is not expected to come up with some of these mathematical recipes/steps, like converting an integer to binary, for example.  But it IS expected to translate the algo/recipe into code.  The “translating” steps in between are not explicitly taught but rather seem to be implicitly assumed.  That’s one flaw with this course I’ve found so far, and also a flaw with Systematic Program Design course.  In my opinion, for beginner level courses, such a technique is important.

There’s another course I took awhile back that teaches this general technique for translation from problem to code.  Be aware that the course I am referring to is not mentioned as part of the OSSU curriculum, although I’m thinking about starting a conversation to add it there (but its a Coursera course so might not get approved).  If you struggle with translating a problem and its solution into code like on problem set 1 of this course, and if you’re curious about that general technique, [here](https://adhilton.pratt.duke.edu/sites/adhilton.pratt.duke.edu/files/u37/iticse-7steps.pdf) is a 1-page PDF describing the technique, maybe you can apply it when doing the problem sets for this course.

If you’re curious about which course(s) I’m referring to, it’s part of the [Coursera Java programming and software engineering fundamentals specialization](https://www.coursera.org/specializations/java-programming) (first few courses).  Not trying to steer anyone away from this course, but the courses from the specialization linked use and teach that technique which I found to be extremely useful when I was a beginner, and seem to not be taught in this MIT course (so far, but I’m only on lecture 6, so I can’t fully judge this course just yet until after I complete it).

I could turn out to be proved wrong, if later in the course such a technique is taught.

Curious what others think about this.

Anyway, now I start watching this lecture.  Never use == to test floats. What gets printed is not always what’s in memory.  Need to be careful in designing algorithms that use floats.

This brings us to an approximation method.  Find an answer that is “good enough”.  We increment by some small amount and we stop when we are close enough (exact is not possible).