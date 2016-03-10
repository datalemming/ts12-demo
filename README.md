# ts12-demo

These are the files for the expanded RiakTS1.2 demonstration.

###Data
The dataset loaded is the February to June 2014 traffic data from Aarhus in Denmark.  See me to get a copy of the ram CSV file to load.  It consists of the following fields:

1. Status - always OK
2. extID - an id for a pair of traffic sensors located somewhere in Aarhus
3. avgTime to pass through the sensor reach
4. avgSpeed going through those sensors
5. medianTime to pass through the sensors
6. vehicle count in a 5 minute span
7. ID - ignore
8. ReportID - ignore

###Notebooks
To make use of the new table structure (per Product Marketing) you need to use the following notebooks:

* Create table aarhus2
* Querying aarhus2 data

After creating the table and before querying you need to use the following to load the data:

* load-data-v2.py


