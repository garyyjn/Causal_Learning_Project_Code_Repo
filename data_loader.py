import pandas as pd


def general_loader():

    happiness = pd.read_csv('Data/Happiness Index/2019.csv',dtype=str)
    education_expenditure = pd.read_csv('Data/EducationalSpenditure.csv',dtype=str)
    country_data = pd.read_csv('Data/countries of the world.csv',dtype=str)
    #print(happiness)
    #print(education_expenditure)
    #print(country_data)

    combined = pd.merge(happiness,education_expenditure,left_on='Country or region', right_on='Country Name')

    #with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        #print(combined['Country or region'])
    #print(combined.info())
    #print(country_data.info())
    #print(combined['Country or region'][1])
    #print(combined['Country or region'][1] == country_data['Country'][54])
    combined['Country or region'] = combined['Country or region'].astype(str)
    country_data['Country'] = country_data['Country'].astype(str)


    a = pd.merge(combined, country_data, left_on = 'Country Name', right_on='Country')
    index = []
    for i in range(1996,2016):
        index.append(str(i))
    a[index] = a[index].astype(float)
    a['average2002-2012'] = a[index].mean(axis=1)
    #with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
       # print(a[["Country", 'average2002-2012']])
    return a

general_loader()