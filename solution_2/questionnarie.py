#  Questionnaire

def questionnaire():
    questions = ["Name: ", "Date of birth: ", "Profession: ", "Gender(m/f): ", "Phone Number: "]

    info_string = ""

    for question in questions:
        info = input(f"{question}")
        info_string += info + ", "
    info_string = info_string[:-2] + "\n"
    return info_string
