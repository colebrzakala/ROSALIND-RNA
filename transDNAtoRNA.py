def DNAtoRNA(fname):
    file = open(fname, 'r')
    sequence = file.read()
    file.close()
    final = ""
    for elem in sequence:
        if elem == "T":
            final += "U"
        else:
            final += elem
    print(final)
