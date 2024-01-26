#!/usr/bin/env python
#
#                               parse_text.py
#

import xml.etree.ElementTree as ET
#from gensim.models import word2vec
#import logging

def parse_xml(i_file):

    tree = ET.parse(i_file)
    root = tree.getroot()
    body = root[0][0]
    div = root[0][0][0]
    w = []
    n = 0
    for child in div:
        if child.tag == 'l' and child.text is not None:
            print ('enter l')
            n = get_new_n(n, child)
            w += [(child.text, n)]
        if child.tag == 'q':    # quote
            w += extract_lines(n, child)
    return w


def extract_lines(n, div):

    w = []
    for child in div:
        #print (child.tag, child.text, 'prev', n, child.attrib, len(child))
        if child.tag == 'l':
            if len(child) >=1:
                if child[0].tag == 'milestone':
                    y = child[0]
                    print (y.tail, 'MILESTONE')
                    text = y.tail
            else:
                text = child.text
        if text is None:
            continue
        n = get_new_n(n, child)
        print (text, n)
        w.append((text, n))
    return w


def get_new_n(n, x):

    attrib = x.attrib
    if 'n' in attrib:
        n = int(attrib['n'])
    else:
        n += 1
    return n


def parse_dir(i_dir):

    import glob
    w = []
    file = glob.glob(i_dir)
    for i_file in sorted(file):
        print ('TEXT FILE:', i_file)
        w += parse_xml(i_file)
    return w


def normalize(text):

    w = []
    for line in text:
        s = ''.join([c for c in line.lower() if c not in STOPWORD])
        print (s)
        w.append(' '.join(s))
    return ' '.join(w)


def write_text(text, o_file):

    print ('WRITE', o_file)
    with open(o_file, 'wt') as o_handle:
        for line in text:
            o_handle.write(line[0] + (' ' * (LINE_LEN - len(line[0]))) + '%3d\n' % line[1])


if __name__ == '__main__':

    LINE_LEN = 60
    STOPWORD = '"\'\:\;\“\”\.\,\(\)\!\?'
    #IDIR    = 'data/perseus/*.xml'
    DIR = 'data/perseus'
    IFILE   = '%s/odysseia_book_9.xml' % DIR; OFILE = '%s/book9.txt' % DIR

    """
    text = parse_dir(IDIR)
    """
    text = parse_xml(IFILE)
    write_text(text, OFILE)
