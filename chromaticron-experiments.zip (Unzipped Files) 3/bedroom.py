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

menuScreen = pygame.image.load("chromaticron-experiments/title/menuFullScreen.png").convert()
 
#################################
bedroom = pygame.image.load('chromaticron-experiments/assets/images/Bedroom/background/bedroom.png').convert()

backButton = pygame.image.load("chromaticron-experiments/assets/buttons/all-screens/backButton.jpg").convert()
leftArrow = pygame.image.load("chromaticron-experiments/assets/buttons/all-screens/leftArrow.jpg").convert()
rightArrow = pygame.image.load("chromaticron-experiments/assets/buttons/all-screens/rightArrow.jpg").convert()
nightStandZoomIn = pygame.image.load('chromaticron-experiments/assets/images/Bedroom/zoomIns/nightstandZoomIn.png').convert()
lockUnlocked = pygame.image.load('chromaticron-experiments/assets/images/Bedroom/items/lockUnlocked.png').convert()
openNightstand = pygame.image.load('chromaticron-experiments/assets/images/Bedroom/zoomIns/openNightstand.png').convert()
floorZoomIn= pygame.image.load('chromaticron-experiments/assets/images/Bedroom/zoomIns/floorboardZoomIn.png').convert()
floorboardRemovedZoomIn = pygame.image.load('chromaticron-experiments/assets/images/Bedroom/zoomIns/floorboardRemovedZoomIn.png').convert() 
recordPlayerZoom = pygame.image.load('chromaticron-experiments/assets/images/Bedroom/zoomIns/RecordplyrNoRecordZoomIn.png').convert()
recordPlayerWithRecordZoom = pygame.image.load('chromaticron-experiments/assets/images/Bedroom/zoomIns/RecordplyrZoomIn.png').convert()
bedroomZoomBed = pygame.image.load('chromaticron-experiments/assets/images/Bedroom/zoomIns/bedzoomin.png')
painting = pygame.image.load('chromaticron-experiments/assets/images/Bedroom/zoomIns/paintingZoomIn.png').convert()
dancingManPainting = pygame.image.load('chromaticron-experiments/assets/images/Bedroom/zoomIns/dancingManPainting.png').convert()
lockZoom = pygame.image.load("chromaticron-experiments/assets/images/Bedroom/zoomIns/lockZoom.png").convert()

record = pygame.image.load("chromaticron-experiments/assets/images/Bedroom/items/record.png").convert()
hammer = pygame.image.load("chromaticron-experiments/assets/images/Bedroom/items/hammer.png").convert()
diary = pygame.image.load("chromaticron-experiments/assets/images/Bedroom/items/poemDiary.png").convert()

lockOne = pygame.image.load("chromaticron-experiments/assets/images/Bedroom/items/lockOne.png").convert()
lockTwo = pygame.image.load("chromaticron-experiments/assets/images/Bedroom/items/lockTwo.png").convert()
lockThree = pygame.image.load("chromaticron-experiments/assets/images/Bedroom/items/lockThree.png").convert()
lockFour = pygame.image.load("chromaticron-experiments/assets/images/Bedroom/items/lockFour.png").convert()
lockFive = pygame.image.load("chromaticron-experiments/assets/images/Bedroom/items/lockFive.png").convert()
lockSix = pygame.image.load("chromaticron-experiments/assets/images/Bedroom/items/lockSix.png").convert()
lockSeven = pygame.image.load("chromaticron-experiments/assets/images/Bedroom/items/lockSeven.png").convert()
lockEight = pygame.image.load("chromaticron-experiments/assets/images/Bedroom/items/lockEight.png").convert()
lockNine = pygame.image.load("chromaticron-experiments/assets/images/Bedroom/items/lockNine.png").convert()
lockTen = pygame.image.load("chromaticron-experiments/assets/images/Bedroom/items/lockTen.png").convert()
lockEleven = pygame.image.load("chromaticron-experiments/assets/images/Bedroom/items/lockEleven.png").convert()
lockTwelve = pygame.image.load("chromaticron-experiments/assets/images/Bedroom/items/lockTwelve.png").convert()
#################################

