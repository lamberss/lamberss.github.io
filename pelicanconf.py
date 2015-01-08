#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Steven E. Lamberson, Jr.'
SITENAME = 'Gaming, Computing, and Physics'
SITEURL = 'http://localhost:8000'

PATH = 'content'
THEME = '/home/lamberss/.pelican-elegant'
PLUGIN_PATHS = ['/home/lamberss/.pelican-plugins']
PLUGINS = ['sitemap', 'extract_toc', 'tipue_search']
STATIC_PATHS = ['theme/images', 'images']
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))
#SITE_LICENSE = r'<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">{}</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://lamberss.github.io" property="cc:attributionName" rel="cc:attributionURL">{}</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.'.format(SITENAME, AUTHOR)
SITE_LICENSE = r'<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/80x15.png" /></a><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">{}</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://lamberss.github.io" property="cc:attributionName" rel="cc:attributionURL">{}</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.'.format(SITENAME, AUTHOR)
#SITE_LICENSE = r'<span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">{}</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://lamberss.github.io" property="cc:attributionName" rel="cc:attributionURL">{}</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.'.format(SITENAME, AUTHOR)
SEL_about = \
r"""
<p>I write things.  You can read them if you want.</p>

<p>I'll put something less snarky here when I find out what to say.</p>
"""
LANDING_PAGE_ABOUT = {'details': SEL_about}
PROJECTS = [{'name': 'acolyteGM',
             'url': 'https://github.com/lamberss/acolyteGM',
             'description': 'A tool to help RPG GMs to prep for ' + \
             'and run games.'},
            {'name': 'improv',
             'url': 'https://github.com/lamberss/improv',
             'description': 'A numerical optimization library for ' +\
             'python.'}
        ]

# CHUNK theme inputs
DEFAULT_DATE_FORMAT = ('%Y-%m-%d') #('%b %d %Y')
SITESUBTITLE = 'or whatever else I might feel like talking about'
#FOOTER_TEXT = 'Replace pelican credit'
COMMENTS_INTRO = 'Please share what you think.'
DISPLAY_CATEGORIES_ON_MENU = True
SINGLE_AUTHOR = True
#MINT = True
#GOOGLE_ANALYTICS = 'Put your google code here'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/lamberss'),
          ('Email', 'mailto:steven.lamberson@gmail.com'),)

DEFAULT_PAGINATION = 10

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
DRAFT_URL = 'drafts/{slug}'
DRAFT_SAVE_AS = 'drafts/{slug}/index.html'
PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
