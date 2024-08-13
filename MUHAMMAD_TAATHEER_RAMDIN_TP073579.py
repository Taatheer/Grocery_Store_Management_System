#MUHAMMAD TAATHEER RAMDIN
#TP073579

def INSERT_NEW_ITEM():

    new_code = int(input("Please enter code of new item: "))

    new_code = VALIDATE_CODE(new_code)

    new_description = input("Please enter description of new item: ")

    new_category = input("Please enter category of new item: ")

    new_unit = input("Please enter unit for new item: ")

    new_price = float(input("Please enter price of new item: "))

    new_quantity = int(input("Please enter quantity of new item: "))

    new_minimum = int(input("Please enter minimum of new item: "))

    new_item = [new_code,new_description,new_category,new_unit,new_price,new_quantity,new_minimum]

    fhand = open('C:\\Users\\Taatheer\\Desktop\\inventory.txt','a')

    line = ''
    
    for value in new_item:
        line = line +((str(value) + ('    ')))
    line.strip()
    fhand.write(line + '\n')
    fhand.close()

def UPDATE_ITEM():
    master_list = []
    found = False
    index = - 1

    READ_INTO_MASTERLIST(master_list)
    
    change_code = int(input('Please enter the code of the item you want to change: '))
    found, index = FIND_ITEM(change_code)

    if found == True: 
        print (''' What do you want to update ?
                    1. Code
                    2. Description
                    3. Category 
                    4. Unit
                    5. Price
                    6. Minimum
                                        ''')
                    
        choice = int(input("Choice: "))

        #validates choice
        while choice < 1 or choice > 7:
            print("Incorrect choice! Please re-enter.")
            choice = int(input("Choice: "))
                    
        if choice == 1:
            the_code = int(input("Please enter the new code of item: "))
            the_code = VALIDATE_CODE(the_code)
            master_list[index][0] = the_code
        elif choice == 2: 
            the_description = input("Please enter the new description of item: ")
            master_list[index][1] = the_description
        elif choice == 3: 
            the_category = input("Please enter the new category of item: ")
            master_list[index][2] = the_category
        elif choice == 4: 
            the_unit = input("Please enter the new unit for item: ")
            master_list[index][3] = the_unit
        elif choice == 5: 
            the_price = float(input("Please enter the new price of item: "))
            master_list[index][4] = the_price
        elif choice == 6: 
            the_minimum = int(input("Please enter the new minimum of item: "))
            master_list[index][6] = the_minimum

        REWRITE_LIST(master_list)
    else:
        print("\nSorry item code does not exist")
        
def DELETE_ITEM():
    master_list = []

    code_del = int(input('Please enter the code of the item you want to delete: '))

    found = False
    index = -1

    READ_INTO_MASTERLIST(master_list)

    found, index = FIND_ITEM(code_del)

    if found == True: 
        list_to_remove = []
        for value in range(0,8):
            list_to_remove.append(master_list[index][value])
        if list_to_remove in master_list:
            master_list.remove(list_to_remove)

        REWRITE_LIST(master_list)
    else:
        print("Sorry! Item code does not exist")




