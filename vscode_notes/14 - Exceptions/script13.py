# jezeli damy normalny cyfrą to zwróci ją jako float, jeżeli damy pusty string "" to bedzie 0, a jezeli uzupelniony to zwróci None
def cell_value(string):
    try:
        return float(string)
    except ValueError:
        if string == "":
            return 0
        else:
            return None
print(cell_value(""))