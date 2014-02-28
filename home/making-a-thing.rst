Making a Thing
##############

:date: 2014-02-27
:tags: making, teaching, pelican, sbg
:summary: I'm working on tying together my sbg command-line / ipython gradebook with my pelican blog and class management tool and my school's moodle site to give me a simple way to manage everything in one place, and my students a simple way to keep up to date on what they need to do and how to improve
:category: nullresult

I'm working on making a thing, which I hope I will be very useful to me.  

I've been using jekyll and/or pelican for a couple of years to manage my site and class work, and I've used blackboard and/or moodle to manage my courses and grades, and sometimes activegrade.com and/or my command-line, standards based gradebook grade.txt.

It's all a little confusing, and the part about integrating with the school provided learning management system has *always*, despite my best efforts, ended up with me having to keep my grades and course materials in two or three different places, not always up to date in each of them.  Problems galore.

This year I've whittled it down to my cli gradebook and emailed grade reports using ipython, and I've mostly not used the moodle site at all.

I've gotten away with it because my new school has been permissive about allowing me to do things my way, and because in a totally new school with a totally new curriculum, I've been figuring out what we're doing on a weekly basis anyway -- it doesn't really matter how you present something if you don't actually know what you're doing yet.

Yesterday I got the word that my school is going to start enforcing moodle use next year, because there have been problems with inconsistency of communication to students and parents about expectations, due dates, grades, etc.  I completely agree that all of us should be communicating clearly and frequently with students and parents, and that it is more convenient if we all use the same system (especially for our Learning Support program, who do a heroic job) -- but I *really* hate the online-databaseified-LMS universe. Too much pointing and clicking, too much repetitive adjustment of settings, too many ways to make mistakes.  Also no way to maintain my own copy of my planning work, no way to use version control, no way to work offline.  And most importantly, the gradebook limitations that end up forcing me to keep the gradebook in more than one place. 

According to our technology coordinator, the number one feature the students actually use in moodle is the calendar block, which allows them to hover over a date and get a tooltip that shows all work that is due on that date -- and Learning Support relies on that feature too, which means that I have definitely been making it harder on them by not using moodle at all.   
So my new thing is going to be commit to using the pelican site to manage course material, but serve it in an iframe on the moodle site so students can find it easily in the same place their other classes are found.  I'll also write a pelican-plugin that will generate an ics calendar file to push notifications of assignments to the moodle site so they can use that number-one-feature to keep track of work.  And I will do more work on the grade.txt-cli and the ipython analysis and reporting notebooks to streamline grading and feedback.  I'm now hoping to have something functional done in the next two weeks, so I can try it out on the spring trimester class, and demonstrate to the school that I can do all the things they want me to do in my own way, before the mandate comes through.

And for a change, I'm going to try to be more public about what I'm doing, in the hope of getting some feedback to me so I actually start getting better at all this -- my coding has been in a bit of a rut for a while, as I seem to keep doing things in the same ways, and not really improving.


The todo list is something like this:

 * Flesh out the pelican labscience site content to serve as the source of daily work, homework, project info, etc. for the spring term course (duedate:2014-03-07) (labscience_)
 * Use the google search box to offer students a way to find content on the site (done)
 * Write a pelican-plugin (create_calendar) which will hunt for duedate tags in course content, then create an ics file with all assignments, which will be pulled into moodle using the Manage Subscription widget.  This will allow students in my classes to see their upcoming assignments in the same place they see upcoming assignments from their other classes (and will allow Learning Support to see the schedule too) (duedate:2014-03-03) (create_calendar_)
 * Have moodle pull the course website into an iframe to display in the moodle site.  Students will come there first, but future clicks will take them directly to my site (duedate:2014-03-07)
 * Continue development of the grade.txt-cli to make data entry faster and more intuitive, as well as the ipython notebooks for processing, sending well-formatted reports, and doing data analysis (grade.txt-cli_)

.. _labscience: http://github.com/itmeson/labscience
.. _create_calendar: http://github.com/itmeson/pelican-plugins
.. _grade.txt-cli: http://github.com/itmeson/grade.txt-cli
 


