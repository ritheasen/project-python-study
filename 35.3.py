
#student = {'id':[123,110,112,100,107],'name': ['Sen','Panha','Thearin','Daravuth','Sara pich']}

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

student = {'Sen':123,'Panha':110,'Thearin':112,'Daravuth':100,'Sara pich':107}

val = [value for key, value in student.items()]
selectionSortIdDescending(val)
print(val)

#value2 = [value for key, value in student.items()]
selectionSortIdAscending(val)
print(val)


