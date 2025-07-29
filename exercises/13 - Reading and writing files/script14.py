with (
    open('ilosc_linii.txt') as infile,
    open('ilosc_linii_copy2.txt','w') as outfile
):
    d = infile.readlines()
    outfile.writelines(d)