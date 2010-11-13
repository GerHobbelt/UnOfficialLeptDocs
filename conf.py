# -*- coding: utf-8 -*-
#
# Leptonica VS2008 Notes documentation build configuration file, created by
# sphinx-quickstart on Fri Mar 19 11:30:04 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.append(os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.extlinks', 'sphinx.ext.todo', 'mathjax']

extlinks = {'papersurl': ('http://leptonica.com/papers/%s',  ''),
            'sourceurl': ('http://leptonica.com/source/%s', ''),
            'unconverted': ('http://leptonica.com/%s', None),
            }

todo_include_todos = True

#mathjax_path = '/MathJax/MathJax.js'

#TEMPORARY! Use above line for real releases!
#mathjax_path = 'file:///F:/MathJax/MathJax.js'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Leptonica Documentation'
copyright = u''

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.67'
# The full version, including alpha/beta/rc tags.
release = '1.67'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["leptonica/glossary", "githtml/*", ]

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# Have to turn off default python highlight language because otherwise
# sometimes NO highlighting is done if line ends with \ char.
highlight_language = "none"

secnumber_suffix = u'\u00a0\u00a0\u00a0'     #\u00a0 is non-break space

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'leptonicatheme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}
html_theme_options = {
    }

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []
html_theme_path = [ "" ]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None
#html_title = u"Leptonica v%s Documentation" % version

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None
html_short_title = u"Unofficial v%s Documentation" % version

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None
#html_logo = '_static/moller52-smaller.jpg'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    'NONE' :
       ['localtoc.html',
        'relations.html',
        'sourcelink.html',
        'searchbox.html',
        ],
    
    '**' :
       ['globaltoc.html',
        'sourcelink.html',
        'searchbox.html',
        ],
    
    }

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True
html_use_modindex = False

# If false, no index is generated.
#html_use_index = True
html_use_index = False

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True
html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'LeptonicaDocs'

rst_prolog="""
.. role:: fs
   :class: filesystem

.. role:: bi(emphasis)
   :class: bold-italic

.. role:: raw-html(raw)
   :format: html

.. role:: cmd
   :class: command

.. role:: subtitle
   :class: subtitle

.. role:: underline
   :class: underline


.. role:: subf(subscript)
   :class: filesystem

.. role:: supf(superscript)
   :class: filesystem

.. role:: subi(subscript)
   :class: italic

.. role:: supi(superscript)
   :class: italic


.. role:: chapter-title(title-reference)
   
.. role:: compilation-title(title-reference)

.. role:: journal(title-reference)

.. role:: jvolume(title-reference)

.. role:: publisher(title-reference)

.. |leptonlib| 	  replace:: :fs:`leptonlib`

.. |Leptonica| 	  replace:: :strong:`Leptonica`

.. |BuildFolder|  replace:: :fs:`BuildFolder`

.. |BR| replace:: :raw-html:`<br />`

.. |versionF|  replace:: :fs:`%s`

.. |versionG|  replace:: :guilabel:`%s`

""" % (version, version)

rst_epilog="""
"""

html_compact_lists = False

# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'LeptonicaVS2008Notes.tex', u'Leptonica VS2008 Notes Documentation',
   u'Tom Powers', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_use_modindex = True


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
#epub_title = ''
#epub_author = ''
#epub_publisher = ''
#epub_copyright = ''

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
#epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3
