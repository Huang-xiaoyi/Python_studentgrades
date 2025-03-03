import os

def sum(a,b):
   return a+b

def isIn():    #查找学生
   search = input('找谁？')
   if search in score:
      print(score[search])
   else:
      print('没这个人')

def add_Student():
   L = []
   name = input('名字：')
   chinese = int(input('语文成绩：'))
   Smath = int(input('数学成绩'))
   if score.get(name):
      print('已经有这么个人了')
   else:
      student.append(name)
      score[name] = [chinese, Smath]
      print('添加成功')

def down_sort(s):     #冒泡排序  升序
   for i in range(len(s)):
      for j in range(len(s)-i-1):
         if sum(score[s[j]][0], score[s[j]][1]) > sum(score[s[j+1]][0], score[s[j+1]][1]) :
            s[j], s[j+1] = s[j+1], s[j]
   for x in range(len(s)):
        if s[x] in score:
            total = sum(score[s[x]][0], score[s[x]][1])
            print(s[x],score[s[x]][0],score[s[x]][1], total)


def up_sort(s):         #冒泡排序  降序
   for i in range(len(s)):
      for j in range(len(s)-i-1):
         if sum(score[s[j]][0], score[s[j]][1]) < sum(score[s[j+1]][0], score[s[j+1]][1]) :
            s[j], s[j+1] = s[j+1], s[j]
   for x in range(len(s)):
        if s[x] in score:
            total = sum(score[s[x]][0], score[s[x]][1])
            print(s[x],score[s[x]][0],score[s[x]][1], total)

def Select_All():
    print('名字  语文  数学  总分')
    for x in range(len(student)):
        if student[x] in score:
            total = sum(score[student[x]][0], score[student[x]][1])
            print(student[x],score[student[x]][0],score[student[x]][1], total)
    while True:
        sub_choose = input('''
           \033[33m1.按总分降序排序
            2.按总分升序排序
            0.返回上一级\n\033[0m''')   #改变字体颜色，用于区分菜单和学生成绩信息

        sub_choose = int(sub_choose)

        match sub_choose:
            case 1:
               os.system('cls')
               up_sort(student)
            case 2:
               os.system('cls')
               down_sort(student)
            case 0:
               break
    return


score = {'a1': [77, 68], 'a2': [79, 89], 'a3': [88, 66]}   #预设学生信息
student = ['a1', 'a2', 'a3']    #为字典服务的学生名单
while True:
    first_choose = input('''
     1.查看全班成绩
     2.按名字查找成绩
     3.添加学生
     0.退出\n''')

    first_choose = int(first_choose)

    match first_choose:
        case 1:
           os.system('cls')
           Select_All()
        case 2:
           os.system('cls')
           isIn()
        case 3:
           os.system('cls')
           add_Student()
        case 0:
           break