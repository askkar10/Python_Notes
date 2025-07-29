import argparse
parser = argparse.ArgumentParser()
parser.add_argument('number1',help='display square of numbers',type=int)
parser.add_argument('number2',help='display square of numbers',type=int)
parser.add_argument('-e','--explanation',action='store_true',help='explain how this work')
args = parser.parse_args()
answer = args.number1 ** args.number2
if args.explanation:
    print('number1: {0}, number2:{1}, answer: {2}'.format(args.number1,args.number2,answer))
else:
    print(args.number1**args.number2)