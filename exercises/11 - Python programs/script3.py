import sys
def main():
    data = sys.stdin.read()
    sys.stdout.write(data.replace(sys.argv[1],sys.argv[2]))
main()

# python script3.py Michał Dawid < script3_tekts.txt > Script3_tekst_zamiana.txt