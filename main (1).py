import csv
import matplotlib.pyplot as plt

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

plt.plot([2000, 2005, 2010, 2015, 2020],[100,200, 300, 400, 500], label = "Europe", marker = "o")

plt.title("Internet Users per Continent")
plt.xlabel("Year")
plt.ylabel("Internet Users")
plt.legend()

plt.grid(True)


plt.tight_layout()
plt.savefig('Internetperpop.png')
plt.show()