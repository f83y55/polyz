import random

def retrouve(x:int, ev:int) -> list :
    """retrouve un polynôme a coefficents entiers qui vaut ev en x"""
    if x == 0 :
        return [ev]
    poly, y, k = [], abs(ev), abs(x//2)
    sy = ev<0
    while y :
        poly.append(y % x)
        y //= x
    for i in range(len(poly)) :
        if poly[i] > k :
            poly[i] -= x
            if i < len(poly)-1 :
                poly[i+1] += 1
            else :
                poly.append(1)
    if sy : 
        for i in range(len(poly)) :
            poly[i] *= -1
    return poly


def poly_hasard(d:int, k:int, neg=True) -> list :
    """renvoie une liste [a_0, ..., a_d] modélisant un polynôme de degré d : a_d x^d + ... + a_0 avec -k <= a_i <= k (neg True) ou bien avec 0 <= a_i <= k (neg False)""" 
    ls = []
    for _ in range(d) :
        ls.append( random.randint(-k, k) if  neg else random.randint(0, k))
    # terme de degré max non nul :
    ls.append((random.choice([-1, 1]) if neg else 1) * random.randint(1, k))
    return ls  


def affiche(poly:list):
    """affiche le polynôme sous forme développée avec indéterminée X"""
    return "".join(reversed([
    f"{' -' if poly[i]<0 else ''}{' +' if poly[i]>0 and i<len(poly)-1 else ''}{abs(poly[i]) if (i>0 and not(poly[i] in (-1, 0, 1))) or (i==0 and poly[i]!=0) else ''}{'X^'+str(i) if i>1 and not(poly[i]==0) else ''}{'X' if i==1 and not(poly[i]==0) else ''}" for i in range(len(poly))]))


def horner(poly:list, n:int) -> int:
    """évalue le polynome poly en n"""
    ev = poly[-1]
    for a in poly[::-1][1::] :
        ev = ev * n + a 
    return ev


def tester(ntest:int=5, dmax:int=20, kmax:int=100) :
    for test in range(ntest) :
        print(f"\nTEST {test} :")
        d = random.randint(0, dmax)
        k = random.randint(1, kmax)
        p = poly_hasard(d, k)
        x = random.randint(2*k+1, 2*kmax+1)
        ev = horner(p, x)
        print(f"{affiche(p)}\nen X={x} vaut {ev}")
        q = retrouve(x, ev)
        res = p==q
        print(f"Polynôme retrouvé :\n{affiche(q)}\nTest : {res}")


def jouer(kmin:int=10, kmax:int=100) :
    continuer = True
    while continuer :
        k = random.randint(kmin, kmax)
        print(f"Choisir un polynôme P à coefficients ENTIERS compris entre {-k} et {k} (inclus)")
        x = random.randint(k+1, kmax+1)
        ev = int(input(f"Entrer la valeur de P({x}) ici : "))
        p = affiche(retrouve(x, ev))
        print(f"Vous aviez choisi le polynôme :\n{p}")
        comtinuer = input("Continuer (n: non) ? : ") == 'n'


if __name__ == "__main__":
    jouer()
