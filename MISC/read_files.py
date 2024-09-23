inputfile = open('inputFile.txt', 'r')
passfile = open('passFile.txt', 'w')
failfile = open('failFile.txt', 'w')

for line in inputfile:
    line_split = line.split()
    if line_split[2] == 'P':
        passfile.write(line)
    else:
        failfile.write(line)
        # print(line)
    
inputfile.close()
passfile.close()
failfile.close()
