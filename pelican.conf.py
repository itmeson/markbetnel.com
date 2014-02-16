#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Mark Betnel"
SITENAME = u"markbetnel.com"
SITEURL = 'http://markbetnel.com/dev'

TIMEZONE = 'America/Los_Angeles'
GOOGLE_ANALYTICS = "UA-20141547-1"
DEFAULT_LANG='en'

DOCUTIL_CSS = True

# Blogroll
LINKS =  (
    ('SAGE', 'http://sagemath.org/'),
    ('Wolfram Alpha', 'http://www.wolframalpha.com/'),
    ('Khan Academy', 'http://www.khanacademy.org'),
    ('Math Fun Facts', 'http://www.math.hmc.edu/funfacts/'),
    ('R - Statistics', 'http://cran.r-project.org'),
    ('DESMOS', 'http://www.desmos.com')	
        )

# Social widget
SOCIAL = (
         ('@markbetnel', 'http://twitter.com/markbetnel'),
         ('github', 'http://github.com/itmeson') 
	 )

DEFAULT_PAGINATION = 20 
DISPLAY_PAGES_ON_MENU = False

DISPLAY_BREADCRUMBS = True

TAG_SAVE_AS = 'tag/{slug}.html'
TAG_URL = 'tag/{slug}.html'    


