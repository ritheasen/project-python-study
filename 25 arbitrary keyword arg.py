def getStudentDetails(*studentInfo):
    #print(f"Student id: {studentInfo[0]}")
    #print(f"Student Name: {studentInfo[1]}")
   # print(f"Student Age: {studentInfo[2]}")
   # print(f"Student City: {studentInfo[3]}")


    print(f"Student id: {studentInfo['id']}")
    print(f"Student Name: {studentInfo['name']}")
    print(f"Student Age: {studentInfo['age']}")
    print(f"Student City: {studentInfo['city']}")

#getStudentDetails(1234,"Sarapich",21,"Siem Reap")
getStudentDetails(id=1234, name="Sarapich", age=21, city="Siem Reap")
