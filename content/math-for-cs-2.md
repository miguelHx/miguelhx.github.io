Title: Math for CS: Quantifiers and Predicate Logic
Date: 2025-12-14 17:24
Category: Math for Computer Science
Tags: ossu,computer-science,math,discrete-math,math-for-cs

We start off with quantifiers.  There are two of them.  “For all” and “there exists”, each with their own notation.  For all is an upside down A and there exists is a backwards E.

We are also introduced to predicates.  a predicate is a statement that contains a variable and becomes a true or false proposition when a value is substituted for the variable.  For example P(x, y), where P is a proposition that takes in any x or y in a domain. In other words, a predicate is a proposition with variables.

There are several ways to express the notions of “always true” and “sometimes
true” in English.

They use keywords such as “all”, “every”, “some”, “at least one”, etc.

All these sentences “quantify” how often the predicate is true. Specifically, an
assertion that a predicate is always true is called a universal quantification, and an
assertion that a predicate is sometimes true is an existential quantification. Sometimes the English sentences are unclear with respect to quantification.

Ex:  If you can solve any problem we come up with, then you get an A for the course. 

This phrase can be reasonably interpreted as a universal or existential quantifier.

you can solve every problem we come up with,

or maybe
you can solve at least one problem we come up with.

### mixing quantifiers

You can also mix quantifiers. Many math statements involve several quantifiers.

Ex:  For every even integer n greater than 2, there exist primes p and q such
that n = p + q.

### order of quantifiers

Swapping the order of different kinds of quantifiers (existential or universal) usually
changes the meaning of a proposition.

Ex:  “Every American has a dream”

This could mean there is a single dream that every American shares OR it could mean that every American has a personal dream.

### negating quantifiers

There are rules for negating quantifiers. The following two sentences mean the same thing:
* Not everyone likes ice cream.
* There is someone who does not like ice cream.

The general principle is that moving a NOT across a quantifier changes the kind of quantifier.

### validity for predicate formulas

The idea of validity extends to predicate formulas, but to be valid, a formula now
must evaluate to true no matter what the domain of discourse may be, no matter
what values its variables may take over the domain, and no matter what interpretations its predicate variables may be given.

Give example in latex.

Moving on to the lectures and more exercises in the form of online quizzes.

The lecture videos go over predicate logic with quantifiers and some rules.

Translation of English language into precise formal language can be ambiguous.  It makes me think of the potential problems with AI translating English into code or math, there’s a chance of producing unintended results, of course.