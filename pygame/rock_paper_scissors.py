import pygame
from sys import exit
from random import randint

#==================================================================
#Functions
#==================================================================
last_click_time = 0
CLICK_COOLDOWN = 200 
def fileToSprite(file_path, width, height):
    '''Converts File to sprite by loading and scaling'''
    image = pygame.image.load(file_path).convert_alpha()
    image = pygame.transform.scale(image, (width, height))
    return image

def handleButton(buttonRect, handImage, handRect, choiceName, moveFlag):
    global last_click_time
    
    current_time = pygame.time.get_ticks()
    mouse_pressed = pygame.mouse.get_pressed()[0]
    mouse_over = buttonRect.collidepoint(pygame.mouse.get_pos())
    
    # Only register click if cooldown has passed
    if mouse_over and mouse_pressed and (current_time - last_click_time > CLICK_COOLDOWN):
        last_click_time = current_time
        moveFlag = True
        global choice1
        choice1 = choiceName

    if moveFlag:
        screen.blit(handImage, handRect)
        if handRect.right <= 400:
            handRect.x += 60
        else:
            moveFlag = False
            global firstChoiceStatus
            firstChoiceStatus = True
    screen.blit(handImage, handRect)
    return moveFlag

def handleButton2(buttonRect, handImage, handRect, choiceName, moveFlag):
    global last_click_time
    
    current_time = pygame.time.get_ticks()
    mouse_pressed = pygame.mouse.get_pressed()[0]
    mouse_over = buttonRect.collidepoint(pygame.mouse.get_pos())
    
    # Only register click if cooldown has passed
    if mouse_over and mouse_pressed and (current_time - last_click_time > CLICK_COOLDOWN):
        last_click_time = current_time
        moveFlag = True
        global choice2
        choice2 = choiceName

    if moveFlag:
        screen.blit(handImage, handRect)
        if handRect.right <= 400:
            handRect.x += 60
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
        if handRect.right > 1470:
            handRect.x -= 30
        else:
            moveFlag = False
            global initiateRound2, botMove
            initiateRound2 = True
            botMove = False
    screen.blit(handImage, handRect)
    return moveFlag

def compare(player, computer):
    if player == computer:
        return "tie"
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

def move_bot_object(botObjectRRect, botObjectLRect, botMoveFlag):
    if botMoveFlag:
        if botObjectRRect.left <= 1470:
            botObjectRRect.x += 60
        if botObjectLRect.left <= 1470:
            botObjectLRect.x += 60
        if botObjectRRect.left >= 1470 and botObjectLRect.left >= 1470:
            global handRetracted
            handRetracted = True
            return False  
    return botMoveFlag  

def retract_hand(handRRect, handLRect, moveFlag, gateFlag):
    if moveFlag:
        if handRRect.right > 0:
            handRRect.x -= 60
        if handLRect.right > 0:
            handLRect.x -= 60
        if handRRect.right <= 0 and handLRect.right <= 0:
            return False, True  # Stop moving, activate gate
    return moveFlag, gateFlag  # Continue moving, keep gate unchanged


def scoreText(score, botScore):
    font = pygame.font.Font("./assets/GameOfSquids.ttf", 72) 
    scoreSurf = font.render(f"{str(score)} : {str(botScore)}", True, (0, 0, 0)) 
    scoreRect = scoreSurf.get_rect(midtop=(735, 20))
    screen.blit(scoreSurf, scoreRect)
def playerRetract(handRect):
    handRect.x -= int(300 * (1/60))  # 300 pixels per second
    if handRect.right < 0:
        handRect.right = 0

def botRetract(handRect):
    handRect.x += int(300 * (1/60))  # 300 pixels per second
    if handRect.left > 1470:
        handRect.left = 1470
        global restart
        restart = True


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

#load font *use font.render('<text>', <AntiAlias either True or False>, '<Color>') to type something

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

botMoveRock2 = None
botMovePaper2 = None
botMoveScissors2 = None

gatePaper = False
gateScissors = False
gateRock = False
botRound2 = None

botMove = None
handRetracted = None

diplayResults = None

