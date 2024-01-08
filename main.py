import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class GDPAnalysis:
    def __init__(self):
        self.data = pd.read_csv('gdp_csv.csv')
        
    def getGrowthPerYear(self, country: str, year: int):
        get_country = self.data[self.data['Country Name'] == country]
        gdp_1 = get_country[get_country['Year'] == year - 1]
        gdp_2 = get_country[get_country['Year'] == year]
        growth_rate = round((gdp_2['Value'].values[0] / gdp_1['Value'].values[0]) - 1, 3)

        return f'{growth_rate * 10}%'
    
    
    def getGrowthPerDecade(self, country: str, decade: int):
        get_country = self.data[self.data['Country Name'] == country]
        decade1 = get_country[get_country['Year'] == decade]
        if decade == 2010:
            decade2 = get_country[get_country['Year'] == decade + 5]
        else:
            decade2 = get_country[get_country['Year'] == decade + 9]
        growth_rate = round((decade2['Value'].values[0] / decade1['Value'].values[0]) - 1, 2)
        
        return f'{growth_rate * 10}%'
    
    
    def GeneratePieChart(self, year: int, country: str):
        country = self.data[self.data['Country Name'] == country]
        world = self.data[self.data['Country Name'] == 'World']
        
        labels = f'{country[country['Year'] == year]['Country Name'].values[0]}', f'{world[world['Year'] == year]['Country Name'].values[0]}'
        sizes = [country[country['Year'] == year]['Value'].values[0], world[world['Year'] == year]['Value'].values[0]]
        explode = (0.1, 0)

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', explode=explode, shadow={'ox': -0.04, 'edgecolor': 'none', 'shade': 0.9},
               pctdistance=1.25, labeldistance=.6)
        
        ax.legend(title='GDP comparison')
        ax.set_title(f"{country[country['Year'] == year]['Country Name'].values[0]}'s GDP compared to the world's GDP")
        
        plt.show()
        
    
    def GenerateStreamGraph(self):
        europe = self.data[self.data['Country Code'] == 'EMU']
        north = self.data[self.data['Country Code'] == 'NAC']
        latin = self.data[self.data['Country Code'] == 'LCN']
        middle_east = self.data[self.data['Country Code'] == 'MEA']
        africa = self.data[self.data['Country Code'] == 'SSF']
        east_asia = self.data[self.data['Country Code'] == 'EAS']
        
        year = [1970, 1980, 1990, 2000, 2010]
        gdp_per_area = {
            'Europe': [europe[europe['Year'] == 1970]['Value'].values[0], europe[europe['Year'] == 1980]['Value'].values[0], 
                       europe[europe['Year'] == 1990]['Value'].values[0], europe[europe['Year'] == 2000]['Value'].values[0],
                       europe[europe['Year'] == 2010]['Value'].values[0]],
            'North America' : [north[north['Year'] == 1970]['Value'].values[0], north[north['Year'] == 1980]['Value'].values[0],
                               north[north['Year'] == 1990]['Value'].values[0], north[north['Year'] == 2000]['Value'].values[0],
                               north[north['Year'] == 2010]['Value'].values[0]],
            'Latin America': [latin[latin['Year'] == 1970]['Value'].values[0], latin[latin['Year'] == 1980]['Value'].values[0],
                              latin[latin['Year'] == 1990]['Value'].values[0], latin[latin['Year'] == 2000]['Value'].values[0],
                              latin[latin['Year'] == 2010]['Value'].values[0]],
            'Middle East and North Africa': [middle_east[middle_east['Year'] == 1970]['Value'].values[0], middle_east[middle_east['Year'] == 1980]['Value'].values[0],
                                             middle_east[middle_east['Year'] == 1990]['Value'].values[0], middle_east[middle_east['Year'] == 2000]['Value'].values[0],
                                             middle_east[middle_east['Year'] == 2010]['Value'].values[0]],
            'Sub-Saharan Africa': [africa[africa['Year'] == 1970]['Value'].values[0], africa[africa['Year'] == 1980]['Value'].values[0], 
                                   africa[africa['Year'] == 1990]['Value'].values[0], africa[africa['Year'] == 2000]['Value'].values[0],
                                   africa[africa['Year'] == 2010]['Value'].values[0]],
            'East Asia and Oceania': [east_asia[east_asia['Year'] == 1970]['Value'].values[0], east_asia[east_asia['Year'] == 1980]['Value'].values[0],
                                      east_asia[east_asia['Year'] == 1990]['Value'].values[0], east_asia[east_asia['Year'] == 2000]['Value'].values[0],
                                      east_asia[east_asia['Year'] == 2010]['Value'].values[0]],
        }
        
        fig, ax = plt.subplots()
        ax.stackplot(year, gdp_per_area.values(),
                    labels=gdp_per_area.keys(), alpha=0.8)
        ax.legend(loc='upper left', reverse=True)
        ax.set_title("Continent's GDP")
        ax.set_xlabel('Year')
        ax.set_ylabel('GDP (in trillions)')

        plt.show()
        
        
    def __repr__(self):
        return self.data.to_string()


def main():
    gdp_analysis = GDPAnalysis()
    country = str(input('Which country would like to see the GDP analysis? ')).capitalize()
    ask = str(input('Would you like to see the yearly analysis or the decade analysis, or maybe both? ')).lower()
    
    if ask in ['yearly']:
        year = int(input('From which year? '))
        print(gdp_analysis.getGrowthPerYear(country, year))
        val = str(input("Would you like to see a graph representing the country's gdp compared to the world? "))
        if val in ['yes']:
            print(gdp_analysis.GeneratePieChart(year, country))
            print(gdp_analysis.GenerateStreamGraph())
        else:
            return
        
    if ask in ['decade']:
        decade = int(input('From which decade? '))
        print(gdp_analysis.getGrowthPerDecade(country, decade))
        
    elif ask in ['both']:
        year = int(input('From which year? '))
        decade = int(input('From which decade? '))
        print(gdp_analysis.getGrowthPerYear(country, year))
        print(gdp_analysis.getGrowthPerDecade(country, decade))
    
    else:
        print(gdp_analysis)

if __name__ == '__main__':
     main()