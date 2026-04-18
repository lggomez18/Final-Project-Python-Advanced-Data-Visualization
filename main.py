import csv

filename = 'data.csv'

#Extract data by creating a reader. Using DictReader creates a reader with headers. 
with open (filename, 'r') as csvfile:
  reader = csv.DictReader(csvfile)
  for line in reader:
    #Create variables for each header instead of printing each line. 
    continent = line['continent']
    year = line['year']
    population = line['population']
    
    #print(line['continent'])
    print(continent)
    #print(line['year'])
    print(year)
    #print(line['population'])
    print(population)