from pandas import DataFrame
from get_time import get_time
import numpy as np
import get_variables as gv


def select_route():
    '''
    The function select_route() ask to the user to input the route key from
    available_routs and returns it. 
    
    Use as following:
    >> route = select_route() 
    '''
    print('\n::::::SELECT ROUTE:::::')
    available_routes = gv.route_options()
    print('\nTable of possible options. Format as key:value')
    for k,v in available_routes.items():
        print(k,":",v)
    while True:
        route_key = input('\nPlease choose the route key: ')
        if route_key in available_routes:
            break
        else:
            print('Invalid selection.')
    return route_key

def select_weather():
    '''
    The select_weather() functions shows the possible general conditions for the weather
    during the travel; records and returns user's choice. 
    
    Use as following:
    >> cond = select_weather()
    '''
    print('\n::::::SELECT WEATHER CONDITION:::::')
    possible_cond = gv.weather_options()
    print('\nTable of possible options. Format as key:value')
    for k,v in possible_cond.items():
        print(k,":",v)
    while True:
        cond_key = input('\nPlease choose the general weather condition key: ')
        if cond_key in possible_cond:
            break
        else:
            print('Invalid selection.')
    return cond_key

def add_data(route,t_begin,t_end,cond):
    '''
    The function add_data() adds the most recent record to file: data.csv
    
    Use as following:
    >> add_data(route,t_begin,t_end,cond)
    '''
    # Prepare data... 
    r = route
    date = t_begin.strftime('%d-%m-%Y')
    day_week = str(t_begin.weekday())
    t0 = float(t_begin.hour) + float(t_begin.minute) / 60 + float(t_begin.second) / 60 ** 2
    t1 = float(t_end.hour)   + float(t_end.minute) / 60   + float(t_end.second) / 60 ** 2
    delta = t1 - t0
    c = cond
    # create dataframe
    d = {'date':str(date),'day_week':day_week,'id_route':r,'t0':t0,'tf':t1	,'delta':delta,'cond':cond}
    cols = ['date','day_week','id_route','t0','tf','delta','cond']
    df = DataFrame(data=d, index=np.arange(1))
    df = df[cols]
    # add to data.csv file
    with open('data.csv','a') as f:
        (df).to_csv(f,header=False,index=False)

def main():
    # Route selection process
    available_routes = gv.route_options()
    flag = ' '
    while flag != 'y':
        route = select_route()
        print('\nYou selected: ', available_routes[route])
        flag = input('\nAre you sure this is your route? (type "y" for yes, any other character for "no") : ')
    
    # Initialize and end record.
    input('\nPress enter to start recording.')
    t_begin = get_time()
    input('\nRecording... Press enter to stop.')
    t_end = get_time()
    
    # Add weather conditions.
    possible_cond = gv.weather_options()
    flag = ' '
    while flag != 'y':
        cond = select_weather()
        print('\nYou selected: ', possible_cond[cond])
        flag = input('\nAre you sure this was the condition? (type "y" for yes, any other character for "no") : ')
    
    # Saving the data
    print('\nSaving the data...')
    add_data(route,t_begin,t_end,cond)
    
    # Add the data and closure
    print('\nAlright, we are good to go.')
    print('Closing...')
    
    print('\nDone.')

main()