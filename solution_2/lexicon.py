#  Run lexicon functionalities
from io_data import data_input, data_output
from questionnarie import questionnaire


def function_call():
    data = questionnaire()
    data_input(data)
    get_data = data_output()
    print(get_data)


if __name__ == "__main__":
    function_call()
