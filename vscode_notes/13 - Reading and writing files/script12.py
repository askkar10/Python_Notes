# pickle -> pozwala na przekształcenie struktury obiektu Pythona (listy itp.) w strumień bajtów, który mozna 
# następnie zapisać do pliku, przesłać przez sieć do bazy danych itp.

# unpicling to operacja odwrotna

# saving data pickle.dump zapisuje wszystko 

import pickle 
a = 42
b = 3.14
c = 'test'
file = open('state','wb')
pickle.dump(a,file)
pickle.dump(b,file)
pickle.dump(c,file)
file.close()