playerScore = 0
robotScore = 0
restart = False
scoreLock = False
comparison = None
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
        scoreText(playerScore, robotScore)
        
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
            botMove = True
            botStatus = True
        if botMove == True:
            if botChoice1 == 'Rock': moveFlag = botHandle(botRockL, botRockLRect, botMoveRock)
            elif botChoice1 == 'Paper': moveFlag = botHandle(botPaperL, botPaperLRect, botMovePaper)
            elif botChoice1 == 'Scissors': moveFlag = botHandle(botScissorL, botScissorLRect, botMoveScissors)
            if botChoice2 == 'Rock': moveFlag = botHandle(botRockR, botRockRRect, botMoveRock)
            elif botChoice2 == 'Paper': moveFlag = botHandle(botPaperR, botPaperRRect, botMovePaper)
            elif botChoice2 == 'Scissors': moveFlag = botHandle(botScissorR, botScissorRRect, botMoveScissors)
        else:
            screen.blit(botRockL, botRockLRect)
            screen.blit(botPaperL, botPaperLRect)
            screen.blit(botScissorL, botScissorLRect)

            screen.blit(botRockR, botRockRRect)
            screen.blit(botPaperR, botPaperRRect)
            screen.blit(botScissorR, botScissorRRect)


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
            movePaper, gatePaper = retract_hand(paperRHandRect, paperLHandRect, movePaper, gatePaper)
            moveScissors, gateScissors = retract_hand(scissorRHandRect, scissorLHandRect, moveScissors, gateScissors)
            moveRock, gateRock = retract_hand(rockRHandRect, rockLHandRect, moveRock, gateRock)

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
                    botMovePaper2 = True
                    botMoveScissors2 = True
                elif botChoice == 'Paper':
                    botMoveScissors2 = True
                    botMoveRock2 = True
                elif botChoice == 'Scissors':
                    botMovePaper2 = True
                    botMoveRock2 = True
                finalComputerChoice = False

            botMovePaper2 = move_bot_object(botPaperRRect, botPaperLRect, botMovePaper2)
            botMoveRock2 = move_bot_object(botRockRRect, botRockLRect, botMoveRock2)
            botMoveScissors2 = move_bot_object(botScissorRRect, botScissorLRect, botMoveScissors2)

            if handRetracted:
                
                comparison = compare(finalChoice, botChoice)
                handRetracted = None
                displayResults = True
            if displayResults and not scoreLock:
                scoreLock = True
                match comparison:
                    case "tie":
                        gameEnd = True
                    case "win":
                        playerScore += 1
                        gameEnd = True
                    case "lose":
                        robotScore += 1
                        gameEnd = True
                displayResults = False
                scoreLock = False
            
            if gameEnd:
                playerRetract(rockLHandRect)
                playerRetract(paperLHandRect)
                playerRetract(scissorLHandRect)
                playerRetract(rockRHandRect)
                playerRetract(paperRHandRect)
                playerRetract(scissorRHandRect) 
                
                botRetract(botRockLRect)
                botRetract(botPaperLRect)
                botRetract(botScissorLRect)
                botRetract(botRockRRect)
                botRetract(botPaperRRect)
                botRetract(botScissorRRect)
                if restart:
                    comparison = None
                    moveRock = movePaper = moveScissors = False
                    firstChoiceStatus = secondChoiceStatus = False
                    choice1 = choice2 = None
                    botStatus = False
                    botChoice1 = botChoice2 = None
                    initiateRound2 = False
                    handRetracted = False
                    displayResults = False
                    gameEnd = False
                    restart = False
                    firstRound = True
                    scoreLock = False
                
                    rockLHandRect.midright = (0, 200)
                    paperLHandRect.midright = (0, 200)
                    scissorLHandRect.midright = (0, 200)
                    rockRHandRect.midright = (0, 600)
                    paperRHandRect.midright = (0, 600)
                    scissorRHandRect.midright = (0, 600)
                    
                    botRockLRect.midleft = (1470, 200)
                    botPaperLRect.midleft = (1470, 200)
                    botScissorLRect.midleft = (1470, 200)
                    botRockRRect.midleft = (1470, 600)
                    botPaperRRect.midleft = (1470, 600)
                    botScissorRRect.midleft = (1470, 600)
                
    pygame.display.update() 
    clock.tick(60)
pygame.quit() 
exit()

    


