import os,re

def isIn(search = ''):    #查找学生
   if search == '':
      search = input('找谁？')
   with open('Student.txt', 'r') as f:
      s = f.readline()
      while s != '':
         G = re.match(r'(\w+) (\d+) (\d+)', s)
         if G.group(1) == search:
            print(G.group(0))
            return True
         else:
            s = f.readline()
      print('没这个人')
      return False

def add_Student():
   name = input('名字：')
   chinese = input('语文成绩：')
   Smath = input('数学成绩')
   if isIn(name):
      print('已经有这么个人了')
   else:
      print("开始插入新数据：\n")
      with open('Student.txt', 'a', encoding= 'UTF-8') as f:
         s = name + ' ' + chinese + ' ' + Smath + '\n'
         f.write(s)

def student_sort(isReverse):
   with open('Student.txt', 'r') as f:
      lines = f.readlines()
   
   student = []
   for line in lines:
      part = line.strip().split()
      name = part[0]
      Smath = int(part[1])
      chinese = int(part[2])
      total = Smath + chinese
      student.append((name, Smath, chinese, total))

   sorted_student = sorted(student, key=lambda x : x[3], reverse=isReverse)

   for student in sorted_student:
      print(f"{student[0]} {student[1]} {student[2]} {student[3]}")


def Select_All():
   print('名字  语文  数学  总分')
   with open('Student.txt', 'r') as f:
      s = f.readline()
      while s != '':
         m = re.match(r'(\w+) (\d+) (\d+)', s)
         s = f.readline()
         total = int(m.group(2)) + int(m.group(3))
         print(m.group(0) + ' %d' % (total))

   while True:
      sub_choose = input('''
         \033[33m1.按总分降序排序
         2.按总分升序排序
         0.返回上一级\n\033[0m''')   #改变字体颜色，用于区分菜单和学生成绩信息


      match sub_choose:
         case '1':
            os.system('cls')
            student_sort(True)
         case '2':
            os.system('cls')
            student_sort(False)
         case '0':
            break
   return



while True:
    first_choose = input('''
     1.查看全班成绩
     2.按名字查找成绩
     3.添加学生
     0.退出\n''')

   

    match first_choose:
        case '1':
           os.system('cls')
           Select_All()
        case '2':
           os.system('cls')
           isIn()
        case '3':
           os.system('cls')
           add_Student()
        case '0':
           break