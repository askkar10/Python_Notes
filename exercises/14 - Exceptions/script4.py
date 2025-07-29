def example(string):
    try:
        return float(string)
    except ValueError:
        if string == '':
            return 0
        else:
            return None
    
print(example(10))
print(example(""))
print(example('siema'))