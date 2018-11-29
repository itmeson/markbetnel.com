#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u"Mark Betnel"
SITENAME = u"Projects"
SITEURL = 'http://markbetnel.com/projects/me'

TIMEZONE = 'America/Los_Angeles'
GOOGLE_ANALYTICS = "UA-20141547-1"
DEFAULT_LANG='en'

DISQUS_SITENAME = 'betnelcourses'
COMMENTS_INTRO = "Is something unclear? Leave a comment below:"

DOCUTIL_CSS = True

DEFAULT_PAGINATION = 20 
DISPLAY_PAGES_ON_MENU = False

TAG_SAVE_AS = 'tag/{slug}.html'
TAG_URL = 'tag/{slug}.html'    

PLUGIN_PATHS = ['/home/mark/Sites/pelican-plugins'] 
PLUGINS = ['gallery', 'tipue_search', 'sitemap', 'latex']

DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))

SITEMAP = { 'format': 'xml'}

LANDING_PAGE_ABOUT = {'details': """<div itemscope itemtype="http://schema.org/Person"><p>This is a private project page for projects I'm working on<p></div>"""}

MATH_JAX = {'color':'blue', 'menuSettings': {"zoom": "Click"}}

HYPOTHESIS = True

# Uncommment this to put future dated items in drafts
#WITH_FUTURE_DATES = False

# List of directories to ignore for this version of the site
ARTICLE_EXCLUDES = ['studentonly']
