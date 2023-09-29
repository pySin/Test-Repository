# Input output data for Lexicon


def data_input(data):
    filename = "lexicon.txt"
    with open(filename, "a") as o_file:
        o_file.write(data)


def data_output():
    filename = "lexicon.txt"
    with open(filename, "r") as o_file:
        return o_file.read()
