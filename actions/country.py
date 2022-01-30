import requests

url = "https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getCountries"



def check_country(country):
    '''
    this function checks if the wanted country in the list or not
    INPUTS:
     country: title of the country
    OUTPUT:
     flag: True if the country exist in the list
     country: 
    '''
    response = requests.get(url)
    countries = response.json()['body']
    con_cap = country.capitalize() 
    con_upper = country.upper() 
    con_lower = country.lower() 
    is_country = [[con_cap in countries,con_cap],[con_upper in countries,con_upper],[con_lower in countries,con_lower]]
    is_country.sort(reverse=True)
    return is_country[0][0],is_country[0][1]
