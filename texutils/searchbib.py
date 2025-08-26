import re
from jsonargparse import CLI
import pyperclip
from pathlib import Path


def find(keys, bib):
    results = []
    for m in re.finditer("|".join(keys),bib):
        s=m.start()
        i = bib[s-20:s].find("@")+s-20
        j=bib[s:].find("@")+s
        results.append(bib[i:j])
        print(bib[i:j])
    pyperclip.copy("\n".join(results))
    print("\n**Copied to clipboard**")


def main(error_log: Path, bib_path: Path):
    """Search missing references (from error log) in (another) bib file"""
    with open(error_log, 'rt') as file:
        log = file.read()
#    keys = re.findall(r'find a database entry for "(.+)"', log)
    keys = re.findall(r"Package natbib Warning: Citation `(.+)' on page", log)
    assert keys, f"Didn't find any match"
    with open(bib_path, 'rt') as file:
        bib = file.read()
    find(keys, bib)


if __name__ == '__main__':
    CLI(main, description=main.__doc__)
