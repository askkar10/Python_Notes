z = 4 + 5j
print(z.imag,z.real)

def fun(x: complex,y: complex) -> complex:
    a = x.imag + y.imag
    b = x.real + y.real
    print(f"Suma części rzeczywistej: {b}")
    print(F"Suma część urojonej: {a}")

fun(4j,3j)
fun(-3j,9j)