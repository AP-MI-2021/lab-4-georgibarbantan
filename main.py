def citire_lista():
    """
    functia citeste o lista de numere ca string si il transforma in numere de tip float
    :return: lista cu numere float
    """
    result_list = []
    string_lista = input("Introduceti lista: ")

    string_elemente = string_lista.split(sep=" ")

    for string_element in string_elemente:
        element = float(string_element)
        result_list.append(element)

    return result_list

def extract_integer(lista):
    """
    extragem partea intreaga a unui numar de tip float
    :param lista:
    :return: partea intreaga a fiecarui numar din lista
    """
    result_list = []

    for element in lista:
        result_list.append(int(str(element).split('.')[0]))

    return result_list

def test_extract_integer():
    assert extract_integer([1.2, 2.3, -4.5]) == [1, 2, -4]
    assert extract_integer([1.5, 3.01]) == [1, 3]

def numbers_in_ab(lista, a, b):
    """
    verificam daca elementele listei se afla in intervalul (a,b) si in caz afirmativ le adaugam la o noua lista
    :param lista:
    :param a: capatul de jos al intervalului
    :param b: capatul de sus al intervalului
    :return:
    """
    result_list = []

    for element in lista:
        if element > a and element < b:
            result_list.append(element)

    return result_list

def test_numbers_in_ab():
       assert numbers_in_ab([1.2, 5.3, 6.9, 8.1], 2, 6) == [5.3]

def fractionar_divide_by_integer(lista):
    """
    verificam daca numerele au partea fractionara divizibila cu cea intreaga si in caz afirmativ le adaugam la o noua lista
    :param lista:
    :return:
    """
    result_list = []

    for element in lista:
        integer = int(str(element).split('.')[0])
        fractionar = int(str(element).split('.')[1])
        if fractionar % integer == 0:
            result_list.append(element)

    return result_list

def float_to_string(lista):
    """
    transformam numerele din float in string inlocuind fiecare cifra cu pronuntia sa
    :param lista:
    :return:
    """
    result_list = ''

    for element in lista:
        elem = str(element)
        string_elem = ''
        for index in range(0, len(elem)):
            if elem[index] == '0':
                string_elem + 'zero'
            elif elem[index] == '1':
                string_elem + 'unu'
            elif elem[index] == '2':
                string_elem + 'doi'
            elif elem[index] == '3':
                string_elem + 'trei'
            elif elem[index] == '4':
                string_elem + 'patru'
            elif elem[index] == '5':
                string_elem + 'cinci'
            elif elem[index] == '6':
                string_elem + 'sase'
            elif elem[index] == '7':
                string_elem + 'sapte'
            elif elem[index] == '8':
                string_elem + 'opt'
            elif elem[index] == '9':
                string_elem + 'noua'
            elif elem[index] == '.':
                string_elem + 'virgula'

        result_list + string_elem

    return result_list

def main():
    stop = False
    lista = []
    while not stop:
        print("""
            1 -> Citire lista 
            2 -> Afișarea părții întregi a tuturor numerelor din listă.
            3 -> Să se afișeze toate numerele care aparțin unui interval deschis citit de la tastatură.
            4 -> Afișarea tuturor numerelor a căror parte întreagă este divizor al părții fracționare
            5 -> Afișarea listei obținute din lista inițială în care numerele sunt înlocuite cu un string format din cuvinte care le descriu caracter cu caracter.
            x -> Iesire
         """)
        command = input("Alege comanda: ")
        if command == 'x':
            stop = True
        elif command == '1':
            lista = citire_lista()
        elif command == '2':
            print(extract_integer(lista))
            test_extract_integer()
        elif command == '3':
            a = float(input('Dati capatul de jos: '))
            b = float(input('Dati capatul de sus: '))
            print(numbers_in_ab(lista, a, b))
            test_numbers_in_ab()
        elif command == '4':
            print(fractionar_divide_by_integer(lista))

        elif command == '5':
            print(float_to_string(lista))


main()
