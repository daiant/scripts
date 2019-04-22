import csv, os

def getDirectories():
    with open('data.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        dir = []
        for row in csv_reader:
            dir += {row[0]}
        return dir

def stringDirectories():
    aux = getDirectories()
    for dir in aux:
        print(dir)

def deleteDirectory(dir):
    aux = getDirectories()
    d = os.path.abspath(dir)
    i = 0
    for aux_dir in aux:
        if aux_dir == d:
            del aux[i]
            updateList(aux)
            exit()
        i+=1
    print(d + " doesn't exist in directory list!")

def updateList(dirs):
    with open('data.txt', 'w') as f:
        writer = csv.writer(f)
        for dir in dirs:
            aux = [dir]
            writer.writerow(aux)

def setDirectory(dir):
    field = [os.path.abspath(dir)]
    with open('data.txt', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(field)
