#import dependecies
import os
​
#module for reading CSV files
import csv
import math
​
budget_file = os.path.join('budget_data.csv')
output_file = os.path.join('budget_data_analysis.txt')
​
#using csv module to read data
with open(budget_file, newline ='') as csvfile:
    
    #csv reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')
    
    print("Financial Analysis")
    print("---------------------------")
    
    #Counter for the total of the months
  
    header = next(csvreader)
#     data = list(csvreader)
#     row_count = len(data)
    
    #Define 'month_total' varible to store the value and set it to 0
    month_total = 0   
    
    
    #Define 'net_change' varible and set to 0
    net_change = 0   
    
    
    
    #Create greatest_change dictionary: this includes the increase value key and value, the increase date key, drecrease value key and value, and decrease date key
    greatest_change = {'increase_value': 0,'increase_date': '','decrease_value': 0,'decrease_date': ''  }
       
    #create empty results list
    results = []    
    #print ("Total Months: " + str(row_count))
    
    
    #loop through each line of the csv file (per the variable csvreader)
    for record in csvreader:  
        #add 1 to 'month_total' value for each row
        month_total += 1   
        #add the value in column 2 (Profit/Loss) to the net change variable
        net_change += int(record[1]) 
        
        #conditional if profit/loss value is greater than the increase value set the greater value as the value for the increase value variable
        #and set the date value as the increase date
        if int(record[1]) > greatest_change['increase_value']:
            
            greatest_change['increase_value'] = int(record[1])   
            
            greatest_change['increase_date'] = record[0]   #... set "Date" value from file as value for 'increase_date' key ...
        
        #otherwise if the profit/loss value is less than the decrease value set the lesser value as the decrese value variable
        #and set the date value as the decrease date
        elif int(record[1]) < greatest_change['decrease_value']:   
            
            greatest_change['decrease_value'] = int(record[1])   
            
            greatest_change['decrease_date'] = record[0]   
       
    
    
    
   #populate the results list created earlier   
    results = [\
        'Total Months: ' + str(month_total) + '\n', \
        'Total: $' + str(net_change) + '\n', \
        'Average Change: $' + str(net_change/month_total) + '\n', \
        'Greatest Increase in Profits: ' + greatest_change["increase_date"] + ' ($'+str(greatest_change["increase_value"]) + '\n', \
        'Greatest Decrease in Profits: ' + str(greatest_change["decrease_date"]) + ' ($' + str(greatest_change["decrease_value"]) + ')' \
    ]
    
    
    total = 0
    for row in csvreader:
        total += int(row[1])
  #open text file and write the results      
with open(output_file, mode='w') as text_file:   
    text_file.writelines(results)   
  #open text file and print results
with open(output_file, mode='r') as text_file:   #Open text write file in read mode and set to 'text_file' variable
    print(text_file.read())   #print contents of text write file to console
    
​
        
print (total)
print(results)