'''
=================================================================================================
#################################################################################################
############################## Documentation: BattleShip Game ###################################
#################################################################################################
=================================================================================================
============= 1.Creating class for randomly position and placing of vessles =====================

 define class with name Vessle
 create method 'ship' with agrguments size and mainShipList
 import random module
 
 create a while loop
 create random X coordinate , Y coordinate and O for orientation
 create a shipList for current the ships being created
 create mainShipList for all the ships being created for later check of overlaps
 if O == 0 then change X part of the coordinate till the ship size is full filled
    then check for over laps
 if O == 1 then change Y part of the coordinate till the ship size is ful filled
    then check for over laps
 if ships over lap do the above steps over again
 if not return ship list for placement of the Grid
==================================================================================================
================================== 2. Playing Game 100 Times =====================================

 Loop 100 times using for loop in range from 1 to 101

======================================= 2.1. Pygame Grid  ========================================

 module import random pygame and time
 initialize pygame display
 initialize and color GameBoard(light sky blue)
 for every X coordinate draw a line length 400 and make spacing between then 20 using for loop
 for every X coordinate draw a line length 400 and make spacing between then 20 using for loop

============================== 2.2. Class Call named Vessels =====================================

 Vessels = Vessle()
 making instance of class
 PTship = Vessels.ship(2, mainShipList)
     Draw PTship color Blue
 Cruiser = Vessels.ship(3, mainShipList)
     Draw Cruiser color Blue
 Destroyer = Vessels.ship(4, mainShipList)
     Draw Destroyer color Blue
 Battleship = Vessels.ship(5, mainShipList)
     Draw Battleship color Blue 
 AircraftCarrier = Vessels.ship(6, mainShipList)
     Draw AircraftCarrier color Blue

======================================= 2.3. Random Search ======================================

 while count <= 4
 declare and initialize variable
    count, shotCounts, CurrentShot_L, Total_S_List, random x and random y
    create random x and y
    put them in a list
    count += 1
    check if list has been created before
    if yes = break and create another list
    if no
         check if the list belongs to the list of one of the vessels
         if yes do local search and destroy vessel

         if no check create another list and do the loop again
         
========================================= 2.4. Local Search =====================================

 if list created on section 2.3. belongs to one of the ships  and is not in the total
 successful shots we put it in currentshot list and go in to local search

 now check for alignment

 if horizontal
     while(length of currentshotlist != length of vessel)
         if left square is part of vessel and is not in current shot list
             we color that list
             and keep going until we go out of the vessel list
 if Vertical
     while(length of currentshotlist != length of vessel)
         if right square is part of vessel and is not in current shot list
             we color that list
             and keep going until we get all the co-ordinates of that vessel

 This local search goes for all the ships no matter the size
 and alignment
=========================================== // ==================================================
*************************************************************************************************
'''
#************************************************************************************************
#================================================================================================
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Class for Vessle Production ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#================================================================================================
class Vessel(object):
    
    def ship(self, size, mainShipList):
        
        import random
        
        overLap = True # Over lap boolean
        
        while(overLap):
            
            #List(Tuple) for holding coordinate spaces
            myTuple = (20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380)
            
            
            RandomX = myTuple[int(random.uniform(0, 19))]# Random number for x coordinate
            RandomY = myTuple[int(random.uniform(0, 19))]# Random number for y coordinate
            RandomO = int(random.uniform(0, 2))# Random number for ship alignment 

            shipList = []# Holds current Vessle list

            
            z = 0
            a = 0
            
            if(RandomO == 0): #0 means Horizontal alignment
                while(z < size):
                    if((RandomX + 20*size) <= 400):
                        shipList.extend([(RandomX+a, RandomY)])
                    
                    elif((RandomX + 20*size) > 400):
                        shipList.extend([(RandomX-a, RandomY)])
                    
                    a += 20
                    z += 1
                    
            elif(RandomO == 1):#1 means Vertical alignment
                while(z < size):
                    if((RandomY + 20*size) <= 400):
                        shipList.extend([(RandomX, RandomY+a)])
                    
                    elif((RandomY + 20*size) > 400):
                        shipList.extend([(RandomX, RandomY-a)])
                    
                    a += 20
                    z += 1
