import pygame
import experimental
from leaderBoardData import savingData
from pygame import mixer
import time
 #this file is for the bedroom and all of its dependencies
clock = pygame.time.Clock()
clock.tick(60)
screenHeight = 400
screenWidth = 700
 
pygame.init()
 
#loading images and game sizing
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Menu")
menuScreen = pygame.image.load("title/menuFullScreen.png").convert()
 

bedroom = pygame.image.load('assets/images/Bedroom/backgroun/bedroom.png').convert()
#DeskFile = pygame.image.load("assets/images/Library/backgrounds/file_inside_of_desk.png")
backButton = pygame.image.load("assets/buttons/all-screens/backButton.jpg").convert()
leftArrow = pygame.image.load("assets/buttons/all-screens/leftArrow.jpg").convert()
rightArrow = pygame.image.load("assets/buttons/all-screens/rightArrow.jpg").convert()
nightStandZoomIn = pygame.image.load('assets/images/Bedroom/zoomIns/nightstandZoomIn.png').convert()
floorZoomIn= pygame.image.load('assets/images/Bedroom/zoomIns/floordboardZoomIn.png').convert()
floorboardRemovedZoomIn = pygame.image.load('assets/images/Bedroom/zoomIns/floorboardRemovedZoomIn.png').convert() 
recordplyrZoomIn = pygame.image.load('assets/images/Bedroom/zoomIns/RecordplyrNoRecordZoomIn.png').convert()
recordplyrWithRecordZoomIn = pygame.image.load('assets/images/Bedroom/zoomIns/RecordplyrZoomIn.png').convert()
painting = pygame.image.load('assets/images/Bedroom/zoomIns/paintingZoomIn.png').convert()
 
dialogBox = pygame.image.load("experimental/dialogueBox.png").convert()

userBox = pygame.image.load("experimental/dialogBox.png").convert()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (111, 78, 55)
Transparent = (0, 0, 0, 0)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('red1')
active = False
 
#inventoryBible = pygame.image.load(" .................. ") #inventory image
#inventoryDancingMen = pygame.image.load(" ................ ") #inventory image
#inventoryBlankBook = pygame.image.load(" ................ ") #inventory image
#Bible = pygame.image.load(" .............. ") #should be the vesion where we see the verses
#DancingMen = pygame.image.load(" .............. ") #version where we see the explanation to the dancing men cipher
#BlankBook = pygame.image.load(" .............. ") #nothing inside until ran under water
 
#i dont have any idea where the images for these are... if yo could please find them id be most gracious
 
 
#work-in-progress
 

timerBg = pygame.image.load("title/timerBg.jpg").convert()
 
 

bibleOnScreen = pygame.image.load('assets/images/Library/booksOnScreen/bibleOnScreen.png').convert_alpha()
inventoryImage = pygame.image.load("assets/images/inv/inventoryIcon.png").convert_alpha()
inventoryHotbar = pygame.image.load("assets/images/inv/inventoryHotbar.png").convert_alpha()
inventoryTextThing = pygame.image.load("assets/images/inv/inventoryTextThing.png").convert_alpha()
keyImage = pygame.image.load("assets/images/inv/keyImage.png").convert_alpha()
bibleInv = pygame.image.load('assets/images/inv/bibleInv.png').convert_alpha()
inventoryBackground = pygame.image.load("assets/images/inv/inventoryBackground.jpeg").convert_alpha()
 
