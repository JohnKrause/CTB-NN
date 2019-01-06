import CTBGame
def ComputeOptimalPlay(numsets, maxroll, numtests):
    results=[]
    for i in range (0,numsets):
        #build game state as binary representation of current set number
        gamestate=[1,1,1,1,1,1,1,1,1,1]
        num=i
        #computer num to binary representation, index 1 of gamestate = 2^0
        for tindex in range(0,10):
            #for this algorithm to work we need to start at 2^9 position
            index = 9-tindex
            if not( int(num/(2**index))==0 ):
                num=num%(2**index)
                #index 0 of gamestate should be ignored, 2^0 is at index 1
                gamestate[index+1]=0
        #create game with chosen random state
        #roll the dice a large number of times
        for roll in range(2,maxroll+1):
            Game=CTBGame.Game(gamestate[1],gamestate[2],gamestate[3],gamestate[4],
                      gamestate[5],gamestate[6],gamestate[7],gamestate[8],
                      gamestate[9])
            #set the dice to the correct value
            Game.startturn_cheat(roll)
            #get possible moves
            availmoves=Game.showmoves()
            #For each available move, perform montecarlo to determine failure chance of making that move
            testedmoves=[]
            for move in availmoves:
                #make the specific move
                Game.makemove(move)
                #make a random roll and see if we lost
                #computer what portion of rolls would make us fail in this situation
                fails=0
                for test in range(0,numtests):
                    Game.startturn()
                    if (Game.gameover()==1):
                        #This was a loss
                        fails = fails+1
                #determined fail chance for this situation, store that chance and the move
                testedmoves.append([move,(1-(fails/numtests))])
                #reset game to starting state
                Game=CTBGame.Game(gamestate[1],gamestate[2],gamestate[3],gamestate[4],
                      gamestate[5],gamestate[6],gamestate[7],gamestate[8],
                      gamestate[9])
                Game.startturn_cheat(roll)
            #We've now tried all moves for this particular dice roll
            #we found the move with highest chance of success, make note of that move
            print(gamestate)
            results.append([gamestate[1],gamestate[2],gamestate[3],gamestate[4],
                      gamestate[5],gamestate[6],gamestate[7],gamestate[8],
                      gamestate[9],roll,testedmoves])
            #now reset game to previous state and roll again to test another set of possible moves
    return results