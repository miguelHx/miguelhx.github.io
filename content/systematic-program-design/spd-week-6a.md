Title: Systematic Program Design: Week 6a learnings
Date: 2025-12-14 17:32
Category: Systematic Program Design
Tags: computer-science,spd,racket

Module overview/summary:

__Binary Search Trees__

> In this module we will investigate how the structure of data affects performance, especially when it comes to the time required to find an element in a large data store. As part of that we will discover a new self-referential form of data, the binary search tree or BST.
We will also learn to design data definitions and functions for BSTs. We will not need any new design techniques for this; we already know enough to do it. In fact, the recipe rules we have already covered can work with a wide range of self-referential data.

> Working through the videos and practice materials for this module should take approximately 5-6 hours of dedicated time to complete.
The programs are bit longer again in this module. To avoid feeling overwhelmed by the new form of data it is really important to let the design recipe help you focus your attention. Don't try to think about the whole problem at once - focus on the current step of the recipe only.
Also be sure to trust the natural recursion! That's the key to making it easy to design functions that operate on data that has self-reference in its definition.

Learning Goals:

* Be able to reason informally about the time required to search data.
* Be able to identify problem domain information that should be represented using binary search trees.
* Be able to check whether a given tree conforms to the binary search tree invariants.
* Be able to use the design recipes to design with binary search trees.


List abbreviations

How we create lists in racket:
Before:  `(cons “a” (cons “b” (cons “c” empty)))`
New list abbreviation:  `(list “a” “b” “c”)`

List is a primitive for constructing lists.

So why have we been using “cons”?

When you construct lists one at a time, you still want to use cons.

In other words, if you want to add one element to a list, use cons. List notation won’t work as expected.

We are given an example of searching for an element in a list.

After this, the next video discusses the binary search optimization on sorted data.
I’m already familiar with this optimization so I won’t go in depth. This blog is meant to serve as a log of what I have been learning, not necessarily teaching everything I learn.

It’s sort of a chronological brain dump of what I’m learning and my general thoughts that arise, without going into too much detail.

Another thought that came to mind is that understanding recursion before taking this course really helped me understand the recursion topics quickly.

Next videos we go over the binary search tree, including how it works, the data definition, lookups, and render the BST as an image.

Here is the data definition:
```racket
(define-struct node (key val l r))
;; BST (Binary Search Tree) is one of:
;; - false
;; - (make-node Integer String BST BST)
;; interp. false means no BST, or empty BST
;;   key is the node key
;;   val is the node val
;;   l and r are left and right subtrees
;; INVARIANT:  for a given node:
;;     key is > all keys in its l(eft) child
;;     key is < all keys in its r(ight) child
;;     the same key never appears twice in the tree
(define BST0 false)
(define BST1 (make-node 1 "abc" false false))
(define BST4 (make-node 4 "dcj" false (make-node 7 "ruf" false false)))
(define BST3 (make-node 3 "ilk" BST1 BST4))
(define BST42
  (make-node 42 "ilk"
             (make-node 27 "wit" (make-node 14 "olp" false false) false)
             (make-node 50 "dug" false false)))
(define BST10
  (make-node 10 "why" BST3 BST42))
#;
(define (fn-for-bst t)
  (cond [(false? t) (...)]
        [else
         (... (node-key t)   ;Integer
              (node-val t)   ;String
              (fn-for-bst (node-l t))    ;BST
              (fn-for-bst (node-r t)))])) ;BST

;; Template rules used:
;; - one of: 2 cases
;; - atomic distinct: false
;; - compound: (make-node Integer String BST BST)
;; - self reference: (node-l t) has type BST
;; - self reference: (node-r t) has type BST
```

Here is the code for how lookups are done:

```racket
;; BST Natural -> String or false
;; Try to find node with given key, if found produce value; if not found produce false.
(check-expect (lookup-key BST0  99) false)

(check-expect (lookup-key BST1   1) "abc")
(check-expect (lookup-key BST1   0) false) ;L fail
(check-expect (lookup-key BST1  99) false) ;R fail
(check-expect (lookup-key BST10  1) "abc") ;L L succeed
(check-expect (lookup-key BST10  4) "dcj") ;L R succeed
(check-expect (lookup-key BST10 27) "wit") ;R L succeed
(check-expect (lookup-key BST10 50) "dug") ;R R succeed


;(define (lookup-key t k) "") ;stub

;<template according to BST, and additional atomic parameter k>

(define (lookup-key t k)
  (cond [(false? t) false]
        [else
         (cond [(= k (node-key t)) (node-val t)]
               [(< k (node-key t)) ;should we go left?
                (lookup-key (node-l t) k)]
               [(> k (node-key t)) ;should we go right?
                (lookup-key (node-r t) k)])]))
```
As you can see, it's a standard recursive binary search algorithm.

After lookups in this module, we go on to write code that will visualize the binary search tree by rendering an image with lines.
Leaving that code out of here. Did several BST exercises, for ex, one of them was inserting a new node in a BST.

I completed week 6a, next up is the mid term project, which is to program the game Space Invaders! Will do a write up when I'm done with it, then moving on to week 6b and beyond.