dialogBox = pygame.image.load("chromaticron-experiments/experimental/dialogueBox.png").convert()

userBox = pygame.image.load("chromaticron-experiments/experimental/dialogBox.png").convert()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (111, 78, 55)
Transparent = (0, 0, 0, 0)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('red1')
active = False

 

timerBg = pygame.image.load("chromaticron-experiments/title/timerBg.jpg").convert()
 

bibleOnScreen = pygame.image.load('chromaticron-experiments/assets/images/Library/booksOnScreen/bibleOnScreen.png').convert_alpha()
inventoryImage = pygame.image.load("chromaticron-experiments/assets/images/inv/inventoryIcon.png").convert_alpha()
inventoryHotbar = pygame.image.load("chromaticron-experiments/assets/images/inv/inventoryHotbar.png").convert_alpha()
inventoryTextThing = pygame.image.load("chromaticron-experiments/assets/images/inv/inventoryTextThing.png").convert_alpha()
keyImage = pygame.image.load("chromaticron-experiments/assets/images/inv/keyImage.png").convert_alpha()
bibleInv = pygame.image.load('chromaticron-experiments/assets/images/inv/bibleInv.png').convert_alpha()
inventoryBackground = pygame.image.load("chromaticron-experiments/assets/images/inv/inventoryBackground.jpeg").convert_alpha()
 
#music
mixer.init()
inventoryDing = mixer.Sound("chromaticron-experiments/assets/sounds/effects/inventoryDing.wav")
#mixer.music.set_volume(0.7)
clueClick = mixer.Sound("chromaticron-experiments/assets/sounds/effects/clueClick.wav")
bgMusic = mixer.Sound("chromaticron-experiments/assets/sounds/music/bgMusic.wav")
#intense music lag moment
 
 
#classes for defining image, scale, and location
class imageScaling():
  def __init__(self, x,y, image, scale):
    width = image.get_width()
    height = image.get_height()
    self.image = pygame.transform.scale(
        image, (int(width * scale), int(height * scale)))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x,y)
 
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
 
#################################
inventoryIcon = imageScaling(600, 10, inventoryImage, 0.3)
inventoryIcon2 = imageScaling(100, 300, inventoryImage, 0.4)
inventoryHotbar = imageScaling(200, 300, inventoryHotbar, 0.5)
inventoryTextThing = imageScaling(180, 40, inventoryTextThing, 0.5)
inventoryBackground = imageScaling(0, 0, inventoryBackground, 3)
bedroomZoomNightstand = imageScaling(0, 0, nightStandZoomIn, 1)
openNightstand = imageScaling(0, 0, openNightstand, 0.28)
bedroomZoomFloorboard = imageScaling(0, 0, floorZoomIn, 1)
bedroomZoomBed = imageScaling(0,0,bedroomZoomBed,1)
recordPlayerZoomWithoutRecord = imageScaling(0, 0, recordPlayerZoom, 1)
bedroomZoomFloorboardRemoved = imageScaling(0, 0, floorboardRemovedZoomIn, 1)
recordPlayerZoom = imageScaling(0, 0, recordPlayerWithRecordZoom, 1)
bedroomZoomPainting = imageScaling(0, 0, painting, 1)
dancingManPainting = imageScaling(0,0,dancingManPainting,0.28)
lockZoom = imageScaling(150,0,lockZoom,0.8)

lockOne = imageScaling(150,0,lockOne,0.8)
lockTwo = imageScaling(150,0,lockTwo,0.8)
lockThree = imageScaling(150,0,lockThree,0.8)
lockFour = imageScaling(150,0,lockFour,0.8)
lockFive = imageScaling(150,0,lockFive,0.8)
lockSix = imageScaling(150,0,lockSix,0.8)
lockSeven = imageScaling(150,0,lockSeven,0.8)
lockEight = imageScaling(150,0,lockEight,0.8)
lockNine = imageScaling(150,0,lockNine,0.8)
lockTen = imageScaling(150,0,lockTen,0.8)
lockEleven = imageScaling(150,0,lockEleven,0.8)
lockTwelve = imageScaling(150,0,lockTwelve,0.8)
lockUnlocked = imageScaling(150, 0, lockUnlocked, 0.8)

