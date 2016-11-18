import csv

tt = 1
filenew = 'csvone.csv'
filename = 'movievalue.csv'
with open(filename, newline='' , encoding='ascii', errors='surrogateescape') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
    	print(row)
    	with open(filenew, 'a', encoding="ascii", errors="surrogateescape") as w:
    		writer = csv.writer(w, delimiter=',', dialect='excel')
    		writer.writerow(row)
w.close()
f.close()