#music
mixer.init()
inventoryDing = mixer.Sound("assets/sounds/effects/inventoryDing.wav")
#mixer.music.set_volume(0.7)
clueClick = mixer.Sound("assets/sounds/effects/clueClick.wav")
bgMusic = mixer.Sound("assets/sounds/music/bgMusic.wav")
#intense music lag moment
 
 
#classes for defining image, scale, and location
class imageScaling():
  def __init__(self, x, y, image, scale):
    width = image.get_width()
    height = image.get_height()
    self.image = pygame.transform.scale(
        image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
 
  def draw(self):
     screen.blit(self.image, (self.rect.x, self.rect.y))
 
#images
menuScreen = imageScaling(0, 0, menuScreen, 0.5)
bedroomScreen = imageScaling(0, 0, bedroom, 1)
#rightTriangleImage = imageScaling(445, 35, rightTriangle, 0.2)
bibleScreen = imageScaling(0, 0, bibleOnScreen, 0.5)
leftArrow = imageScaling(100, screenHeight/2, leftArrow, 0.3)
rightArrow = imageScaling(540, screenHeight/2, rightArrow, 0.3)
 

 
backButton = imageScaling(10, 10, backButton, 1)
timerBg = imageScaling(604, 7, timerBg, 1)
 
#inventory media
keyImageButton = imageScaling(440, 180, keyImage, 0.3)
inventoryKey = imageScaling(197, 297, keyImage, 0.1)
bibleInvItem = imageScaling(237, 297, bibleInv, 0.15)
#inventoryBible = imageScaling(w, x, inventoryBible, 0.1)
#inventoryBlankBook = imageScaling(w, x, inventoryBlankBook, 0.1)
#inventoryDancingMen = imageScaling(w, x, inventoryDancingMen, 0.1)
 
inventoryIcon = imageScaling(600, 10, inventoryImage, 0.3)
inventoryIcon2 = imageScaling(100, 300, inventoryImage, 0.4)
inventoryHotbar = imageScaling(200, 300, inventoryHotbar, 0.5)
inventoryTextThing = imageScaling(180, 40, inventoryTextThing, 0.5)
inventoryBackground = imageScaling(0, 0, inventoryBackground, 3)
bedroomZoomNightstand = imageScaling(0, 0, nightStandZoomIn, 1)
bedroomZoomFloorboard = imageScaling(0, 0, floorZoomIn, 1)
bedroomZoomRecordplyr = imageScaling(0, 0, recordplyrZoomIn, 1)
bedroomZoomFloorboardRemoved = imageScaling(0, 0, floorboardRemovedZoomIn, 1)
bedroomZoomRecordplyrWithRecord = imageScaling(0, 0, recordplyrWithRecordZoomIn, 1)
bedroomZoomPainting = imageScaling(0, 0, painting, 1)
#adding clock times individually to test

 
#cutscene
 
#lists
imageList = []
bedroomZooms = [bedroomZoomNightstand, 'bedroomZoomBed', bedroomZoomRecordplyr, bedroomZoomPainting, bedroomZoomFloorboard, bedroomZoomFloorboardRemoved, bedroomZoomRecordplyrWithRecord]

inventory = [inventoryKey, bibleInvItem]# inventoryBlankBook, inventoryDancingMen
booksList = []
inventoryOpen = False
global userName
userName = ''
 
#initialization
keySelected = False #false until key in inventory is clicked
bibleSelected = False
recordSelected = False
 
run = True
imageOne = False  #used to cycle images and put arrows
clocksIteration = True #avoid stacked images and lag
 
menuOpen = True #will say menu is open until startButton clicked

 
zoomIn = False #checks if user zoomed into certain shelves
firstOpen = True #if user clicks bookshelf for first time, game bugs out (this is a temporary solution)
 

 

 
largeSans = pygame.font.Font("fonts/OpenSans-Regular.ttf", 28)
 
t = 1800
timerDelay = True
 
while run:
  #testing music
  #pygame.mixer.music.play(-1)

   

 
 
  '''while t > 0 and timerDelay == False:
    mins = t // 60
    secs = t % 60
    timer = '{:02d}:{:02d}'.format(mins, secs)
    # display timer
    timerBg.draw()
    timerText = largeSans.render(timer, True, (0, 0, 0))
    screen.blit(timerText,[610,1])
    pygame.display.update()
    timerDelay = True
    time.sleep(1)
    timerDelay = False
    t -= 1'''
 

 
  #for all rooms
 
  for event in pygame.event.get():
      #pygame.quit() will run and close window
    print(event)
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.KEYDOWN:
      #This is to allow pressing the 'e' key to open the inv and then close it (should have a note telling the user this option)
      if inventoryOpen == True and event.key == pygame.K_e and zoomIn == False:
        print('E pressed while in inv')
        screen.fill((0, 0, 0, 0))
        if imageIndex == 1:
          clocksIteration = True
        if bibleSelected == True:
          screen.fill((BLACK))
          bibleScreen.draw()
          backButton.draw()
          bibleSelected = False
          imageIndex = 3
        imageList[imageIndex].draw()
        imageOne = True
        leftArrow.draw()
        rightArrow.draw()
        pygame.display.set_caption("Byrne Mansion")
        inventoryOpen = False
       
      elif inventoryOpen == False and menuOpen == False and event.key == pygame.K_e and zoomIn == False:
        print("E pressed")
        screen.fill((0, 0, 0,0))
        inventoryBackground.draw()
        inventoryIcon.draw()
        inventoryIcon2.draw()
        inventoryHotbar.draw()
        pygame.display.set_caption("Inventory")
        print("Inventory drawn")
        inventoryOpen = True
        inventoryBorder = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(197, 297, 300, 105), 2)
        inventoryTextThing.draw()
        pygame.display.update()
        try:
          if inventory[0] == 'Key' or inventory [1] == 'Key':
            inventoryKey.draw()
            pygame.display.update()
          if inventory[1] == 'Bible' or inventory[0] == 'Bible':
            bibleInvItem.draw()
            pygame.display.update()
        except:
          print("The key has not been obtained yet.")
 
       
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      x, y = event.pos
      leftArrowRect = pygame.Rect(100, 200, 30, 30)
      rightArrowRect = pygame.Rect(540, 200, 30, 30)
      backButtonMenu = pygame.Rect(10, 10, 30, 30)
 
      if leftArrowRect.collidepoint(x, y) or rightArrowRect.collidepoint(x, y):
        inventoryOpen = False
 
     
      
    bedroomBed = pygame.Rect(0, 70, 130, 110)
    bedroomNightstand = pygame.Rect(141, 0, 184, 300)
    bedroomRecordplyr = pygame.Rect(331, 0, 194, 300)
    bedroomFloorboard = pygame.Rect(525, 60, 175, 120)
    bedroomPainting = pygame.Rect(0, 0, screenWidth, screenHeight)
    backButtonRect = pygame.Rect(10, 10, 30, 30)

    if bedroomBed.collidepoint(x, y) and inventoryOpen == False and zoomIn == False and menuOpen == False:
        print("Shelf one clicked")
        bedroomZooms[1].draw()
        backButton.draw()
        pygame.display.update()
        zoomIn = True
        poemRead = True
        if firstOpen == True:
            zoomIn = False
            firstOpen = False
        #BibleRect = pygame.Rect(w, x, y, z)
        #if BibleRect.collidepoint(x, y) and inventoryOpen == False and zoomIn == True and menuOpen == False:
    """print("Bible clicked!")
        screen.fill((0, 0, 0, 0))

        inventory.append("inventoryBible")
        #pygame.mixer.Sound.play(inventoryDing)
        pygame.mixer.music.stop()
        inventory = list(set(inventory))
        print(inventory)"""
        
    if bedroomNightstand.collidepoint(x, y) and inventoryOpen == False and zoomIn == False and menuOpen == False:
        print("nightstand")
        bedroomZooms[0].draw()
        backButton.draw()
        pygame.display.update()
        zoomIn = True
        lockCode = pygame.Rect(0, 0, screenWidth, screenHeight)
        lock = pygame.Rect(0, 0, screenWidth, screenHeight)
        if poemRead == True and lockCode.collidepoint(x/y):
            print('lock time')
            'lockZoom'.draw() 
            #code is 1617
            firstNumber = pygame.Rect(0, 0, screenWidth, screenHeight)
            SecondNumber = pygame.Rect(0, 0, screenWidth, screenHeight)
            ThirdNumber = pygame.Rect(0, 0, screenWidth, screenHeight)
            FourthNumber = pygame.Rect(0, 0, screenWidth, screenHeight)
            if firstNumber.collidepoint(x, y):
                print('changing first digit')
                firstDigitIndex += 1
                if firstDigitIndex == 9:
                    firstDigitIndex = 0
                firstDigitIndex.draw()
            if SecondNumber.collidepoint(x, y):
                print('changing 2nd digit')
                secondDigitIndex += 1
                if secondDigitIndex == 9:
                    secondDigitIndex = 0
                secondDigitIndex.draw()
            if ThirdNumber.collidepoint(x, y):
                print('changing 3rd digit')
                thirdDigitIndex += 1
                if thirdDigitIndex == 9:
                    thirdDigitIndex = 0
                thirdDigitIndex.draw()
            if FourthNumber.collidepoint(x, y):
                print('changing 4th digit')
                fourthDigitIndex += 1
                if fourthDigitIndex == 9:
                    fourthDigitIndex = 0
                    fourthDigitIndex.draw()
            if firstDigitIndex == 1 and secondDigitIndex == 6 and thirdDigitIndex == 1 and fourthDigitIndex == 7 and lock.collidepoint(x, y):
                lockStatus = 'Open'
                'lockOpen'.draw()
                'record'.draw()
                recordCollect = pygame.Rect(0, 0, screenWidth, screenHeight)
                if recordCollect.collidepoint(x, y):
                    print('Record has been touched')
                    inventory[2] = 'Record'
                    mixer.Sound.play(inventoryDing)
                    inventory = list(set(inventory))
                    print(inventory)
                    pygame.display.flip()

    if bedroomRecordplyr.collidepoint(x, y) and inventoryOpen == False and zoomIn == False and menuOpen == False:
        print("Record Player interacted")
        bedroomZooms[2].draw()
        backButton.draw()
        pygame.display.update()
        zoomIn = True
        if firstOpen == True:
            zoomIn = False
            firstOpen = False
        if recordSelected == True and bedroomRecordplyr.collidepoint(x, y) and inventoryOpen == False and zoomIn == True:
          bedroomZooms[6].draw()
          recordOnPlyrRect = pygame.Rect(0, 0, screenWidth, screenHeight)
          if recordOnPlyrRect.collidepoint(x, y) and inventoryOpen == False and zoomIn == True:
            print('playing record')
            mixer.Sound.play('record.wav')
    if bedroomFloorboard.collidepoint(x, y) and inventoryOpen == False and zoomIn == False and dancingManCodeShown == True:
        print("f l o o r")
        bedroomZooms[4].draw()
        backButton.draw()
        zoomIn = True
        removableFloorboard = pygame.Rect(0 , 0, screenWidth, screenHeight)
        if removableFloorboard.collidepoint(x, y) and inventoryOpen == False and zoomIn == True and dancingManCodeShown == True:
          bedroomZooms[5].draw()
        #pygame.rect(BLACK)

        #if DancingMenRect.collidepoint(x, y) and inventoryOpen == False and zoomIn == True and menuOpen == False
    
    if bedroomPainting.collidepoint(x, y) and inventoryOpen == False and zoomIn == False and menuOpen == False:
        print('PAINTING TIME!')
        bedroomZooms[3].draw()
        paintingZoomRect = pygame.Rect(0, 0, screenWidth, screenHeight)
        if paintingZoomRect.collidepoint(x, y) and 'recordPlayed' == True:
            'paintingFlipped'.draw()
            dancingManCodeShown = True

    if backButtonRect.collidepoint(x, y):
        imageOne = True
        zoomIn = False
 
      #clocks
      
         
      #adds key to inventory
      
      #inventory
    if inventoryOpen == True:
        slotOneRect = pygame.Rect(196, 296, 45, 56)
        slotTwoRect = pygame.Rect(254, 296, 45, 56)
        if slotOneRect.collidepoint(x, y):
          try:
              print("In the first slot, there is a " + inventory[0])
              if inventory[0] == 'Key':
                keySelectedRect = pygame.draw.rect(screen, (220, 20, 60), pygame.Rect(0, 0, 700, 700), 2)
                keySelected = True
                print("Where does this key lead me?")
              elif inventory[0] == 'Bible':
                print('Slot 2 has a ' + inventory[1])
                bibleSelectedRect = pygame.draw.rect(screen, (220, 20, 60),  pygame.Rect(0, 0, 700, 700), 2)
                bibleSelected = True
          except:
            print("There is nothing in that slot.")
        if slotTwoRect.collidepoint(x, y):
          try:
            print('Slot 2 has a ' + inventory[1])
            if inventory[1] == 'Bible':
              bibleSelectedRect = pygame.draw.rect(screen, (220, 20, 60),  pygame.Rect(0, 0, 700, 700), 2)
              bibleSelected = True
            if inventory[1] == 'Key':
              keySelectedRect = True
              keySelected = True
          except:
            print('no book to open :(')
 
    
 
