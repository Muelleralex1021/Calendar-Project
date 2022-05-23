from p11_event import P11_Event

class P11_Calendar():
    event_list = [] #initialize list for events
    conflict_list = []#initialize list for time conflicts
    def __init__(self):
        pass
        
    def add_event(self,e):
        count = 0 #initalize times through for loop
        dates_list = [] #adds different dates that are trying to be added to events list just as dates
        new_date = getattr(e, 'date') #get date of input
        start, end = P11_Event.get_time_range(e) #call prev function to get start and end time
        for value in P11_Calendar.event_list:
            dates_list.append(getattr(value, 'date')) #append dates
            
        if new_date not in dates_list:
            P11_Calendar.conflict_list.append((start,end))
            P11_Calendar.event_list.append(e)
            return True #if date is not yet in list then return true
            
        if P11_Calendar.conflict_list != []: #if list is not empty
            for value in P11_Calendar.conflict_list:
                if start>value[0] and start<value[1]: #if start time is between other times return False
                    return False
                if end>value[0] and end<value[1]:#if end time is between other times return False
                    return False
                else:
                    count += 1 #count for appending
                    
            
        if count == len(P11_Calendar.conflict_list): #if we reach end of list and there are no conflicts
            P11_Calendar.conflict_list.append((start,end)) #append to conflicts
            P11_Calendar.event_list.append(e)#append to events
            return True
            
        if P11_Calendar.conflict_list == []: #if list is empty any event can be added
            P11_Calendar.conflict_list.append((start,end))
            P11_Calendar.event_list.append(e)

  
        
    
    def delete_event(self,date,time):
        ind=-1 #index initialize
        for value in P11_Calendar.event_list: #iterate through event list
            v_date = P11_Event.get_date(value) #get current date 
            v_time = P11_Event.get_time(value)#get current time 
            ind+=1 #add to get the right index
            if v_date == date and v_time == time: #if date and time match input date and time
                final_ind = ind #index of event
            
        del P11_Calendar.event_list[final_ind] #deleteevent
            

    
    def day_schedule(self,date):
        schedule= [] #initialize schedule
        for value in P11_Calendar.event_list: #iterate through events list
            v_date = P11_Event.get_date(value) #collect date from  event list
            if v_date == date: #if date matches input date
                schedule.append(value) #append that event to the schedule for the list of the day
        schedule.sort() #sort by start time
        
        return schedule
           
    def __str__(self):
        final_string = 'Events in Calendar:\n' #header
        for value in P11_Calendar.event_list: #iterate through events list
            final_string += str(value) #create just one string to return by adding all values
            final_string += '\n' #add new lines after each event
        return final_string
    
    
    
    def __repr__(self):
        s = ''
        for e in self.event_list:
            s += e.__repr__() + ";"
        return s[:-1]
    
    def __eq__(self,cal):
        '''PROVIDED: returns True if all events are the same.'''
        if not isinstance(cal,P11_Calendar):
            return False
        if len(self.event_list) != len(cal.event_list):
            return False
        L_self = sorted(self.event_list)
        L_e = sorted(cal.event_list)
        for i,e in enumerate(L_self):
            if e != L_e[i]:
                return False
        return True