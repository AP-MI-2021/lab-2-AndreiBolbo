def is_prime(n):
    '''
    determina daca numarul dat este prim
    Input:
    -n:int
    Output:
    True/False
    '''
    if n < 2:
        return False
    for i in range(2,n//2+1):
        if n % i == 0:
            return False
    return True

def get_goldbach(n):
    '''
    determina numerele prime p1,p2 pentru care n=p1+p2 iar altfel valoarea lui p1 respectiv p2 este 0
    in cazul in care nu se poate obtine relatia n=p1+p2(in cazul in care nu se verifica conjectura lui Goldbach)
    Input:
    -n:int
    output:
    p1,p2
    Exista  solutie pentru orice numar intreg par mai mare decat sau egal cu 4
    '''
    for i in range(2,n):
        p1=i
        p2=n-i
        if is_prime(p1) & is_prime(p2):
            return p1,p2
    return 0,0
def main():
    nr=int(input('Pentru a avea solutie 100% dati un numar par >=4 . Dati un numar: '))
    g,d=get_goldbach(nr)
    if g==0 &d==0:
        print(f'Nu exista perechile p1,p2 prime pentru care {nr}=p1+p2')
    else:
        print(g,d)
main()