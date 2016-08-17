# Driving Records

[proyect in current development]

This personal proyect aims to determine the best "driving time" for specific routes by using empirical data feed to a simple neural netrwork. 

### Dataset

* data.csv: contains the empirical data in a .csv file. 

#### Variables
List and description of the variables (columns) in data.csv

* fecha: day in format dd/mm/yyyy 
* dsemana: day of the week i.e. [LUN, MAR, MIE, JUE, VIE, SAB, DOM]
* ruta: path or route taken e.g. casa_iteso_p (see **routes** section).
* inicio: departing hour HHhMM
* fin: Arriving hour HHhMM
* t: 
* cond: general weather condition i.e. [LR, NR, HR] (see **cond** section)

#### Routes
Variable that specifies the route taken.
 
* casa_iteso_p & iteso_casa_p: route from @rhdzmota's home to ITESO University using 'periferico'.
* [ add ]

#### Cond
Variable that describes the general weather condition.

* LR: light rain
* NR: no rain
* HR: heavy rain

### Scripts

* log_data.sh:
* log_data.py: script used to log new data into data.csv	
* get_time.py: contains the functions get_time() and show_timezones()
* data_cleaning.py: contains the functions load_data() and data_cleaning()
    - **load_data()** reads the data.csv and returns a pandas dataframe.
    - **data_cleaning()** transforms the dataframe from load_data() into a more useful dataset.	
* data_analysis.py: not available
* neural_network.py: not available

### To do list

* Complete data_cleaning() function in data_cleaning.py file
* Code data_analyisis.py script.
* Code neural_network.py script.





