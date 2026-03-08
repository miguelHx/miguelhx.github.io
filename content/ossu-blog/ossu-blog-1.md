Title: OSSU Blog 1 - Progress Update from October 18, 2025 until January 24, 2026
Date: 2026-01-27 10:00
Category: OSSU Blog
Tags: ossu
Slug: ossu-blog-1
Pin: true

I'm happy to share that I have made good progress on [OSSU](https://github.com/ossu/computer-science?tab=readme-ov-file) since I started back in October 2025! In this blog post, I will be briefly discussing the courses I took so far, along with a break-down of the time I took to complete them. Then I will talk about what's next.

## What is OSSU?

OSSU stands for [Open Source Society University](https://github.com/ossu/computer-science?tab=readme-ov-file). The OSSU curriculum is a complete education in computer science using online materials.

It is designed according to the degree requirements of undergraduate computer science majors, minus general education (non-CS) requirements, as it is assumed most of the people following this curriculum are already educated outside the field of CS. The courses themselves are among the very best in the world, often coming from Harvard, Princeton, MIT, etc.

If you want to know more about my background and why I'm doing this, check out my other blog post [here](revisiting-software-fundamentals.html).

My learning plan has changed since I wrote that blog post. I worked on three courses instead of just the two listed.

Here's a little bit about my background, to give you some perspective of where I'm at while going through this curriculum.

I am a software engineer with 3.5 years of professional experience and about 10 years of coding or learning about code/CS/software engineering/programming. I earned a 4-year bachelor's degree in Computer Science & Engineering back in 2019. Between my graduation and now, apart from my professional experience, I've had a few gap years of non-coding.

Now, I'm re-building my career from the ground up, starting with OSSU courses. I'll try to discuss two perspectives. One trying to put myself in the shoes of a beginner, and the other as an experienced engineer.

> "No man ever steps in the same river twice, for it's not the same river and he's not the same man"
> \- Heraclitus

The three courses I worked on since Oct. 2025 are [Systematic Program Design](https://learning.edx.org/course/course-v1:UBCx+SPD1x+2T2015/home), [Math for Computer Science](https://openlearninglibrary.mit.edu/courses/course-v1:OCW+6.042J+2T2019/course/), and [Intro to CS and Programming using Python](https://ocw.mit.edu/courses/6-100l-introduction-to-cs-and-programming-using-python-fall-2022/).

I completed Systematic Program Design and Intro to CS courses, but only about a quarter of Math for CS.  I was taking these courses concurrently, though I didn't start them at the same time.

I started with Systematic Program Design on Oct. 18.  Then, about a month later, I began Math for CS. Then about another month later, I began Intro to CS.

So, between Dec. 16 and now, I was taking the three courses concurrently.

My schedule was to work on Intro to CS every day except Sundays for 1-2 hours each day, and on Mon/Wed/Fri work on SPD for 3-6 hours each day, and on Tue/Thu/Sat work on Math for CS for 3-6 hours each day.

I was able to complete 2 out of the 3 courses. For math for CS course, I only completed 1 unit out of 4.

Now, let's do a time break-down followed by a brief overview of my thoughts of each course.

Note: I track my time spent as a way to measure my productivity and keep myself on track based on the effort guidelines from the GitHub.

## Systematic Program Design

__Total time taken:  98.39 hours__ from Oct. 18, 2025 until Jan 26, 2026, which is about 14 weeks. I took a 1 week break to prepare for an interview, so technically 13 weeks.

The expected duration from the OSSU GitHub is 13 weeks, at a rate of 8-10 hours per week.

Below you will see there are 16 weeks. The way I counted them was, if I started week 1 on a Saturday, I counted the whole week as week 1. Same for the tail end. That's why there are 2 extra weeks.

Weekly breakdown:

* Week 1 =>   __3.78 hours__ (Started on Friday that week)
* Week 2 =>   __3.67 hours__
* Week 3 =>   __7.51 hours__
* Week 4 =>   Break to prep for interview
* Week 5 =>   __2.55 hours__
* Week 6 =>   __3.90 hours__
* Week 7 =>   __7.44 hours__
* Week 8 =>   __8.72 hours__
* Week 9 =>   __8.25 hours__
* Week 10 =>  __8.63 hours__
* Week 11 =>  __7.12 hours__
* Week 12 =>  __7.55 hours__
* Week 13 =>  __8.61 hours__
* Week 14 =>  __7.33 hours__
* Week 15 =>  __9.54 hours__
* Week 16 =>  __3.79 hours__ (Ended on Monday that week)

__Weekly Average: 6.56 hours__

__Video watch speed:__  Most of the videos I watched at 1.25x speed. For some of the meatier or harder videos, I watched at 1x speed, which was about 10-15% of the videos, I think. I took notes on some of the things the instructor said, mainly the key takeaways, which I found to be valuable.

I plan to write a full course review in a separate post. For this blog post I will briefly discuss my thoughts.

Overall it was a great course ! It gave me a different perspective about problem-solving in code and how to think about code in general.

Some of the general principles, ideas and recipes such as how to design data, designing data before designing functions, how to design functions, using pen and paper to perform a domain analysis and to keep track of TODOs (also track TODOs using comments in the actual program), the rules for creating helper functions, function composition, and seeing code as structure rather than just characters on a screen seem to be useful.

The idea of breaking down complex problems into simpler problems that we know how to solve is also useful, and we practice this in the course.  The idea of test-driven development is also practiced.

They also discuss recursion and that can be useful for certain algorithms and you never know you might run into recursion on the job. Recursion is a big topic in this course. I'd say it probably accounts for over 30% of the class!

Recursion comes up in foundational computer science courses, but not much on the job. So it might feel like a waste to spend so much time on recursion, only to rarely come across it on the job. Luck is a big factor here whether you come across it or not in the industry. I guess it's OK to have an understanding of recursion "just in case", advantageous even. You never know, the concept might come up as an interview question as well.

Though I wish the instructor would have gone into more detail about recursion and how the call stack works, but instead he says to "trust the recursion".  That's fine, because if you trust that the recursive procedure is doing what it's supposed to, then having that faith is enough, compared to understanding exactly the call stack the recursion will go through. As someone who is already comfortable with recursion; I had no problem. I was able to visualize the steps in my head.

Also, Dr. Racket has the stepper feature which can help in stepping through the recursive process to understand its flow.

If you have experience programming already, I would still take it because the language Racket is used in the [Programming Languages course(s)](https://www.coursera.org/learn/programming-languages), and future courses such as [Class-based Program Design](https://course.ccs.neu.edu/cs2510sp22/index.html) (though they use Java) will probably use this course's principles and/or assume you already know them. Plus, if you plan on reading the book Structure and Interpretation of Computer Programs (SICP), then you'll be able to pick up the language used there more easily.

Even if you already knew most of the principles, it doesn't hurt to refine them, see them from a different perspective, or close any gaps that may have existed or you may have potentially missed. I feel like this course improved my recursion skills too.

I like the habits that it's promoting, such as the steps taken when designing a data definition or function.  For designing a data definition, we put in a comment its data type, and a short description of how to interpret it, followed by some examples, and a template for how to use it in a function. For designing a function, we start by writing a signature, purpose, and stub. Then, we define examples and write them in test cases. Next, we identify the right template to use, followed by coding the function body and testing/debugging until correct.

I am an experienced software engineer so it was a walk in the park for me.

<!-- Here is the recipe for designing data:

The first step of the recipe is to identify the inherent structure of the information.

Once that is done, a data definition consists of four or five elements:

1. A possible structure definition (not until compound data)
2. A type comment that defines a new type name and describes how to form data of that type.
3. An interpretation that describes the correspondence between information and data.
4. One or more examples of the data.
5. A template for a 1 argument function operating on data of this type.


For designing functions, we start by defining its arguments and return value, for example:  `Integer -> Boolean`, then you write a short comment describing its behavior, then you define what's called a "stub" which is the function name, its arguments and a placeholder return value.  then, you create the test cases, testing expected output based on given inputs.  After this, you run the program and of course the tests fail, but the fact that it ran without errors shows you that the code is well-formed, then we move on to implementing the function and making the tests actually pass.

Here is a summary of the 5-step process for designing functions, to give you an idea:

1. Signature, purpose and stub.
2. Define examples, wrap each in check-expect.
3. Template and inventory.
4. Code the function body. 
5. Test and debug until correct -->

These processes can be applied to any programming language and can be considered "good habits", though you might need to adapt the steps a little because you might not have a documentation of proper templates in other languages, though you could make up your own or find examples.

There is also a gap with one of the steps, which is one of the cons of this course. I will get more into this gap when I write the course review.

Another big idea learned was one way on how to think about code. Rather than looking at code as characters on a screen, we are taught to look at code as having structure. Structure that is derived from templates.

This trained me to start looking at code differently and I can see how this idea can be useful for my career. For example, when coming up with solutions, you can break things down in terms of code structure. To illustrate:

![color coded image](images/code-structure-colors.png) 

You can identify the potential structure of the solution after putting some thought and identifying patterns, based on the information given. On the job, you might identify some code structure to apply to the problem you are trying to solve.

Another important note is that the style of programming in this class is [functional programming](https://en.wikipedia.org/wiki/Functional_programming). This way of programming was new to me. Though I have come across some of its ideas such as map, filter, and lambda functions. And of course, I used functions themselves extensively throughout my career.

> Functional programming is a declarative paradigm that builds software by composing pure, deterministic functions, emphasizing immutability and avoiding shared state or side effects. It treats functions as first-class entities, allowing them to be passed as arguments or returned. Key techniques include immutable data, higher-order functions, and recursion.

I've known about functional programming for the awhile. I just never got around to formally learning about it. Until now. Or maybe I have and just didn't think about it much. I think that the [Programming Languages](https://www.coursera.org/learn/programming-languages) course series will go deeper into this concept. For now, we utilize this way of programming without necessarily defining it until the end of the course.

If you're experienced with programming already like I was, and are trying to be pragmatic, you might be wondering if you can get away with skipping this course.  It's hard to tell. I can come up with theories as to why it is useful, as I did above, but won't truly know until more time passes by and I go through more programming experiences. I'll probably update this blog post if anything comes to mind in the future.

But if you do decide to skip this course, you would be missing out on a good, structured way of approaching problem-solving in code, if you don't have such a process already learned from another source. That, along with missing other important ideas, mentioned above.

If you're a beginner and struggle with this course, it's OK and normal. Recursion can be hard to wrap your head around. If you find yourself looking at the solutions often, don't feel bad. I recommend using the DrRacket stepper feature to step through a smaller example to understand how it works step by step. Maybe even draw out some iterations using pen/pencil and paper.

Just go through the course. Ask for help in the discord. Try not to waste too much time being stuck.  But also don't jump to the solution right away without putting much thought into it. Learn to enjoy the process.

I plan to go a little more into detail about this course in a separate blog post, which I will link [here]() when it's done. Same for the rest of the courses below.

## Math for Computer Science

__Total time taken so far: 59.55 hours__ from Nov. 18, 2025 until Jan 15, 2026, which is about 9 weeks. 

The expected duration is 13 weeks, at 5 hours per week. Not sure if I'll finish within the expected time frame. We'll see how it pans out.

Weekly breakdown:

* Week 1 =>   __3.70 hours__
* Week 2 =>   __8.24 hours__
* Week 3 =>   __9.37 hours__
* Week 4 =>   __6.45 hours__
* Week 5 =>   __5.73 hours__
* Week 6 =>   __4.98 hours__
* Week 7 =>   __7.68 hours__
* Week 8 =>   __8.37 hours__
* Week 9 =>   __5.02 hours__

__Weekly Average: 6.62 hours__

__Video watch speed:__ Mostly at 1.25x speed.

I only finished Unit 1 of the course !  There are 4 units total, of varying lengths.

The problem sets were hard. I took my time reading the lessons and went down a few rabbit holes.

BTW, I skipped the calculus courses from OSSU. I decided to skip calculus 1-3 because I took them in college and I feel like I could pick up any calculus concepts if they come up in Math for CS on an as-needed basis.  Not much calculus I've come across so far though.  But the intuition I built about functions, algebra, some trig, etc. during my calculus years turned out to be useful.

I'd like to finish this course before I start on Core Theory. I have plenty of time before I get there, since I plan on finishing Core Programming before starting another section.

I like math, so I'm enjoying this course so far.

Writing proofs is hard though. It's a skill set. A skill set which can, of course, be improved with deliberate practice. Similar to programming and writing, it requires a blend of logic and creativity. Reading and understanding some of the proofs (though not all) is not easy either. I was able to grasp most of the proof methods, but actually implementing them was not always easy.

I often have writer's block when it comes to writing proofs, unless I follow some of the given templates, or adapt from a similar example. Even then, it's not always clear how to argue and reason why something is true.

In the Discord, some say that this course is too difficult and doesn't teach very well. I think it's OK. I will continue with this course because I am able to understand the topics for the most part. Susanna Epp's Discrete Math book is recommended as an alternative. I plan to complete this course first, then I want to go through Epp's book.

I agree that many of the problems are difficult to solve.  I find myself eventually looking up the solutions for most.  I'm okay with doing this. I don't think it takes away too much from my learning as long as I give the problems an honest attempt first, and understand the solutions.

If you take this course and find yourself constantly looking up the solutions, don't feel bad.

The first half of unit 1 is mainly about proofs and various math notations they use.  Then we learn about Sets, Binary Relations, State Machines, Recursion, and Infinite Sets.

Maybe I'll write a review about unit 1 so far in a separate post.

So should you take this course?  I think Discrete Math is important, so I'd say yes. You'll need it as a pre-req to other courses. It's a good exercise for your brain in logic. This will make you a better programmer, because logic is used a lot in programming.

But be prepared to struggle. It is not easy. Also try not to overcomplicate things. I would actually recommend reading Susanna Epp's book first, since I hear the author does a gentler approach and more hand-holding. I'm doing this course first, yes, but I'm not getting stuck for too long because I look up the solutions after struggling for some time. If I don't fully understand a solution, then I'll move on.

If you haven't taken Calculus, trust the OSSU recommendations and take Calculus before this course or Epp's book.

## Intro to CS and Programming using Python

__Total time taken: 32.33 hours__ from Dec. 16, 2025 until Jan 24, 2026, which is about 6 weeks.

The expected duration is 14 weeks, with 6-10 hours/week of effort.

Weekly breakdown:

* Week 1 =>   __6.99 hours__
* Week 2 =>   __5.08 hours__
* Week 3 =>   __3.52 hours__
* Week 4 =>   __4.56 hours__
* Week 5 =>   __6.02 hours__
* Week 6 =>   __6.15 hours__

__Weekly Average: 5.39 hours__

__Video watch speed:__ 2x because I am experienced and this is mostly review for me.

So why am I taking this course if I'm experienced in this topic already?

Mostly out of curiosity. I want to see if there’s anything in the basics/fundamentals that I may have missed, and want to see if I learn something new despite having experience with Python and programming already.

Also, I'm rebuilding my CS/software knowledge from the ground up, so this course helped me get my bases covered.

I'm satisfied with the course material. I did skip some sections that I felt were unnecessary for me to learn, like the plotting library for example. If I cross that bridge later, then I'll revisit that lecture video but will also do google searching and reading documentation.

Is it the best course for a beginner? Haven't tried all intro to CS courses, so I can't tell. I'm also not a beginner.  I can try putting myself in the shoes of a beginner though. I think they might struggle with the problem sets, which is normal.

I think it's still a good course for a beginner to take. However, in the early problem sets, you are not taught explicitly how to solve these problems. It is assumed that you have a problem solving approach already, which may leave beginners struggling to come up with solutions on their own.

Later, around lecture 12, the instructor does introduce some problem solving/debugging methods, which should be helpful. Personally, I relied on my own problem solving method learned from another course.

But I remember struggling with writer's block when I started my coding journey many years ago.

Another thing I noticed about this course is that a lot of math examples are used. I am not surprised.  Math and CS/Programming go hand in hand. Some say that theoretical computer science could be considered a branch of mathematics.  They are closely intertwined.

You'll come across a calculus example with a derivative during one of the lectures but don't worry if you haven't taken calculus yet. You don't need to know that specific topic to do well in the course, as it doesn't show up on problem sets.

The problem sets were good practice for me. Each one took me between 1-3 hours. They were well-designed, utilizing knowledge from the lectures. With the exception of one part of the last problem set, which I feel like could have been better defined.

Test files are included, so I was able to test my code. But the test files work only for Python version 3.9 and below. I had to create a lower version Python environment to accomodate for this.

I don't regret taking this course. It helped me brush up on my fundamentals knowledge. Though I'd say like 80-90% of it was review for me.

If you're a beginner, definitely take this course. The knowledge is fundamental. If you find it too difficult, try asking for help in the Discord, or read the GitHub for easier alternatives, then maybe revisit this course.

I do plan on making some walkthrough videos for the problem sets. This will hopefully help beginners have some training wheels for how to approach and solve these problem sets and beyond.

If you're experienced, especially with Python, you can probably get away with skipping this course. Most of it will probably be review if you've taken a proper introductory to CS/programming course and are a decent programmer.

But if you want to be thorough, then go ahead and go through the whole course. Maybe watch at 2x speed, slowing down to 1x for some parts that you feel like you should slow down for.

Maybe see if you can do the problem sets to test your knowledge and only then watch the related lectures if you get stuck.  You can also look up the solution on my GitHub if you truly get stuck.

Overall I am happy with what I've accomplished so far. I'm averaging about __18.57 hours__ each week of total effort on OSSU. For my next run, I'm aiming for closer to __20 hours__ each week. But maybe I'll take 2 courses instead of 3 concurrently, not sure yet.

## What's Next

Next up, I plan on taking [Class-based Program Design](https://course.ccs.neu.edu/cs2510sp22/index.html) concurrently with [Programming Languages parts A/B/C](https://www.coursera.org/learn/programming-languages). But before that, I want to take [The Missing Semester of Your CS Education](https://missing.csail.mit.edu/). I'm also considering taking [Harvard's CS50x](https://learning.edx.org/course/course-v1:HarvardX+CS50+X/home).

However, before continuing with the next courses in OSSU, I think I want to take a 1-3 month break from it. Not because I'm tired of it or anything like that; I'm really enjoying the learning process and I'm actually eager to learn more !

But I have some other initiatives that I wanted to work on. One of them is creating a YouTube channel and making videos about programming and OSSU. I can start by creating some problem set walkthrough videos for the Intro to CS using Python course, since those don't exist anywhere.

I want to assist beginners in these problem sets by guiding them through my process of solving them. Then, I can create some course review videos on the courses I've completed so far before moving on.

I also want to invest time in meta-learning. That is, learning how to learn. I already have some base knowledge on how to learn, but this time I want to go deeper. I've compiled some solid resources about learning which includes YouTube videos and the book [Ultralearning](https://www.amazon.com/Ultralearning-Essential-Mastering-Skills-Future-Proofing/dp/006285268X). And I want to blog all about it!

There's also some other blog posts on my backlog that I want to create, which include reflections from past interviews, reflections on my past work experiences, and an essay about where I'm at right now, career-wise and life-wise.

I also want to work on adding features to one of my side projects, which is a [music website](https://github.com/miguelHx/Latino_Nostalgia) that I created.

I think I can deliver all of this within 2-3 months. Then I'll be in a better position to continue the OSSU curriculum, especially since I'll be armed with the latest knowledge about learning.

This plan is subject to change. It's possible that I decide last minute to not do one or more of what I planned above. I'm still weighing my options. I need to invest time into thinking and planning more about all this.

> "Give me six hours to chop down a tree and I will spend the first four sharpening the axe." – Abraham Lincoln

Sharpening the axe here for me is thinking about and planning what to do next. Chopping the tree is actually carrying out the plan. The planning to execution ratio might not be exactly like from the quote, but the key idea here is to invest time in thinking and planning, so that's what I am going to do.

Stay tuned until my next OSSU blog.