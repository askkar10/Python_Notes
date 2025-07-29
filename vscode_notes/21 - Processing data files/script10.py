# przed sortowanie zamiana na male litery

lines = open('datafile').readlines()
lines.sort(key=str.lower)
print(lines)

# przed sortowaniem ignoruje 5 znaków

lines.sort(key=lambda x: x[5:])
print(lines)