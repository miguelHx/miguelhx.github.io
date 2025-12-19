import os

from datetime import datetime

AUTHOR = 'Miguel Hernandez'
SITENAME = "Miguel's Personal Website"
SITETITLE = "Miguel Hernandez"
SITESUBTITLE = "Welcome to my blog/website"
# SITEDESCRIPTION = "Miguel's personal website, where he blogs about tech."

SITELOGO = '/images/yinyang.png'

PATH = "content"
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

DISQUS_SITENAME = "miguels-personal-website"
plugin_path = os.environ['PIN_PLUGIN_PATH']
PLUGIN_PATHS = [plugin_path]
PLUGINS = ['pin_to_top']

DISABLE_URL_HASH = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

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

THEME = "/Users/miguelhernandez/pelican-themes/Flex"

MAIN_MENU = True

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

STATIC_PATHS = ["images"]

GOOGLE_GLOBAL_SITE_TAG = "G-Z648JEYS71"