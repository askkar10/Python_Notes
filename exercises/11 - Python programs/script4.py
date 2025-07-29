import argparse
parser = argparse.ArgumentParser()
parser.add_argument('number1',help='number1',type=int)
parser.add_argument('number2',help='numbe2',type=int)
parser.add_argument('-e','--explanation',action='store_true',help='multiply two numbers')
args = parser.parse_args()
answer = args.number1 * args.number2
if args.explanation:
    print(f"number1: {args.number1} number2: {args.number2} answer: {answer}")
else:
    print(answer)