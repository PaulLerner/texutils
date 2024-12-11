# texutils
## strip
Strip all comments and whitespaces from LaTeX -> raw text.

Relies on https://github.com/asweigart/pyperclip to read/write from clipboard:
- On Windows, no additional modules are needed.
- On Mac, this module makes use of the `pbcopy` and `pbpaste` commands, which should come with the os.
- On Linux, this module makes use of the `xclip` or `xsel` commands, which should come with the os. 
  Otherwise run `sudo apt-get install xclip` or `sudo apt-get install xsel` (Note: `xsel` does not always seem to work.)
