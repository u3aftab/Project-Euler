## 19)How many Sundays fell on the first of the month during the twentieth century?

year=1901
day=2 
Sunday_count=0 
while year<=2000:
    month=1
    while month<=12:
        if month==2:
            if year%4==0:
                if year%100==0:
                    if year%400==0:
                        day=day+29
                    else:
                        day=day+28
                else:
                    day=day+29
            else:
                day=day+28
        elif month==4 or month==6 or month==9 or month==11:
            day=day+30
        else:
            day=day+31
        if day%7==0:
            Sunday_count=Sunday_count+1
        month=month+1
    year=year+1
print Sunday_count        
                
    

