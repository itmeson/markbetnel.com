Factoring Problem
#################

:tags: ipython, factoring, problems, method, thinkingoutloud
:date: 2015-05-16
:category: nullresult
:status: draft

.. raw:: html

   <blockquote class="twitter-tweet" lang="en"><p>Oh I must be tired!! I meant..&#10;For which n is (n-1)!/n an integer?&#10;&#10;(Other version legit too but not interesting!!)</p>&mdash; James Tanton (@jamestanton) <a href="https://twitter.com/jamestanton/status/588343984533061637">April 15, 2015</a></blockquote>
   <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>
..


                
Problem of the day, via James Tanton on twitter:

The other version had been the inverse -- for which **n** is
:math:`\frac{n}{(n-1)!}` an integer. I saw that one first, just after I
got on the bus this morning, and had already been thinking about it for
a minute when I saw the followup.

Why is the original one "not interesting"?

How do we go about thinking about a problem like this?

.. code:: python

    def factorial(n):
        """Simple factorial function.  Note that this function is NOT a good one for large numbers"""
        if n == 0 or n == 1:
            return 1
        else:
            return n*factorial(n-1)
    
    for i in range(1,10):
        print i, "\t", factorial(i-1), "\t", float(i)/factorial(i-1)

.. parsed-literal::

    1 	1 	1.0
    2 	1 	2.0
    3 	2 	1.5
    4 	6 	0.666666666667
    5 	24 	0.208333333333
    6 	120 	0.05
    7 	720 	0.00972222222222
    8 	5040 	0.0015873015873
    9 	40320 	0.000223214285714


We could just calculate.

And we learn that when :math:`n=1` and :math:`n=2` we get integers, and
that it doesn't seem likely there will be any more, because the top
number in the fraction is growing *really* fast at this point, but the
bottom number isn't. So the result is getting closer and closer to zero.

So we learned *something*, but not much.

What about the second version? Let's try the same calculation:

.. code:: python

    for i in range(1,10):
        print i, "\t", factorial(i-1), "\t", factorial(i-1)/float(i)

.. parsed-literal::

    1 	1 	1.0
    2 	1 	0.5
    3 	2 	0.666666666667
    4 	6 	1.5
    5 	24 	4.8
    6 	120 	20.0
    7 	720 	102.857142857
    8 	5040 	630.0
    9 	40320 	4480.0


Hmm. Now we see more integers, :math:`n=1,6, 9` all work. Why? Let's try
a few more.

.. code:: python

    for i in range(10,17):
        print i, "\t", factorial(i-1), "\t", factorial(i-1)/float(i)

.. parsed-literal::

    10 	362880 	36288.0
    11 	3628800 	329890.909091
    12 	39916800 	3326400.0
    13 	479001600 	36846276.9231
    14 	6227020800 	444787200.0
    15 	87178291200 	5811886080.0
    16 	1307674368000 	81729648000.0


More integers. When :math:`n=10,12,13,14,15,16`.

When I was doing this on the bus, I was doing it in my head, and I made
a couple of mistakes. I thought I noticed that all the even numbers
worked, except 2. So I conjectured that all the even numbers worked,
which surprised me. Then I noticed that 15 works, which was the first
odd one I noticed (I had gotten 9 wrong as well)

