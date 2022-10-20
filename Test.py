cities = {
   'Lagos': {
        'country': 'nigeria',
        'population': 15000000,
        'fact': 'fastest growing city in africa',
   },
   'Newyork':{
        'country': 'usa',
        'population': 18000000,
        'fact': 'financial capital of the world',
   },
   'Shenzen':{
        'country': 'china',
        'population': 21000000,
        'fact': "china's tech hub", 
   },
}

for city, city_info in cities.items():
    print('City:' + city)
    print('Country:' + city_info['country'])
    print('Population:' + str(city_info['population']))
    print('Fact:' + city_info['fact'].title)
    print('\n')