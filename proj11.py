#project 11 is a program that creates a calendar of events and contains two self made classes and numerous functions.
#the program prompts the user for one of four options. Delete event, add event, list of events on a given day or quit



from p11_calendar import P11_Calendar
from p11_event import P11_Event


CAL_TYPE = ['meeting','event','appointment','other']

MENU = '''Welcome to your own personal calender.
  Available options:
    (A)dd an event to calender
    (D)elete an event
    (L)ist the events of a particular date
    (Q)uit'''


    
def check_time(time,duration): #checks if time and duration are valid
    too_early = 360   #6am too  early in minutes
    too_late = 1020#5pm  or later is too late (also in minutes) 
    if len(time)==4: #if hour has just one index
        start = int(time[0])*60+int(time[2:]) #initalize start time
    if len(time)==5:#if hour has 2 indexes
        start = int(time[0:2])*60+int(time[3:]) #initalize start time
    if len(time) !=4 and len(time) !=5:
        return False #if time structure is invalid
    if type(duration) != int: #if duration isnt a number. Error
        return False
    if duration<=0: #duration must be positive int
        return False
    
    
    end = start+duration  #end time is start plus duration
    if start<too_early or start>too_late: #if event starts before 6am or 5pm
        return False
    if end<too_early or end>too_late:#if event ends before 6am or 5pm
        return False
    else:
        return True
    
def event_prompt():
    done = False #creates while loop 
    while done == False:
        date = input("Enter a date (mm/dd/yyyy): ") #date prompt
        time = input("Enter a start time (hh:mm): ")#time prompt
        duration = int(input("Enter the duration in minutes (int): "))#duration prompt
        cal_type = input("Enter event type ['meeting','event','appointment','other']: ")#calendar type prompt
            
        if check_time(time,duration) == False: #check validity of time and duration
            print("Invalid event. Please try again.") #if false print error statement
            continue #reprompt
            

    
        e = P11_Event(date,time,duration,cal_type) #turn variables into an event
        if getattr(e, 'valid') == True: #if event is valid
            done = True #end loop and return value
        if getattr(e, 'valid') == False:#if event is not valid
            print("Invalid event. Please try again.") #if false print error statement
            continue #reprompt
        
    return e #return event
        
        
        
        


    
                
def main():
    calendar = P11_Calendar() #name calendar
    print(MENU) #print menu options
    option = input("Select an option: ").lower() #prompt for option
    
    while option == 'q' or option == 'a' or option == 'd' or option == 'l': #while loop with valid options
        
        if option == 'a': #a to add event
            e =  event_prompt() #prompt for event information and valid check variables
            print('Add Event') #header
            added_event = calendar.add_event(e) #add event to events list this returns valid (true or valse)
            if added_event == True: #if event is valid to be added
                print("Event successfully added.") #success statement
                print(MENU) #print menu options
                option = input("Select an option: ").lower()#prompt for new option
            if added_event == False:#if event is not valid to be added
                print("Event was not added.")#error statement
                print(MENU)#print menu options
                option = input("Select an option: ").lower()#prompt for new option
        
        if option == 'd': #if option is to delete event
            print("Delete Event")#header
            date = input("Enter a date (mm/dd/yyyy): ")#date prompt
            time = input("Enter a start time (hh:mm): ")#time prompt
            del_event = calendar.delete_event(date, time) #call delete event function from calendar check for valid
            if del_event != False: #if event is valid to be deleted
                print("Event successfully deleted.")#success statement
                print(MENU)#print menu options
                option = input("Select an option: ").lower()#prompt for new option
            if del_event == False:#if event is not valid to be deleted
                print("Event was not deleted.")#error statement
                print(MENU)#print menu options
                option = input("Select an option: ").lower()#prompt for new option
            
        
        if option == 'l': #if option is to see list for the day
            print("List Events")#header
            date = input("Enter a date (mm/dd/yyyy): ")#date prompt
            cal_events = calendar.day_schedule(date) #call function to return sorted list of events for the day
            if cal_events == []: #if day is empty
                print("No events to list on ",date) #print empty statement
                print(MENU)#print menu options
                option = input("Select an option: ").lower()#prompt for new option
            if cal_events != []:#if day is not empty
                for value in cal_events: #print each event for the day
                    print(value)
                    
                print(MENU)#print menu options
                option = input("Select an option: ").lower()#prompt for new option

            
                
        if option == 'q': #q to quit
            exit()
                

    
    
if __name__ == '__main__':
     main()