#===================================================================
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#======================= Check for overlaps ========================               
            for i in range(0, len(shipList)):
                for j in range(0, len(mainShipList)):
                    if(shipList[i] == mainShipList[j]):
                        overLap = True
                        break
                    else:
                        overLap = False
                if(overLap):
                    break
                                    
        return shipList
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#============================= // ==================================
#*******************************************************************
#*******************************************************************
#===================================================================
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#======================= Game Grid =================================
for h in range(1, 101): #
    import pygame 
    import random
    import time
    pygame.display.init()
    GameBoard = pygame.display.set_mode((425, 425))
    GameBoard.fill((0,191,255))
            
    x = 20# spacing on x direction
    y = 20# spacing on y direction

    for i in range(20):
        pygame.draw.line(GameBoard, (255,255,255),(20,y),(400,y))
        pygame.draw.line(GameBoard, (255,255,255),(x,20),(x,400))
        y += 20
        x += 20
    
    #===================================================================
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    #============================ Patrol Ship ==========================
    mainShipList = [(0,0)]

    Vessels = Vessel() # Calling class Vessle 

    PTship = Vessels.ship(2, mainShipList)
    for i in range(0, len(PTship)):
        X = PTship[i][0]
        Y = PTship[i][1]
        GameBoard.fill((0,0,255), rect=(X,Y,20,20))    
    mainShipList.extend(PTship)
    #===================================================================
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    #=========================== Cruiser ===============================
    Cruiser = Vessels.ship(3, mainShipList)
    for i in range(0, len(Cruiser)):
        X = Cruiser[i][0]
        Y = Cruiser[i][1]
        GameBoard.fill((0,0,255), rect=(X,Y,20,20))
    mainShipList.extend(Cruiser)
    #===================================================================
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    #========================== Destroyer ==============================
    Destroyer = Vessels.ship(4, mainShipList)
    for i in range(0, len(Destroyer)):
        X = Destroyer[i][0]
        Y = Destroyer[i][1]
        GameBoard.fill((0,0,255), rect=(X,Y,20,20))
    mainShipList.extend(Destroyer)
    #===================================================================
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    #======================= BattleShip ================================
    Battleship = Vessels.ship(5, mainShipList)
    for i in range(0, len(Battleship)):
        X = Battleship[i][0]
        Y = Battleship[i][1]
        GameBoard.fill((0,0,255), rect=(X,Y,20,20))
    mainShipList.extend(Battleship)
    #===================================================================
    #|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
    #===================== Aircraft Carrier ============================
    AircraftCarrier = Vessels.ship(6, mainShipList)
    for i in range(0, len(AircraftCarrier)):
        X = AircraftCarrier[i][0]
        Y = AircraftCarrier[i][1]
        GameBoard.fill((0,0,255), rect=(X,Y,20,20))
    mainShipList.extend(AircraftCarrier)
    #===================================================================
    pygame.display.update()
    #===================================================================  

    Scount = 0 # count for checking if all the vessels be hit or not
    shotCount = 0 # Total random shots needed to take down the fleet

    # check for the random shot not to be shot at that place again
    CurrentShot_L = [] 
    
    # To not to shoot the vessel already been taken/contains all successful shots
    Total_S_List = [] 

    Tuple = (20,40,60,80,100,120,140,160,180,200,220,240,260,280,300,320,340,360,380)
    
    #=======================================================================================    
    while(Scount <= 4) :
           
        X = Tuple[int(random.uniform(0, 19))]
        Y = Tuple[int(random.uniform(0, 19))]
        RandomShot = [] # Contains random x and random y co-ordinates as a tuple
        CurrentShot_L = [] # Reseting this list every loop 
        RandomShot.extend([(X, Y)])
        shotCount += 1
        if(RandomShot in Total_S_List):
            break
        elif(not(RandomShot in Total_S_List)):
        #===================================================================================       
            if(RandomShot[0] in PTship) and (not(RandomShot[0] in Total_S_List)):
                GameBoard.fill((255,0,0), rect=(X,Y,20,20))
                CurrentShot_L.extend([(X, Y)])
                Total_S_List.extend([(X, Y)])
                    
                   
                if((X-20, Y) in PTship) or ((X+20, Y) in PTship):
                    while(len(CurrentShot_L) != len(PTship)):
                        for j in range(1):
                            i = Tuple[j]
                            if((X-i, Y) in PTship) and (not((X-i, Y) in CurrentShot_L)):
                                GameBoard.fill((255,0,0), rect=(X-i,Y,20,20))
                                CurrentShot_L.extend([(X-i, Y)])
                                Total_S_List.extend([(X-i, Y)])
                                pygame.display.update()
                                
                                    
                            elif((X+i, Y) in PTship) and (not((X+i, Y) in CurrentShot_L)):
                                    
                                GameBoard.fill((255,0,0), rect=(X+i,Y,20,20))
                                pygame.display.update()
                                    
                                CurrentShot_L.extend([(X+i, Y)])
                                Total_S_List.extend([(X+i, Y)])
                              
                    
                            
                elif((X, Y-20) in PTship) or ((X, Y+20) in PTship):
                    while(len(CurrentShot_L) != len(PTship)):
                        for j in range(1):
                            i = Tuple[j]
                            if((X, Y-i) in PTship) and (not((X, Y-i) in CurrentShot_L)):
                                GameBoard.fill((255,0,0), rect=(X,Y-i,20,20))
                                CurrentShot_L.extend([(X, Y-i)])
                                Total_S_List.extend([(X, Y-i)])
                                pygame.display.update()
                                
                                    
                            elif((X, Y+i) in PTship) and (not((X, Y+i) in CurrentShot_L)):
                                GameBoard.fill((255,0,0), rect=(X,Y+i,20,20))
                                CurrentShot_L.extend([(X, Y+i)])
                                Total_S_List.extend([(X, Y+i)])
                                pygame.display.update()
                                
                Scount += 1
        #=======================================================================================                        
            if(RandomShot[0] in Cruiser) and (not(RandomShot[0] in Total_S_List)):
                    GameBoard.fill((255,0,0), rect=(X,Y,20,20))
                    CurrentShot_L.extend([(X, Y)])
                    Total_S_List.extend([(X, Y)])
                    
                    
                    if((X-20, Y) in Cruiser) or ((X+20, Y) in Cruiser):
                        while(len(CurrentShot_L) != len(Cruiser)):
                            
                            
                            for j in range(2):
                                i = Tuple[j]
                                if((X-i, Y) in Cruiser) and (not((X-i, Y) in CurrentShot_L)):
                                    GameBoard.fill((255,0,0), rect=(X-i,Y,20,20))
                                    CurrentShot_L.extend([(X-i, Y)])
                                    Total_S_List.extend([(X-i, Y)])
                                    pygame.display.update()
                                    
                                elif((X+i, Y) in Cruiser) and (not((X+i, Y) in CurrentShot_L)):
                                    GameBoard.fill((255,0,0), rect=(X+i,Y,20,20))
                                    CurrentShot_L.extend([(X+i, Y)])
                                    Total_S_List.extend([(X+i, Y)])
                                    pygame.display.update()
                            
                                
                    elif((X, Y-20) in Cruiser) or ((X, Y+20) in Cruiser):
                        while(len(CurrentShot_L) != len(Cruiser)):
                            
                            
                            for j in range(2):
                                i = Tuple[j]
                                if((X, Y-i) in Cruiser) and (not((X, Y-i) in CurrentShot_L)):
                                    GameBoard.fill((255,0,0), rect=(X,Y-i,20,20))
                                    CurrentShot_L.extend([(X, Y-i)])
                                    Total_S_List.extend([(X, Y-i)])
                                    pygame.display.update()
                                    
                                elif((X, Y+i) in Cruiser) and (not((X, Y+i) in CurrentShot_L)):
                                    GameBoard.fill((255,0,0), rect=(X,Y+i,20,20))
                                    CurrentShot_L.extend([(X, Y+i)])
                                    Total_S_List.extend([(X, Y+i)])
                                    pygame.display.update()
                                    
                    Scount += 1
        #=======================================================================================
            if(RandomShot[0] in Destroyer) and (not(RandomShot[0] in Total_S_List)):
                    GameBoard.fill((255,0,0), rect=(X,Y,20,20))
                    CurrentShot_L.extend([(X, Y)])
                    Total_S_List.extend([(X, Y)])
                    
                    
                    if((X-20, Y) in Destroyer) or ((X+20, Y) in Destroyer):
                        while(len(CurrentShot_L) != len(Destroyer)):
                            
                            
                            for j in range(3):
                                i = Tuple[j]
                                if((X-i, Y) in Destroyer) and (not((X-i, Y) in CurrentShot_L)):
                                    GameBoard.fill((255,0,0), rect=(X-i,Y,20,20))
                                    CurrentShot_L.extend([(X-i, Y)])
                                    Total_S_List.extend([(X-i, Y)])
                                    pygame.display.update()
                                    
                                    
                                elif((X+i, Y) in Destroyer) and (not((X+i, Y) in CurrentShot_L)):
                                    GameBoard.fill((255,0,0), rect=(X+i,Y,20,20))
                                    CurrentShot_L.extend([(X+i, Y)])
                                    Total_S_List.extend([(X+i, Y)])
                                    pygame.display.update()
                                    
                        
                    
                    elif((X, Y-20) in Destroyer) or ((X, Y+20) in Destroyer):
                        while(len(CurrentShot_L) != len(Destroyer)):
                            
                            for j in range(3):
                                i = Tuple[j]
                                if((X, Y-i) in Destroyer) and (not((X, Y-i) in CurrentShot_L)):
                                    GameBoard.fill((255,0,0), rect=(X,Y-i,20,20))
                                    CurrentShot_L.extend([(X, Y-i)])
                                    Total_S_List.extend([(X, Y-i)])
                                    pygame.display.update()
                                    
                                    
                                elif((X, Y+i) in Destroyer) and (not((X, Y+i) in CurrentShot_L)):
                                    GameBoard.fill((255,0,0), rect=(X,Y+i,20,20))
                                    CurrentShot_L.extend([(X, Y+i)])
                                    Total_S_List.extend([(X, Y+i)])
                                    pygame.display.update()
                                    
                    Scount += 1
        #============================================================================================
            if(RandomShot[0] in Battleship) and (not(RandomShot[0] in Total_S_List)):
                    GameBoard.fill((255,0,0), rect=(X,Y,20,20))
                    CurrentShot_L.extend([(X, Y)])
                    Total_S_List.extend(CurrentShot_L)
                    
                    
                    if((X-20, Y) in Battleship) or ((X+20, Y) in Battleship):
                        while(len(CurrentShot_L) != len(Battleship)):
                            
                            for j in range(4):
                                i = Tuple[j]
                                
                                if((X-i, Y) in Battleship) and (not((X-i, Y) in CurrentShot_L)):
                                    GameBoard.fill((255,0,0), rect=(X-i,Y,20,20))
                                    CurrentShot_L.extend([(X-i, Y)])
                                    Total_S_List.extend([(X-i, Y)])
                                    pygame.display.update()
                        
                                    
                                elif((X+i, Y) in Battleship) and (not((X+i, Y) in CurrentShot_L)):
                                    GameBoard.fill((255,0,0), rect=(X+i,Y,20,20))
                                    CurrentShot_L.extend([(X+i, Y)])
                                    Total_S_List.extend([(X+i, Y)])
                                    pygame.display.update()
                        
                    
                    elif((X, Y-20) in Battleship) or ((X, Y+20) in Battleship):
                        while(len(CurrentShot_L) != len(Battleship)):
                            
                            for j in range(4):
                                i = Tuple[j]
                                if((X, Y-i) in Battleship) and (not((X, Y-i) in CurrentShot_L)):
                                    GameBoard.fill((255,0,0), rect=(X,Y-i,20,20))
                                    CurrentShot_L.extend([(X, Y-i)])
                                    Total_S_List.extend([(X, Y-i)])
                                    pygame.display.update()
                                    
                                    
                                elif((X, Y+i) in Battleship) and (not((X, Y+i) in CurrentShot_L)):
                                    GameBoard.fill((255,0,0), rect=(X,Y+i,20,20))
                                    CurrentShot_L.extend([(X, Y+i)])
                                    Total_S_List.extend([(X, Y+i)])
                                    pygame.display.update()
                                    
                    Scount += 1
        #==============================================================================================
            if(RandomShot[0] in AircraftCarrier) and (not(RandomShot[0] in Total_S_List)):
                    GameBoard.fill((255,0,0), rect=(X,Y,20,20))
                    CurrentShot_L.extend([(X, Y)])
                    Total_S_List.extend(CurrentShot_L)
                    
                    
                    if((X-20, Y) in AircraftCarrier) or ((X+20, Y) in AircraftCarrier):
                        while(len(CurrentShot_L) != len(AircraftCarrier)):
                            
                            for j in range(5):
                                i = Tuple[j]
                                if((X-i, Y) in AircraftCarrier) and (not((X-i, Y) in CurrentShot_L)):
                                    GameBoard.fill((255,0,0), rect=(X-i,Y,20,20))
                                    CurrentShot_L.extend([(X-i, Y)])
                                    Total_S_List.extend([(X-i, Y)])
                                    pygame.display.update()
                                    
                                    
                                elif((X+i, Y) in AircraftCarrier) and (not((X+i, Y) in CurrentShot_L)):
                                    GameBoard.fill((255,0,0), rect=(X+i,Y,20,20))
                                    CurrentShot_L.extend([(X+i, Y)])
                                    Total_S_List.extend([(X+i, Y)])
                                    pygame.display.update()
                        
                    
                    elif((X, Y-20) in AircraftCarrier) or ((X, Y+20) in AircraftCarrier):
                        while(len(CurrentShot_L) != len(AircraftCarrier)):
                            
                            for j in range(5):
                                i = Tuple[j]
                                if((X, Y-i) in AircraftCarrier) and (not((X, Y-i) in CurrentShot_L)):
                                    GameBoard.fill((255,0,0), rect=(X,Y-i,20,20))
                                    CurrentShot_L.extend([(X, Y-i)])
                                    Total_S_List.extend([(X, Y-i)])
                                    pygame.display.update()
                                    
                                    
                                elif((X, Y+i) in AircraftCarrier) and (not((X, Y+i) in CurrentShot_L)):
                                    GameBoard.fill((255,0,0), rect=(X,Y+i,20,20))
                                    CurrentShot_L.extend([(X, Y+i)])
                                    Total_S_List.extend([(X, Y+i)])
                                    pygame.display.update()
                    Scount += 1
        #================================================================================================                            

            elif(not(RandomShot[0] in mainShipList)):
                   X = RandomShot[0][0]
                   Y = RandomShot[0][1]
                   GameBoard.fill((0,0,0), rect=(X,Y,20,20))
                   pygame.display.update()

        
        time.sleep(0.004) # Slowing down ship construction and shooting each loop 
        
    print("In Game number ",h ,"It took ", shotCount, " shots to sink all Vessle.")
    time.sleep(0.5) # Pauses every time loop ends by 0.5 seconds    
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#======================================== THE END ======================================================




