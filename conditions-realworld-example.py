#Your teacher asked from you to write a program that allows her to enter student 3 exam result and then the program calculates the average and displays whether student had passed the semester or no. in order to pass the semester, the average score must be 50 or more.
NoOfExam=4
eng=float(input("Enter the marks in eng : "))
math=float(input("Enter the marks in math :"))
sci=float(input("Enter the marks in sci :"))
stat=float(input("Enter the marks in stat :"))
result = eng+math+sci+stat
AvverageMarks = result/NoOfExam
if (AvverageMarks <= 50):
    print("The student failed the exam")
else:
    print("The student passed the exam")
    