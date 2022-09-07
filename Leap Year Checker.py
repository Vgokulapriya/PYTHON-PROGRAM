# Leap Year Checker

def Is_Leap_Year(Year):
    if Year % 4 == 0:
        if Year % 100 == 0:
            if Year % 400 == 0:
                print("Leap Year")
            else:
                print("Not Leap Year")
        else:
         print("Leap Year")                
    else:     
        print("Not Leap Year")

Is_Leap_Year(2004)