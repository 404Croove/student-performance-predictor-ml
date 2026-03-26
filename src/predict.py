import pickle

def get_grade(marks):
    if marks >= 91:
        return "S"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"


def predict_result(hours, attendance, marks):

    if hours < 2 or attendance < 75 or marks < 40:
        return "Fail", "Fail"

    with open('model/model.pkl', 'rb') as f:
        model = pickle.load(f)

    result = model.predict([[hours, attendance, marks]])

    if result[0] == 1:
        grade = get_grade(marks)
        return "Pass", grade
    else:
        return "Fail", "Fail"