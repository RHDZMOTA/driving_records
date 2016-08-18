import numpy as np
import pandas as pf
import matplotlib.pyplot as plt



def main():
    data = pd.read_csv('data.csv')
    
    # DESCRIPTIVE STATS
    # Just basic statistics and visualizations. 
    
    # general delta stats
    general_stats = {'Number of obs':size(data,1),'Mean':np.mean(data['delta']), ...
        'Standard Deviation':np.std(data['delta'])}
    general_stats = pd.DataFrame(data=general_stats,index=np.arange(1))
    print('General stats\n', general_stats)
    # delta time stats per route taken
    
    plt.plot()
    plt.show()
    # delta time stats per day
    
    plt.plot()
    plt.show()
    # t1 vs t0
    plt.plot(data['t1'],data['t0'])
    plt.show()
    


main()