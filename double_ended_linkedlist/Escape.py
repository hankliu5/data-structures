from DarkRoom import DarkRoom
import sys

game = DarkRoom()
game.readFromFile(sys.argv[1])
game.escapeDarkroom('stack')
game.clear()
game.escapeDarkroom('queue')
