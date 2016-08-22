from datetime import datetime
from pytz import timezone, all_timezones

def get_time():
    '''
    The function get_time() returns a date object 'now_here' with
    the date and time information in 'America/MexicoCity'.
    
    Use as following:
    >> now = get_time()
    >> print(str(now))
    '''
    
    now_utc = datetime.now(timezone('UTC'))
    
    now_here = now_utc.astimezone(timezone('America/Mexico_City'))
    return now_here

def show_timezones():
    '''
    	The show_timezones() functions prints all the available timezones in pytz
    all_timezones module. 
    
    Use as following:
    >> show_timezones()
    '''
    print('Total available timezones:',	len(all_timezones))
    for zone in all_timezones:
        #if 'Mexico	' in zone:
        #    print(	zone)
        print(zone)
        

	