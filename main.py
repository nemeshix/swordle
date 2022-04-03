import re
import cmd

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# E-A-O-S-R-N-I-D-L-C. most used words

def table_print(foolist):
    cli = cmd.Cmd()
    cli.columnize(foolist, displaywidth=80)
# You even then have the option of specifying the output location, with cmd.Cmd(stdout=my_stream)


def word_filter(template, exclude, include):
    this_regex = fr"(?=.*[{include}]+)(^{template})(?<=[^{exclude}])$"
    print(this_regex)
    pattern = re.compile(this_regex, re.UNICODE)
    rae_list = open(r".\rae_palabras_5letras.txt", encoding="utf-8").read().splitlines()
    # for word in rae_list:
    #    print(word)
    #    if pattern.match(word):
    #        print(word)
    newlist = list(filter(pattern.match, rae_list))  # Read Note below

    return newlist


def solver():
    # Use a breakpoint in the code line below to debug your script.
    solution = word_filter("a....", "poriscnedz", "b")
    table_print(solution)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solver()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

