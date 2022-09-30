# -*- coding: utf-8 -*-
import re

def parse_bib(bib):
    """
    Parameters
    ----------
    bib: str
        Raw text BibTeX
        
    Returns
    -------
    papers: dict[str, str]
        {key of the paper: corresponding BibTeX entry}
    """
    bib = re.sub('\s+', ' ', bib)
    papers = {}
    for paper in bib.split('@'):
        key = re.findall(r"\w*{(\w*),.*}", paper)
        if key:
            papers[key[0]] = paper
    return papers


def get_authors(bib_entry, last_name_only=False):
    """
    Parameters
    ----------
    bib_entry: str
        A value of the dict returned by parse_bib
    
    Returns
    -------
    names: List[str]
        List of authors names
    """
    text = re.findall(r"author ?= ?{([\w, -\.]*)}", bib_entry)[0]
    names = re.split(r" and ", text)
    if last_name_only:
        names = [re.findall(r"\w+", name)[0] for name in names]
    return names