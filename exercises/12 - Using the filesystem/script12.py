import os
katalog_startowy = ""
for root,dir,files in os.walk(r"C:\Users\askka\Desktop\python_programs"):
    print(root)
    print(dir)
    print(files)