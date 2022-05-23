def scene0():
  from pygame import mixer
  import pygame
  import sys
  import textwrap
  #this music is mainly to test unless it is widely accepted. If using headphones make sure to click the check box at the bottom right of the game window
  global userNameEntered
  global userText
  mixer.init()
  mixer.music.load('assets/sounds/music/bgMusic.mp3')
  mixer.music.set_volume(11)

  WINDOW_WIDTH = 700
  WINDOW_HEIGHT = 400
  animationDone = False
  clock = pygame.time.Clock()
  pygame.init()
  screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
  dialogBox = pygame.image.load("experimental/dialogueBox.png").convert()
  mansionImage = pygame.image.load("experimental/mansionImage.jpg").convert()
  userBox = pygame.image.load("experimental/dialogBox.png").convert()

  WHITE = (255, 255, 255)
  BLACK = (0, 0, 0)
  BROWN = (111, 78, 55)
  color_inactive = pygame.Color('lightskyblue3')
  color_active = pygame.Color('red1')
  

  def display_text_animation(string,x,y):
      text = ''
      for i in range(len(string)):
          text += string[i]
          screen.fill(BROWN)
          font = pygame.font.Font("fonts/OpenSans-Regular.ttf", 17)
          text_surface = font.render(text, True, WHITE)
          mansionImage.draw()
          dialogBox.draw()
          text_rect = text_surface.get_rect()
          text_rect.center = (x, y)
          screen.blit(text_surface, text_rect)
          pygame.display.update()
          pygame.time.wait(1)

  largeSans = pygame.font.Font("fonts/OpenSans-Regular.ttf", 40)
    
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

  dialogBox = imageScaling(40, 290, dialogBox, 0.4)
  mansionImage = imageScaling(130, 0, mansionImage, 0.65)
  userBox = imageScaling(30, 160, userBox, 0.4)

  def fadeout():
    global animationDone
    animationDone = True
    fadeout = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    fadeout = fadeout.convert()
    fadeout.fill(BLACK)
    for i in range(255):
      fadeout.set_alpha(i)
      screen.blit(fadeout, (0, 0))
      pygame.display.update()
    
  cutScene = True
  mixer.music.play(1)
  display_text_animation('It all started long ago...',320,315)
  pygame.time.wait(1000)
  display_text_animation("with a rich mansion owner...",320,315)

  archibaldIntro = textwrap.wrap("Archibald Byrne III was an eccentric man, thought of as a legend. After all, Byrne Mansion and its owner were by far the most interesting things in the little town of Asheville. Archibald Byrne III was a devout Christian that enjoyed spending his time either with puzzles or engrained in his mathematic research, until....",70, break_long_words = False)

  for line in archibaldIntro:
    display_text_animation(line,320,315)
    
  print(archibaldIntro)

  #display_text_animation()
  pygame.time.wait(5000)
  display_text_animation("The mansion burned down in a mysterious fire...",320,315)
  pygame.time.wait(300)
  display_text_animation("with Archibald in a deep slumber inside.", 320,315)
  pygame.time.wait(500)
  display_text_animation("No one knew the cause, even nearly a hundred years later...",320,315)
  pygame.time.wait(500)
  display_text_animation("Regardless, the tale of Mr. Byrne has never been forgotten...",320,315)
  pygame.time.wait(500)
  display_text_animation("Some say his ghost still haunts the mansion to this day...",320,315)
  pygame.time.wait(500)
  display_text_animation("Many folks have tried to explore the mansion...", 320,315)
  pygame.time.wait(500)
  display_text_animation("Some searched out of curiosity, others for bragging rights.", 320, 315)
  pygame.time.wait(500)
  display_text_animation("But none have ever resurfaced from the depths of the ruined building.",320,315)
  pygame.time.wait(1500)

  display_text_animation("Eighty-five years later, you and your friends pass by Byrne Mansion...", 320,315)
  pygame.time.wait(500)
  display_text_animation("Your friend dares you to enter the wicked Mansion...", 320, 315)
  pygame.time.wait(500)
  display_text_animation("And you foolishly accept...", 320,315)

  # mixer.music.pause()
  fadeout()
  # mixer.music.resume()
  pygame.time.wait(5000)

  display_text_animation("Upon stepping foot into the mansion...", 320,315)
  pygame.time.wait(500)
  display_text_animation("a mystical force drags you deeper and into the library...", 320,315)
  pygame.time.wait(500)
  display_text_animation("The door flips inside-out, and reality begins to sink in...", 320,315)
  pygame.time.wait(500)
  display_text_animation("You have time-warped into the past...", 320, 315)
  pygame.time.wait(500)
  display_text_animation("And you must locate the key to the Mansion's door...", 320, 315)
  pygame.time.wait(500)
  display_text_animation("Otherwise, you'll be engulfed by the flames...", 320, 315)
  pygame.time.wait(500)

  fadeout()
  #are we going to describe the cutscene part of going into the mansion, old decor/furniture, door flips/locks, or no? -titiksha
  #I agree with explaining that. its very important or else the key would be unessecary to escape

  """
  display_text_animation("As you enter the mansion, you are mysteriously pushed forward...", 320,315)
  pygame.time.wait(500)
  display_text_animation("and the door flipped inside out.", 320,315)
  pygame.time.wait(500)
  display_text_animation("Now the only way to get out is to find the key which opens the door...", 320,315)
  pygame.time.wait(500)
  display_text_animation("With nowhere else to go, you reluctantly enter the library.", 315, 320)
  '''
  #not too sure about this portion. If you guys want it we can keep it.
  display_text_animation("To do what no one else could...", 320,315)
  pygame.time.wait(500)
  display_text_animation("and live your predecessor's dreams.", 320,315)'''
  """

  mixer.music.stop()
  mixer.music.load('assets/sounds/music/SelectionMusic.mp3')
  mixer.music.play()
  cutScene = False
  run = True
  userText = ''
  font = pygame.font.Font('fonts/OpenSans-Regular.ttf', 32)
  clickedBox = False
  textBox = pygame.Rect(30, 155, 630, 135)
  userNameEntered = False

  while run:
    if cutScene == False:
        userNameText = largeSans.render("Enter your username to proceed...", True, (WHITE))
        directions = largeSans.render("Press RETURN when done.", True, (WHITE))
        screen.blit(userNameText, (20, 20))
        screen.blit(directions, (20, 320))
        pygame.display.update()
      
    for event in pygame.event.get():
      print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
        
    
      if event.type == pygame.MOUSEBUTTONDOWN:
          if textBox.collidepoint(event.pos):
              clickedBox = True
          else:
              clickedBox = False
            
      if clickedBox == True:
        if event.type == pygame.KEYDOWN:

          # Check for backspace
          if event.key == pygame.K_BACKSPACE:
              userText = userText[:-1]
          elif event.key == pygame.K_RETURN:
            if len(userText) >= 15:
              print("Username is too long, please enter something shorter")
              userNameEntered = False
            elif userText == "":
              print("Enter a username")
              userNameEntered = False
            elif userText != "":
              print('You are ready to begin your quest, ' + str(userText))
              userNameEntered = True
              return userText
              return userNameEntered
          else:
              userText += event.unicode
            
      if clickedBox:
          color = color_active
      else:
          color = color_inactive
      pygame.draw.rect(screen, color, textBox)

      text_surface = font.render(userText, True, WHITE)
      screen.blit(text_surface, (textBox.x+5, textBox.y+5))
      textBox.w = max(650, text_surface.get_width()+10)
      pygame.display.flip()
      clock.tick(60)
      mixer.music.stop()