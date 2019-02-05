import sys
reload(sys)
sys.setdefaultencoding('utf8')
import os
from clint.textui import colored, puts
import requests
import bs4




def head():
    clear()
    #printing the header of program
    Gsoc_banner = r"""
       ____ ____   ___   ____   ____                                       
      / ___/ ___| / _ \ / ___| / ___|  ___ _ __ __ _ _ __  _ __   ___ _ __ 
     | |  _\___ \| | | | |     \___ \ / __| '__/ _` | '_ \| '_ \ / _ \ '__|
     | |_| |___) | |_| | |___   ___) | (__| | | (_| | |_) | |_) |  __/ |   
      \____|____/ \___/ \____| |____/ \___|_|  \__,_| .__/| .__/ \___|_|   
                                                    |_|   |_|           
    _--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--_--
                                                    --By Narender Singh
    """
    puts(colored.yellow(Gsoc_banner))
    
def clear():
    # for removing the clutter from the screen when necessary
    os.system('cls' if os.name == 'nt' else 'clear')
    
def choice():
    print("Enter Your Choice :: ::  ")
    x = int(input())
    if x==1:
        GSoctwo()
    elif x==2:
        GSocThree()
    else:
        print("Wrong Input \\ Try Again ")
        choice()
    
def menu():
    #menu of program
    print(" 1 -- To compare common organisations b/w 2 years ")
    print(" 2 -- To compare common organisations b/w 3 years \n")
    print("Years Supported 2016,2017,2018  \n\n")
    choice()
    
def GSoctwo():
    """ to compare b/w 2 years """
    y1 = int(input("Enter Year 1 :: "))
    y2 = int(input("Enter Year 1 :: "))
    
    if(y1>2018 or y1<2016 or y2>2018 or y2<2016):
        print("Wrong Input Try Again \n\n")
        GSoctwo()
    
    print("Loding.........\n\n")

    
    u1 = requests.get('https://summerofcode.withgoogle.com/archive/' + str(y1) + '/organizations/')
    u2 = requests.get('https://summerofcode.withgoogle.com/archive/' + str(y2) + '/organizations/')
    
    u1 = requests.get('https://summerofcode.withgoogle.com/archive/' + str(y1) + '/organizations/')
    u2 = requests.get('https://summerofcode.withgoogle.com/archive/' + str(y2) + '/organizations/')

    s1 = bs4.BeautifulSoup(u1.text , 'lxml')
    s2 = bs4.BeautifulSoup(u2.text , 'lxml')
    #print(type(soup))
    l1 = s1.select('.organization-card__name')
    l2 = s2.select('.organization-card__name')

    print("\n\n  ____________________________ Organisations ____________________________ \n\n")

    cnt  = 1
    for data1 in l1:
        str1 = str(data1.getText())
        for data2 in l2:
            str2 = str(data2.getText())
            if str1==str2:
                print(str(cnt) + "  -  " + str1) 
                cnt += 1
    
    print("\n\n  _______________________________________________________________________")

    
    
def GSocThree():
    """ to compare b/w 2 years """
    y1 = int(input("Enter Year 1 :: "))
    y2 = int(input("Enter Year 2 :: "))
    y3 = int(input("Enter Year 3 :: "))
    
    if(y1>2018 or y1<2016 or y2>2018 or y2<2016 or y3>2018 or y3<2016):
        print("Wrong Input Try Again \n\n")
        GSocThree()
        
    print("Loding.........\n\n")
    
    u1 = requests.get('https://summerofcode.withgoogle.com/archive/' + str(y1) + '/organizations/')
    u2 = requests.get('https://summerofcode.withgoogle.com/archive/' + str(y2) + '/organizations/')
    u3 = requests.get('https://summerofcode.withgoogle.com/archive/' + str(y3) + '/organizations/')

    s1 = bs4.BeautifulSoup(u1.text , 'lxml')
    s2 = bs4.BeautifulSoup(u2.text , 'lxml')
    s3 = bs4.BeautifulSoup(u3.text , 'lxml')
    #print(type(soup))
    l1 = s1.select('.organization-card__name')
    l2 = s2.select('.organization-card__name')
    l3 = s3.select('.organization-card__name')
    
    print("\n\n  ____________________________ Organisations ____________________________ \n\n")
    cnt = 1;
    for data1 in l1:
        str1 = str(data1.getText())
        for data2 in l2:
            str2 = str(data2.getText())
            if str1==str2:
                for data3 in l3:
                    str3 = str(data3.getText())
                    if str2==str3 and str1==str3:
                        #file.write(s1)
                        #file.write("\n")
                        print(str(cnt) + "  -  " + str1) 
                        cnt += 1
    print("\n\n  _______________________________________________________________________")

                    


    
head()
menu()

