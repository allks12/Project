import os,pickle

def Calories(questions):
    cal = input(questions)
    if cal.isdigit():
        cal = int(cal)
        if cal > 0 and cal < 50000:
            return cal
        else:
            print("Error, enter again")
            return Calories(questions)
    else:
        print("Error, enter again")
        return Calories(questions)

def getAweek():
    
    print("Please enter your calories for the last 7 days")
     
    week = []
    for i in range(7):
        day = Calories(questions = "Day " + str(i+1) + ":")
        week.append(day)

    total = sum(week)
    average = int(total / 7)

    print("\n\nYour total calories:", total)
    print("\nYour average calories:", average)

    if total > 21000:
        print("\nYou are eating too many calories. You will get fat!")
    elif total < 9000:
        print("\nYou are eating too few calories. You will become anorexic!")
    input("Press enter to continue") 
    return week

def main():
    
    print("/////////   This is the calorie counter   \\\\\\\\\\\n\n")
    print("Num\tMon   \tTues  \tWeds  \tThurs  \tFri   \tSat   \tSun   \tAvg   \tTot   ")
    count = 1
    for week in month:
        if len(week) == 7:
            print(count, end="\t")
            for day in week:
                print(day,end="\t")
            print(int(sum(week)/7),end="\t")
            print(sum(week),end="\n")
        else:
            print("")
        count = count + 1
    

    numWeek = int(input("\n\nPick week 1,2,3 or 4: "))
    if numWeek> 4:
        print("Error, enter again")
        numWeek= int(input("\n\nPick week 1,2,3 or 4: "))
        
    month[numWeek-1] = getAweek()
    pickle.dump( month, open( "data.p", "wb" ) )


    main() 


try:
    month = pickle.load( open( "data.p", "rb" ) ) 
except:
    month = [[],[],[],[]] 


main()