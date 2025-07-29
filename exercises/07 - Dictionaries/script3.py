string = 'to be or not to be'
occurencies = {}
for word in string.split():
    occurencies[word] = occurencies.get(word,0) + 1

print(occurencies)