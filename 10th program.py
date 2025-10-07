#1.Given a dictionary

student_grades={'Alice':90,'Bob':85,'Charlie':74,'Mike':70}
#print the grade of Charlie
print("The grade of Charlie is",student_grades['Charlie'])
#Update the grade of Bob to 90
student_grades['Bob']=90

#Add new item 'Sam':75 to the dictionary
student_grades['Sam']=75
#print the total number of students in the dictionary
print("the total number of students is",len(student_grades))
#print all student names from the dictionary
print(student_grades.keys())

#2.Given a list
colors=['red','green','yellow']

#Add new color 'black'
colors.append('black')
print(colors)
#update 2nd index to blue
colors[2]='blue'
print(colors)
#3.Given a set
s={'guitar','veena','drums'}
#add new item 'flute' to set
s.add('flute')
print(s)