def SEARCH_ITEM():

    master_list = []

    READ_INTO_MASTERLIST(master_list)

    print (''' Select your search criteria :
                    1. Description
                    2. Code range
                    3. Category 
                    4. Price range
                                        ''')
                    
    choice = int(input("Choice: "))
    #validates choice
    while choice < 1 or choice > 4:
        print("Incorrect choice! Please re-enter.")
        choice = int(input("Choice: "))

    if choice == 1:
        user_description = input("Please enter a description to search: ")

        for count in range(0, len(master_list)):
            
            if master_list[count][1] == user_description:
                print(f'\n{master_list[count][0]}    {master_list[count][1]}    {master_list[count][2]}    {master_list[count][3]}    {master_list[count][4]}    {master_list[count][5]}    {master_list[count][6]}')
    elif choice == 2: 
        starting_code = int(input('\nPlease enter minimum code: '))
        end_code = int(input('Please enter maximum code: '))

        code_list = []
        for count in range(0,len(master_list)):
            if int(master_list[count][0]) >= starting_code and int(master_list[count][0]) <= end_code:
                code_list.append(int(master_list[count][0]))
        
        code_list.sort()

        print('\n')
        for count1 in range(0,len(code_list)):
            for count2 in range(0,len(master_list)):
                if str(code_list[count1]) == master_list[count2][0]:
                    print(f'{master_list[count2][0]}    {master_list[count2][1]}    {master_list[count2][2]}    {master_list[count2][3]}    {master_list[count2][4]}    {master_list[count2][5]}    {master_list[count2][6]}')
    elif choice == 3: 
        user_category = input("Please enter a category to search: ")

        print('\n')
        for count in range(0, len(master_list)):
                
            if master_list[count][2] == user_category:
                print(f'{master_list[count][0]}    {master_list[count][1]}    {master_list[count][2]}    {master_list[count][3]}    {master_list[count][4]}    {master_list[count][5]}    {master_list[count][6]}')
    elif choice == 4:
        starting_price = float(input('\nPlease enter minimum price: RM'))
        end_price = float(input('Please enter maximum price: RM'))

        price_list = []
        for count in range(0,len(master_list)):
            if float(master_list[count][4]) >= float(starting_price) and float(master_list[count][4]) <= float(end_price):
                if float(master_list[count][4]) not in price_list:
                    price_list.append(float(master_list[count][4]))
        
        price_list.sort()

        print('\n')
        for count1 in range(0,len(price_list)):
            for count2 in range(0,len(master_list)):
                if str(price_list[count1]) == master_list[count2][4]:
                    print(f'{master_list[count2][0]}    {master_list[count2][1]}    {master_list[count2][2]}    {master_list[count2][3]}    {master_list[count2][4]}    {master_list[count2][5]}    {master_list[count2][6]}')

def STOCK_TAKING():
    master_list = []

    READ_INTO_MASTERLIST(master_list)

    code_check = input("Please enter code of item for stock-taking: ")

    index = - 1
    found = False
    found, index = FIND_ITEM(code_check)
    if found == True:
        if str(code_check) == master_list[index][0]:
            print(f"Quantity available: {master_list[index][5]}" )
            print('''Select action: 
                            1. Confirm quantity
                            2. Change quantity
                            ''')
            choice = int(input("Choice: "))

            #validates choice
            while choice < 1 or choice > 2:
                print("\nIncorrect choice! Please re-enter.")
                choice = int(input("Choice: "))
            if choice == 1:
                print('\nConfirmed')
            else:
                new_quantity = int(input('Please enter new quantity: '))
                print('\nQuantity changed!')
                master_list[index][5] = new_quantity
                REWRITE_LIST(master_list)             
    else:
        print("\nSorry! Item code does not exist") 


def VIEW_REPLENISH_LIST():
    master_list = []
    READ_INTO_MASTERLIST(master_list)

    print('\n')
    
    for count in range(0, len(master_list)):
        if int(master_list[count][5]) < int(master_list[count][6]):
            print(f'Code: {master_list[count][0]}    Description: {master_list[count][1]}    Quantity: {master_list[count][5]}')

def STOCK_REPLENISHMENT():
    master_list = []

    READ_INTO_MASTERLIST(master_list)
    
    code_rep = int(input("Please enter code of item for stock-replenishment: "))

    index = - 1
    found = False
    
    found, index = FIND_ITEM(code_rep)
    if found == True:
        if str(code_rep) == master_list[index][0]:
            print(f"\nQuantity available: {master_list[index][5]}" )
            quantity_purchased = int(input('Please enter quantity of item purchased: '))
            new_quantity = int(master_list[index][5]) + quantity_purchased
            master_list[index][5] = new_quantity
            print('\nQuantity updated!\n')
            REWRITE_LIST(master_list)
    else:
        print("\nSorry! Item code does not exist") 
 


def USER_AUTHENTICATION():
    master_list= []
    my_user_access = ''
    my_valid = False

    print('Login\n')
    user_username = input('Please enter username: ')
    user_password = input('Please enter password: ')

    fhand = open("C:\\Users\\Taatheer\\Desktop\\userdata.txt", 'r')

    line = fhand.readline()

    while line: 
        list_read = []
        list_read = list(map(str,line.split('    ')))
        master_list.append(list_read)
        line = fhand.readline()
    
    fhand.close()
    
    dec_pass, index = DECRYPT_PASS(master_list, user_username)

    if user_password == dec_pass:     
        my_user_access = master_list[index][2]
        my_valid = True       
        
    else:  
        print('Incorrect password or username')
    
    return my_user_access, my_valid

