import pygame
from sys import exit
from random import randint

#==================================================================
#Functions
#==================================================================

def fileToSprite(file_path, width, height):
    '''Converts File to sprite by loading and scaling'''
    image = pygame.image.load(file_path).convert_alpha()
    image = pygame.transform.scale(image, (width, height))
    return image

def handleButton(buttonRect, handImage, handRect, choiceName, moveFlag):
    '''moves sprite in frame is button is clicked'''
    if buttonRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        moveFlag = True
        global choice1
        choice1 = choiceName

    if moveFlag:
        screen.blit(handImage, handRect)
        if handRect.right <= 400:
            handRect.x += 30
        else:
            moveFlag = False
            global firstChoiceStatus
            firstChoiceStatus = True
    screen.blit(handImage, handRect)
    return moveFlag

def handleButton2(buttonRect, handImage, handRect, choiceName, moveFlag):
    '''Same function as previous but announces a different global function'''
    if buttonRect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
        moveFlag = True
        global choice2
        choice2 = choiceName

    if moveFlag:
        screen.blit(handImage, handRect)
        if handRect.right <= 400:
            handRect.x += 30
        else:
            moveFlag = False
            global secondChoiceStatus 
            secondChoiceStatus = True
    screen.blit(handImage, handRect)
    return moveFlag

def botHandle(handImage, handRect, moveFlag):
    '''moves bot hands based on choices'''
    moveFlag = True
    if moveFlag:
        screen.blit(handImage, handRect)
        if handRect.right >= 1500:
            handRect.x -= 30
        else:
            moveFlag = False
            global initiateRound2
            initiateRound2 = True
    screen.blit(handImage, handRect)
    return moveFlag

def lastOneRemains(HandRect):
    if HandRect.right != 0:
        HandRect.x -=30

def compare(player, computer):
    if player == computer:
        return "It's a tie!"
    elif player == 'Rock' and computer == 'Scissors':
        return "win"
    elif player == 'Paper' and computer == 'Rock':
        return "win"
    elif player == 'Scissors' and computer == 'Paper':
        return "win"
    elif computer == 'Rock' and player == 'Scissors':
        return "lose"
    elif computer == 'Paper' and player == 'Rock':
        return "lose"
    elif computer == 'Scissors' and player == 'Paper':
        return "lose"

def move_bot_hand(moveType, leftHandRect, rightHandRect):
    global botMovement, botRound2

    if moveType:
        if leftHandRect.left < 1470:
            leftHandRect.x += 30
        if rightHandRect.left < 1470:
            rightHandRect.x += 30
        elif leftHandRect.left >= 1470 and rightHandRect.left >= 1470:
            moveType = False
            botRound2 = True
    return moveType

#==================================================================
#initialization
#==================================================================

pygame.init()
screen = pygame.display.set_mode((1470, 800)) 
pygame.display.set_caption("Rock-Paper-Scissors-Minus-One")
run = True
game_icon = pygame.image.load("./assets/game_icon.png") 
pygame.display.set_icon(game_icon)
background = pygame.image.load("./assets/background.png").convert() #load background image
background = pygame.transform.scale(background, (1470, 800)) #scale background image to fit the screen
clock = pygame.time.Clock() #create a clock object to control the frame rate

font = pygame.font.Font("./assets/Game Of Squids.ttf", 30) #load font *use font.render('<text>', <AntiAlias either True or False>, '<Color>') to type something
score_surface = font.render("Score: ", True, (255, 255, 255)) #create a surface for the score text
score_rect = score_surface.get_rect(topleft=(50, 50)) #create a rect for the score text


#==================================================================
#Game photos
#==================================================================
menuButton = fileToSprite('./assets/menu.png', 102, 67)
paperButton = fileToSprite("./assets/paper_icon.png", 120, 120)
rockButton = fileToSprite("./assets/rock_icon.png", 120, 120)
scissorsButton = fileToSprite("./assets/scissor_icon.png", 120, 120)
helpButton = fileToSprite("./assets/help.png", 82, 85)
logo = fileToSprite("./assets/logo.png", 1050, 50)
                           #hand images
rockLHand = fileToSprite("./assets/RockHand.png", 445, 229)  
paperLHand = fileToSprite("./assets/paperHand.png", 490, 252)
scissorLHand = fileToSprite("./assets/ScissorHand.png", 445, 229)
rockRHand = fileToSprite("./assets/RockHandARIght.png", 445, 229)
paperRHand = fileToSprite("./assets/PaperHandRIght.png", 490, 252)
scissorRHand = fileToSprite("./assets/ScissorHandRight.png", 445, 229)

botRockL = fileToSprite("./assets/robotRock.png", 455, 308)
botPaperL = fileToSprite("./assets/robotPaper.png", 455, 308)
botScissorL = fileToSprite("./assets/robotScissors.png", 455, 308)
botRockR = fileToSprite("./assets/robotBottomRock.png", 455, 308)
botPaperR = fileToSprite("./assets/robotBottomPaper.png", 455, 308)
botScissorR = fileToSprite("./assets/robotBottomScissors.png", 455, 308)

