import pandas as pd

# radious of the earth
r = 6367.4447 

def load_select(geo_data,date, t0, tf):
    '''
    The select function loads the data with specific reestrictions. 
    '''
    df = geo_data[geo_data.day==date]
    n = len(df)
    ind1 = list(map(float,df.time)) > [float(t0)] * n
    ind2 = list(map(float,df.time)) < [float(tf)] * n
    ind  = ind1 == ind2
    print(ind)
    '''
    df = df[:][ind]
    df = to_radians(df)
    df = change_hour(df)
    df = rect_coord(df)
    '''
    return df

def change_hour(dataframe):
    '''
    The function change_hour modifies the hour format in a given dataframe
    and returns the corresponding column adjusted.
    '''
    b = []
    from numpy import true_divide
    for i in dataframe.time:
        a = list(map(int,str.split(i,':')))
        b.append(a[0] + true_divide(a[1],60) + true_divide(a[2], 60**2))
    dataframe.time = b	
    return dataframe    	

def to_radians(dataframe):
    ''' 
    thefunction to_radians(dataframe) uses a given dataframe with
    with a longitude and latitude columns in degrees to output a dataframe
    with those columns converted to randians. 
    
    Use as following:
    geo_data = to_radians(pd.read_csv('geo_data.csv'))
    ''' 
    from math import radians
    from numpy import true_divide
    # convert to radians
    dataframe.longitude = list(map(radians, dataframe.longitude))	
    dataframe.latitude  = list(map(radians, dataframe.latitude))
    dataframe.altitude  = true_divide(dataframe.altitude,1000)
    
    return dataframe

def rect_coord(geo_data):
    '''
    '''
    from numpy import sin, cos, array
    coord_x = [(r+a)*sin(phi)            for phi,lambd,a in zip(geo_data.latitude, geo_data.longitude, geo_data.altitude)	]
    coord_y = [(r+a)*cos(phi)*sin(lambd) for phi,lambd,a in zip(geo_data.latitude, geo_data.longitude, geo_data.altitude)	]
    coord_z = [(r+a)*cos(phi)*cos(lambd) for phi,lambd,a in zip(geo_data.latitude, geo_data.longitude, geo_data.altitude)	]	
    geo_data['position'] = [array([x,y,z]) for x,y,z in zip(coord_x,coord_y,coord_z) ]
    return geo_data

def plot_traj(t_init, t_end, data):
    '''		
    '''


def main():
    '''
    '''
    from numpy import arange, array
    # Reads data (with the route data) and geo_data (with the geo.coord data)
    data = pd.read_csv('data.csv')
    geo_data = pd	.read_csv('geo_data.csv')
    
    # select specific parameters...
    #note input route.
    route = 1
    use_data = data[data.id_route==route]
    gen_data = []
    i = 0
    for date,t0,tf in zip(use_data.date,use_data.t0,use_data.tf):
        gen_data.append(load_select(geo_data, date, t0, tf))
    
    # Print
    print(len(gen_data))

main()