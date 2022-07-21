def selectionSortNameAscending(student):
    for i in range(0, len(student)):
        min = i
        for j in range(i, len(student)):
            if len(student[j]) < len(student[min]):
                min = j
        student[i], student[min] = student[min], student[i]

def selectionSortNameDescending(student):
    for i in range(0, len(student)):
        min = i
        for j in range(i, len(student)):
            if len(student[j]) > len(student[min]):
                min = j
        student[i], student[min] = student[min], student[i]

student = {123:'Sen',110:'Panha',112:'Thearin',100:'Daravuth',107:'Sara pich'}
#student = {'Sen':123,'Panha':110,'Thearin':112,'Daravuth':100,'Sara pich':107}

val = [value for key ,value in student.items() ]
selectionSortNameAscending(val)
print(val)

selectionSortNameDescending(val)
print(val)
