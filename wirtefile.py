def writefiles(filename,reptext):
    f = open(filename,"a+",encoding="utf-8")
    f.write(reptext)
    f.write("\n")
    f.close()