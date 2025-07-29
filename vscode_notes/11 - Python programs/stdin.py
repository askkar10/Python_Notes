import sys
def main():
    content = sys.stdin.read()
    sys.stdout.write(content.replace("This","That"))
main()