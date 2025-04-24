pi = 3.14159
a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
#a) a área do triângulo retângulo que tem A por base e C por altura.
triangulo = (a*c)/2
print(f'TRIANGULO: {triangulo:.3f}')
#b) a área do círculo de raio C. (pi = 3.14159)
circulo = pi*c**2
print(f'CIRCULO: {circulo:.3f}')
#c) a área do trapézio que tem A e B por bases e C por altura.
trapezio = ((a+b)*c)/2
print(f'TRAPEZIO: {trapezio:.3f}')
#d) a área do quadrado que tem lado B.
quadrado = b**2
print(f'QUADRADO: {quadrado:.3f}')
#e) a área do retângulo que tem lados A e B.
retangulo = a*b
print(f'RETANGULO: {retangulo:.3f}')