"""
Title: Fiscal Calendar
Author: Cameron Schweeder
Summary: Creates a importable csv file that will input fiscal week with quarter markers
Time: 2H 45M
"""
from datetime import datetime
from datetime import timedelta

def datetimeInput(startDate):
    """
    Input: STR : Date in format YYYY/MM/DD
    Output: datetime : converted date to datetime and run through calculateweek()
    """
    day = datetime.strptime(startDate, "%Y/%m/%d").date()
    calculateWeek(day)

def calculateWeek(startdate):
    """
    Input: datetime : The start date from datetimeInput()
    output: CSV : file with headers formatted to import to calendars.
    Takes the first day, and calculates the full week, appends the fiscal week# and Quarter # and writes it to a CSV file.
    """
    f = open("fiscal-calendar.csv", 'a')
    # Create headers for CSV
    f.write("subject,start date,end date\n")
    
    fiscalWeek = 0

    for i in range(52):
        fiscalWeek +=1
        # Define Quarters
        if fiscalWeek < 13:
            quarter = "Q1"
        elif fiscalWeek < 26:
            quarter = "Q2"
        elif fiscalWeek < 39:
            quarter = "Q3"
        else:
            quarter = "Q4"
        
        monday = startdate
        sunday = monday + timedelta(days=6)

        # Write the week into csv
        f.write("FW" + str(fiscalWeek)+ " " + str(quarter) +","+ str(monday)+","+ str(sunday + timedelta(days=1))+ "\n")

        # Change start date to the next monday
        startdate = sunday + timedelta(days=1)

        i +=1

    f.close
    return

def showCalendar(calendar):
    return


startDate = str(input("What is the first day[YYYY/MM/DD]"))
datetimeInput(startDate)
