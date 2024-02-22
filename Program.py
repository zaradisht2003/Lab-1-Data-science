
num=int(input("Enter the number of students : "))
lis=[]
for i in range(num):
    name=input("Enter the name of student #"+str(i+1)+": ")
    id=input("Enter the ID of student #"+str(i+1)+": ")
    age=input("Enter the Age of student #"+str(i+1)+": ")
    faculty=input("Enter the Faculty of student #"+str(i+1)+": ")
    lis.append([name,id,age,faculty])

for i in range(num):
    print("Student #",i+1,": ")
    print("  Name: ",lis[i][0])
    print("  ID:   ",lis[i][1])
    print("  Age:   ",lis[i][2])
    print("  Faculty:   ",lis[i][3])

