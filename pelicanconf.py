import os

from datetime import datetime, date

AUTHOR = 'Miguel Hernandez'
SITENAME = "Miguel's Personal Website"
SITETITLE = "Miguel Hernandez"
SITESUBTITLE = "Welcome to my blog/website"
SITEURL = "https://blog.miguelhx.com"
# SITEURL = "http://localhost:8000"
# SITEDESCRIPTION = "Miguel's personal website, where he blogs about tech."

SITELOGO = '/images/yinyang.png'
FAVICON = "/images/favicon.ico"

PATH = "content"
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

DISQUS_SITENAME = "miguels-personal-website"
pin_plugin_path = '/Users/miguelhernandez/programming/pelican-plugins/pin_to_top'
sitemap_plugin_path = '/Users/miguelhernandez/programming/pelican-plugins/sitemap/pelican/plugins/sitemap'
PLUGIN_PATHS = [pin_plugin_path, sitemap_plugin_path]
PLUGINS = ['pin_to_top', 'sitemap']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.5,
        'pages': 0.4
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'weekly',
        'pages': 'monthly'
    }
}


DISABLE_URL_HASH = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# MinimalXY Theme
THEME = "/Users/miguelhernandez/pelican-themes/minimal-xy"

# Theme customizations
MINIMALXY_CUSTOM_CSS = 'static/custom.css'
MINIMALXY_FAVICON = 'images/favicon.ico'
MINIMALXY_START_YEAR = 2025
MINIMALXY_CURRENT_YEAR = date.today().year

# Author
AUTHOR_INTRO = "Hello world! I'm Miguel Hernandez, a software engineer based in California. " \
"Welcome to my blog, where I write about Computer Science, Programming, Learning, and Software Engineering."
AUTHOR_DESCRIPTION = "Hello world! I'm Miguel Hernandez. I am a software engineer with a Bachelor's degree in Computer Science & Engineering and 3.5 years of professional experience. " \
"I am currently re-building my career from the ground up, starting with online courses from Open Source Society University curriculum. " \
"I'm using this space to distill insights from books, courses, and hands-on projects. " \
"Feel free to follow my journey. "
AUTHOR_AVATAR = SITEURL + FAVICON
AUTHOR_WEB = SITEURL + '/pages/about-me.html'

# Services
GOOGLE_ANALYTICS = 'G-Z648JEYS71'
# DISQUS_SITENAME = 'johndoe'

# Menu
# MENUITEMS = (
#     ('Categories', '/' + CATEGORIES_SAVE_AS),
#     ('Archive', '/' + ARCHIVES_SAVE_AS),
# )

# Blogroll
LINKS = (
    # ("Python.org", "https://www.python.org/"),
    # ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    # ("You can modify those links in your config file", "#"),
)

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True

# Social widget
SOCIAL = (
    ("github", "https://github.com/miguelhx"),
    ("linkedin", "https://www.linkedin.com/in/miguel-hernandez-535b05102/"),
)

# CC_LICENSE = {
#     "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
#     "version": "4.0",
#     "slug": "by-sa",
#     "icon": True,
#     "language": "en_US",
# }
# CC_LICENSE = {
#     "name": "Creative Commons Attribution-ShareAlike",
#     "version": "4.0",
#     "slug": "by-sa"
# }

COPYRIGHT_YEAR = datetime.now().year
COPYRIGHT_NAME = 'Miguel Hernandez'


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# THEME = "/Users/miguelhernandez/pelican-themes/Flex"

MAIN_MENU = True

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

STATIC_PATHS = ["images", 'extra/CNAME', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'}
}

FEED_ALL_ATOM  = 'feed.xml'
FEED_MAX_ITEMS = 100
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None