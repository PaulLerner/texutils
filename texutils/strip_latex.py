import re
from pathlib import Path
from jsonargparse import CLI


def multi_line_input(message=""):
    print(message, end="")
    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break
    return '\n'.join(lines)


def main(tex_file: Path = None, split: str = r"\section{"):
    do_macro=False

    if tex_file is not None:
        with open(tex_file, 'rt') as file:
            tex = file.read()
    else:
        tex = multi_line_input("Paste your tex here then press Ctrl+D\n>>> ")
    # strip comments
    tex = re.sub(r"([^\\])%.*", r"\g<1>", tex)

    if do_macro:
        # parse macros
        macros = re.findall(r"\\newcommand{(.+)}{(.+)}", tex)
        # print(macros)
        # TODO replace macros
        raise NotImplementedError("need to fix escape characters because of '\\'")
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
    if tex_file is not None:
        with open(tex_file.with_suffix('.txt'), 'wt') as file:
            file.write(tex)
    else:
        print("\n\n", tex)


if __name__ == '__main__':
    CLI(main)
