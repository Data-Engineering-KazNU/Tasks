# DESCRIPTION
This project contains data of regions of the USA with the year, value and region

The scripts are located in the "scripts" folder. In the "archive" folder you will find the original csv file with which i worked with. "data" folder contains the finished product, and it consists of **3 columns and 3 rows**. 
1. The first column shows the exact date
2. the second column has different types of regions in it
3. the third column has different values

The python script is in the "script" folder. It currently has only 2 libraries- *"import csv" and "from datetime import datetime0*". The script takes the data from the "source3.csv", changes the date format from **YYYY-MMM to DD-MM-YYYY** in the 1 column, compiles it, and then posts the outcome into the "source4.csv" file.