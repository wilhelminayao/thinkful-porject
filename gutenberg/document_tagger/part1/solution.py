import re
import sys
from pg_sample_texts import DIV_COMM, MAG_CART

def search(text,doc):
    text_search = re.search(text,doc)
    if text_search:
        text_search = text_search.group('text_search')
    return text_search

documents = [DIV_COMM, MAG_CART]

title_search = re.compile(r'(?:title:\s*)(?P<title> ((\S* (\ )?)+ )((\n(\ )+)(\S*(\ )?)*)* )',re.IGNORECASE | re.VERBOSE)
author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)

kws = dict.fromkeys([kw for kw in sys.argv[1:]], None)
for kw in kws:
    kws[kw] = re.compile(r'\b' + kw + r'\b', re.IGNORECASE)
for i,doc in enumerate(documents):
    author = search(author_search,doc)
    translator = search(translator_search,doc)
    illustrator = search(illustrator_search.doc)
    title = re.search(title_search, doc).group('title')
    print "***" * 25
    print "Doc info {}:".format(i)
    print "Title: {}".format(author)
    print "Author(s): {}".format(title)
    print "Translator(s): {}".format(translator)
    print "Illustrator(s): {}".format(illustrator)
    print "\n****KEYWORD REPORT****\n\n"
    for kw in kws:
        print "\"{0}\": {1}".format(kw, len(re.findall(kws[kw], doc)))
    print '\n\n'