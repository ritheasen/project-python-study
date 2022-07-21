def selectionSortIdDescending(student):
    for i in range(0, len(student)):
        min = i
        for j in range(i, len(student)):
            if student[j] > student[min]:
                min = j
        student[i], student[min] = student[min], student[i]
def selectionSortIdAscending(student):
    for i in range(0, len(student)):
        min = i
        for j in range(i, len(student)):
            if student[j] < student[min]:
                min = j
        student[i], student[min] = student[min], student[i]
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

student = {'Sen':123,'Panha':110,'Thearin':112,'Daravuth':100,'Sara pich':107}
val = [value for key, value in student.items()]
selectionSortIdDescending(val)
print("ID descending sort",val)
selectionSortIdAscending(val)
print("ID ascending sort",val)

student = {123:'Sen',110:'Panha',112:'Thearin',100:'Daravuth',107:'Sara pich'}
val = [value for key, value in student.items()]
selectionSortNameAscending(val)
print("Name ascending sort",val)
selectionSortNameDescending(val)
print("Name descending sort",val)


