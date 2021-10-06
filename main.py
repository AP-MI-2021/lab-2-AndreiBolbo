def is_prime(n):
    """
    determina daca numarul dat este prim
    Input:
    -n:int
    Output:
    True/False
    """
    if n < 2:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    return True


def get_goldbach(n):
    """
    determina numerele prime p1,p2 pentru care n=p1+p2 iar altfel valoarea lui p1 respectiv p2 este 0
    in cazul in care nu se poate obtine relatia n=p1+p2(in cazul in care nu se verifica conjectura lui Goldbach)
    Input:
    -n:int
    output:
    p1,p2
    Exista  solutie pentru orice numar intreg par mai mare decat sau egal cu 4
    """
    for i in range(2, n):
        p1 = i
        p2 = n-i
        if is_prime(p1) & is_prime(p2):
            return p1, p2
    return 0, 0


def is_palindrome(n):
    """
    determina oglinditul numarului n adica
    pune cifrele numarului n in ordine inversa(de la stanga la dreapta)
    input:
    -n:int
    output:
    True(daca numarul este palindrom )
    False(daca nu este)
    """
    x = n
    p = 0
    while x:
        p = p*10 + x % 10
        x = x//10
    if p == n:
        return True
    return False


def test_goldbach():
    assert get_goldbach(4) != 0, 0
    assert get_goldbach(12) != 0, 0
    assert get_goldbach(10) != 0, 0
    assert get_goldbach(8) != 0, 0
    assert get_goldbach(6) != 0, 0


def get_newton_sqrt(n, steps):
    """"
    Determina radicalul folosind algoritmul lui Newton cu un anumit numar de pasi
    acesta pleaca de la functia f(x)=x^2-a cu f'(x)=2x
    urmand sa folosim formula x1=x0-f(x0)/f'(x0)
    unde  se specifica ca x0=2 initial.
    input:
    -n ,steps:int
    output:
    -x1:float

    """
    i = 1
    x0 = 2
    x1 = n
    while i <= steps:
        x1 = x0-(pow(x0, 2)-n)/(2*x0)
        x0 = x1
        i += 1
    return x1


def test_get_newton_sqrt():
    assert get_newton_sqrt(16, 2) == 4.1
    assert get_newton_sqrt(18, 2) == 4.386363636363637
    assert get_newton_sqrt(36, 1) == 10.0
    assert get_newton_sqrt(49, 2) == 8.474056603773585


def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(151) == True
    assert is_palindrome(11) == True
    assert is_palindrome(6) == True
    assert is_palindrome(123) == False


def main():
    while True:
        print('1. Pentru a determina numerele prime p1,p2 pentru care n=p1+p2(conjectura lui Goldbach)')
        print('2. Calculul radicalului cu metoda lui Newton')
        print('3. Verifica daca numarul dat este palindrom ')
        print('x. Pentru a iesi din program')
        optiune = (input('Alegeti optiunea dorita :'))
        if optiune == '1':
            nr = int(input('Pentru a avea solutie 100% dati un numar par >=4 . Dati un numar: '))
            g, d = get_goldbach(nr)
            if g == 0 & d == 0:
                print(f'Nu exista perechile p1,p2 prime pentru care {nr}=p1+p2')
            else:
                print(f'{nr}={g}+{d}')
        elif optiune == '2':
            nr1=int(input('Dati un numar: '))
            steps=int(input('Dati numarul de pasi: '))
            print(get_newton_sqrt(nr1, steps))
        elif optiune == '3':
            nr2=int(input('Dati un numar: '))
            if is_palindrome(nr2):
                print('Numarul dat este palindrom')
            else:
                print('Numarul nu e palindrom')
        elif optiune == 'x':
            break
        else:
            print('Optiune incorecta! ')


test_is_palindrome()
test_get_newton_sqrt()
test_goldbach()
main()