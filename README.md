# Driving Records

[proyect in current development]

This personal proyect aims to determine the best "driving time" for specific routes by using empirical data feed to a simple neural netrwork. 

### Instructions

This instructions are mainly for anyone who easily forgets what he/she has done (myself). 

To run this scripts in any android device:

  1. Download GNURoot Debian from GooglePlay.
  2. Download GNURoot Octave from GooglePlay.
  3. Open and install the app from step 1. This will install a linux distro (Debian Jessy) with a fake root into Android. 
  4. Open and install the app from step 2. This will provide you with Octave (a MATLAB-like program). 
  5. Close all...
  6. Open the app from step 1 and run _apt-get update_ 
  7. Install python3: _apt-get install python3_
  8. Install pandas and numpy: _pip install numpy_ (and so on...)
  9. Download Termux app from GooglePlay.
  10. Open Termux and type _apt-get update && upgrade_
  11. Install git in Termux	: _apt-get install git_
  12. Now you can clone or make git-directories (see "**download or clone this repository**")
  13. Follow the instructions in **"To run in a debian distro (linux)"**.

Download or clone this repository.
  1. Type in termial: git clone https://github.com/RHDZMOTA/driving_records.git

To run in a debian distro (linux):
  1. Type in console: apt-get update
  2. Go to your directory: cd /go_to_your_directory
  3. Enjoy.
    - To add new data, type in console: sh ./log_data.sh
    - To see analyitcs (simple stats): python3 stats.py
    - To ask the neural network for a particular value: unavailable
    - To see predictions from the neural network: unavailable

NOTE: if matplotlib is not installed, avoid showing graphs in python scripts. 
 
### Dataset

* **data.csv**: contains the empirical data in a .csv file. 

#### Variables
List and description of the variables (columns) in data.csv

* **date**: text day in format dd-mm-yyyy 
* **day_week**: day of the week as a number (see **day_week** section)
* **id_route**: id of the path or route taken (see **routes** section).
* **t0**: departing time measured in hours.
* **tf**: Arriving time measured in houres. 
* **delta**: t0 - tf 
* **cond**: id of the general weather condition (see **cond** section)

#### day_week

The day of the week i.e. _Mon, Tue, Wed, Thu, Fri, Sat, Sun_ --> _0, 1, 2, 3, 4, 5, 6_.

#### id_route
Variable that specifies the route taken.
 
* **1:home_university_p** route from @rhdzmota's home to ITESO University using 'periferico'.
* **2:university_home_p** route form ITESO Univerity to @rhdzmota home using 'periférico'.
* ...

#### Cond
Variable that describes the general weather condition.

* **1:"light rain"**
* **2:"no rain"**
* **3:"heavy rain"**

### Scripts

#### Add and remove datapoints
* **log_data.sh**: bash script to facilitate running the program.
* **log_data.py**: script used to log new data into data.csv	
* **get_time.py**: contains the functions get_time() and show_timezones()
    - *get_time()* returns the date and time for MX's timezone.
    - *show_timezones()* prints the available timezones in pytz package
* **data_cleaning.py**: contains the functions load_data() and data_cleaning()
    - *load_data()* reads the data.csv and returns a pandas dataframe.
    - *data_cleaning()* transforms the dataframe from load_data() into a more useful dataset.

#### Statistical analysis	
* **stats.py**: general descriptive stats and visualizations. 

#### Artificial Intelligence 
* **neural_network.py**: not available

### To do list

* Code encryption file and functions (from a given ke and input, return the encrypted data).
* Modify log_data.sh and log_data.py to automatically start to record data when exiting a given area defined by each route. Implement the log of lon lat and alt.
* Visualization for pos, velocity and acceleration. Investigate how to interpret the geo coord.  
* Code data_analyisis.py script taking into account the extra information for each route. 
* Code neural_network.py script.





