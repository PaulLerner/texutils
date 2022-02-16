"""Usage: strip_latex.py <tex_file>"""
from docopt import docopt
import re
from pathlib import Path


def main(tex_file):
    with open(tex_file, 'rt') as file:
        tex = file.read()
    # strip comments
    tex = re.sub(r"([^\\])%.*", r"\g<1>", tex)

    # TODO
    # parse macros
    # macros = re.findall(r"\\newcommand{(.+)}{(.+)}", tex)
    # print(macros)
    # for macro, value in macros:
    #     m = re.findall(r"{([\w\.:/]+)}", value)
    #     print(m)
    #     if m:
    #         value = m[0]
    #
    #     tex = re.sub(macro[1:]+"%s{}", value, tex)
    # replace macros

    # replace all whitespaces with ' '
    tex = re.sub('\s+', ' ', tex)

    # save output
    with open(tex_file.with_suffix('.txt'), 'wt') as file:
        file.write(tex)


if __name__ == '__main__':
    args = docopt(__doc__)
    main(Path(args['<tex_file>']))