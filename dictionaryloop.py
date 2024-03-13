student = {
    "name" :"Jesee",
   " Reg_no" : "BSCIT-05-0116/2022",
   " DOB" : "2005"
}
for x in student:
    print(student[x])

for x in student.values():
    print(x)

for x in student.keys():
    print(x)

for x, y in student.items():
    print(x, y)            