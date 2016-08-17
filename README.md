# Driving Records

[proyect in current development]

This personal proyect aims to determine the best "driving time" for specific routes by using empirical data feed to a simple neural netrwork. 

### Dataset

* data.csv: contains the empirical data in a .csv file. 

#### Variables
List and description of the variables (columns) in data.csv

* date: text day in format dd-mm-yyyy 
* day_week: day of the week as a number (see **day_week** section)
* id_route: id of the path or route taken (see **routes** section).
* t0: departing time measured in hours.
* tf: Arriving time measured in houres. 
* delta: t0 - tf 
* cond: id of the general weather condition (see **cond** section)

#### day_week

The day of the week i.e. _Mon, Tue, Wed, Thu, Fri, Sat, Sun_ as 0,1,2,3,4,5,6.

#### id_route
Variable that specifies the route taken.
 
* **1:home_university_p** route from @rhdzmota's home to ITESO University using 'periferico'.
* **2:university_home_p** route form ITESOUniverity to @rhdzmota home using 'periférico'.
* ...

#### Cond
Variable that describes the general weather condition.

* 1:"light rain"
* 2:"no rain"
* 3:"heavy rain"

### Scripts

* log_data.sh: not available
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





