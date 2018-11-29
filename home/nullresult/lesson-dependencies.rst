Lesson Dependencies
###################

:date: 2014-07-21
:tags: teaching, planning, swc, techism
:category: nullresult
:status: draft

There's been quite a bit of discussion at Software Carpentry the last few
months about why it is that collaborative creation and maintenance of
lessons/curriculum is far less common than collaborative creation and
maintenance of software (all of open source / github / etc. ) and of content
(wikipedia).

Greg and others in the SWC community are mostly focused on the tooling aspect
of the issue: they suggest that the problem is the lack of easily used tools to
manage the dependencies between lessons.  Without such tools it is unclear how
a GitHub-lessons would work, as a potential contributor to my set of lessons on
geometry would fork my project, write new lessons that contribute to the
project, submit the pull request -- and I as maintainer would have no idea how
to merge it.  Does their lesson on similar triangles come before the one on
measuring angles?  Or before it?  Have they broken the dependencies that I
envisioned by making use of a concept that isn't yet defined in the course?

For myself, I'd love to be able to work on a curriculum project with others,
using all the tools of the open source community, but I think teachers working
together like that first need to solve the problem of collaboration-with-self.
I tend to recreate my own content over and over again, because it is far easier
to rethink and rewrite than it is to sift through all the stuff I have created
before, edit it for new use, and then run with it again.

I'm making first steps in this direction by hosting all my course materials on
github, and using branches to manage multiple versions of a course.  But let's
say I have a great lesson that I like on ...


http://software-carpentry.org/blog/2014/03/collaborative-lesson-development.html#comment-1313416352

