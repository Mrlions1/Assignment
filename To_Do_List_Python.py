# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 23:53:21 2021

@author: HP
"""

def dispMenu():
    print('============== Main Menu ===============') 
    print('=========================================')
    print('1. Add an Item')
    print('2. Remove Item')
    print('3. Mark Complete/Incomplete in list') 
    print('=========================================')
    
user_choice = 'random'
data = list()  
usertwo_choice = 'random' 

while user_choice != '4': 
    dispMenu()
    user_choice = input('\nSelect Your Option : ') 
    if user_choice == '1':
        item = input('What do you want to do? : ')
        data.append(item)
        print("Item Added:", item)
    elif user_choice == '2':
        item = input('What item do you want to remove? : ')  
        if item in data:  
            data.remove(item)
            print("Removed item:", item) 
        else: 
            print('Item is not in the list') 
    elif user_choice == '3': 
        print('What item do you want to mark as complete or incomplete?') 
        for items in data:
            print(items) 
            print('Press 3 to mark as complete and 4 to incomplete')
            if usertwo_choice == 3: 
                print('Complete', items) 
            elif usertwo_choice == 4: 
                print('Incomplete', items)
