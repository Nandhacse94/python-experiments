# place your account statement in this path and run this program
# please make sure that this program support your statement, 
# else modify format_data func def

import matplotlib.pyplot as plt
from datetime import datetime 
import csv

# pass a formatted list of lists 
# store into csv file 
def store_data(data_dict):
    f = open("acc_db.csv","w",newline="")
    obj = csv.writer(f)

    for i in data_dict:
        currdata = [i,data_dict[i][0],data_dict[i][1],data_dict[i][2]]
        obj.writerow(currdata)
    f.close()

# convert given csv format to easy csv format 
# easy csv format will be used for graph
def format_data():
    f = open("AccountTrans.csv","r")
    data = list(csv.reader(f))
    data_dict = {} 

    for curr_row in reversed(data):
        if len(curr_row) == 6 and curr_row[0].strip() != 'Date':
            credit = curr_row[3]
            debit = curr_row[4]
            date = datetime.strptime(curr_row[0].strip(), '%d/%m/%Y') # converting from string to date type
            fmtDate = date.strftime("%b %d") # converting date to string type in format "Month date"
            data_dict[curr_row[1]] = [fmtDate,credit,debit]
    
    store_data(data_dict) # to store into csv file as list
    f.close()

def show_graph():
    f = open("acc_db.csv","r")
    data = list(csv.reader(f))
    date = []
    details = []
    credit_history = [] 
    debit_history = []

    for index in data:
        details.append(index[0])
        date.append(index[1])
        if index[2] == '':
            credit_history.append(0)
        else:
            credit_history.append(float(index[2].replace(',','')))
        if index[3] == '':
            debit_history.append(0)
        else:
            debit_history.append(float(index[3].replace(',','')))
        
    print(date,end="\n\n") 
    print(credit_history,end="\n\n") 
    print(debit_history,end="\n\n")

    ## need to write code to show graph properly
    fig = plt.figure()
    #plot = fig.add_subplot(111)

    plt.bar(date,debit_history)
    #plt.bar(date,credit_history)
    plt.ylabel("Expenses")
    plt.xlabel("Date")

    fig.canvas.mpl_connect('motion_notify_event', on_plot_hover)           
    plt.show()
    f.close()

def on_plot_hover(event):
    print(event.inaxes,event.xdata,sep="\n")

format_data()
show_graph()

#if you want to show graph in website
#uncomment below code and implement
# import mpld3
# from mpld3._server import serve 
#implementation of mpld3 example 
# x = [1,2,3]
# y = [2,3,4]
# fig1 = plt.figure()
# plt.bar(x,y, label = 'label for bar', color = 'b')
# # create html for both graphs 
# html1 = mpld3.fig_to_html(fig1)
# serve(html1)
