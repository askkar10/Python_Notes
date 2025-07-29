def c_to_kelvin(deg_c):
    return deg_c + 273.15
def k_to_celsjusz(deg_k):
    return deg_k - 273.15

dic = {'ctok':c_to_kelvin,'ktoc':k_to_celsjusz}
print(dic['ctok'](27))
print(dic['ktoc'](300.15))