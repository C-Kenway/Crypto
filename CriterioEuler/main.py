#Residuo Cuadratico para un modulo p
def residQuad(p):
        residuos = []
        expo=(p-1)/2
        i=0
        # Evalua el valor x en cada parte del modulo que solicita e imprime el QR donde se cumpla la condicion
        for i in range (p):
                modEuler = pow(i,expo) % p
                if modEuler == 1:
                        residuos.append(i)
        return residuos

def RaicesQuad(n, p):
    """Encuentra una raíz cuadrada de n módulo p"""
    if pow(n, (p-1)//2, p) != 1:
        return None
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p+1)//4, p)
    for z in range(2, p):
        if pow(z, (p-1)//2, p) == p-1:
            break
    c = pow(z, q, p)
    r = pow(n, (q+1)//2, p)
    t = pow(n, q, p)
    m = s
    while True:
        if t == 1:
            return r
        i = 0
        for i in range(m):
            if pow(t, 2**i, p) == 1:
                break
        b = pow(c, 2**(m-i-1), p)
        r = (r * b) % p
        t = (t * b * b) % p
        c = (b * b) % p
        m = i

#Paramteros de curva eliptica dada una funcion y^2 = x^3 + ax + b (mod p)
def ParametrCurvElipt(a,b,NumeroP):
        ValCurva = []
        t = 0
        for t in range(0, NumeroP):
                #Lo que en teoria se resolvio al hacerce funcion e ingresar a y b como valores en general
                val = (pow(t, 3) + a * t + b) % NumeroP
                ValCurva.append(val)
        return ValCurva

def PuntosCurvaElip(a, b, p):
    """Encuentra los puntos en la curva elíptica y^2 = x^3 + ax + b (mod p)"""
    ValCurv = ParametrCurvElipt(a, b, p)
    x_vals = []
    y_vals = []
    for x in range(p):
        y_cuad = ValCurv[x]
        y = RaicesQuad(y_cuad,p)
        if y is not None:
            x_vals.append(x)
            y_vals.append(y)
    points = []
    for i in range(len(x_vals)):
        points.append((x_vals[i], y_vals[i]))
        if y_vals[i] != 0:
            points.append((x_vals[i], p-y_vals[i]))
    points.append("(infinito)")
    return points


#Aqui comineza el programa
print("------------------------------------")
print("Notacion: y^2 = x^3 + ax + b (mod p)  ")
print("------------------------------------")
#Ingresa el valor para "a" en la expresion de la formula
a=int(input("Ingrese l valor de a: \n"))
#Ingresa el valor para "b" en la expresion de la formula
b=int(input("Ingrese l valor de b: \n"))
#Ingresa valor de Modulo
p=int(input("Ingrese l valor de p: \n"))

"""Validacion de 4a^3 + 27b^2 mod p !=0"""
#valid = (((4*a)^3 + (27*b)^2) % p)
valid = (4*pow(a,3)+27*pow(b,2))
if valid != 0 :
    # Imprime los valores de residuo Cuadratico
    print("\n Residuo Cuadratico QR: ")
    print(residQuad(p))

    # Imprime los parametros para la curva eliptica en funcion de
    # y^2 = x^3 + ax + b (mod p) todavia no imprime puntos, ni las raices cuadraticas.
    print(f"\n Parametros de la curva evaluados en los a: {a} y b: {b} ")
    ValCurv = []
    ValCurv=ParametrCurvElipt(a, b, p)
    print(ValCurv)

    # Para encontrar los puntos
    print("\n Puntos de la curva: ")
    print(PuntosCurvaElip(a, b, p))
else:
    print("Valores invalidos para a,b y p")