def ADD_NEW_USER():
    user_list = []

    username = input('\nPlease enter username of new user: ')
    user_type = input('Please enter user type: ')

    while user_type.lower() != 'admin' and user_type.lower() != 'purchaser' and user_type.lower() != 'inventory-checker':
        print("Choose between 'Admin', 'Purchaser, 'Inventory-checker''")
        user_type = input('Please enter user type: ')

    password = input('Please enter password of new user: ')
    confirm_password = input('Please re-enter password for confirmation: ')

    while password != confirm_password: 
        print('Passwords do not match')
        password = input('Please enter password of new user: ')
        confirm_password = input('Please re-enter password for confirmation: ')
        
    en_pass = ENCRYPT_PASS(password)
    
    user_list = [username, en_pass, user_type]

    fhand = open("C:\\Users\\Taatheer\\Desktop\\userdata.txt", 'a')

    line = ''
    
    for value in user_list:
        line = line +((str(value) + ('    ')))
    line.strip()
    fhand.write(line + '\n')

    fhand.close()

    print('\nUser added!\n')

#function to validate code
def VALIDATE_CODE(new_code):

    #rejects item code that are not of type integer and not of length 5
    while len(str(new_code)) != 5 or isinstance(new_code,int) != True:
        print("Code must consists of 5 digits") 
        new_code = int(input("Please enter new code: "))

    # initialisation
    my_found = True
    while my_found == True:
        #checks if item code already exists in the file
        my_found, my_index = FIND_ITEM(new_code)

        #if it exists, the user needs to re-enter a new one
        if my_found == True:
            new_code = int(input('\nItem code already exists! Please enter another code: '))
        
    return new_code
        
def REWRITE_LIST(the_master_list):
    fhand = open('C:\\Users\\Taatheer\\Desktop\\inventory.txt', 'w')

    for value in the_master_list:
        line = '    '.join(str(list_written) for list_written in value)
        fhand.write(line)


    fhand.close()

def FIND_ITEM(search_code):
    my_master_list = []
    my_found = False
    my_index = -1

    READ_INTO_MASTERLIST(my_master_list)
    
    for count in range(0, len(my_master_list)):
        if str(search_code) == my_master_list[count][0]:
            my_found = True
            my_index = count
            break
    return my_found, my_index

def READ_INTO_MASTERLIST(the_master_list):
    fhand = open('C:\\Users\\Taatheer\\Desktop\\inventory.txt','r')

    line = fhand.readline()
    while line: 
        list_read = []
        list_read = list(map(str,line.split('    '))) 
        the_master_list.append(list_read)
        line = fhand.readline()
    
    fhand.close()
def ENCRYPT_PASS(the_password):
    all_chars = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']    
    key = ['e', 'u', '*', '-', '6', 'G', 'y', '$', 'T', 'z', 'Z', '_', '=', '@', '9', 'D', 'j', '4', 'O', 'Y', 'm', ':', '3', 'p', '2', '&', 'C', 'w', "'", 't', 'V', 'J', '%', 'l', '.', 'F', ';', '|', '^', 'f', '0', '7', 'X', '"', '?', 'K', 'I', 'M', ']', 'k', 'o', 'h', 'R', 'S', '!', 'x', 'A', 'g', ')', 'B', '1', 'c', '\\', 'E', '8', '#', 'v', '`', '/', '~', 'd', '(', '<', 'a', 'r', 'L', '}', 's', 'U', '[', 'i', ',', 'n', 'b', 'P', 'N', 'H', '5', 'W', '>', 'Q', 'q', '{', '+']

    the_enc_pass = ''
    
    for letter in the_password:
        index = all_chars.index(letter)
        the_enc_pass += key[index]

    return the_enc_pass


