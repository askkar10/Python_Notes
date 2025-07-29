import os 
print(os.path.exists('/content/sample_data')) # sprawdza czy dany path istnieje
print(os.path.exists('/content/sample_data/README.md')) # sprawdza czy dany plik istnieje (2 funkcje)
print(os.path.exists('/content/sample_data/slasdlgdas')) # jeżeli to nie istnieje to zwraca false
print(os.path.isdir('/content/sample_data/README.md')) # sprawdza czy jest to path
print(os.path.isdir('/content/sample_data')) # jezeli to path to zwroci true
print(os.path.isfile('/content/sample_data/README.md')) # sprawdza czy dany path to plik