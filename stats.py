import numpy as np
import pandas as pd
import get_variables as gv

def load():
    data = pd.read_csv('data.csv')
    available_routes = gv.route_options()
    possible_cond = gv.weather_options()
    return data, available_routes, possible_cond

def weekdayfunc(x):
    wd = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',
        4:'Friday',5:'Saturday',6:'Sunday'}
    return wd[x]

def scatter_t0tf(f):
    plt.figure(f)
    data, available_routes, possible_cond = load()
    routes = set(data.id_route)
    #color = iter(cm.rainbow(np.linspace(0, 1, len(routes))))
    for i in routes:
        index = data.id_route == i
        plt.scatter(data.t0[index],
            data.tf[index], color=color_hex(i-1),alpha=0.7,
            label=available_routes[str(i)],s=124,marker='x')
    plt.title('Scatterplot: departure time vs arriving time')
    plt.xlabel('Departure time (h)')
    plt.ylabel('Arrival time (h)')
    plt.legend(loc='upper left')
    plt.xlim(0,24)
    plt.ylim(0,24)
    plt.grid()
    #plt.show()
    f = f + 1
    return f

def scatter_t0delta(f):
    plt.figure(f)
    data, available_routes, possible_cond = load()
    routes = set(data.id_route)
    #color = iter(cm.rainbow(np.linspace(0, 1, len(routes))))
    for i in routes:
        index = data.id_route == i
        plt.scatter(data.t0[index],
            data.delta[index], color=color_hex(i-1),alpha=0.8,
            label=available_routes[str(i)],s=160,marker='o')
    plt.title('Scatterplot: departure time vs delta')
    plt.xlabel('Departure time (h)')
    plt.ylabel('delta (h)')
    plt.legend(loc='upper left')
    plt.xlim(0,24)
    plt.ylim(0,1.2)
    plt.grid()
    #plt.show()
    f = f + 1
    return f

def bar_route(bar_data,f):
    plt.figure(f)
    x_pos = list(range(len(bar_data['_routes'])))
    plt.bar(x_pos,list(bar_data['mean']),yerr=list(bar_data['standard_deviation']),
        align='center',alpha=0.5, color='#6e8ca6'); plt.grid()
    plt.ylabel('Time spend (h)')
    plt.xticks(x_pos,list(bar_data._routes))
    plt.title('Average time to reach destination')
    #plt.show()
    f = f + 1
    return f

def barplot_week(bar_data,k,f):
    plt.figure(f)
    title = 'Time to reach destination per day - route: '+k
    x_pos = list(range(len(bar_data['_weekday'])))
    plt.bar(x_pos,list(bar_data['mean']),yerr=list(bar_data['standard_deviation']),
        align='center',alpha=0.5, color='#6e8ca6'); plt.grid()
    plt.ylabel('Time spend (h)')
    plt.xticks(x_pos,list(bar_data._weekday))
    plt.title(title)
    #plt.show()
    f = f + 1
    return f
    

def main():
    
    # Variable for futures figures
    f = 1
    
    # Load data
    data, available_routes, possible_cond = load()

    # DESCRIPTIVE STATS
    # Just basic statistics and visualizations. 
    
    # General delta stats
    print('\n:::::::::::::::::General stats:::::::::::::::::\n')
    general_stats = {'number_of_obs':len(data),'mean':np.mean(data.delta),
        'standard_deviation':np.std(data['delta'])}
    general_stats = pd.DataFrame(data=general_stats,index=np.arange(1))
    print(general_stats) 
         
    # Delta stats per route
    print('\n:::::::::::::::::Route stats:::::::::::::::::\n')
    routes = set(data.id_route)
    route_stats = pd.DataFrame()
    for i in routes:
        index = data.id_route == i
        r = available_routes[str(i)]
        m = np.mean(data.delta[index])
        sd = np.std(data.delta[index])
        route_stats = route_stats.append({'_routes':r,'mean':m,'standard_deviation':sd},
            ignore_index=True)
    print(route_stats)
    
    # Delta stats per day of week
    print('\n:::::::::::::::::WeekDay stats:::::::::::::::::\n')
    for j in routes:
        print('\n>>>> Data from route:',available_routes[str(j)])
        index = data.id_route == j
        subdata = data[index]
        weekday = set(subdata.day_week)
        weekday_stats = pd.DataFrame()
        for i in weekday:
            subindex = subdata.day_week == i
            r = weekdayfunc(i)
            m = np.mean(subdata.delta[subindex])
            sd = np.std(subdata.delta[subindex])
            weekday_stats = weekday_stats.append({'_weekday':r,'mean':m,'standard_deviation':sd},
                ignore_index=True)
        print(weekday_stats)
        if flag == 'y':
            # barplot week
            f = barplot_week(weekday_stats,available_routes[str(j)],f)
    
    # Visualizations... 
    if flag == 'y':
        
        # BarPlot for route
        f = bar_route(route_stats,f)
 
        # Scatterplot t0 vs t1
        f = scatter_t0tf(f)
    
        # Scatterplot t0 vs delta
        f = scatter_t0delta(f)
        
        # Show'em all
        plt.show()


print('\n*****************DESCRIPTIVE STATS*****************\n')
print('This program shows basic statistics and optional visualizations...')
print('___________________________________________________')
flag = input('Show graphs? (type "y" for yes): ')
if flag == 'y':
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm
    from color_hex import color_hex
    # Close pre-existing figures
    plt.close("all")

main()