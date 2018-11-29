Testing IPy Blogging
####################

:tags: ipython, blogging, test
:date: 2014-04-09
:category: nullresult


This is a test post. I just want to see what markdown and code blocks
look like in my theme so I can start doing some analysis posts. The
method for doing this comes from this
`notebook <http://nbviewer.ipython.org/github/keflavich/blog/blob/master/content/BloggingFromIPython.ipynb>`_.
I'll have to do some fussing with it later to get format right, and to
make sure I can use matplotlib and the new interact mechanism.

.. code:: python

    def fib(n):
        if n == 0 or n == 1:
            return 1
        else:
            return fib(n-1) + fib(n-2)
    
    for i in range(10):
        print i, fib(i)

.. parsed-literal::

    0 1
    1 1
    2 2
    3 3
    4 5
    5 8
    6 13
    7 21
    8 34
    9 55

