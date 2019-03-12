import glob, os

def menu():#выводит меню 
    print ("Выберите команду:\n0-Выход из программы\n1-посчитать количество файлов \n2-Отсортировать файлы по цене \n3-дичь\n4-Сохранить изменения")
    n=int(input())
    print("Вы выбрали",n,"-ую команду\n")
    return n

def end():#выводит вопрос после выполнения функции
        print("Желаете продолжить?")
        print("yes or no")
        answ=str(input())
        return answ
def firstf():
    print("Количество файлов в папке:", len(os.listdir("newfolder")))
    pass
def secondf():
    f = open('newfolder/products.txt', 'r')
    for line in f: 
        line.split(";")
        print(line)
        #незаконченная функция
def thirdf():
     #незаконченная функция
def fourthf():
     #незаконченная функция


answ="yes"
while answ=="yes":
    n=menu()
    if n!=0:
        if n==1:#1я функция
            firstf()
        elif n==2:#2я функция
            secondf()
        elif n==3:#3я функция
            thirdf()
        elif n==4:#4я функция
            fourthf()
    else:
        print("Выход из программы....")
        break
    answ=end()