#==================================================================
#photo rects
#==================================================================

#menuButtonRect = menuButton.get_rect(topleft=(20, 10))
rockButtonRect = rockButton.get_rect(midtop=(500, 550))
paperButtonRect = paperButton.get_rect(midtop=(735, 550))
scissorsButtonRect = scissorsButton.get_rect(midtop=(970, 550))
#helpButtonRect = helpButton.get_rect(topleft=(1348, 675))
#logoRect = logo.get_rect(topleft=(200, 100))

#hand rects
rockLHandRect = rockLHand.get_rect(midright=(0, 200))
paperLHandRect = paperLHand.get_rect(midright=(0, 200))
scissorLHandRect = scissorLHand.get_rect(midright= (0, 200))
rockRHandRect = rockRHand.get_rect(midright=(0, 600))
paperRHandRect = paperRHand.get_rect(midright=(0, 600))
scissorRHandRect = scissorRHand.get_rect(midright=(0, 600))

botRockLRect = botRockL.get_rect(midleft=(1470, 200))
botPaperLRect = botPaperL.get_rect(midleft=(1470, 200))
botScissorLRect = botScissorL.get_rect(midleft=(1470, 200))
botRockRRect = botRockR.get_rect(midleft=(1470, 600))
botPaperRRect = botPaperR.get_rect(midleft=(1470, 600))
botScissorRRect = botScissorR.get_rect(midleft=(1470, 600))

#==================================================================
#initial positions
#==================================================================
moveRock = False
movePaper = False
moveScissors = False
move = False
firstChoiceStatus, secondChoiceStatus  = False, False
choice1, choice2 = None, None
finalChoiceStatus = False
finalChoice = None

botStatus = False
botChoice1, botChoice2 = None, None
finalComputerChoice = None
firstRound = True
initiateRound2 = None
secondRound = False

finalMove = False
botChoice = []
botMovement = None

botMoveRock = None
botMovePaper = None
botMoveScissors = None

gatePaper = False
gateScissors = False
gateRock = False
botRound2 = None


#==================================================================
#Markov chain tracker for Rock Paper Scissors Minus 1
#==================================================================
options = ('Rock','Paper','Scissors')
transition_counts = {
    "Rock": {"Rock": 0, "Paper": 0, "Scissors": 0},
    "Paper": {"rock": 0, "Paper": 0, "Scissors": 0},
    "Scissors": {"rock": 0, "Paper": 0, "Scissors": 0}
}
last_move = None

def predict_player_move():
    global last_move
    if last_move is None:  
        return options[randint(0, 2)]

    predicted_move = max(transition_counts[last_move], key=transition_counts[last_move].get)

    counter_moves = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}
    return counter_moves[predicted_move]

#==================================================================
#Game loop
#==================================================================

