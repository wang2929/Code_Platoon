# Book Club - Nice parts

## Composition vs Inheritance

Composition is an alternative that reverses these costs and benefits. In composition, the relationship between objects is not codified in the class hierarchy; instead
objects stand alone and as a result must explicitly know about and delegate messages


186 Chapter 8. Combining Objects with Composition to one another. 
Composition allows objects to have structural independence, but at the cost of explicit message delegation. Now that you’ve seen examples of inheritance and composition you can begin to think about when to use them. The general rule is that, faced with a problem that
composition can solve, you should be biased toward doing so. If you cannot explicitly
defend inheritance as a better solution, use composition. Composition contains far
fewer built-in dependencies than inheritance; it is very often the best choice.
Inheritance is a better solution when its use provides high rewards for low risk.
This section examines the costs and benefits of inheritance versus composition and
provides guidelines for choosing the best relationship.


## Inheritance Disadvantages

Concerns about the use of inheritance fall into two different areas. The first fear is
that you might be fooled into choosing inheritance to solve the wrong kind of prob-
lem. If you make this mistake, a day will come when you need to add behavior but
find there’s no easy way do so. Because the model is incorrect, the new behavior
won’t fit; in this case you’ll be forced to duplicate or restructure code.

Second, even when inheritance makes sense for the problem, you might be writ-
ing code that will be used by others for purposes you did not anticipate. These other
programmers want the behavior you have created but may not be able to tolerate the
dependencies that inheritance demands.