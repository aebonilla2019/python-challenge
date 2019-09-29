#import dependencies
import os   
import csv   

#csv variable pointing to csv file
data_file = os.path.join('resources','election_data.csv')


#write file variable
write_file = os.path.join('Election_Results.txt')

#with csv folder open set set variable for CSV reder
with open(data_file, mode='r') as csv_file:  
    csv_reader = csv.reader(csv_file, delimiter=',')
    
    #Define header row
    header = next(csv_reader)
    
    #Define total_votes variable
    total_votes = 0   #Define 'totalVote' variable and set it to 0
    
    #Create the results list dictionary
    results_list = {}
    
    #create a winner dictionary
    winner_dict = {'name': '', 'votes': 0}
    
    
    #loop through the csv_reader variable by line
    for vote in csv_reader:   
        
        #add one to the total_votes
        total_votes += 1   
        
        # if the candidate name is not in the dictionary as a key add it tot he dictionary along with the number of vote and vote percentage
        if vote[2] not in results_list.keys():   
            results_list[vote[2]] = {'num_votes': 0, 'percentVotes': 0}   
        
        # if the candidate is in the dictionary add 1 to the votes for that candidate
        if vote[2] in results_list.keys():   
            results_list[vote[2]]['num_votes'] += 1   
    
    #set results list that contains total_votes
    resultsSummary = ['Total Votes: ' + str(total_votes) + '\n']   
    
    
    #loop through each candidates name in the results list
    for candidate in results_list.keys():   
        
        #set percentvote as num_votes devided by total_votes *100
        results_list[candidate]['percentVotes'] = int(results_list[candidate]['num_votes'] / total_votes * 100)   
        
        #if num_votes key value is greater than votes value of the winner dictionary se the name in the winner dictionary to current candidate name
        #and set the votes key value of the winner dictionary to the num_votes key value
        if results_list[candidate]['num_votes'] > winner_dict['votes']:   
            
            winner_dict['name'] = candidate   
            
            winner_dict['votes'] = results_list[candidate]['num_votes']
                                   
        #Append to 'resultsSummary' list: current candidate's name, 'percentVotes' key value , and 'num_votes' key value
        resultsSummary.append(\
            candidate + ': ' + \
            "{:.2f}".format(results_list[candidate]['percentVotes']) + '% (' + \
            str(results_list[candidate]['num_votes']) + ') ')

    
    #Append to 'resultsSummary' list: 'name' key value of 'winner' dict
    resultsSummary.append('\nWinner: ' + winner_dict['name'])   
    
    #with write_file open write each line of resultssummary to the file
    with open(write_file, mode='w') as text_file:   
        text_file.writelines(resultsSummary)   

    #print results of the text file
    with open(write_file, mode='r') as text_file:   
        print(text_file.read())   