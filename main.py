from src.predict import predict_result

hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance: "))
marks = float(input("Enter marks: "))

result, grade = predict_result(hours, attendance, marks)

print("Result:", result)

if result == "Pass":
    print("Grade:", grade)