"""Usage: strip_latex.py <tex_file> [--split=<keyword>]"""
from docopt import docopt
import re
from pathlib import Path


def main(tex_file, split=None, do_macro=False):
    with open(tex_file, 'rt') as file:
        tex = file.read()
    # strip comments
    tex = re.sub(r"([^\\])%.*", r"\g<1>", tex)

    if do_macro:
        # parse macros
        macros = re.findall(r"\\newcommand{(.+)}{(.+)}", tex)
        # print(macros)
        # TODO replace macros
        for macro, value in macros:
            print(macro, value)
            macro = r"\%s{}" % macro
            print(macro, value)
            # m = re.findall(r"{([\w\.:/]+)}", value)
            # print(m)
            # if m:
            #     value = m[0]

            tex = re.sub(macro, value, tex)

    # replace all whitespaces with ' '
    tex = re.sub('\s+', ' ', tex)

    # add newlines between split keyword
    if split is not None:
        tex = split+f"\n\n\n{split}".join(tex.split(split))

    # save output
    with open(tex_file.with_suffix('.txt'), 'wt') as file:
        file.write(tex)


if __name__ == '__main__':
    args = docopt(__doc__)
    main(Path(args['<tex_file>']), split=args['--split'])
