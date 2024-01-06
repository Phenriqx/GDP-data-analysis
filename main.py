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
    
    
    def GeneratePieChart(self, year: int):
        val = self.data[self.data['Year'] == year]
        
        
    def __repr__(self):
        return self.data.to_string()


def main():
    gdp_analysis = GDPAnalysis()
    country = str(input('Which country would like to see the GDP analysis? '))
    ask = str(input('Would you like to see the yearly analysis or the decade analysis, or maybe both? ')).lower()
    
    if ask in ['yearly']:
        year = int(input('From which year? '))
        print(gdp_analysis.getGrowthPerYear(country, year))
        val = str(input("Would you like to see a graph representing the country's gdp compared to the world?"))
        if val in ['yes']:
            return gdp_analysis.GeneratePieChart()
        
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