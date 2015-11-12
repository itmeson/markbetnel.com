#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Mark Betnel"
SITENAME = u"markbetnel.com"
SITEURL = 'http://markbetnel.com'

TIMEZONE = 'America/Los_Angeles'
GOOGLE_ANALYTICS = "UA-20141547-1"
DEFAULT_LANG='en'

DISQUS_SITENAME = 'nullresult'

DOCUTIL_CSS = True
DISPLAY_PAGES_ON_MENU = True

# Blogroll
LINKS =  (
    ('SAGE', 'http://sagemath.org/'),
    ('Software Carpentry', 'https://software-carpentry.org'),
    ('R - Statistics', 'https://cran.r-project.org'),
    ('DESMOS', 'https://www.desmos.com'),
    ('Seattle Academy', 'http://www.seattleacademy.info/wp/')	
        )

# Social widget
SOCIAL = (
         ('Twitter', 'https://twitter.com/markbetnel'),
         ('github', 'https://github.com/itmeson') 
	 )

PLUGIN_PATHS = ["../pelican-plugins/"]
PLUGINS = ["tipue_search", "latex", 'sitemap', 'pelican_youtube']

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))

SITEMAP = { 'format': 'xml'}

DEFAULT_PAGINATION = 20 

DISPLAY_BREADCRUMBS = True

TAG_SAVE_AS = 'tag/{slug}.html'
TAG_URL = 'tag/{slug}.html'    
