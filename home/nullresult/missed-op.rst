Missed Opportunity
##################

:date: 2017-05-10
:tags: logarithm, information, noodling, missed opportunity 
:category: nullresult

The logarithm.

I've had my Algebra 3 students working on logarithms for the last week, which was an interesting experience.

I don't personally really use logs very often, except on logarithmic graph scales, and I like thinking about them because of the connection to entropy and information content.  Probably the most authentic way for me to teach them/introduce them would have been through information theory, which I have kind of done before with decent results.

I remember, vaguely, that when I learned them they were very mechanical.  The definition of the logarithm is through the equation :math:`\log_b x = a` means that :math:`b^a = x`.  So finding the logarithm of a number is about figuring out what exponent you need, with a given base, to get that number.  The definition leads to some cool properties, like that the log of a product of two numbers is the sum of the logs of those numbers:  :math:`\log (a\cdot b) = \log a + \log b`, which comes from the way that  when multiplying products of exponents, you can add the exponents. And you can change the base of a logarithm by thinking very carefully about the definition, or by memorizing the base change formula. The operation of a slide rule depends heavily on understanding the log properties, so logs *used* to be a singularly important concept. 

And you can also use logarithms to turn really big numbers into small manageable ones: the base-10 logarithm of a million is 6, of a trillion is 12.  This makes it easier to compare really big numbers -- a trillion is 6 orders of magnitude larger than a million.  It's a million times bigger than a million.  It also makes it easier to think about things like the national budget and the debt, or what a new aircraft carrier costs.  A program that costs 3 billion dollars for the United States takes about $10 from every person in the country, because the log of 3 billion over the log of 300 million is ... 1.

I introduced them a little differently for this class.  I asked them to solve some simple single-variable equations, of the algebra 1 type.  :math:`6x = 12`, :math:`-3x - 5 = 17` and others like that.  My students are really comfortable solving those.  We've worked a lot on the idea that the equation represents a relationship between numbers and operations, and that the equation is true for some numbers but not others.  And that the algebraic operations help us to get the equation to *tell us* what numbers it is true of, by performing transformations that do not change the underlying relationships.  And they get that the algebraic operations that they perform are *inverses*.  You divide by 6 because the equation has a multiplication by 6.  You can undo the multiplication by 6 by doing the inverse operation, which is division by 6.  Doing an operation followed by its inverse is equivalent to doing nothing at all.  So the "6" is now gone from the left side of the equation.  And of course you have to do the same operation to every term of the equation or you break the balance of the equals sign.

So what about the equation :math:`5^x = 625`?

You could guess and check your way to an answer, just like we used to do when we were first starting algebraic reasoning, but if we want to follow the pattern of how we learned to approach the single variable equations, we want to get the x by itself so the equation can tell us what numbers it is true for.  And we need to do so in a way that preserves the underlying relationship.  So what we need is an inverse operation, one that inverts "exponentiation with 5 as the base".

What is that operation?

It's not division.  It's not square root.  It's not addition or subtraction.  It's unfamiliar.

We can guess & check, but that's not fun for very long.

So the pro move is to invent an operation, one that is *defined to be the inverse of exponentiation*.  It's defined to do the job we want, of undoing the exponent with base 5, which will get the x out of the exponent.  We just need to investigate the properties of this invented operation to see whether we can make it work for us.  Whether there are problems with it (like dividing by zero) that should raise red flags.  And then decide how and when we will use this new operation, and when we will prefer to use other ways to think about exponents.

------

If I was really a pro, I would have had them come up with their own name and symbol for this operation, and we would have steadily discovered the log properties and discussed whether this idea was useful, and in what circumstances they would choose to use it.

I don't think I pulled out the full pro on this one, though -- with this group we had good discussions of the one-variable algebra and how the inverse concept is key to solving them, then helped them understand that what we want to solve this question is a new inverse operation  (so far so good), but then I only went halfway, and ended up giving them the standard notation, told them that this new symbol stands for "inverse of exponention with the base of ...." and then showed them how to use desmos to finish the problem: :math:`\log_5 5^x = x = \log_5 625`, and desmos can tell them that the result is 4.  And then we did a bunch of examples together and alone, and I think they can mostly use logarithms now, which they will get their first chance to demonstrate on a skills quiz today, but I feel like I missed an opportunity to discover something.

I think I backed down a little because of the usefulness thing -- I made my own judgement about the usefulness (that they aren't inherently all that useful anymore), and settled for a quasi-investigation that got them to be able to use a good tool to solve logarithmic problems.  They will be in decent shape for precalculus, and they exercised the "investigate mathematical relationships muscle" in a new context.

------

So what would the progression have been if I were really a pro?  What activities would we do so they could construct some meaning around the idea of an inverse-exponent operation and own whether or not it is useful for themselves, rather than depending on my judgement alone?  Could I have gotten them to the point of understanding it well enough to make an informed decision for themselves that they aren't really that useful in themselves anymore, since slide rules were left on the ed-tech trash heap, but that they are kind of cool as another way of thinking about and understanding magnitude and relations?  Could that have lead to deeper investigations, proposed by the students?




