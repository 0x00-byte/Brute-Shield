import datetime
from data_structure import c_queue
import logger

WINDOW = 60      #In seconds. The time frame withtin which limits need to be checked.
BLOCK = 60 * 5   #In seconds. Lock out time.
LIM = 5          #Number maximum requests per WINDOW.


class User:
    """A User class that contains all the information about the user and also has built in brute force detection."""
    def __init__(self, password, ip):
        self.password = password        
        self.ip = ip
        self.logged = False               #Flag for logging status
        self.blocked = False              #Flag for blocking the user
        self.block_time = None            #Timer to the point of time where block will be lifted
        self.entries = c_queue(LIM + 1)   #Queue of all current requests 
        self.current = None               #Last recorded time stamp of the user


    #Checks all the entries and removes any expired ones.
    def check(self, current):
        while not(self.entries.is_empty()) and self.entries.peek() != None:
            first = self.entries.peek()
            if ((current - first) > datetime.timedelta(seconds=WINDOW)):
                self.entries.dequeue()
            
    #Blocks the user and starts the timer when called. 
    def block(self):
        if not self.blocked:
            self.blocked = True
            self.block_time = self.current + datetime.timedelta(seconds=BLOCK)
            return True

    #Checks if the user is blocked, and lifts the block if the timer expires.
    def is_block(self):
        if self.blocked:
            if datetime.datetime.now() < self.block_time:
                return True
            else:
                self.blocked = False
                self.block_time = None
                return False
        else:
            return False
    
    #Makes the acctual request that needs to be processed.
    def request(self):
        #Checks if the user is already logged in or not.
        if self.logged:
            print("Already logged in.")
            return 
        
        #Checks if the user is blocked or not.
        if not self.is_block():
            
            #Set current time and re-evaluate all the entires based on current time.
            self.current = datetime.datetime.now()
            self.check(self.current)

            #Take input from the user and add to the records.
            entry = input("Enter password: ")
            self.entries.enqueue(self.current)

            if self.entries.is_full():
                print("Too many attemps. Please wait and try again.")
                self.block()
                logger.log_event("Too many attempts.", self.current, self.ip)
                return
            
            elif self.is_block():
                print("You are blocked till: ", self.block_time)
                return

            #Basic validation
            if entry != self.password:
                print("invalid password. Please try again.")
                return
        
            print("Access granted.")
            self.logged = True
                
        else:
            print("Entry restricted. Please wait " + str(self.block_time - datetime.datetime.now()))

if __name__=="__main__":
    #Local user registry 
    users = {"user1":User("pass","11.11.11.11"),
             "user2":User("password","22.22.22.22")}
    
    #Basic menu with user recognition and quitting functionality. 
    ch = ""
    while True:
        print("_"*20)
        ch = input("Enter your username: ")
        if ch in ["Quit", "quit", "Q", "q"]:break
        if ch in users.keys():
            users[ch].request()
        else:
            print("Invalid username. Try again or create an account(if you do not have one.).")