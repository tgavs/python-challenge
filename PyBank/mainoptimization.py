# PyBank Solution

import os
import csv

months=[]
profit_losses=[]
index=[]
shift=[]
change=[]

i=0


rd_path= os.path.join('Resources','budget_data.csv')

with open(rd_path) as raw_data:

    reader=csv.reader(raw_data)

    header=next(reader)
    
    for row in reader:

        date=row[0]
        pl=float(row[1])
        months.append(date)

        profit_losses.append(pl)
        index.append(i)    
        i+=1

    shift.append(0)

    for j in range(0,len(profit_losses)-1):

        shift.append(profit_losses[j])    

    for i in index:

        change.append(profit_losses[i]-shift[i])

    change[0]=0
    
    totalmonths= len(months)
    totalp_l = sum(profit_losses)
    av_change= sum(change)/(len(change)-1)
    maxlist_value= max(change)
    maxlist_date=months[change.index(max(change))]
    minlist_value=min(change)
    minlist_date=months[change.index(min(change))]

    print('Financial Analysis')

    print('-------------------------------------')

    print(f'Total Months:  {totalmonths}')
    print(f'Total:  ${totalp_l:,.2f}')
    print(f'Average Change:  ${av_change:,.2f}')
    print(f'Greatest Increase in Profits: {maxlist_date }  ${maxlist_value:,.2f}')
    print(f'Greatest Decrease in Profits: {minlist_date }  ${minlist_value:,.2f}')










