def c_to_kelvin(deg_c):
    return deg_c + 273.15
def k_to_celsjusz(deg_k):
    return deg_k - 273.15

ctok = c_to_kelvin
print(ctok(31))
ktoc = k_to_celsjusz
print(ktoc(290))