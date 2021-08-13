import csv
import re
import os,psutil
import time
end = time.time()
f = open('french_dictionary.csv','r')
reader=csv.reader(f)
people = []
for row in reader:
    people.append(row)

#Replacing English word by french word and updating in csv
data = ['English word', 'French word', 'frequency']
f1=open('frequency.csv', 'w+', newline='')
write=csv.writer(f1) 
write.writerow(data)
filename = 't8.shakespeare.txt'
file = open(filename, 'r')
filedata = file.read()
for i in range (0, 1000):
  count1 = filedata.count(people[i][0])
  count2 = filedata.count(people[i][0].upper())
  count3 = filedata.count(people[i][0].capitalize())
  count = count1 + count2 + count3
  filedata = filedata.replace(people[i][0], people[i][1])   
  filedata = filedata.replace(people[i][0].upper(), people[i][1].upper())
  filedata = filedata.replace(people[i][0].capitalize(), people[i][1].capitalize())             
  row1 = [[people[i][0], people[i][1], count]]
  write.writerows(row1)
with open('t8.shakespeare.translated.txt', 'w') as file:
   file.write(filedata) 

#TO print memory usage
pid = os.getpid()
ps = psutil.Process(pid)
memoryUse=ps.memory_info().rss
memoryUse=str(ps.memory_info().rss/ 1024 ** 2)

#To print execution time
temp = str(time.time()-end)

#writing execution time and memory usage in performance.txt file
with open('performance.txt', 'w') as file:
   file.write('Time to process:' + " " + temp + " " + 'seconds')
   file.write("\n" + 'Memory used:' + " " + memoryUse + " " 'MB') 






   
       
       





















