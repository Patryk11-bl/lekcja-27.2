try:



    plik = open('test.txt', 'r')



    plik.write('Y')
    plik.close()

except FileNotFoundError:
    print(' Plik nie istnieje, utwórz plik')
except:
    print('Nieznany błąd')


