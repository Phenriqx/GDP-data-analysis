import pandas as pd

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
        pass
        
    def __repr__(self):
        return self.data.to_string()

def main():
    gdp_analysis = GDPAnalysis()
    country = str(input('Which country would like to see the GDP analysis? '))
    ask = str(input('Would you like to see the yearly analysis or the decade analysis, or maybe both? ')).lower()
    if ask in ['yearly']:
        year = int(input('From which year? '))
        print(gdp_analysis.getGrowthPerYear(country, year))
    if ask in ['decade']:
        print('not implemented yet')
    elif ask in ['both']:
        print('not implemented yet')
    
    print(gdp_analysis)

if __name__ == '__main__':
     main()