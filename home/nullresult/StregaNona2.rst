Strega Nona 2 - How much pasta?
###############################

:tags: ipython, sngn, modelling, fun
:date: 2014-04-11
:category: nullresult

So `last
time <http://markbetnel.com/enough-enough-my-pasta-pot.html%20Strega%20Nona%201>`_
I outlined the story of Strega Nona and Big Anthony and asked a couple
of questions about the scenario. This time I want to do some
back-of-the-envelope estimates of the amount of pasta involved.

First we know that when Strega Nona prepares pasta just for her and Big
Anthony, the pot is "full of steaming hot pasta." Thus we know that the
pot itself is actually not very big, producing enough pasta for two
people. Let's be generous, since this is an Italian story, and say that
together they eat about **1 pound of pasta** -- this is the size of a
typical box of spaghetti sold in American supermarkets, which is a bit
more than I need for dinner for my family. But, again, Big Anthony is
*big*, and they *are Italian*. :)

To cook 1 pound of pasta the normal way requires boiling about 3 quarts
of water for about 10 minutes (first bringing the water to a boil on the
stove, then adding the pasta and allowing it to boil for 10 minutes). So
we have the following unit definitions:

.. code:: python

    OnePastaPotVolume = 3 #quarts
    OnePastaPotMass = 1 #pound 
    OnePastaPotTime = 1 #second (it takes 1 second to make a single serving of pasta)
    OnePastaPotServings = 2 #people (one full pot serves two people)

We'll use those unit definitions in a moment -- the simple family meal
for two is not really that interesting yet.

What about serving the entire village? Well it's a little hard to tell
how many people live in this "town in Calabria". There is a Mayor, there
is a Priest, there are "the sisters of the convent", there's Big Anthony
and Strega Nona of course, and some number of regular townsfolk. Tomie
de Paola's artwork never shows more than 10 or 15 people at a time, but
this seems to be too small for such a town. Comparing to some
demographics for `medieval European
settlement <http://www222.pair.com/sjohn/blueroom/demog.htm%20demographics>`_
we get a figure of about 100-300 for a "village" and 1000-8000 for a
"town" -- both of these seem too big given the artwork in the story, so
I'll settle for the lower number of 100:

.. code:: python

    TownPopulation = 100

This brings us to our first derived result -- the mass and volume of the
pasta produced to feed the town:

.. code:: python

    PastaPotsPerTown = TownPopulation / OnePastaPotServings
    PastaMassPerTown = PastaPotsPerTown * OnePastaPotMass
    PastaVolumePerTown = PastaPotsPerTown * OnePastaPotVolume
    TimeToFeedTown = PastaPotsPerTown * OnePastaPotTime
    print PastaPotsPerTown, PastaMassPerTown, PastaVolumePerTown, TimeToFeedTown


.. parsed-literal::

    50 50 150 50


50 pots of pasta, with a mass of 50 pounds, a volume of 150 quarts (37.5
gallons), in 50 seconds of cooking time.

Which is our first strange result -- surely it took longer than 50
seconds to feed everyone in the town? Some of them twice? Big Anthony
wasn't moving *that* fast.

So what does this mean? **The pot must have two cooking modes** --
"dinner-for-two" mode, which is essentially instantaneous, and
"feed-the-multitude" mode, which is actually *slower* than
dinner-for-two, or Big Anthony would have been swimming in pasta long
before he had finished serving the whole town.

This actually makes sense, so let's figure out how fast the pot is
working in this "feed-the-multitude" mode: I'll assume it takes about 20
minutes to feed everyone. This is a little fast, but they seemed to be
very excited about the freee pasta:

.. code:: python

    ActualTimeToFeedTown = 20.0 #minutes
    MultitudeModeCookRate = ActualTimeToFeedTown / PastaPotsPerTown
    print MultitudeModeCookRate


.. parsed-literal::

    0.4


So Multitude-Mode works at 40% of the speed of normal dinner-for-two
mode. You might argue that in fact the pot just produces a new pound of
pasta whenever it is empty, so the rate could go as high as you need to
feed a larger multitude -- but **this would only work if someone helped
Big Anthony serve**. The pot may indeed be magical, but Big Anthony is
most certainly **not**.

And come to think of it, we already know that the pot will keep
producing more pasta even when it is not empty, because we saw that
pasta was spilling onto the floor when Big Anthony returned with the
townsfolk. Which means that there is a third cooking mode:
**ThePotIsLonelyMode** is slower than MultitudeMode and slower than
DinnerForTwoMode -- since it certainly took more than 5 minutes for
Anthony to return with the townsfolk, which would have been enough time
to produce **300** pounds of pasta in DinnerForTwoMode, and **120**
pounds in MultitudeMode.

Next time let's think about the last stage of the story, which ends with
the townsfolk *running* down the hillside toward the town square with a
wall of pasta pursuing them:

**Q: How big is the town?**

**Q: What volume of pasta is required to fill the area from Strega
Nona's cottage to the town square? What assumptions are required to
answer this question?**
