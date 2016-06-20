#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u"L'\xe9quipe Le.Taxi"
SITENAME = 'Le Taxi'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

DEFAULT_DATE_FORMAT = '%a %d %B %Y'

LOCALE = 'fr_FR.UTF8'

DISPLAY_PAGES_ON_MENU = True

DISPLAY_CATEGORIES_ON_MENU = True

THEME = 'themes/taxitheme';
PLUGIN_PATHS = [THEME + "/plugins"]
PLUGINS = ['assets','who']

STATIC_PATHS = ['images', 'extra', 'files']

EXTRA_PATH_METADATA = {
  'extra/main.py': {'path': 'main.py'},
  'extra/app.yaml': {'path': 'app.yaml'},
  'extra/robots.txt': {'path': 'robots.txt'},
  'extra/apple-touch-icon-precomposed.png': {'path': 'apple-touch-icon-precomposed.png'},
  'extra/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
  'extra/apple-touch-icon-57x57.png': {'path': 'apple-touch-icon-57x57.png'},
  'extra/apple-touch-icon-60x60.png': {'path': 'apple-touch-icon-60x60.png'},
  'extra/apple-touch-icon-72x72.png': {'path': 'apple-touch-icon-72x72.png'},
  'extra/apple-touch-icon-76x76.png': {'path': 'apple-touch-icon-76x76.png'},
  'extra/apple-touch-icon-114x114.png': {'path': 'apple-touch-icon-114x114.png'},
  'extra/apple-touch-icon-120x120.png': {'path': 'apple-touch-icon-120x120.png'},
  'extra/apple-touch-icon-144x144.png': {'path': 'apple-touch-icon-144x144.png'},
  'extra/apple-touch-icon-152x152.png': {'path': 'apple-touch-icon-152x152.png'},
  'extra/apple-touch-icon-180x180.png': {'path': 'apple-touch-icon-180x180.png'},
  'extra/favicon.ico': {'path': 'favicon.ico'},
  'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},
  'extra/favicon-32x32.png': {'path': 'favicon-32x32.png'},
  'extra/favicon-194x194.png': {'path': 'favicon-194x194.png'},
  'extra/favicon-96x96.png': {'path': 'favicon-96x96.png'},
  'extra/browserconfig.xml': {'path': 'browserconfig.xml'},
  'extra/mstile-144x144.png': {'path': 'mstile-144x144.png'},
  'extra/mstile-150x150.png': {'path': 'mstile-150x150.png'},
  'extra/mstile-310x150.png': {'path': 'mstile-310x150.png'},
  'extra/mstile-310x310.png': {'path': 'mstile-310x310.png'},
  'extra/mstile-70x70.png': {'path': 'mstile-70x70.png'},
  'extra/manifest.json': {'path': 'manifest.json'},
  'extra/android-chrome-144x144.png': {'path': 'android-chrome-144x144.png'},
  'extra/android-chrome-36x36.png': {'path': 'android-chrome-36x36.png'},
  'extra/android-chrome-48x48.png': {'path': 'android-chrome-48x48.png'},
  'extra/android-chrome-72x72.png': {'path': 'android-chrome-72x72.png'},
  'extra/android-chrome-96x96.png': {'path': 'android-chrome-96x96.png'},
  'extra/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
  'extra/manifest.json': {'path': 'manifest.json'},
  'extra/safari-pinned-tab.svg': {'path': 'safari-pinned-tab.svg'}
  }

PAGE_PATHS = ['']

ARTICLE_PATHS = ['news', 'openlab']

# put articles (posts) in news/
ARTICLE_URL = 'news/{slug}.html'
ARTICLE_SAVE_AS = 'news/{slug}.html'
# we need to change the main index page now though...
INDEX_SAVE_AS = 'news/index.html'
INDEX_URL = 'news/'
#now move all the category and tag stuff to that news/ dir as well
CATEGORY_URL = 'news/category/{slug}.html'
CATEGORY_SAVE_AS = 'news/category/{slug}.html'
CATEGORIES_URL = 'news/category/'
CATEGORIES_SAVE_AS = 'news/category/index.html'
TAG_URL = 'news/tag/{slug}.html'
TAG_SAVE_AS = 'news/tag/{slug}.html'
TAGS_URL = 'news/tag/'
TAGS_SAVE_AS = 'news/tag/index.html'
ARCHIVES_SAVE_AS = 'news/archives/archives.html'
ARCHIVES_URL = 'news/archives/archives.html'
AUTHOR_SAVE_AS = 'news/{slug}.html'
AUTHORS_SAVE_AS = 'news/authors.html'
# put pages in the root directory
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'


DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives']
PAGINATED_DIRECT_TEMPLATES = ['index']

SUMMARY_MAX_LENGTH = 50

WITH_FUTURE_DATES = True

SLUGIFY_SOURCE = 'basename'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_METADATA = {}

PIWIK_URL = 'stats.data.gouv.fr'
PIWIK_SITE_ID = '18'

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False


OUTPUT_PATH = 'output/'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
