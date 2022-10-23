#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from utils.filters import sidebar
from markdown.extensions.tables import TableExtension

AUTHOR = "PyTexas Devs"
SITETITLE = "PyTexas Foundation"
SITENAME = "PyTexas Foundation"
SITESUBTITLE = "Home of Python in Texas"
SITEDESCRIPTION = "The PyTexas Foundation is a non-profit dedicated to educating engineers about Python in the state of Texas"
SITEURL = "http://localhost:8000"
SITESRC = "https://github.com/pytexas/pytexas.github.io"
SITELOGO = SITEURL + "/static/favicon.png"
FAVICON = SITEURL + "/static/favicon.ico"

PATH = "content/"

TIMEZONE = "America/Chicago"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# URL settings
ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"
PAGE_URL = "pages/{slug}/"
PAGE_SAVE_AS = "pages/{slug}/index.html"
# DRAFT_URL = '{slug}.html'
# DRAFT_SAVE_AS = 'drafts/{slug}.html'

# Theme
THEME = "theme/twenty-pelican-html5up"

MARKDOWN = {"extensions": [TableExtension()]}

# Plugins
# PLUGIN_PATHS = ['pelican-plugins']
# PLUGINS = ['neighbors']

# static files
STATIC_PATHS = ["static", "favicon.ico"]

JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.do"]}

COPYRIGHT_YEAR = 2022
COPYRIGHT_NAME = "PyTexas Foundation"

MAIN_MENU = True

DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ("About", "/pages/about"),
    ("Community", "/pages/community")
    # ('Categories', '/categories.html'),
    # ('Tags', '/tags.html'),
)

JINJA_FILTERS = {"sidebar": sidebar}

# Blogroll
LINKS = {"PyCon": "https://pycon.org/", "Python.org": "https://www.python.org/"}

# Social widget

SOCIAL = {
    "Twitter": "https://twitter.com/pytexas",
    #'LinkedIn': '#',
    "Discord": "https://discord.gg/jNPAbcNukj",
    "YouTube": "https://www.youtube.com/channel/UCkn0L-L6auy9YAmlSy9Kv1Q/playlists",
}

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