def DECRYPT_PASS(the_master_list, the_user_username):
    all_chars = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']    
    key = ['e', 'u', '*', '-', '6', 'G', 'y', '$', 'T', 'z', 'Z', '_', '=', '@', '9', 'D', 'j', '4', 'O', 'Y', 'm', ':', '3', 'p', '2', '&', 'C', 'w', "'", 't', 'V', 'J', '%', 'l', '.', 'F', ';', '|', '^', 'f', '0', '7', 'X', '"', '?', 'K', 'I', 'M', ']', 'k', 'o', 'h', 'R', 'S', '!', 'x', 'A', 'g', ')', 'B', '1', 'c', '\\', 'E', '8', '#', 'v', '`', '/', '~', 'd', '(', '<', 'a', 'r', 'L', '}', 's', 'U', '[', 'i', ',', 'n', 'b', 'P', 'N', 'H', '5', 'W', '>', 'Q', 'q', '{', '+']
    
    for value in range(0, len(the_master_list)):
        if the_master_list[value][0] == the_user_username:
            the_dec_pass = ''
    
            for letter in the_master_list[value][1]:
                index = key.index(letter)
                the_dec_pass += all_chars[index]
            break
    return the_dec_pass, value

#function to display inventory
def DISPLAY():
    the_master_list = []
    READ_INTO_MASTERLIST(the_master_list)

    print('''\nDisplay in in the following order:
Code    Description    Category    Unit    Price    Quantity    Minimum\n''')
    for count in range(0,len(the_master_list)):
        line = ''
        the_master_list[count].remove(the_master_list[count][7])
        for value in range(0, len(the_master_list[count])):
            line += the_master_list[count][value] + '    '
            
        line.strip()
        print(line)

        
#main program

choice = 0

while choice != -1: 
    
    user_access, valid = USER_AUTHENTICATION()
    while choice != 10:
        if valid == True:
            if user_access.lower() == 'admin':
                print('\nAccess granted: Admin\n')
                print('''Choose your action: 
                                1. Insert item
                                2. Update item
                                3. Delete item
                                4. Stock taking
                                5. View replenish list
                                6. Stock replenishment
                                7. Search item
                                8. Add new user
                                9. Display items
                                10. Logout
                                ''')
                choice = int(input('Please enter your choice: '))
                #validates choice
                while choice > 9 or choice < 1:
                    choice = int(input('Please re-enter your choice: '))         

                if choice == 1:
                    INSERT_NEW_ITEM()
                elif choice == 2: 
                    UPDATE_ITEM()
                elif choice == 3:
                    DELETE_ITEM()
                elif choice == 4:
                    STOCK_TAKING()
                elif choice == 5:
                    VIEW_REPLENISH_LIST()
                elif choice == 6:
                    STOCK_REPLENISHMENT()
                elif choice == 7:
                    SEARCH_ITEM()
                elif choice ==8:
                    ADD_NEW_USER()
                else:
                    DISPLAY()
            elif user_access.lower() == 'inventory-checker':
                print('\nAccess granted: Inventory-checker\n')
                print('''Choose your action: 
                                1. Stock taking
                                2. Search item
                                ''')
                choice = int(input('Please enter your choice: '))
                while choice > 2 or choice < 1:
                    choice = int(input('Please re-enter your choice: '))

                if choice == 1:
                    STOCK_TAKING()
                else: 
                    SEARCH_ITEM()
            elif user_access.lower() == 'purchaser':
                print('\nAccess granted: Purchaser\n')
                print('''Choose your action: 
                                1. View replenishment list
                                2. Stock replenishment
                                3. Search item
                                ''')
                choice = int(input('Please enter your choice: '))
                while choice > 3 or choice < 1:
                    choice = int(input('Please re-enter your choice: '))
                
                
                if choice == 1:
                    VIEW_REPLENISH_LIST()
                elif choice == 2:
                    STOCK_REPLENISHMENT()
                elif choice == 3:
                    SEARCH_ITEM()

            choice = int(input('\nPress 10 to log out, any other to continue: '))
            if choice == 10:
                print('\nLogging out!\n')
        else:
            print('\nAccess denied\n')
            choice = 10   
    
    choice = int(input('Enter -1 to exit, any other to continue: '))
    print('\n')
    
