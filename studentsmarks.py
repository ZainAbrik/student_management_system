student_marks={"zain":50,"rama":30,"rana":25,"leen":52}
index=""
while True:
    length=len(student_marks)
    keys=list(student_marks.keys())
    x=input("input name of student: ")
    if x in keys:
        for i in range(length):
            if x==keys[i]:
             index=keys.index(x)
        print("student found")
        x2=input("would you like the key index for student?[Y/N]: ")
        if x2.lower()=="n":
            print("bye")
            break
        elif x2.lower()=="y":
            print("key index is",index,"and marks are",student_marks[x])
            n=input("would you like to perform more actions?")
            if n.lower() == "n":
                print("bye")
                break
            elif n.lower() =="y":
                print("what would you like to do?")
                n2=int(input("1.change name of student\n2.change marks of student\n3.remove a student: "))
                while True:
                 if n2==1:
                  marks=student_marks[x]
                  student_marks.pop(x)
                  print(student_marks)
                  while True:
                        m=(input("input new name"))
                        student_marks.update({m:marks})
                        print(student_marks)
                        break

                  break
                 if n2==2:
                    while True:
                        nnn=int(input("input new marks"))
                        if nnn>100 or nnn<0:
                           print("can not be over 100 or a neg")
                        else:
                           student_marks[x]=nnn
                           print("marks changed")
                           break
                    break
                 if n2==3:
                   student_marks.pop(x)
                   print('removed')
                   break
                 else:
                    print("invalid")
    else:
        print("name not found")
