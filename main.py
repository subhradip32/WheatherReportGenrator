import datetime as dt
from datetime import date


def read_csv():

    TEMP2020 = [] #contains a dictionary like [{date:(max_temp,min_temp)}]
    TEMP2021 = []

    with open("Wheather\data\Wheather_for_2020.csv") as datafile2020:
        #false read to move forward
        for i in range(1,21):
            datafile2020.readline()

        lines = datafile2020.readlines()

        for each_ent in lines :
            temp = each_ent.split(",") #list of all the datas 

            TEMP2020.append({
                str(temp[0]+"-"+temp[1]+"-"+temp[2]) : (temp[8],temp[9])
            })

    with open("Wheather\data\Wheather_for_2021.csv") as datafile2021:
        #false read to move forward
        for i in range(1,21):
            datafile2021.readline()

        lines = datafile2021.readlines()

        for each_ent in lines :
            temp = each_ent.split(",") #list of all the datas 

            TEMP2021.append({
                str(temp[0]+"-"+temp[1]+"-"+temp[2]) : (temp[8],temp[9])
            })

    return (TEMP2020,TEMP2021) #tuple containg all the data



def MaxAvg_Temp(Date,List_of_data):
    res = 0
    for entries in List_of_data:

        if Date in str(entries.keys()) and "2020" in str(entries.keys()):
            mx2020 = entries["2020-"+str(Date)][0]
            res += float(mx2020)
            
        if Date in str(entries.keys()) and "2021" in str(entries.keys()):
            mx2021 = entries["2021-"+str(Date)][0]
            res += float(mx2021)
            
    return (res)//2      


def MinAvg_Temp(Date,List_of_data):
    res = 0
    for entries in List_of_data:

        if Date in str(entries.keys()) and "2020" in str(entries.keys()):
            mn2020 = entries["2020-"+str(Date)][1]
            res += float(mn2020)
            

        if Date in str(entries.keys()) and "2021" in str(entries.keys()):
            mn2021 = entries["2021-"+str(Date)][1]
            res += float(mn2021)
            
    return (res)//2    




all_data = read_csv()

ask = input("Enter the Date to predict temparature of(T,yyyy-mm-dd): ")

todays_date = ""
max_temp = 0
min_temp = 0

if ask == "T":
    date_object = date.today() #yyyy-mm-dd
    
    todays_date = str(date_object.month) + "-"  + str(date_object.day) 

    for year in all_data:
        max_temp += MaxAvg_Temp(todays_date,year) #total of maxTemparature
        min_temp += MinAvg_Temp(todays_date,year)  #total of minTemparature
    
    #for better user experience
    todays_date = date_object

else:
    todays_date = ask 
    for year in all_data:
        max_temp += MaxAvg_Temp(todays_date,year) #total of maxTemparature
        min_temp += MinAvg_Temp(todays_date,year)  #total of minTemparature
    
    #for better user experience
    todays_date = ask 

print(f"Todays Wheather Report({todays_date}): \n\tMaximumTemp: {max_temp} \N{DEGREE SIGN}C\n\tMinimumTemp: {min_temp} \N{DEGREE SIGN}C")