while run == True:
    menu = False
    rpsM1 = True
    help = False
    for game_event in pygame.event.get(): #checks for events in the game
        if game_event.type == pygame.QUIT:
            run = False
    screen.blit(background, (0, 0)) #draws the background image on the screen
    
    #==================================================================
    #Rock paper scissors minus one
    #==================================================================
    if rpsM1 == True:
        #default variables
        computerScore = 0
        playerScore = 0
        
        screen.blit(menuButton, (20, 10))
        if firstRound:
            screen.blit(rockButton, rockButtonRect)
            screen.blit(paperButton, paperButtonRect)
            screen.blit(scissorsButton, scissorsButtonRect)
        
        #Player Picks
        if firstChoiceStatus == False:
            moveRock = handleButton(rockButtonRect, rockLHand, rockLHandRect, "Rock", moveRock)
            movePaper = handleButton(paperButtonRect, paperLHand, paperLHandRect, "Paper", movePaper)
            moveScissors = handleButton(scissorsButtonRect, scissorLHand, scissorLHandRect, "Scissors", moveScissors)
        else:
            screen.blit(rockLHand, rockLHandRect)
            screen.blit(paperLHand, paperLHandRect)
            screen.blit(scissorLHand, scissorLHandRect)
        
        if firstChoiceStatus == True and secondChoiceStatus == False:
            moveRock = handleButton2(rockButtonRect, rockRHand, rockRHandRect, "Rock", moveRock)
            movePaper = handleButton2(paperButtonRect, paperRHand, paperRHandRect, "Paper", movePaper)
            moveScissors = handleButton2(scissorsButtonRect, scissorRHand, scissorRHandRect, "Scissors", moveScissors)
        else:
            screen.blit(rockRHand, rockRHandRect)
            screen.blit(paperRHand, paperRHandRect)
            screen.blit(scissorRHand, scissorRHandRect)

        if firstChoiceStatus == True and secondChoiceStatus == True:
            firstRound = False

        #bot picks
        if firstChoiceStatus == True and secondChoiceStatus == True and botStatus == False:
            botChoice1 = predict_player_move()
            botChoice2 = predict_player_move()
            botStatus = True
        
        if botChoice1 == 'Rock': moveFlag = botHandle(botRockL, botRockLRect, move)
        elif botChoice1 == 'Paper': moveFlag = botHandle(botPaperL, botPaperLRect, move)
        elif botChoice1 == 'Scissors': moveFlag = botHandle(botScissorL, botScissorLRect, move)
        if botChoice2 == 'Rock': moveFlag = botHandle(botRockR, botRockRRect, move)
        elif botChoice2 == 'Paper': moveFlag = botHandle(botPaperR, botPaperRRect, move)
        elif botChoice2 == 'Scissors': moveFlag = botHandle(botScissorR, botScissorRRect, move)

        if initiateRound2:
            if rockLHandRect.right >= 400 or rockRHandRect.right >= 400:
                screen.blit(rockButton, rockButtonRect)
            if paperLHandRect.right >= 400 or paperRHandRect.right >= 400:
                screen.blit(paperButton, paperButtonRect)
            if scissorLHandRect.right >= 400 or scissorRHandRect.right >= 400:
                screen.blit(scissorsButton, scissorsButtonRect)

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()[0]

            if rockButtonRect.collidepoint(mouse_pos) and mouse_pressed:
                finalChoice = 'Rock'
                movePaper = True
                moveScissors = True
                gateRock = True

            elif paperButtonRect.collidepoint(mouse_pos) and mouse_pressed:
                finalChoice = 'Paper'
                moveRock = True
                moveScissors = True
                gatePaper = True
            elif scissorsButtonRect.collidepoint(mouse_pos) and mouse_pressed:
                finalChoice = 'Scissors'
                movePaper = True
                moveRock = True  
                gateScissors = True
            if movePaper:
                if paperRHandRect.right > 0:
                    paperRHandRect.x -= 60
                if paperLHandRect.right > 0:
                    paperLHandRect.x -= 60 
                if paperRHandRect.right <= 0 and paperLHandRect.right <= 0:
                    movePaper = False
                    gatePaper = True
    
            if moveScissors:
                if scissorRHandRect.right > 0:
                    scissorRHandRect.x -= 60
                if scissorLHandRect.right > 0:
                    scissorLHandRect.x -= 60
                if scissorRHandRect.right <= 0 and scissorLHandRect.right <= 0:
                    moveScissors = False
                    gateScissors = True

            if moveRock:
                if rockRHandRect.right > 0:
                    rockRHandRect.x -= 60
                if rockLHandRect.right > 0:
                    rockLHandRect.x -= 60
                if rockRHandRect.right <= 0 and rockLHandRect.right <= 0:
                    moveRock = False
                    gateRock = True
            if gateRock == True and gatePaper == True and gateScissors == True:
                botRound2 = True
                finalComputerChoice = True
                gatePaper = False
                gateScissors = False
                gateRock = False
                initiateRound2 = False
        if botRound2:
            if finalComputerChoice :
                botChoice = [botChoice1, botChoice2]
                botChoice = botChoice[randint(0,1)]
                if botChoice == 'Rock':
                    botMovePaper = True
                    botMoveScissors = True
                    botRound2 = False
                elif botChoice == 'Paper':
                    botMoveScissors = True
                    botMoveRock = True
                    botRound2 = False
                elif botChoice == 'Scissors':
                    botMovePaper = True
                    botMoveRock = True
                    botRound2 = False
                finalComputerChoice = False

        elif botRound2 == False:
            if botMovePaper: 
                if botPaperRRect.right <= 1470:
                    botPaperRRect.x += 60
                if botPaperLRect.right <= 1470:
                    botPaperLRect.x += 60 
                if botPaperRRect.right >= 1470 and botPaperLRect.right >= 1470:
                    botMovePaper = False
            if botMoveRock:
                if botRockRRect.right <= 1470:
                    botRockRRect.x += 60
                if botRockLRect.right <= 1470:
                    botRockLRect.x += 60
                if botRockRRect.right >= 1470 and botRockLRect.right >= 1470:
                    botMoveRock = False

            if botMoveScissors:
                if botScissorRRect.right <= 1470:
                    botScissorRRect.x += 60
                if botScissorLRect.right <= 1470:
                    botScissorLRect.x += 60
                if botScissorRRect.right >= 1470 and botScissorLRect.right >= 1470:
                    botMoveScissors = False

            if botMoveScissors == False and botMoveRock == False and botMovePaper == False:
                print(compare(finalChoice, botChoice))

            
            
    


    

        

        
        


        

        
        
                
    
    pygame.display.update() #updates the screen
    clock.tick(60)



pygame.quit() 

exit()

    


