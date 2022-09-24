from asyncore import read
from optparse import Values
from operations import   str_check,mail_check,pass_check,date_check,mobile_check
import time
def reg_menu():
    print("----------------welcome to our site------------------")
    first_name=str_check("enter Your First name: ")
    sec_name=str_check("Enter Your secound name: ")
    mail=mail_check("please Enter your email: ")
    password=pass_check("please Enter your password: ")
    phone=mobile_check("enter your phone: ")
    print(phone)        
    return [first_name,sec_name,mail,password,phone]

#############################################
def main_menu():
    ch=input("1)for regeister\n2)for login\nenter your choice: ")
    if ch=="1":
        create_user()
    if ch=="2":
        login()
    else:
        print("please enter a number from the list")
        main_menu()
####################
def login():
    global mail_in
    global nam
    mail_in=input("please Enter Your mail: ")
    pas=input("enter Your password: ")
    with open('users.txt') as file:
        for line in file:
            values = line.split(":")
            if values[2]== mail_in and values[3]==pas :
                nam=values[0]
                project_menu(nam)
                break
                 
            else:
                continue
        else:
            print("error")
            login()
    ####################################################################################
def project_menu(nam):
    print(f"welcome {nam}")
    cho=input("1)to add new project\n2)to view all projects\n3)edit y projects\n4)delete your projects\n5)search by date\nenter your choice: ")
    if cho=="1":
        print("yes")
        create_project()

    elif cho=="2":
        view_all()
    elif cho=="3":
        edit_project()
    elif cho=="4":
        delete_project()
    elif cho=="5":
        searchbydate()

#####################################
def view_all():
    with open('projects.txt') as file:
        for line in file:
            values = line.split(":")
            print(values[1],values[2])
    project_menu(nam) 

def new_project():
    print("----------------welcome to our site------------------")
    id = str(round(time.time()))
    tit=str_check("enter Project Title:  ")
    details=str_check("Enter Project Details: ")
    target=input("please Enter your target: ")
    str_date=date_check("enter Your Start date: ")
    end_date=date_check("enter Your End date: ")
    return [id,tit,details,target,str_date,end_date]
#######################################################################################################
def create_user():
    details=reg_menu()
    print(details)
    details=":".join(details)
    print(details)
    try:
        f=open("users.txt","a")
    except:
        print("issue while creating user")
        return False

    else:
        f.write(f"{details}\n")
        f.close()
    main_menu()
###############################################################################
def create_project():
    details=new_project()
    details.insert(0,mail_in)
    print(details)
    details=":".join(details)
    print(details)
    try:
        f=open("projects.txt","a")
    except:
        print("issue while creating user")
        return False

    else:
        f.write(f"{details}\n")
        f.close()
    project_menu(nam)
###############################################
def write_book_list_to_the_file(projlist):
    try:
        file = open("projects.txt", "w")
    except Exception as e:
        print(e)
        return False
    else:
        file.writelines(projlist)
        file.close()
        return True

def delete_project():
    file=open('projects.txt')
    projects= file.readlines()
    file.close()
    pro_id = input("please choose id of the project you want to delete: ")

    #print(projects)
    for line in projects:
        values=line.strip("\n")
        values = values.split(":")
        if values[0] == mail_in and values[1]== str(pro_id):
            proj_idx=projects.index(line)
                # print(proj_idx) 
            del projects[proj_idx]
            deleted=write_book_list_to_the_file(projects)
            if deleted:
                print("---- project deleted successfully ---- ")
                #return True
                project_menu(nam)

    print("project not found ")
    #return False
    project_menu(nam)

# def delete_project():
#     with open('projects.txt') as file:
#         projects= file.readlines()
#         for line in projects:
#             values=line.strip("\n")
#             values = values.split(":")
#             if values[0] == mail_in:
#                 #print(line)
#                 proj_idx=projects.index(line)
#                 # print(proj_idx) 
#                 print(projects[proj_idx])

#                 de=input("do you want to delete This project (Y):")
#                 if de=="Y" or de=="y":
#                     del projects[proj_idx] 
#                     print("successfully deleted")
#                     continue
#                 #     # file.writelines(projects)
#                 # elif de=="N" or de=="n":
#                 #     continue
#                 # else:
#                 #     continue
#                 # delet_check(projects[proj_idx])
#     deleted=write_book_list_to_the_file(projects)
    


 
def delet_check(line):
    de=input("do you want to delete This project (Y):")
    if de=="Y" or de=="y":
        del line 
        print("successfully deleted")
        # file.writelines(projects)
                
    # elif de=="N" or de=="n":

def searchbydate():
    choice= input("1-search by start date, \n2-list end date \n") 
    if choice =="1":
        indate=date_check('Please enter start date you want to search by: ')
    elif choice =="2":
        enddate=date_check('Please enter end date you want to search by: ')
    else:
        print('wrong input')
        return False
    with open('projects.txt') as file:    
        projects=file.readlines()
        for pro in projects:
            Values = pro.strip("\n")
            Values = Values.split(":")
            if choice== "1":
                if Values[5]==indate:
                    print(Values,'\n')
            elif choice=="2":
                if Values[6]==enddate:
                    print(Values,'\n')



##########################################33
def edit_project():
    file=open('projects.txt')
    projects= file.readlines()
    file.close()
    pro_id = input("please choose id of the project you want to delete: ")
    for line in projects:
        values=line.strip("\n")
        values = values.split(":")
        if values[0] == "omarkorety@hotmail.com" and values[1]== str(pro_id):
            proj_idx=projects.index(line)
            del projects[proj_idx]
            deleted=write_book_list_to_the_file(projects)
    print("enter new data")
            # tit=str_check("enter Project Title:  ")
            # details=str_check("Enter Project Details: ")
            # target=input("please Enter your target: ")
            # str_date=date_check("enter Your Start date: ")
            # end_date=date_check("enter Your End date: ")
    details= new_project()
    details.insert(0,mail_in)
    print(details)
    details=":".join(details)
    print(details)
    try:
        f=open("projects.txt","a")
    except:
        print("issue while creating user")
        return False

    else:
        f.write(f"{details}\n")
        f.close()
    project_menu(nam)


main_menu()
# with open('users.txt') as topo_file:
#     for line in topo_file:
#         values = line.split(":")
#         print(values)
