
import turtle #imported turtle module
wind = turtle.Screen()#initialize screen
wind.title("Ping Pong")#set the title of the window
wind.bgcolor("black")# set the backeground of the window
wind.setup(width= 800, height= 400)#set the width and height of the window
wind.tracer(0)#stops the window from updating automatically
#main game loop
while True:
    wind.update()#updates the screen everytime the loop run
