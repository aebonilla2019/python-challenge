# import dependencies
import os 
import csv   


#path of the source file
source_path = os.path.join('employee_data.csv')   

#path to the write file
write_path = os.path.join('converted_employee_data.csv')   


#dictionary of US state abbrviations
us_state_abbrev = {   
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}


#create results_list based on the row column headers
results_list = [['Emp', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']]   


#open source file
with open(source_path, mode='r') as csv_file:   
    
    #set variable to read csv file
    csv_reader = csv.reader(csv_file, delimiter=',')  
    
    #skip header
    next(csv_reader) 
    
    
    #loop through the every line in the file reader variable
    for record in csv_reader:  
        
        #create an empty results list
        result_row = [] 
        
        #append result_row with employee number
        result_row.append(record[0])   
        
        #when a blank space is found take the first name and append to result_row
        result_row.append(record[1].split(' ')[0])   
        
        #when that same blank space is encountered take the last name and append it to resultrow
        result_row.append(record[1].split(' ')[1])   
        
        #append date to resultrow to seperate columns when we encounter -
        result_row.append(record[2].split('-')[1] + '/' + record[2].split('-')[2] + '/' + record[2].split('-')[0])
        
        #append the last 4 from SSN to resultrow with #'s when we encounter an -
        result_row.append('###-##-' + record[3].split('-')[2])   
        
        #use state name to pull the abbreviations from the us state abbrv dict
        result_row.append(us_state_abbrev[record[4]])   
        
        #append result_row to results_list
        results_list.append(result_row)  

 #with write file open       
with open(write_path, 'w', newline='') as csv_file: 
    
    #set variable with writing function for csv_file
    csv_writer = csv.writer(csv_file) 
    
    #write restultslist to open file
    csv_writer.writerows(results_list) 
    
#open write file in read mode and set variable to read csv file    
with open(write_path, mode='r') as csv_file:   
    csv_reader = csv.reader(csv_file, delimiter=',')   
    
    #loop through csv_reader and print
    for record in csv_reader:   
        print(record)   