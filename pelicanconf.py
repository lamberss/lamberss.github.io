#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Steven E. Lamberson, Jr'
SITENAME = 'Computing, Gaming, and Physics'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'en'
DATE_FORMATS = { 'en': '%Y-%m-%d' }

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
          ('google-plus', 'https://google.com/+StevenLamberson'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# Plugins
PLUGIN_PATHS = ['/home/lamberss/.pelican-plugins']
PLUGINS = ['better_figures_and_images', 'neighbors']
RESPONSIVE_IMAGES = True

# Static paths
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/custom.css': {'path': 'custom.css'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# THEME
THEME = "/home/lamberss/.pelican-themes/pelican-bootstrap3"
BOOTSTRAP_THEME = "flatly"
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True
DISPLAY_TAGS_INLINE = True
CC_LICENSE = 'CC-BY-SA'
ABOUT_ME = 'I like playing games, writing software, and numerical physics.'
AVATAR = '/images/profile.jpg'
CUSTOM_CSS = 'custom.css'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