diary = imageScaling(0,0,diary,0.29) 
#################################

#cutscene
 
 #################################
#lists
lockList = [lockOne, lockTwo, lockThree, lockFour, lockFive, lockSix, lockSeven, lockEight, lockNine, lockTen, lockEleven, lockTwelve, lockUnlocked]
lockIndex = 0
imageList = [bedroomScreen,bedroomZoomBed, diary, bedroomZoomNightstand, lockList[lockIndex], recordPlayerZoomWithoutRecord, bedroomZoomPainting, dancingManPainting, bedroomZoomFloorboard, openNightstand]
imageIndex = 0
bedroomZooms = [bedroomZoomNightstand, bedroomZoomBed, recordPlayerZoom, bedroomZoomPainting, bedroomZoomFloorboard, bedroomZoomFloorboardRemoved, recordPlayerWithRecordZoom]
#################################

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
 
menuOpen = False #will say menu is open until startButton clicked

 
zoomIn = False #checks if user zoomed into certain shelves
firstOpen = True #if user clicks bookshelf for first time, game bugs out (this is a temporary solution)
 
#################################
userCode = ''
dancingManCodeShown = False
recordPlayed = False
lockOpen = False
poemRead = False
nightstandOpen = False
#################################
 
largeSans = pygame.font.Font("chromaticron-experiments/fonts/OpenSans-Regular.ttf", 28)
 
t = 1800
timerDelay = True

while run:
  
  if not inventoryOpen: 
    imageList[imageIndex].draw()
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
 

################################# 
  bedroomBed = pygame.Rect(220, 230, 250, 110)
  bedroomNightstand = pygame.Rect(431, 170, 75, 80)
  bedroomRecordplyr = pygame.Rect(201, 157, 75, 70)
  bedroomPainting = pygame.Rect(496, 75, 40, 125)
  bedroomFloorboard = pygame.Rect(35, 340, 640, 60)
  backButtonRect = pygame.Rect(10, 10, 30, 30)
  bedroomFrame = pygame.Rect(191, 1, 314, 399)

  diaryRect = pygame.Rect(263,244,117,61)
  lockRect = pygame.Rect(440,370,20,25)
  comboLockRect = pygame.Rect(230,170,240,205)
  confirmRect = pygame.Rect(540,120,105,30)
  paintingZoomRect = pygame.Rect(200, 0, 325, 400)


  #pygame.draw.rect(surface,BLACK,bedroomBed,0)
  #pygame.draw.rect(screen, (0,0,0), bedroomBed)
  pygame.draw.rect(screen, (255,0,0), bedroomNightstand)
  pygame.draw.rect(screen, (0,255,0), bedroomRecordplyr)
  #pygame.draw.rect(screen, (0,0,255), bedroomFloorboard)
  pygame.draw.rect(screen, (0,255,255), bedroomPainting)
  
  
  if imageIndex != 0:
    backButton.draw()
  
  if imageIndex == 1:
    pygame.draw.rect(screen,(0,0,0),diaryRect)

  if imageIndex == 3:
    pygame.draw.rect(screen,(255,255,255),lockRect)

  if imageIndex == 4:
    pygame.draw.rect(screen,(0,255,0), confirmRect)
    if lockIndex == 0:
      lockOne.draw()
    elif lockIndex == 1:
      lockTwo.draw()
    elif lockIndex == 2:
      lockThree.draw()
    elif lockIndex == 3:
      lockFour.draw()
    elif lockIndex == 4:
      lockFive.draw()
    elif lockIndex == 5:
      lockSix.draw()
    elif lockIndex == 6:
      lockSeven.draw()
    elif lockIndex == 7:
      lockEight.draw()
    elif lockIndex == 8:
      lockNine.draw()
    elif lockIndex == 9:
      lockTen.draw()
    elif lockIndex == 10:
      lockEleven.draw()
    elif lockIndex == 11:
      lockTwelve.draw()
    elif lockIndex == 12:
      lockUnlocked.draw()
