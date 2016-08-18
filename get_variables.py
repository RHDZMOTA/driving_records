'''
Functions to make available the data for routes and weather conditions. 
'''
def route_options():
    available_routes = {'1':'home_university_p','2':'university_home_p',
        3:'home_atrh_u',4:'atrh_home_u',5:'university_atrh_u'}
    return available_routes
    
def weather_options():
    possible_cond = {'1':'Light Rain','2':'No Rain','3':'Heavy Rain'}
    return possible_cond
    
    
    