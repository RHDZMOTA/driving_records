echo ************ Log Location/Position ************ 
echo This program will record the device s postion
echo and save it to geo_data.csv

i=1
while true
do
    echo --------------------------------------
    echo Recording data - number of cycle: $i
    
    # Get the current location using termux 
    echo Getting location... 
    loc=$(termux-location)

    # Save the date and time in variables
    day=$(date "+%Y-%m-%d")
    time=$(date "+%H:%M:%S")
    
    # Save the relevat info. in loc
    lat=$(echo $loc | jq .latitude)
    lon=$(echo $loc | jq .longitude)
    alt=$(echo $loc | jq .altitude)
    
    # Variable with all the information
    res=$(echo ${day},${time},${lon},${lat},${alt})
    
    
    # Save data into geo_data.csv file 
    echo Saving data into .csv file... 
    echo $res >> geo_data.csv
    
    # Autoincrement variable 'i'
    i=$((i+1))
    echo Alright!
done

#export lat lon alt
#python loc.py