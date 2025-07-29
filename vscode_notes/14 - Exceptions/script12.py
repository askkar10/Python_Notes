# tak mozemy skopiowac
# with open('empty.txt') as infile, open('other.txt','w') as outfile:
#   data = infile.read()
#   outfile.write(data)

# lub

with (
    open('moby_dick.txt','r',encoding='utf-8') as infile,
    open('moby_dick_copy.txt','w',encoding='utf-8') as outfile
):
  data = infile.read()
  outfile.write(data)
  print("Plik został skopiowany!!!")