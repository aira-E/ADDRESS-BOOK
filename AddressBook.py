# Empty Lists
Book_Address = []
List_FN = []
List_LN = []
List_ADD = []
List_CONTACTNUM = []

# Banner
print (" -------------------- Address Book -------------------- \n")

# Calling the lists for it can use at loops
def Add_Book ():
    global Book_Address, List_FN , List_LN , List_ADD , List_CONTACTNUM

def Main_Menu (): # The user's choices input in one place
    while True:
        if len (Book_Address) <50: # So the items in the contact will limit to only 50 entry.
            #Asking user on what to do
            AskUser = int (input ("What would you like to do? \n 1. Add Contact \n 2. Edit Contact \n 3. Delete Contact \n 4. View Contacts \n 5. Search Address Book \n 6. Exit \n : "))
            if AskUser == 1:
                Add_Contact()
            elif AskUser == 2: 
                Edit_Contact()
            elif AskUser == 3: 
                Delete_Contact()
            elif AskUser == 4: 
                View_Contact ()
            elif AskUser == 5: 
                Search_Contact ()
            elif AskUser == 6: 
                break

def Add_Contact():
 #User will add a contact 
    Input_First_Name = input ("Please Fill up the following: \nFirst Name: ") #User will type the First Name
    First_Name = Input_First_Name.upper() #User input's case will convert to upper case
    List_FN.append(First_Name) #User input will add to the First Name List's Empty List
            
    Input_Last_Name = input ("Last Name: ") #User will type the Last Name
    Last_Name = Input_Last_Name.upper() #User input's case will convert to upper case
    List_LN.append(Last_Name) #User input will add to the Last Name List's Empty List
            

    Input_Address = input ("Address: ") #User will type the Address
    Address = Input_Address.upper () #User input's case will convert to upper case
    List_ADD.append(Address) #User input will add to the Address List's Empty List
            

    Contact_Num = (input("Contact Number: ")) #User will type the Address
    List_CONTACTNUM.append(Contact_Num) #User input will add to the Contact Number's Empty List
            

    Book_Address.append([First_Name] + [Last_Name] + [Address] + [Contact_Num]) #All the Sublist will add to the Mainlist
    
def Edit_Contact ():
    Edit = int (input ("Edit Contact. Enter what you wish to do: \n 1. Change Item in the Contact \n 2. Sort Contacts \n 3. Reverse the order of the Contacts \n : "))

    if Edit == 1: #User will Change an item on the contact
        Change = int (input ("Change Item. Enter what item you wish to change: \n 1. First Name \n 2. Last Name \n 3. Address \n 4. Contact Number \n: ")) 
                
        if Change == 1: #User will Change firstname on the contact
            Ask_User_Change_FN = input (f"this is the list of First Names: {List_FN} type what you want to change: ") #User will pick firstname to change
            Change_FN = Ask_User_Change_FN.upper() #User input's case will convert to upper case
            if Change_FN in List_FN: #Checking if the User input is present on the list
                Input_Replacement = input (f"from {Change_FN} change it into: ") #User will pick a replacement for the firstname
                Replacement = Input_Replacement.upper() #User input's case will convert to upper case
                New_Var = List_FN.index(Change_FN) #Program will identify the user input variable's index
                List_FN[New_Var] = Replacement #Program will replace the old variable into user's new variable
                print (f"{Change_FN} replaced ! Here is the updated contacts:  \n {List_FN}") #Program will inform the user for the updated contact
            else:
                print (F"{Change_FN} is not in this list, please try a different keyword or in different list.") #If user's input is not present on the list

        elif Change == 2:
            Ask_User_Change_LN = input (f"this is the list of Last Names: {List_LN} type what you want to change: ")
            Change_LN = Ask_User_Change_LN.upper()
            if Change_LN in List_LN:
                Input_Replacement_LN = input (f"from {Change_LN} change it into: ")
                Replacement_LN = Input_Replacement_LN.upper()
                New_Var_LN = List_LN.index(Change_LN)
                List_LN[New_Var_LN] = Replacement_LN
                print (f"{Change_LN} replaced ! Here is the updated contacts:  \n {List_LN}")
            else:
                print (F"{Change_LN} is not in this list, please try a different keyword or in different list.")                

        elif Change == 3:
            Ask_User_Change_ADD = input (f"this is the list of Addresses: {List_ADD} type what you want to change: ")
            Change_ADD = Ask_User_Change_ADD.upper()
            if Change_ADD in List_ADD:
                Input_Replacement_ADD = input (f"from {Change_ADD} change it into: ")
                Replacement_ADD = Input_Replacement_ADD.upper()
                New_Var_ADD = List_ADD.index(Change_ADD)
                List_ADD[New_Var_ADD] = Replacement_ADD
                print (f"{Change_ADD} replaced ! Here is the updated contacts:  \n {List_ADD}")
            else:
                print (F"{Change_ADD} is not in this list, please try a different keyword or in different list.")           

        elif Change == 4:
            Ask_User_Change_NUM = input (f"this is the list of Contact Numbers: {List_CONTACTNUM} type what you want to change: ")
            Change_NUM = Ask_User_Change_NUM.upper()
            if Change_NUM in List_CONTACTNUM:
                Replacement_NUM = input (f"from {Change_NUM} change it into: ")
                #Replacement_NUM = Input_Replacement_NUM.upper()
                New_Var_NUM = List_CONTACTNUM.index(Change_NUM)
                List_CONTACTNUM[New_Var_NUM] = Replacement_NUM
                print (f"{Change_NUM} replaced ! Here is the updated contacts:  \n {List_CONTACTNUM}")
            else:
                print (F"{Change_NUM} is not in this list, please try a different keyword or in different list.")       

    if Edit == 2: #User will sort the items on the contact
        List_FN.sort()
        List_LN.sort()
        List_ADD.sort()
        List_CONTACTNUM.sort()
        print (f"Sorted! Here is the updated contacts: \n {List_FN}, \n {List_LN}, \n {List_ADD}, \n {List_CONTACTNUM}")
       
    if Edit == 3: #User will reverse the items on the contact
        List_FN.reverse()
        List_LN.reverse()
        List_ADD.reverse()
        List_CONTACTNUM.reverse()
        print (f"Reversed! Here is the updated contacts: \n {List_FN}, \n {List_LN}, \n {List_ADD}, \n {List_CONTACTNUM}")

