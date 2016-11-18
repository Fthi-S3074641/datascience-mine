import csv
# import pygal
import json
# from bson import json_util
import codecs
import datetime
# from urllib2 import urlopen  # python 2 syntax
from urllib.request import urlopen, HTTPError, URLError # python 3 syntax

filenew = 'csvone.csv'
filename = 'movievalue.csv'
storage = ['ttimdb']
i =0
with open(filename, newline='' , encoding='ascii', errors='surrogateescape') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
    	if (datetime.datetime.strptime(row[1], "%m/%d/%Y")):
    		datay = datetime.datetime.strptime(row[1], "%m/%d/%Y").year
    		lengh = len(row)
    		lengh = lengh - 1
    		title = row[2]
    		url = 'http://www.omdbapi.com/?t={title}&y={datay}&plot=short&r=json'
    		url = url.format(datay=datay,
    		    			title = title)
    		try:
    			result = urlopen(url).read().decode('utf-8')
    		except HTTPError as e:
    			content = e.read()
    		except URLError as e:
    			content = e.read()
    		parsed = json.loads(result)
    		if (parsed['Response'] == 'True'):
    			lsright = [parsed['imdbID'], parsed['Title'], parsed['Year'], row[lengh]]
    			if (parsed['imdbID'] in storage):
    				continue
    			else:
    				storage.append(parsed['imdbID'])
    		else:
    			print('nothing')
    			continue
    		with open(filenew, 'a', encoding="utf_8", errors="surrogateescape") as w:
    			writer = csv.writer(w, delimiter=',', dialect='excel')
    			writer.writerow(lsright)
    			i = i +1
    			print(i)
    	else:
    		continue
w.close()
f.close()
url = 'http://www.omdbapi.com/?t=avatar&y=2009&plot=short&r=json'
result = urlopen(url).read().decode('utf-8')
parsed = json.loads(result)
if (parsed['Response'] == 'True'):
	print(parsed['Year'] + parsed['imdbID'])
else:
	print('nothing')