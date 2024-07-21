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
print("---------------------------------")

#A company is looking to hire a typist with writing speed more than 80 word per minute. They asked from you to design a program that’s allows the candidates to enter their typing speed. If their typing speed above 80, their will display to the user that he passed the first interview and that company will contact him later for the second interview. If speed 80 or less then inform him that the company looking only for typist with writing above 80 WPM.
speed = int (input("Enter your tyoing speed : "))
if (speed>=80):
    print("You passed the first interview and that company will contact him later for the second interview")
else:
    print("Company looking only for typist with writing above 80 WPM.")   
print("-----------------------------------------")
#Design a program that converts student score into grades (A,B,C,D, and failed)
marks=int(input("Enter your marks :"))
if (marks>=90):
    print("You Got A+ Grade")
elif(marks>=80):
    print("You got B Grade")
elif(marks>=60):
    print("You got C Garde")
else:
    print("Congrats; You got D Grade! You are fail")
 