import csv
import matplotlib.pyplot as plt

def generate_population_dictionary_from_csv(filename):
  """
  Generate population dictionary from csv data

  Return dictionary following this structure
  {
    "Africa":{population:[100, 200, 300], years:[1990, 2000, 2010]},
    "Asia":{population:[100, 200, 300], years:[1990, 2000, 2010]}
  }
  """
  population_per_continent = {}
  
  
 #Extract data by creating a reader. Using DictReader creates a reader with headers. 
  with open (filename, 'r') as csvfile:
   reader = csv.DictReader(csvfile)
   for line in reader:
     #Create variables for each header instead of printing each line. 
     continent = line['continent']
     year = int(line['year'])
     population = int(line['population'])

     #create if/in statement to create the dictionary called population_per_continent. The formula basically says: "If Africa is not in the list add it."
     if continent not in population_per_continent:
       population_per_continent[continent] = {'population':[], 'year':[]}

     #Use .append to add data to each continent
     population_per_continent[continent]['population'].append(population)
     population_per_continent[continent]['year'].append(year)



  return population_per_continent


def plots_population_from_dictionary(population_dictionary):
  """
  Generate the population plots from a dictionary
  One plot per continent 
  Level AA colors for accessibility compliance
  Improved scaling for better readability 
  """
  index = 0

  #Testing colors using WebAIM. Level AA. 
  colors = {
   "Africa": "#0072B2",
   "Europe": "#E69F00",
   "Asia": "#009E73",
   "North America": "#000000",
   "South America": "#CC79A7",
   "World": "#7E5207"
   }

  for continent in population_per_continent:
    year = population_per_continent[continent]['year']
    population = population_per_continent[continent]['population']



    plt.plot(
      year, 
      population, 
      label = continent,  
      color= colors[continent], 
      alpha = 0.8,
      markersize=6,
      marker = "o"
    )

  index += 1


  plt.title("Internet Users per Continent", fontsize = 14)
  plt.xlabel("Year", fontsize = 12)
  plt.ylabel("Internet Users (in Billion)", fontsize = 12)
  plt.legend(ncol=2, title="Continent")
  plt.grid(color='#B0B0B0', linewidth=1)



 

filename = 'data.csv'


#Display internet population in a plot
population_per_continent= generate_population_dictionary_from_csv(filename)
plots_population_from_dictionary(population_per_continent)



plt.tight_layout()
plt.savefig('Internetperpop.png')
#plt.show()

