Title: Math for CS: Binary Relations
Date: 2025-12-24 11:46
Category: Math for Computer Science
Tags: computer-science,math,discrete-math

We start by going over Functions.  Its definition, what domains, codomains and images are, examples, and function composition.  I was surprised to see some of the creative ways we can define a function.  For example let f(y) be the length of a left to right search of the bits in the binary string y until a 1 appears, so f(0010) = 3, f(000) = undefined, f(100) = 1.

One important fact about functions: they need not assign a value to every element in the domain.  

Some authors refer to the codomain as the range of a function, but they shouldn’t.  The distinction between the range and codomain will be important later in Sections 4.5 when we relate sizes of sets to properties of functions between them.

Then we go on to Binary Relations.  Turns out a function is a special type of binary relation.  All functions are binary relations but not all binary relations are functions.  Here is the definition of a binary relation:  A binary relation, R, consists of a set, A, called the domain of R, a set, B, called the codomain of R, and a subset of A x B called the graph of R.

Examples are given.  Then we are given the different types of binary relations, including function, surjective, total, injective, bijective.  The idea of an image of a set under a function extends to binary relations.  We then talk about the inverse image and finite cardinality.

My guess is that this topic is applicable in database systems, in particular when defining relationships between tables.  Can use this math terminology to classify the relations.

Finite cardinality.  A finite set is one that has only a finite number of elements. This number of elements is the “size” or cardinality of the set.  We make some relations between the cardinality of relational sets and their properties, along with their proofs.

In the lecture the instructor says you can use these concepts in databases.  You can express queries and assertions about the database using a combination of relational operators and set operators.

It seems like a handful to remember all the properties and the implications of each property.  I usually just keep referring to the definition if I come across it.  Then I think about it, imagining the arrows and the inverse and what the inverse means, etc.  It may or may not stick, but at least I know in general where to look if I come across this topic in the future, for example when I come across databases.

Over a little time, I came up with ways to easily memorize.  For example, I just remember that injective means arrows going in to the co-domain, and that it’s <= 1 for each element.  I make a mental note that surjective is still arrows in but the opposite amount, so >= 1 for each element in co-domain.

The exercises were good.  On to 1.8, Induction.