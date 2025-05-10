try:



    plik = open('test.txt', 'r+')



    plik.write('Hello')
    plik.close()

except FileNotFoundError:
    print('Yyy plik nie istnieje, utwórz plik')