pygame.quit()
 
#osvaldo stuff
"""
This if for the Arcostic Poem!
I will add the code you guys asked for here and we'll most likely edit the minor stuff such as the images and stuff later when we have it.
 
##Variables called
ArcosticButtonImageObject = pygame.image.load(
    "assets/buttons/second_screen/dialogButton.jpeg")
# Created a variable which holds an image of the dialog
ArcosticImageObject = pygame.image.load(
    "assets/buttons/second_screen/dialog.jpeg")
 
## Basically what gives the variables a visible output
ArcosticButtonImageObject = Button(1, 1, ArcosticButtonImageObject, 0.05)
ArcosticImageObject = Button(100, screenHeight / 8, ArcosticImageObject, 1.6)
##
 
#will go inside of the run loop
ArcosticButtonImageObject.draw()
#
 
###Button creation
ArcosticButtonRect = pygame.Rect(1, 1, 64, 36)
###
 
#### Basically the button which we created when clicked will collide with the (x, y) which'll cause the Arcostic Image which is the poem to draw itself onto the user's screen.
if ArcosticButtonRect.collidepoint(x, y):
                ArcosticImageObject.draw()
####
 
That's about it. idk where we're going to put it, but it's there
"""
"""
clicking sound code:
 
      pygame.mixer.music.play( whatever the file name for the clicking sound goes here )
 
just add it to the places where its needed. I didn't do that
############################################################################################################################################################################################################
when you need the moving bookshelves sound do the same code but with a different file name inside the paranthesis. It should work if not tell me (Osvaldo) and ill fix it.
############################################################################################################################################################################################################
      """
 
"""
#I renamed the deskBg to the new image which is technically the zoomed in version but i think it works best in contrast to the other one. I don't have any idea of where to put the code. So please do that for me. Thank you - Osvaldo
DeskLockRect = pygame.Rect(480, 360, 30, 30)
 
if DeskLockRect == imageList[2][0] and keySelected == True and DeskLockRect.collidepoint(x, y) and inventoryOpen == False and zoomIn == False and menuOpen == False:
  DeskOpen.draw()
  DeskFile.draw()
else:
  print("You need a key to unlock this desk.")
  print("If you have the key, you have to grab it from your inventory. Then try to open the desk.")
 
 
NUMBERS ARE 4 and 7
"""

