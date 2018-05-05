import math
def main():
    global p, q
    p = int(input('p = '))
    q = int(input('q = '))
    return p,q

def discriminant(b, c, a = 1):
    d = b**2 - 4*a*c
    return d

def large_root (p, q):
    d = discriminant(p, q)
    if d > 0:
        x = (-p + (math.sqrt(d)))/2
        return 'large is', x
    if d == 0:
        x = (-q/2)
        return 'large is', x

def small_root(p, q):
    d = discriminant(p,q)
    if d > 0:
        x = (-p - (math.sqrt(d)))/2
        return 'small is', x
    if d == 0:
        x = (-q/2)
        return 'small is', x

main()
print(large_root(p,q))
print(small_root(p,q))
print('discriminant is ',discriminant(p,q))
