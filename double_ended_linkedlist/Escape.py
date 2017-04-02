from DarkRoom import DarkRoom
import sys

"""The main function that explores the dark room with BFS and DFS"""
game = DarkRoom()
game.readFromFile(sys.argv[1])
game.escapeDarkroom('stack')
game.clear()
game.escapeDarkroom('queue')