#################################
  
  for event in pygame.event.get():
      #pygame.quit() will run and close window
    print(event)
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.KEYDOWN:
      #This is to allow pressing the 'e' key to open the inv and then close it (should have a note telling the user this option)
      if inventoryOpen == True and event.key == pygame.K_e: #and zoomIn == False:
        print('E pressed while in inv')
        screen.fill((0, 0, 0, 0))
        '''if bibleSelected == True:
          screen.fill((BLACK))
          bibleScreen.draw()
          backButton.draw()
          bibleSelected = False
          imageIndex = 3
          '''
        imageList[imageIndex].draw()
        imageOne = True
        leftArrow.draw()
        rightArrow.draw()
        pygame.display.set_caption("Byrne Mansion")
        inventoryOpen = False
        pygame.display.update()
       
      elif inventoryOpen == False and menuOpen == False and event.key == pygame.K_e: #and zoomIn == False:
        print("E pressed")
        screen.fill((0, 0, 0, 0))
        inventoryBackground.draw()
        inventoryIcon.draw()
        inventoryIcon2.draw()
        inventoryHotbar.draw()
        pygame.display.set_caption("Inventory")
        #pygame.event.pump()
        print("Inventory drawn")
        inventoryOpen = True
        inventoryBorder = pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(197, 297, 300, 105), 2)
        inventoryTextThing.draw()
        pygame.display.update()
        try:
          if inventory[0] == 'Key' or inventory [1] == 'Key':
            inventoryKey.draw()
            pygame.display.update()
          '''if inventory[1] == 'Bible' or inventory[0] == 'Bible':
            bibleInvItem.draw()
            pygame.display.update()'''
        except:
          print("The key has not been obtained yet.")
 
       
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      x= pygame.mouse.get_pos()[0]
      y= pygame.mouse.get_pos()[1]
      #print(x,y)
      #leftArrowRect = pygame.Rect(100, 200, 30, 30)
      #rightArrowRect = pygame.Rect(540, 200, 30, 30)
      #backButtonMenu = pygame.Rect(10, 10, 30, 30)
 
      #if leftArrowRect.collidepoint(x,y) or rightArrowRect.collidepoint(x,y):
      #  inventoryOpen = False
 
      #################################
      if bedroomBed.collidepoint(x,y) and imageIndex == 0 and menuOpen == False and inventoryOpen == False:
        print("b e d")
        imageIndex = 1
        backButton.draw()
        print("bed drawn")

      if diaryRect.collidepoint(x,y) and imageIndex == 1 and menuOpen == False and inventoryOpen == False:
        print("diary drawn")
        screen.fill((0,0,0,0))
        imageIndex = 2
        diary.draw()
        backButton.draw()
        poemRead = True
        '''if firstOpen == True:
              zoomIn = False
              firstOpen = False'''

        #BibleRect = pygame.Rect(w, x, y, z)
        #if BibleRect.collidepoint(x, y) and inventoryOpen == False and zoomIn == True and menuOpen == False:
      """print("Bible clicked!")
        screen.fill((0, 0, 0, 0))

        inventory.append("inventoryBible")
        #pygame.mixer.Sound.play(inventoryDing)
        pygame.mixer.music.stop()
        inventory = list(set(inventory))
        print(inventory)"""
      
      if bedroomNightstand.collidepoint(x,y) and imageIndex == 0 and inventoryOpen == False and menuOpen == False and lockOpen == False:
        print("nightstand")
        imageIndex = 3
        
        backButton.draw()
        pygame.display.update()
        zoomIn = True
        lock = pygame.Rect(0, 0, screenWidth, screenHeight)

      elif bedroomNightstand.collidepoint(x, y) and imageIndex == 0 and inventoryOpen == False and menuOpen == False and lockOpen == True:
        print('open nightstand')
        imageIndex = 9
        backButton.draw()
        zoomIn = True
        pygame.display.update()

      if lockRect.collidepoint(x,y) and poemRead == True and imageIndex == 3:
        print('lock time')
        screen.fill((222,216,211))
        imageIndex = 4
        #code is 31617
      if comboLockRect.collidepoint(x,y) and imageIndex == 4:
        print("lock clicked")
        print(lockIndex)
        if lockIndex == 11:
          lockIndex = 0
        else:
          lockIndex += 1
          print("lock turned")
        print(lockIndex)
        pygame.display.update()
      if confirmRect.collidepoint(x,y):
        userCode = userCode + str(lockIndex + 1)
        print(userCode)
        if userCode =='31617':
          print('lock unlocked')
          lockIndex = 12
          lockOpen = True
          nightstandOpen = True
          pygame.display.update()
          imageIndex = 9
          pygame.display.update()
        #################################
          '''
            if recordCollect.collidepoint(x,y):
                print('Record has been touched')
                inventory[2] = 'Record'
                mixer.Sound.play(inventoryDing)
                inventory = list(set(inventory))
                print(inventory)
                pygame.display.flip()'''

                    

      if bedroomRecordplyr.collidepoint(x,y) and inventoryOpen == False and imageIndex == 0 and menuOpen == False:
        print("Record Player interacted")
        imageIndex = 5
        backButton.draw()
        pygame.display.update()
        zoomIn = True
        if firstOpen == True:
            zoomIn = False
            firstOpen = False
        if recordSelected == True and bedroomRecordplyr.collidepoint(x,y) and inventoryOpen == False and zoomIn == True:
          bedroomZooms[6].draw()
          recordOnPlyrRect = pygame.Rect(0, 0, screenWidth, screenHeight)
          if recordOnPlyrRect.collidepoint(x,y) and inventoryOpen == False and zoomIn == True:
            print('playing record')
            mixer.Sound.play('record.wav')
            recordPlayed = True

      #############################
      if bedroomPainting.collidepoint(x,y) and inventoryOpen == False and imageIndex == 0 and menuOpen == False and dancingManCodeShown == False:
        print('PAINTING TIME!')
        imageIndex = 6
        pygame.display.update()
      
      elif bedroomPainting.collidepoint(x,y) and inventoryOpen == False and imageIndex == 0 and menuOpen == False and dancingManCodeShown == True:
        imageIndex = 7
        pygame.display.update()

      if bedroomFrame.collidepoint(x, y) and imageIndex == 6:# and recordPlayed == True:
          print('Flip the Mona Lisa')
          imageIndex = 7
          dancingManCodeShown = True
      ################################

      if bedroomFloorboard.collidepoint(x,y) and inventoryOpen == False and imageIndex == 0 and dancingManCodeShown == True:
        print("f l o o r")
        imageIndex = 8
        backButton.draw()
        zoomIn = True
        removableFloorboard = pygame.Rect(0 , 0, screenWidth, screenHeight)
        if removableFloorboard.collidepoint(x,y) and inventoryOpen == False and zoomIn == True and dancingManCodeShown == True:
          bedroomZooms[5].draw()
        #pygame.rect(BLACK)

        #if DancingMenRect.collidepoint(x, y) and inventoryOpen == False and zoomIn == True and menuOpen == False
    
      

      if backButtonRect.collidepoint(x,y):
        imageIndex = 0
        if lockOpen == True:
          userCode = '31617'
        else:
          userCode = ''
 
      #clocks
      
         
      #adds key to inventory
      
      #inventory
    if inventoryOpen == True:
        x= pygame.mouse.get_pos()[0]
        y= pygame.mouse.get_pos()[1]
        slotOneRect = pygame.Rect(196, 296, 45, 56)
        slotTwoRect = pygame.Rect(254, 296, 45, 56)
        if slotOneRect.collidepoint(x,y):
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
        if slotTwoRect.collidepoint(x,y):
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
  pygame.display.update()
 
    
 
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
