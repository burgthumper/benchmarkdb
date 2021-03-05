# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import create_inserts
import tsload
import tsload_exec_many


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

x = True
while x==True:
    badInput = False
    print("Operations:")
    print("1: insert CPU (timeseries) data in support database")
    #print("3: ExecMany insert CPU (timeseries) data in support database")
    print("2: create sql inserts for benchmark databases")
    print("0: EXIT")
    print("Select Operation (enter integer):")
    try:
        value = int(input())
        print("value = ")
        print(value)
        if 0 <= value <= 2:
            x=False
        else:
            badInput = True
    except:
        badInput = True
    if(badInput == True):
        print('Please select an integer value between 0-2\n')



if(value==1):
    print_hi('Zippy')
    tsload.HelloWorld()
    tsload.insertCPUValues()

if(value==3):
    print_hi('Zippy3')
    #tsload.HelloWorld()
    tsload_exec_many.insertCPUValues()


tables = 'both'
#coupon_issued
#coupon_transaction
#both
dbs = ['pg']
#pg
#ts
#mysql
max_lines = 250000
#1 ~ debugging
#250000 ~ initial (small) tests
#9999999 ~ full tests

if(value==2):
    create_inserts.create_inserts(tables, dbs, max_lines)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
