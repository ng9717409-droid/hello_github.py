marks=[]
overall_marks=int(input("Enter the overall marks="))
subjects=int(input("Enter the total number of subjects="))
for i in range (1,subjects+1):
  mark=int(input("Enter the your marks="))
  marks.append(mark)
print("The list of your marks is=", marks)
total=0
for i in marks:
  total=total+i
print("The total marks you obtained=", total)
percent=(total/overall_marks)*100
print("percentage", percent)
if percent>90:
  print("Outstanding performance")
elif percent>80:
  print("Very good performance")
else:
  print("keep it up like this")