def Delete_Contact ():
    #User will delete a contact 
    Ask_User_Delete = input ("Delete. Enter what you wish to delete: ") #User will input what contact to delete 
    Delete = Ask_User_Delete.upper()  #User input's case will convert to upper case
    Checker = (any(Delete in inner_list for inner_list in Book_Address)) #Program will check if user input is present in the Mainlist
    if Checker == True: #Program checked ! User's input is present in the Mainlist
        YesOrNo = input (f"Are you sure ? You want to delete {Delete} Type Y if Yes and N if No: ") #Program will ask the user if he/she is sure
        if YesOrNo == "y" or YesOrNo == "Y": #User said yes
            Deleted = [[g for g in sub_list if g!= Delete]for sub_list in Book_Address] #Program will delete the element 
            print (f"{Delete} is Deleted! Here is the updated contacts: {Deleted}") #Program will inform the user for the updated contact
        elif YesOrNo == "n" or YesOrNo == "N": #User said no
            print (f"{Delete} was not deleted.") #Program will inform the user that the element was not deleted
        else:
            print("Error. Please enter a valid letter.")
    else:#Program checked ! User's input is not present in the Mainlist
        print (f"Sorry! {Delete} is not in the list, please try a different keyword.") #Program will inform the user that the element was not on the list.

def View_Contact (): 
    #User will input what contact to view 
    Input_View = int (input ("View Contacts. What list do you wish to see? \n 1. First Names \n 2. Last Names \n 3. Addresses \n 4. Contact Numbers \n 5. All \n: ")) 
    if Input_View == 1: #User want to view the First Name List
        print (f"Here is the list of all the First Names: \n{List_FN}") #Program will prompt the List of First Names
    if Input_View == 2: #User want to view the Last Name List
        print (f"Here is the list of all the Last Names: \n{List_LN}") #Program will prompt the List of Last Names
    if Input_View == 3: #User want to view the Address List
        print (f"Here is the list of all the Addresses: \n{List_ADD}") #Program will prompt the List of Address
    if Input_View == 4: #User want to view the Contact List
        print (f"Here is the list of all the Contact Numbers: \n{List_CONTACTNUM}") #Program will prompt the List of Contact Numbers
    if Input_View == 5: #User want to view the All List
        print ("Here is the list of all the contacts:") 
        for k in List_FN, List_LN, List_ADD, List_CONTACTNUM:
            print (k) #Program will prompt the List of all the lists

def Search_Contact ():
    #User will input what contact to search
    User_Input_Search = int (input ("Search in the Address Book. What are you looking for? \n 1. First Name \n 2. Last Name \n 3. Address \n 4. Contact Number \n 5. All \n:  "))
    
    if  User_Input_Search == 1: #User want to search through First Name List
        User_Search_FN = input ("Search via First Names. What are you looking for?: ") #Program will ask for what the user is searching for
        Search_FN = User_Search_FN.upper () #User input's case will convert to upper case
        if Search_FN in List_FN:  #Program will check if user input is present in the sasid list
            print (f"{Search_FN} is in the Address Book.") #Program checked ! User's input is present in said list
        else:
            print (f"Sorry. {Search_FN} is not in the Address Book") #Program checked ! User's input is not present in said list
            
    elif User_Input_Search == 2:
        User_Search_LN = input ("Search via Last Names. What are you looking for?: ")
        Search_LN = User_Search_LN.upper ()
        if Search_LN in List_LN:
            print (f"{Search_LN} is in the Address Book.")
        else:
            print (f"Sorry. {Search_LN} is not in the Address Book")    

    elif User_Input_Search == 3:
        User_Search_ADD = input ("Search via Address. What are you looking for?: ")
        Search_ADD = User_Search_ADD.upper ()
        if Search_ADD in List_ADD:
            print (f"{Search_ADD} is in the Address Book.")
        else:
            print (f"Sorry. {Search_ADD} is not in the Address Book")    

    elif User_Input_Search == 4:
        Search_NUM = input ("Search via Contact Number. What are you looking for?: ")
        if Search_NUM in List_CONTACTNUM:
            print (f"{Search_NUM} is in the Address Book.")
        else:
            print (f"Sorry. {Search_NUM} is not in the Address Book")    

    elif User_Input_Search == 5:
        Ask_User_Search = input ("Search in the Address Book. What are you looking for? ")
        Search = Ask_User_Search.upper()
        Search_Checker = (any(Search in inner_list for inner_list in Book_Address))
        if Search_Checker == True:
            print (f"{Search} is in the Address Book.")
        else:
            print (f"Sorry. {Search} is not in the Address Book")        

Main_Menu() #For the program to run