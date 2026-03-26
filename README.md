# Student Performance Predictor 🎓

## About the Project

This project is a simple machine learning-based system that predicts whether a student will pass or fail based on a few important academic factors like study hours, attendance, and internal marks.

Along with predicting pass/fail, the system also assigns a grade (S, A, B, D) to students who pass. The idea behind this project is to simulate how real academic performance evaluation works while applying concepts learned in AI and ML.

---

## Why I Made This

In real life, student performance depends on multiple factors, not just marks. Attendance and effort (study hours) also play an important role.

So instead of just using marks, I built a model that considers:

* Study hours
* Attendance percentage
* Internal marks

This makes the system more realistic and meaningful.

---

## How It Works

The project uses a **Logistic Regression model** to predict whether a student will pass or fail.

On top of that, I have added a **rule-based check** to ensure:

* Minimum study hours ≥ 2
* Minimum attendance ≥ 75%
* Minimum marks ≥ 40

If these conditions are not satisfied, the system directly outputs "Fail".

If the student passes, a grade is assigned based on marks.

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Pickle (for saving the model)

---

## Project Structure

```plaintext
student-performance-predictor/
│
├── data/
│   └── student_data.csv
│
├── src/
│   ├── train.py
│   ├── predict.py
│
├── model/
│   └── model.pkl
│
├── main.py
├── requirements.txt
└── README.md
```

---

## How to Run the Project

### 1. Install dependencies

Make sure Python is installed, then run:

```
pip install -r requirements.txt
```

---

### 2. Train the model

```
python src/train.py
```

This will create a trained model file inside the `model` folder.

---

### 3. Run the program

```
python main.py
```

You will be asked to enter:

* Study hours
* Attendance
* Marks

The system will then output the result and grade.

---

## Example

Input:

```
Study Hours: 5
Attendance: 80
Marks: 85
```

Output:

```
Result: Pass
Grade: A
```

---

## Grading System

* 91–100 → S Grade
* 75–90 → A Grade
* 60–74 → B Grade
* 40–59 → D Grade
* Below 40 → Fail

---

## Key Learning

Through this project, I understood:

* How supervised learning works
* How classification models are trained
* The importance of good dataset design
* Difference between rule-based logic and ML predictions
* How both can be combined to build a better system

---

## Possible Improvements

If I had more time, I would:

* Use a larger dataset
* Add accuracy metrics and graphs
* Build a simple GUI for better interaction
* Try different models like Decision Trees

---

## Final Thoughts

This project may be simple, but it helped me understand the basics of machine learning and how it can be applied to real-world scenarios. It also shows how combining logic and ML can create more reliable systems.

---

## Author

Siddhartha Singh Sikarwar
