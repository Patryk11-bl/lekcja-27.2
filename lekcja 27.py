try:



    plik = open('test.txt', 'r')



    plik.write('Y')
    plik.close()

except FileNotFoundError as e:
    print('Plik nie istnieje')
    print(e)
except Exception as e:
    print('Nieznany błąd')
    print(e)

