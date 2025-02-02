=========
FlashText
=========

.. image:: https://travis-ci.org/francbartoli/pyflashtext.svg?branch=master
    :target: https://travis-ci.org/francbartoli/pyflashtext
    :alt: Build Status

.. image:: https://readthedocs.org/projects/pyflashtext/badge/?version=latest
    :target: http://pyflashtext.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://badge.fury.io/py/pyflashtext.svg
    :target: https://badge.fury.io/py/pyflashtext
    :alt: Version

.. image:: https://coveralls.io/repos/github/francbartoli/pyflashtext/badge.svg?branch=master
    :target: https://coveralls.io/github/francbartoli/pyflashtext?branch=master
    :alt: Test coverage

.. image:: https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000
    :target: https://github.com/francbartoli/pyflashtext/blob/master/LICENSE
    :alt: license


This module can be used to replace keywords in sentences or extract keywords from sentences. It is based on the `FlashText algorithm <https://arxiv.org/abs/1711.00046>`_.


Installation
------------
::

    $ pip install pyflashtext


API doc
-------

Documentation can be found at `FlashText Read the Docs
<http://pyflashtext.readthedocs.io/>`_.


Usage
-----
Extract keywords
    >>> from pyflashtext import KeywordProcessor
    >>> keyword_processor = KeywordProcessor()
    >>> # keyword_processor.add_keyword(<unclean name>, <standardised name>)
    >>> keyword_processor.add_keyword('Big Apple', 'New York')
    >>> keyword_processor.add_keyword('Bay Area')
    >>> keywords_found = keyword_processor.extract_keywords('I love Big Apple and Bay Area.')
    >>> keywords_found
    >>> # ['New York', 'Bay Area']

Replace keywords
    >>> keyword_processor.add_keyword('New Delhi', 'NCR region')
    >>> new_sentence = keyword_processor.replace_keywords('I love Big Apple and new delhi.')
    >>> new_sentence
    >>> # 'I love New York and NCR region.'

Case Sensitive example
    >>> from pyflashtext import KeywordProcessor
    >>> keyword_processor = KeywordProcessor(case_sensitive=True)
    >>> keyword_processor.add_keyword('Big Apple', 'New York')
    >>> keyword_processor.add_keyword('Bay Area')
    >>> keywords_found = keyword_processor.extract_keywords('I love big Apple and Bay Area.')
    >>> keywords_found
    >>> # ['Bay Area']

Span of keywords extracted
    >>> from pyflashtext import KeywordProcessor
    >>> keyword_processor = KeywordProcessor()
    >>> keyword_processor.add_keyword('Big Apple', 'New York')
    >>> keyword_processor.add_keyword('Bay Area')
    >>> keywords_found = keyword_processor.extract_keywords('I love big Apple and Bay Area.', span_info=True)
    >>> keywords_found
    >>> # [('New York', 7, 16), ('Bay Area', 21, 29)]

Get Extra information with keywords extracted
    >>> from pyflashtext import KeywordProcessor
    >>> kp = KeywordProcessor()
    >>> kp.add_keyword('Taj Mahal', ('Monument', 'Taj Mahal'))
    >>> kp.add_keyword('Delhi', ('Location', 'Delhi'))
    >>> kp.extract_keywords('Taj Mahal is in Delhi.')
    >>> # [('Monument', 'Taj Mahal'), ('Location', 'Delhi')]
    >>> # NOTE: replace_keywords feature won't work with this.

No clean name for Keywords
    >>> from pyflashtext import KeywordProcessor
    >>> keyword_processor = KeywordProcessor()
    >>> keyword_processor.add_keyword('Big Apple')
    >>> keyword_processor.add_keyword('Bay Area')
    >>> keywords_found = keyword_processor.extract_keywords('I love big Apple and Bay Area.')
    >>> keywords_found
    >>> # ['Big Apple', 'Bay Area']

Add Multiple Keywords simultaneously
    >>> from pyflashtext import KeywordProcessor
    >>> keyword_processor = KeywordProcessor()
    >>> keyword_dict = {
    >>>     "java": ["java_2e", "java programing"],
    >>>     "product management": ["PM", "product manager"]
    >>> }
    >>> # {'clean_name': ['list of unclean names']}
    >>> keyword_processor.add_keywords_from_dict(keyword_dict)
    >>> # Or add keywords from a list:
    >>> keyword_processor.add_keywords_from_list(["java", "python"])
    >>> keyword_processor.extract_keywords('I am a product manager for a java_2e platform')
    >>> # output ['product management', 'java']

To Remove keywords
    >>> from pyflashtext import KeywordProcessor
    >>> keyword_processor = KeywordProcessor()
    >>> keyword_dict = {
    >>>     "java": ["java_2e", "java programing"],
    >>>     "product management": ["PM", "product manager"]
    >>> }
    >>> keyword_processor.add_keywords_from_dict(keyword_dict)
    >>> print(keyword_processor.extract_keywords('I am a product manager for a java_2e platform'))
    >>> # output ['product management', 'java']
    >>> keyword_processor.remove_keyword('java_2e')
    >>> # you can also remove keywords from a list/ dictionary
    >>> keyword_processor.remove_keywords_from_dict({"product management": ["PM"]})
    >>> keyword_processor.remove_keywords_from_list(["java programing"])
    >>> keyword_processor.extract_keywords('I am a product manager for a java_2e platform')
    >>> # output ['product management']

