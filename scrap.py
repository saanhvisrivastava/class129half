import csv
data=[]
with open('129data.csv','r') as f:
    csv_reader=csv.reader(f)

    for row in csv_reader:
        data.append(row)
    
headers=data[0]
planet_data=data[1:]

for datapoint in planet_data:
    datapoint[0]=datapoint[0].lower()

planet_data.sort(key=lambda planet_data:planet_data[0])

with open('sorted.csv','a+') as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)


