import xmixclass

if __name__ == "__main__":

    game = xmixclass.Board(4)

    # display.grid
    while True:

        game.display()
        game.next_move()
        game.changeplayer()
        result = game.victory()
        if result[0] != xmixclass.Gameresult.none:
            break
            
    #
    # comment 1 : The results should take all options :
    #
    match result[0]:
        case Gameresult.row:
            print(f"The winner is player: {result[1]} on  row {result[1]}")
        case Gameresult.col:
            print(f"The winner is player: {result[1]} on  column {result[1]}")
        case Gameresult.left:
            print(f"The winner is player: {result[1]} on  diagonal left")
        case Gameresult.right:
            print(f"The winner is player: {result[1]} on  diagonal right")
        case Gameresult.teko:
            print(f"No winners this is a teko")
        case _:
            print("Game internal error: ",result)
            
    #print(f" the winner is player: {result[1]} in mode: {result[0]} on row {result[2]+1}")
    #result = game.victory()
    #print(result)





