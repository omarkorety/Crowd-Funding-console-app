import re
import datetime

def str_check(msg): #check string conditions
    mystr=input(msg)
    if mystr.isspace() or not mystr or mystr.isdigit():
        print("please enter suitable name")
        return str_check(msg)
    return mystr
    ###########################################################################
def pass_check(msg): #check password and its confermation
    spec_char=["@","!","#","$","%","^","&","*","(",")","_","+","=","|","/","-"]
    pas=input(msg)
    pass_conf=input(msg+" Again:")
    if len(pas)<8:
        print("password should be al least 8 char")
        return pass_check(msg)
    elif not any(char in spec_char for char in pas):

        print("password should has a special char")
        return pass_check(msg)
    elif pass_conf != pas:
        print("the password doesn't identical Try Again")
        return pass_check(msg)
    return pas
    
    
def mobile_check(msg):
    num=input(msg)
    # if digit_Check(num):
    #     return num
    # else:
    #     return mobile_check(num)
    regex = r"^01[0125][0-9]{8}$"
    if re.fullmatch(regex,num):
        return num
    else:
        print("enter correct moblie phone")
        return mobile_check(msg)
######################################################################
# def digit_Check(num):
#     if  num.isdigit():

#         return num
#     else:
#         print("please enter suitable name")
#         return digit_Check(num)
def digit_check(msg):
    num = input(msg)
    try:
        num = int(num)
    except:
        print("---- please provide number not a string ---- ")
        return digit_check(msg)
    else:
        return num

    #################################################3333
def mail_check(msg):
    mail=input(msg).strip().lower()
    if not "@" in mail:
        print("invalid email")
        return mail_check(msg)
    elif not mail[-4:] in ".com.org.edu.gov.net":
        print("invalid email")
        return mail_check(msg)

    with open('users.txt') as file:
        for line in file:
            values = line.split(":")
            if values[2]==mail:
                print("this mail alrady exist!!")
                return mail_check(msg)
    return mail
    ##############################################
def date_check(msg):
    date_text=input(msg)
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except:
        print("Incorrect data format, should be YYYY-MM-DD")
        return date_check(msg)
    else:
        return date_text

