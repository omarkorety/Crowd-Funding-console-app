from itertools import count


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
    with open('projects.txt') as file:
        projects= file.readlines()
        temp=projects
        #for ind,line in enumerate(projects):
        cou=0
        while cou <len(projects):
            #print(line)
            # print(ind,line)
            # omar=line
            # print(omar)
            values=projects[cou].strip("\n")
            values = values.split(":")
            if values[0] == "omarkorety@hotmail.com":
                #print(line)
                #proj_idx=projects.index(line)
                # print(proj_idx) 
                # print(projects[proj_idx])
                print(projects[cou])


                de=input("do you want to delete This project (Y):")
                if de=="Y" or de=="y":
                    del projects[cou]
                    #ind=ind-1 
                    continue

                    
                    #del line 
                    print("successfully deleted")
                    #print("before continue"+line)
                cou =cou+1
                    
    #             #     # file.writelines(projects)
    #             # elif de=="N" or de=="n":
    #             #     continue
    #             # else:
    #             #     continue
    #             # delet_check(projects[proj_idx])
    deleted=write_book_list_to_the_file(projects)
delete_project()