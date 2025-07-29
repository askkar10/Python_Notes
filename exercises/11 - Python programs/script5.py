import fileinput
def main():
    for line in fileinput.input(files=('script3_tekst.txt','script3_tekst_zamiana.txt','script3_tekst_nadpisanie.txt')):
        print(line)
main()