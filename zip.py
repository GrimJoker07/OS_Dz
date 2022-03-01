def Zad5():
    import zipfile
    import os
    i=input()
    newzip = zipfile.ZipFile('bdseoru.zip', 'w')
    f = open("fike.txt", "w")
    f.write(i)
    f.close()
    newzip.write('fike.txt')
    os.remove("fike.txt")
    while True:
        x = int(input("Показать содержимое файла:1-да/2-извлечь файл/3-удалить"))
        if x == 0:
            break
        elif x == 1:
            newzip.printdir()
        elif x == 2:
            newzip.extract('fike.txt')
            with open("fike.txt", "r") as f:
                y = f.read()
                print(y)
                f.close()
        elif x == 3:
            newzip.close()
            os.remove("bdseoru.zip")
            try:
                os.remove("fike.txt")
            except FileNotFoundError:
                pass
            else:
                os.remove("fike.txt")
            break