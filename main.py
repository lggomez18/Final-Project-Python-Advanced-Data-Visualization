import csv
import matplotlib.pyplot as plt

filename = 'data.csv'


population_per_continent = {}

#Extract data by creating a reader. Using DictReader creates a reader with headers. 
with open (filename, 'r') as csvfile:
  reader = csv.DictReader(csvfile)
  for line in reader:
    #Create variables for each header instead of printing each line. 
    continent = line['continent']
    year = line['year']
    population = line['population']

    #create if/in statement to create the dictionary called population_per_continent. The formula basically says: "If Africa is not in the list add it."
    if continent not in population_per_continent:
      population_per_continent[continent] = {'population':[], 'year':[]}

    #Use .append to add data to each continent
    population_per_continent[continent]['population'].append(population)
    population_per_continent[continent]['year'].append(year)

print(population_per_continent)


plt.plot([2000, 2005, 2010, 2015, 2020],[100,200, 300, 400, 500], label = "Europe", marker = "o")

plt.title("Internet Users per Continent")
plt.xlabel("Year")
plt.ylabel("Internet Users")
plt.legend()

plt.grid(True)


plt.tight_layout()
plt.savefig('Internetperpop.png')
#plt.show()
