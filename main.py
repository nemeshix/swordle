import re
import cmd

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# E-A-O-S-R-N-I-D-L-C. most used words


def get_hint(template, exclude, include):
    most_used = "eaosrnidlc"
    left = most_used.translate({ord(i): None for i in exclude})
    return ""


def table_print(foolist):
    cli = cmd.Cmd()
    cli.columnize(foolist, displaywidth=80)
# You even then have the option of specifying the output location, with cmd.Cmd(stdout=my_stream)


def word_filter(template, exclude, include, wrong_position):
    # "^(?!.*[ignore]).*(?=.*[include].*)(?=.*[include]+)(^.u...)$"gm
    this_regex = "^"
    for wrong in wrong_position:
        # split wrong into two parts
        # wrong[0] is the letter
        # wrong[1] is the position
        # regex exclude strings where letter wrong[0] is in position wrong[1]
        this_regex += "(?!.{" + str(int(wrong[1])-1) + "}[" + wrong[0] + "]).*"


    if exclude:
        # all excluded letters
        this_regex += fr"(?!.*[{exclude}]).*"
    if include:
        # one for each letter must include
        for character in include:
            this_regex += fr"(?=.*[{character}].*)"
    this_regex += fr"(^{template})$"
    print(this_regex)
    pattern = re.compile(this_regex, re.UNICODE)
    rae_list = open(r".\rae_palabras_5letras.txt", encoding="utf-8").read().splitlines()
    # for word in rae_list:
    #    print(word)
    #    if pattern.match(word):
    #        print(word)
    newlist = list(filter(pattern.match, rae_list))  # Read Note below
    return newlist

# filter list by regex ignore words with letters in determinate position


def solver():
    # Use a breakpoint in the code line below to debug your script.
    pattern = "..u.."
    exclude = "cre"
    include = "l"
    wrong_position = ["p1", "a1"]
    solution = word_filter(pattern, exclude, include, wrong_position)
    hint = get_hint(pattern, exclude, include)
    table_print(solution)
    table_print(hint)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solver()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