To check Number of terms in KeywordProcessor
    >>> from pyflashtext import KeywordProcessor
    >>> keyword_processor = KeywordProcessor()
    >>> keyword_dict = {
    >>>     "java": ["java_2e", "java programing"],
    >>>     "product management": ["PM", "product manager"]
    >>> }
    >>> keyword_processor.add_keywords_from_dict(keyword_dict)
    >>> print(len(keyword_processor))
    >>> # output 4

To check if term is present in KeywordProcessor
    >>> from pyflashtext import KeywordProcessor
    >>> keyword_processor = KeywordProcessor()
    >>> keyword_processor.add_keyword('j2ee', 'Java')
    >>> 'j2ee' in keyword_processor
    >>> # output: True
    >>> keyword_processor.get_keyword('j2ee')
    >>> # output: Java
    >>> keyword_processor['colour'] = 'color'
    >>> keyword_processor['colour']
    >>> # output: color

Get all keywords in dictionary
    >>> from pyflashtext import KeywordProcessor
    >>> keyword_processor = KeywordProcessor()
    >>> keyword_processor.add_keyword('j2ee', 'Java')
    >>> keyword_processor.add_keyword('colour', 'color')
    >>> keyword_processor.get_all_keywords()
    >>> # output: {'colour': 'color', 'j2ee': 'Java'}

For detecting Word Boundary currently any character other than this `\\w` `[A-Za-z0-9_]` is considered a word boundary.

To set or add characters as part of word characters
    >>> from pyflashtext import KeywordProcessor
    >>> keyword_processor = KeywordProcessor()
    >>> keyword_processor.add_keyword('Big Apple')
    >>> print(keyword_processor.extract_keywords('I love Big Apple/Bay Area.'))
    >>> # ['Big Apple']
    >>> keyword_processor.add_non_word_boundary('/')
    >>> print(keyword_processor.extract_keywords('I love Big Apple/Bay Area.'))
    >>> # []


Test
----
::

    $ git clone https://github.com/francbartoli/pyflashtext
    $ cd pyflashtext
    $ pip install pytest
    $ python setup.py test


Build Docs
----------
::

    $ git clone https://github.com/francbartoli/pyflashtext
    $ cd pyflashtext/docs
    $ pip install sphinx
    $ make html
    $ # open _build/html/index.html in browser to view it locally


Why not Regex?
--------------

It's a custom algorithm based on `Aho-Corasick algorithm
<https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm>`_ and `Trie Dictionary
<https://en.wikipedia.org/wiki/Trie Dictionary>`_.

.. image:: https://github.com/francbartoli/pyflashtext/raw/master/benchmark.png
    :target: https://twitter.com/RadimRehurek/status/904989624589803520
    :alt: Benchmark


Time taken by FlashText to find terms in comparison to Regex.

.. image:: https://thepracticaldev.s3.amazonaws.com/i/xruf50n6z1r37ti8rd89.png


Time taken by FlashText to replace terms in comparison to Regex.

.. image:: https://thepracticaldev.s3.amazonaws.com/i/k44ghwp8o712dm58debj.png

Link to code for benchmarking the `Find Feature <https://gist.github.com/francbartoli/604eefd92866d081cfa19f862224e4a0>`_ and `Replace Feature <https://gist.github.com/francbartoli/dc3335ee46ab9f650b19885e8ade6c7a>`_.

The idea for this library came from the following `StackOverflow question
<https://stackoverflow.com/questions/44178449/regex-replace-is-taking-time-for-millions-of-documents-how-to-make-it-faster>`_.


Citation
----------

The original paper published on `FlashText algorithm <https://arxiv.org/abs/1711.00046>`_.

::

    @ARTICLE{2017arXiv171100046S,
       author = {{Singh}, V.},
        title = "{Replace or Retrieve Keywords In Documents at Scale}",
      journal = {ArXiv e-prints},
    archivePrefix = "arXiv",
       eprint = {1711.00046},
     primaryClass = "cs.DS",
     keywords = {Computer Science - Data Structures and Algorithms},
         year = 2017,
        month = oct,
       adsurl = {http://adsabs.harvard.edu/abs/2017arXiv171100046S},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
    }

The article published on `Medium freeCodeCamp <https://medium.freecodecamp.org/regex-was-taking-5-days-pyflashtext-does-it-in-15-minutes-55f04411025f>`_.


Contribute
----------

- Issue Tracker: https://github.com/francbartoli/pyflashtext/issues
- Source Code: https://github.com/francbartoli/pyflashtext/


License
-------

The project is licensed under the MIT license.
