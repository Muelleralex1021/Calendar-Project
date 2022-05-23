CAL_TYPE = ['meeting','event','appointment','other']


class P11_Event():
    def __init__(self,date=None,time='9:00',duration=60,cal_type='meeting',valid = False):
        self.date = date #initialize all variables
        self.time = time
        self.duration = duration
        self.cal_type = cal_type
        self.valid = valid
        
        if self.time != None: 
            if ':'not in self.time: #if not formatted correctly return none for the variable
                self.time = None
        
        if self.date != None:
            if '/' not in self.date:#if not formatted correctly return none for the variable
                self.date = None
                
        
                
        if self.date != None: #initalizing month day and year for the three possible lengths of dates inputted
            if self.date[1] == '/':
                month = int(self.date[0])
                if self.date[3] == '/':
                    day = int(self.date[2])
                    year = int(self.date[4:])
                else:
                    day = int(self.date[2:4])
                    year = int(self.date[5:])
            if self.date[1] != '/':
                month = int(self.date[:2])
                if self.date[4] == '/':
                    day = int(self.date[3])
                    year = int(self.date[5:])
                else:
                    day = int(self.date[3:5])
                    year = int(self.date[6:])
       
        
        if self.time != None: #initialize hour and minute for two different time lengths inputted
            if len(self.time) == 5:
                hour = int(self.time[0:2])
            if len(self.time) != 5:
                hour = int(self.time[0:1])
            minute = int(self.time[3:])
        
            
        if self.date != None: #if date is valid number for month day and year variables created earlier
            if day <1 or day>31:
                self.date = None
        
            if month<1 or month>12:
                self.date = None
       
            if year<0 or year>9999:
                self.date = None
        
        if self.time != None: #if time is valid number for hour and minute variables created earlier
            if hour <0 or hour>23:
                self.time = None
        
            if minute <0 or minute>59:
                time = None
           
        try:
            if cal_type not in CAL_TYPE: #make sure calendar type is in list of valid options
                self.cal_type = None
        except:
                self.cal_type = cal_type
                
        try:
            if duration <0: #duration must be positive integer
                self.duration = None
        except:
                self.duration = duration
                
        if type(duration) != int:#duration must be positive integer
            self.duration = None
        
            
        if self.date != None and self.time != None and self.duration != None and self.cal_type != None:
            self.valid = True #if all  variables are valid options they may be created and valid is true
        else:
            self.valid = False #if any are not the valid returns false
            
 
            
        
    
    def get_date(self):
        return self.date #return date
    
    
    def get_time(self):
        return self.time#return time
    
    def get_time_range(self):
        start_time = 0 #initialize start time in minutes
        if self.time != None: #create hour and minute variables so that the hour can be multiplied by 60 and minutes can be added to find start
            if len(self.time) == 5:
                hour = int(self.time[0:2])
            if len(self.time) != 5:
                hour = int(self.time[0:1])
            minute = int(self.time[3:])
            
        start_time += hour * 60
        start_time += minute
        end_time = start_time + self.duration #end time is just already created start time plus duration
        
        
        return (start_time,end_time)
            
        
    
    def __str__(self):
        return '{}: start: {}; duration: {}'.format(self.date,self.time,self.duration) #create string version of event
        
        
    
    def __repr__(self):
        if self.date and self.time and self.duration:
            return self.date + ';' + self.time + '+' + str(self.duration)
        else:
            return 'None'

    def __lt__(self,e):
        if self.time != None:
            if len(self.time) == 5:#create hour and minute variables 
                hour = int(self.time[0:2])
            if len(self.time) != 5:
                hour = int(self.time[0:1])
            minute = int(self.time[3:])
            
        if e.time != None: #if time entered was valid
            if len(e.time) == 5:#create hour and minute variables 
                e_hour = int(e.time[0:2])
            if len(e.time) != 5:
                e_hour = int(e.time[0:1])
            e_minute = int(e.time[3:])
            
        if self.time == None or e.time == None: #if either are not valid return false
            return False
        
        self_min = (hour*60) + minute #create two variables to be compared that are in minutes
        e_min = (e_hour*60) + e_minute
        
        if self_min<e_min:
            return True
        else:
            return False
   
    
    def __eq__(self,e):
        '''PROVIDED'''
        return self.date == e.date and self.time == e.time and self.duration == e.duration and self.cal_type == e.cal_type # and self.status == e.status