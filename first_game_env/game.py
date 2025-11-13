import pygame
import sys
import os

pygame.init()

def gameQuit():   # Game Quit function
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
def startAnime(mainScreen, startAnimeElements, clock): # Start Animation function
    
    checkTime = pygame.time.get_ticks()
    animeDuration = 6000

    while (pygame.time.get_ticks() - checkTime) < animeDuration:
        
        gameQuit()

        logoRect = startAnimeElements["image"].get_rect(center=(startAnimeElements["coordinates"]["axisX"], startAnimeElements["coordinates"]["axisY"] - 50))
        
        logoNameRender = startAnimeElements["fonts"]["button"].render(startAnimeElements["compName"], True, (220, 220, 220))
        
        logoNameRect = logoNameRender.get_rect(center=(startAnimeElements["coordinates"]["axisX"], startAnimeElements["coordinates"]["axisY"] + 20))
        
        elepsed = (pygame.time.get_ticks() - checkTime) / animeDuration        
        progress = elepsed * 255
        
        startAnimeElements["image"].set_alpha(progress)
        logoNameRender.set_alpha(progress)
        mainScreen.fill((0, 0, 0))
        mainScreen.blit(startAnimeElements["image"],(logoRect))
        mainScreen.blit(logoNameRender,(logoNameRect))
        
        pygame.display.update()
        clock.tick(60)

def formPage(mainScreen, formElmt, clock) :
    
    pygame.draw.rect(formElmt["design"]["formBox"],(235,235,235,125),(0,0,350,460),border_radius=15)
    pygame.draw.rect(formSurf,(225,225,225),(20,120,310, 32),border_radius=8)
    pygame.draw.rect(formSurf,(225,225,225),(20,190,310, 32),border_radius=8)
    pygame.draw.rect(formSurf,(225,225,225),(20,260,310, 32),border_radius=8)
    pygame.draw.rect(formSurf,(225,225,225),(20,330,310, 32),border_radius=8)
    pygame.draw.rect(formSurf,(0,0,235),(45, 372, 260, 40), border_radius= 8)
    
    formX = formElmt["design"]["coordinates"]["axisX"] - formElmt["design"]["formBox"].get_width() // 2
    formY = formElmt["design"]["coordinates"]["axisY"] - formElmt["design"]["formBox"].get_height() // 2
    
    titleRect = formElmt["register"]["title"].get_rect(midtop=(formElmt["design"]["formBox"].get_width() // 2, 10))
    lableNameRect = formElmt["register"]["lable"][0].get_rect(midtop=(formElmt["design"]["formBox"].get_width() // 4.5, 90))
    lableAgeRect = formElmt["register"]["lable"][1].get_rect(midtop=(formElmt["design"]["formBox"].get_width() // 6.8, 160))
    lableEmailRect = formElmt["register"]["lable"][2].get_rect(midtop=(formElmt["design"]["formBox"].get_width() // 6.2, 230))
    lablePassRect = formElmt["register"]["lable"][3].get_rect(midtop=(formElmt["design"]["formBox"].get_width() // 4.5, 300))
    submitRect = formElmt["register"]["submit"].get_rect(midtop=(formElmt["design"]["formBox"].get_width() // 2, 370))
    lableTextRect = formElmt["register"]["lable"][4].get_rect(midtop=(formElmt["design"]["formBox"].get_width() // 2.5, 430))
    lableLogRect = formElmt["register"]["lable"][5].get_rect(midtop=(formElmt["design"]["formBox"].get_width() // 2 + 100, 430))
    
    formElmt["design"]["formBox"].blit(formElmt["register"]["title"],titleRect)
    formElmt["design"]["formBox"].blit(formElmt["register"]["lable"][0],lableNameRect)
    formElmt["design"]["formBox"].blit(formElmt["register"]["lable"][1],lableAgeRect)
    formElmt["design"]["formBox"].blit(formElmt["register"]["lable"][2],lableEmailRect)
    formElmt["design"]["formBox"].blit(formElmt["register"]["lable"][3],lablePassRect)
    formElmt["design"]["formBox"].blit(formElmt["register"]["submit"],submitRect)
    formElmt["design"]["formBox"].blit(formElmt["register"]["lable"][4],lableTextRect)
    formElmt["design"]["formBox"].blit(formElmt["register"]["lable"][5],lableLogRect)
    
    
    while True:
        gameQuit()
        mainScreen.fill((180,180,180))
        mainScreen.blit(formElmt["design"]["formBox"],(formX,formY + 60))
        pygame.display.update()
        clock.tick(60)

mainScreen = pygame.display.set_mode((1120, 640))
pygame.display.set_caption("Number Hunt")
clock  = pygame.time.Clock()
os.path.join(os.getcwd(),"Poppins")

fonts = {
    "title" : pygame.font.Font("Poppins/Poppins-Bold.ttf",40),
    "subtitle" : pygame.font.Font("Poppins/Poppins-Medium.ttf",32),
    "button" : pygame.font.Font("Poppins/Poppins-Regular.ttf",20),
    "text" : pygame.font.Font("Poppins/Poppins-Light.ttf",16),
    "small" : pygame.font.Font("Poppins/Poppins-Thin.ttf",12)
   }

centerX = mainScreen.get_width() // 2
centerY =mainScreen.get_height() //2

logo = pygame.image.load("logo.png").convert_alpha()
imageLogo = pygame.transform.scale(logo, (70, 70))

formSurf = pygame.Surface((350, 460),pygame.SRCALPHA)

startAnimeElements = { # This is for starting animation dictionary
    "image" : imageLogo,
    "fonts" : fonts,
    "compName" : "Redent Games World",
    "coordinates" : {
        "axisX" : centerX,
        "axisY" : centerY
    }
}

formElmt = {  # This is for formpage means login or sign Up page dictionary
    "design" : {
        "bgColor" : (173, 216, 230),
        "image" : imageLogo,
        "font" : fonts,
        "title" : "Number Hunt",
        "quote" : '“Numbers may look silent,but each one hides a secret waiting to be hunted. Sharpen your mind — the hunt begins now.”',
        "coordinates" : {
        "axisX" : centerX,
        "axisY" : centerY
        },
        "formBox" : formSurf
    },
    "register" : {
        "title" : fonts["subtitle"].render("Register",True,(0,0,0)),
        "lable" : 
            [fonts["button"].render("Fullname",True,(0,0,0)),
             fonts["button"].render("Age",True,(0,0,0)),
             fonts["button"].render("Email",True,(0,0,0)),
             fonts["button"].render("Password",True,(0,0,0)),
             fonts["text"].render("Already have an account?",True,(30,30,30)),
             fonts["text"].render("Sign In",True,(0,0,238))],
        "submit" :fonts["subtitle"].render("Submit",True,(255,255,255))
    }
}


startAnime(mainScreen, startAnimeElements, clock)
formPage(mainScreen, formElmt, clock)

# while True:
#     gameQuit()
#     # mainScreen.fill("red")
#     pygame.display.update()
#     clock.tick(60)