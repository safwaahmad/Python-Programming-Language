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
    