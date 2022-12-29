"""Restaurant rating lister."""
import sys
import random

#pseudocode
#allow the user to provide any name file as he wants
#open the file
#create an rate dictionary
#iterate over thr file
#and save the restaurante name as key and the rate as value to the rate dictionary
#display the rates in alphabetic order by restaurante, user sorted

def rating(file):
    
    rates = {}
    restaurante_rate_file = open(file)
    valid_rates = "12345"

    for line in restaurante_rate_file:
        restaurante = line.rstrip().split(":")        
        rates[restaurante[0]] = restaurante[1]

    while True:  
        question = input("\n Type 'see' if you want to see all the ratings, \n Type 'add' if you want to add a new restaurante and rating it, \n If you want to update a rating type 'update' \n or type 'q' to quit the program: ")
               
        if question == "q" or question == "Q":
            break  
        elif question == "add" or question =="Add":
            new_restaurante_rate = input("Please enter a new restaurante name: ").title()
            new_rate = input("Please enter a new rate from 1 to 5 for this restaurante: ")         
            
            if new_rate not in valid_rates:
                print("make sure you are entering a valid rate")
                continue
            rates[new_restaurante_rate] = new_rate  
        elif question == "see" or question == "See":

            for key, value in sorted(rates.items()):    
                print(key,value) 

        elif question == "update" or question == "Update":
            rate_to_update = random.choice()
            print(rate_to_update)        

file = sys.argv[1]
rating(file)        








