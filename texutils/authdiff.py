# -*- coding: utf-8 -*-
"""
usage: authdiff.py [-h] bib a b

Shows intersection and differences between the authors of two papers.

positional arguments:
  bib         Path to the bib file
  a           Key of the first paper
  b           Key of the second paper

optional arguments:
  -h, --help  show this help message and exit
"""

import argparse

from .utils import parse_bib, get_authors


def authdiff(bib, a, b):
    with open(bib, 'rt') as file:
        bib = file.read()
    bib = parse_bib(bib)
    a_authors = set(get_authors(bib[a]))
    b_authors = set(get_authors(bib[b]))
    print(f"Authors in both {a} and {b}: {a_authors&b_authors}")   
    print(f"Authors in {a} but not {b}: {a_authors-b_authors}")    
    print(f"Authors in {b} but not {a}: {b_authors-a_authors}")  
    

def main():
    parser = argparse.ArgumentParser(
        description="Shows intersection and differences between the authors of two papers."
    )
    parser.add_argument('bib', type=str, help='Path to the bib file')
    parser.add_argument('a', type=str, help='Key of the first paper')
    parser.add_argument('b', type=str, help='Key of the second paper')

    args = parser.parse_args()
    authdiff(**vars(args))


if __name__ == '__main__':
    main()