#!/usr/bin python3
from teacher import PiggyParent
import sys
import time

class Piggy(PiggyParent):

    '''
    *************
    SYSTEM SETUP
    *************
    '''

    def __init__(self, addr=8, detect=True):
        PiggyParent.__init__(self) # run the parent constructor

        ''' 
        MAGIC NUMBERS <-- where we hard-code our settings
        '''
        self.LEFT_DEFAULT = 75
        self.RIGHT_DEFAULT = 70
        self.MIDPOINT = 1500  # what servo command (1000-2000) is straight forward for your bot?
        self.set_motor_power(self.MOTOR_LEFT + self.MOTOR_RIGHT, 0)
        self.load_defaults()
        
    def load_defaults(self):
        """Implements the magic numbers defined in constructor"""
        self.set_motor_limits(self.MOTOR_LEFT, self.LEFT_DEFAULT)
        self.set_motor_limits(self.MOTOR_RIGHT, self.RIGHT_DEFAULT)
        self.set_servo(self.SERVO_1, self.MIDPOINT)
        
    def menu(self):
        """Displays menu dictionary, takes key-input and calls method"""
        ## This is a DICTIONARY, it's a list with custom index values. Python is cool.
        # Please feel free to change the menu and add options.
        print("\n *** MENU ***") 
        menu = {"n": ("Navigate", self.nav),
                "d": ("Dance", self.dance),
                "o": ("Obstacle count", self.obstacle_count),
                "s": ("Shy", self.shy),
                "f": ("Follow", self.follow),
                "c": ("Calibrate", self.calibrate),
                "q": ("Quit", self.quit),
                "sq": ("Square", self.square),
                "m": ("Move to wall", self.move),
                "t": ("Move and Turn", self.move_and_turn),
                "b": ("Move around a box", self.around_a_box),
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = str.lower(input("Your selection: "))
        # activate the item selected
        menu.get(ans, [None, self.quit])[1]()

    '''
    ****************
    STUDENT PROJECTS
    ****************
    '''
  
    def square(self):
      for side in range (4): 
        self.fwd()
        time.sleep(2)
        self.stop()
        self.right(90)
        time.sleep(0.8)
        self.stop()


      
    def dance(self):
        """A higher-ordered algorithm to make your robot dance"""
        # TODO: check to see if it's safe before dancing
        if self.safe_to_dance():
          self.right()
          time.sleep(3)
          self.stop()
          time.sleep(1)
          self.left()
          time.sleep(3)
          self.stop()

    def safe_to_dance(self):
      """ Does a 360 distance check and returns true if safe """
      self.servo(1000)
      time.sleep(0.25)
      if self.read_distance()<= 300:
        return False
      self.servo(2000)
      time.sleep(0.25)
      if self.read_distance()<=300:
        return False
      else:
        return True

    def shake(self):
        """ Another example move """
        self.deg_fwd(720)
        self.stop()

    def move(self):
     

        """"
    def move_and_turn(self):
      while self.read_distance()>=600:
        self.read_distance() 
        self.fwd()
        time.sleep(0.5) 
      else:
        self.stop()
        self.right()
        time.sleep(1)
        self.stop()
        self.fwd()
     

    def move_and_turn(self):
        while True:
          self.fwd()
          self.read_distance()
          if self.read_distance()<= 600:
            return False 
          if False:
            self.stop()
            self.right()
            time.sleep(2)
            self.stop()
            return True
          else:
            return True
       

    def move_and_turn(self):
      while self.read_distance()>= 600:
        self.read_distance()
        self.fwd() 
        time.sleep(0.5)
      else: 
        self.stop()
        self.right()
        time.sleep(0.8)
        self.stop()
        self.read_distance()
        """

    def move_and_turn(self):
      while True: 
        self.servo(self.MIDPOINT)
        self.fwd()
        if self.read_distance()<= 500:
          self.stop()
          self.turn_by_deg(180)
       
    """def around_a_box(self):
    
      while True:
        while self.read_distance()>=400:
          self.fwd()
          time.sleep(0.5) 
        else:
          self.turn_by_deg(50)
          self.fwd()
          time.sleep(1)
          self.stop()
          self.servo(2000)
          self.read_distance()
          return True
     

    def around_a_box(self):
      while True:
        self.fwd()
        self.read_distance()
        self.read_distance()>=300 = box
          if box:
            self.stop()
            self.turn_by_deg(40)
            return True """

    def around_a_box(self):
       while True: 
        self.servo(self.MIDPOINT)
        self.fwd()
        if self.read_distance()<= 200:
          self.stop()
          self.servo(1000)
          time.sleep(0.25)
          dis_right=self.read_distance()
          self.servo(2000)
          time.sleep(0.25)
          dis_left=self.read_distance()
          if dis_right > dis_left:
            self.right()
            time.sleep(0.7)
            self.stop()
            self.fwd()
            time.sleep(1)
            self.stop()
            self.servo(2000)
            box_side= self.read_distance()
            time.sleep(0.25)
            if box_side <50:
              self.fwd()
            else:
              self.left()
              time.stop(0.5)
              self.stop()
              self.fwd()
            
            
          if dis_left>dis_right :
            self.left()
            time.sleep(1)
            self.stop()
          
     
   
    def scan(self):
        """Sweep the servo and populate the scan_data dictionary"""
        for angle in range(self.MIDPOINT-350, self.MIDPOINT+350, 3):
            self.servo(angle)
            self.scan_data[angle] = self.read_distance()

    def obstacle_count(self):
        """Does a 360 scan and returns the number of obstacles it sees"""
        pass

    def nav(self):
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-------- [ Press CTRL + C to stop me ] --------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        
        # TODO: build self.quick_check() that does a fast, 3-part check instead of read_distance
        while self.read_distance() > 250:  # TODO: fix this magic number
            self.fwd()
            time.sleep(.01)
        self.stop()
        # TODO: scan so we can decide left or right
        # TODO: average the right side of the scan dict
        # TODO: average the left side of the scan dict
        


###########
## MAIN APP
if __name__ == "__main__":  # only run this loop if this is the main file

    p = Piggy()

    if sys.version_info < (3, 0):
        sys.stdout.write("Sorry, requires Python 3.x\n")
        p.quit()

    try:
        while True:  # app loop
            p.menu()

    except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
        p.quit()  
