'''
ICS3U-01
Joey Zaka
Mr. Macanovik
Paint Project    
'''

#importing all required modules
from pygame import *
from math import *
from random import *
from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import *


#closes the Tk window
root = Tk()
root.withdraw()

init() #initializes everything for pygame ex. fonts, mixer

#width and height of the display
screen = display.set_mode((1650,950))


#Colours
BLACK =(0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
DARK_BLUE = (20,26,117)


#other variables
cols = BLACK #default colour
fillcol = WHITE #default colour for eraser
pos = 0 #for backgrounds
m = 0 #for index of music
music_choice = "False" #for playing and pausing
tool = "no tool" #default tool
running=True
omx,omy = 0,0 #old mx and my
th = 15 #default thickness/size



#empty lists
basictoolsimg = [] #this is a list where loaded images will be added
shapetool_list = [] #this is a list where all loaded shape images will be placed
stamps_loaded_small = [] #list for loaded small stamps
stamps_loaded_large = [] #list for all loaded large stamp images
bottom_tools_loaded = [] #list for all loaded bottom tools
background_loaded_small = [] #list for background images to be loaded into (smaller images)
background_loaded_large = [] #list for background images to be loaded into (larger images for canvas)
desc_loaded = [] #list to add loaded images into


#loads and blits the background pic
backPic = image.load("Images/Background.png") #loads the background image
screen.blit(backPic,(0,0)) #displays the background image


#loads and blits the logo pic
logoPic = image.load("Images/FifaLogo.png") #loads the fortnite logo
logoPic = transform.scale(logoPic,(500,150)) #the logo decreases in size
screen.blit(logoPic,(0,0)) #displays the logo, logo is shifted up by -40


#picture of the rectangle with all colours, transformed
colimg = image.load("Images/colourwheel.png")
colimg = transform.scale(colimg,(265,80))


###TOOLS
basicTools = ["Images/PencilTool.png","Images/EraserTool.png","Images/FillTool.png","Images/BrushTool.png"] #this is a list of the images of the tools (unloaded)


#this loop loads all the images, and adds the to the basictoolsimg list
for i in basicTools:
    loadbasic = image.load(i) #all images are loaded
    basictoolsimg.append(loadbasic) #all loaded images are added to the basictoolsimg list
    
toolRects = [Rect(50,175,75,75),Rect(150,175,75,75),Rect(250,175,75,75),Rect(350,175,75,75)] #this is a list of all rectangular dimensions of the tools


#line seperators
draw.line(screen,DARK_BLUE,(50,258),(425,258),5)
draw.line(screen,DARK_BLUE,(50,410),(425,410),5)
draw.line(screen,DARK_BLUE,(51,518),(425,518),5)


#SHAPES
shapesTools = ["Images/FilledRectangleIcon.png","Images/UnfilledRectangleIcon.png","Images/LineTool.png",
               "Images/FilledEllipseIcon.png", "Images/UnfilledEllipseIcon.png", "Images/clear.png",
               "Images/spraypaint.png"] #this is a list of all unloaded shape tool images



for i in shapesTools: #this loop loads all images from shapesTools list and puts them into shapetool_list
    loadshapes = image.load(i) #loads the images
    shapetool_list.append(loadshapes) #adds loaded images from loadshapes variable into this list
    
shapeRects = [Rect(51,350,50,50),Rect(106,350,50,50),Rect(161,350,50,50),
              Rect(216,350,50,50),Rect(271,350,50,50),Rect(326,350,50,50),Rect(381,350,50,50)] #list of all rectangular dimensions for the shapes tools


#stamps
stamps_images_small = ["Images/Stamps/SoccerBallSmall.png", "Images/Stamps/RonaldoSmall.png", "Images/Stamps/EALogoSmall.png","Images/Stamps/PlayerKickingBallSmall.png",
                "Images/Stamps/ManchesterUnitedSmall.png", "Images/Stamps/Fifa20LogoSmall.png"] #list of all small versionstamps


stamps_images_large = ["Images/Stamps/SoccerBallLarge.png", "Images/Stamps/RonaldoLarge.png", "Images/Stamps/EALogoLarge.png",
                        "Images/Stamps/PlayerKickingBallLarge.png", "Images/Stamps/ManchesterUnitedLarge.png", "Images/Stamps/Fifa20LogoLarge.png"] #list for large stamp images


#loading all small stamp images, adding to the list for loaded images
for i in stamps_images_small: 
    loadstamps = image.load(i)
    stamps_loaded_small.append(loadstamps)

#loading all large stamp images, adding them to the list for loaded images
for i in stamps_images_large:
    loadstamps = image.load(i)
    stamps_loaded_large.append(loadstamps)


#list rectangular dimensions of stamps
stampsRects = [Rect (51,450,60,60), Rect (114,450,60,60), Rect (177,450,60,60), Rect (239,450,60,60), Rect (301,450,60,60), Rect (363,450,60,60)]


###bottom icons
bottom_tools = ["Images/MusicPlayer.png", "Images/UndoIcon.png", "Images/RedoIcon.png",  "Images/LoadIcon.png",  "Images/SaveIcon.png", 
                 "Images/PaintBucket.png", "Images/MarkerIcon.png", "Images/SepiaIcon.png"] #list for all icon images for bottom tools

#this loop takes the images from the bottom_tools list, loads them, transforms the image to fit in the box, then adds the loaded images to the list
for i in bottom_tools:
    loadtools = image.load (i)
    loadtools = transform.scale (loadtools, (100, 100))
    bottom_tools_loaded.append (loadtools)
    

bottom_Rects = [Rect (835,840,100,100), Rect (950,840,100,100), Rect (1065,840,100,100)
                , Rect (1180,840,100,100), Rect (1295,840,100,100), Rect (1410,840,100,100), Rect (1525,840,100,100)] #list for bottom rectangular boxes



###backgrounds
background_images = ["Images/Backgrounds/Fifa19Stadium.png", "Images/Backgrounds/Fifa18Backgorund.png", "Images/Backgrounds/WalkingOntoFIeld.png"
		    , "Images/Backgrounds/Background4.png", "Images/Backgrounds/Background5.png", "Images/Backgrounds/Background6.png"] #list for all backgrounds


#this loop takes the images from the list, loads them, transforms for other list, appends to larger list
for i in background_images:
	loadimages_large = image.load(i) #loads the image for larger and smaller images
	loadimages_small = transform.scale(loadimages_large,(117,83)) #makes the images smaller for the selection
	background_loaded_small.append (loadimages_small) #adds transformed to small list
	background_loaded_large.append (loadimages_large) #original loaded image is added to large list
	
#list for all background image rects
background_Rects = [Rect (51,560,117,83), Rect (178,560,117,83), Rect (305,560,117,83), Rect (51,651,117,83), Rect (178,651,117,83), Rect (305,651,117,83)]


#descriptions
desc_images = ["Images/Descriptions/IntroDesc.png", "Images/Descriptions/PencilDesc.png", "Images/Descriptions/EraserDesc.png"
                ,"Images/Descriptions/FillDesc.png", "Images/Descriptions/BrushDesc.png", "Images/Descriptions/FIlledRectDesc.png",
                "Images/Descriptions/UnfilledRectDesc.png", "Images/Descriptions/LineDesc.png", "Images/Descriptions/FilledEllipseDesc.png", 
                "Images/Descriptions/UnfilledEllipseDesc.png", "Images/Descriptions/ClearDesc.png", "Images/Descriptions/SparyDesc.png",
                "Images/Descriptions/StampDesc.png", "Images/Descriptions/BackgroundDesc.png", "Images/Descriptions/PauseMusicDesc.png",
                "Images/Descriptions/PrevSongDesc.png", "Images/Descriptions/NextSongDesc.png", "Images/Descriptions/UndoDesc.png",
                "Images/Descriptions/RedoDesc.png", "Images/Descriptions/LoadDesc.png", "Images/Descriptions/SaveDesc.png",
                "Images/Descriptions/CompleteFillDesc.png", "Images/Descriptions/MarkerDesc.png", "Images/Descriptions/SepiaDesc.png"] #image descripions list


for i in desc_images: #this loop takes images in desc_images, loads them, adds them to desc_loaded
    load_image = image.load (i)
    desc_loaded.append (load_image)




#rectangle dimensions of canvas and palette
canvasRect = Rect(500,25,1125,800) #Determines the dimensions of the canvas for drawing
paletteRect = Rect(50,265,265,80) #The dimensions of the palette rectangle
descriptionRect = Rect(50,800,400,200) #dimensions of description rectangles
col_previewRect = Rect(330,270,90,70) #dimensions of colour preview

canvas_outline = [Rect (495, 20, 1135, 5), Rect (495, 20, 5, 810), Rect (1625, 20, 5, 810), Rect (495, 825, 1135, 5)]


draw.rect(screen,WHITE,canvasRect) #Draws the canvas



screen.blit(colimg,(50,265)) #displays colour wheel
draw.rect (screen,DARK_BLUE,(325,265,100,80))#outline for col preview
draw.rect (screen, BLACK, col_previewRect) #colour preview box


###Fonts
eaFont = font.Font("Font/EASPORTS15.ttf", 40) #loads the ea font wihtout it having to be installed in the system
arial_font = font.SysFont("Arial",40)

#rendering fonts
stampsText = eaFont.render("Stamps",True,(20,26,117)) #"stamps"
backgroundText = eaFont.render("Backgrounds",True, (20,26,117))#"backgrounds"
pixelloaction_title = eaFont.render ("Pixel Location:", True, BLACK) #"pixel location"

#transforming some text
pixelloaction_title = transform.scale (pixelloaction_title, (208, 35))

#blits the text
screen.blit(stampsText,(161,410))
screen.blit (backgroundText,(114,518))


#music
music = ["Music/(FIFA 14) John Newman - Love Me Again.mp3","Music/FIFA 18 Menu Music.mp3", "Music/KNAAN - Wavin Flag (Coca-Cola Celebration Mix).mp3",
        "Music/Muse-Supermassive Black Hole lyrics.mp3", "Music/Avicii - The Nights.mp3", "Music/(FIFA 14) Disclosure - F For You.mp3"] #list containing all music


mixer.music.load(music[m]) #loads music of m
mixer.music.play(-1) #plays and loops music


#icon and title of the window
display.set_caption("Soccer Paint")
display.set_icon(stamps_loaded_small[0])

#tools

tool_list = ["pencil", "eraser", "fill", "brush", "filled rectangle", "unfilled rectangle", "line", "filled ellipse", "unfilled ellipse"
            , "clear", "spray paint", "soccer ball stamp", "ronaldo stamp", "ea logo stamp", "player kicking ball stamp", "manchester united stamp",
            "fifa text stamp", "undo", "redo", "load", "save", "complete fill", "marker", "filter", "background1", "background2", "background3",
            "background4", "background5", "background6"] #tool list


#screen captures
#canvas
canvas = screen.subsurface(canvasRect).copy() 


undo = [canvas] #list for undo function, starts with canvas screenshot
redo = [] #list for redo function

prev_eraser = ["none"] #list to help with eraser


while running: #main pygame loop

    keys = key.get_pressed()  #gets the key pressed
    mx,my = mouse.get_pos() #gets mouse position
    mb = mouse.get_pressed() #gets if the mouse is clicked or not



# event loop
    for evt in event.get ():

        if evt.type==QUIT: #checks if the user quits the window
            asksave = askquestion("Save?","Would you like to save your soccsterpiece?",type="yesnocancel") #prompts the user if they would like to save or not
             
            if asksave == "yes": #checks if the user selects yes
                filename = filedialog.asksaveasfilename() #lets the user save where ever they want and give it specific name
                filename = filename+".png" #saves in png
                image.save (canvas,filename) #saves the image
                running = False #pygame quits


            if asksave == "no": #checks if the user selects no
                running = False #quits pygame

            
        if evt.type == MOUSEBUTTONDOWN: #when the user clicks the mouse button initially
            sx,sy = evt.pos #gets initial position of click


            if evt.button == 1 and (mx-770)**2+(my-876)**2 <= 36**2 and music_choice == "False": #checking for left click, mouse over circle for unpause, and if the music choice is false
                mixer.music.unpause() #unpauses music
                music_choice = "True" #sets music choice to true for pausing


            elif evt.button == 1 and (mx-770)**2+(my-876)**2 <= 36**2 and music_choice == "True": #checking for left click, mouse over circle for pause, and if music choice is true
                mixer.music.pause() #pauses music
                music_choice = "False" #sets music choice to false for unpausing


            if evt.button == 1 and (mx-738)**2+(my-921)**2 <= 20**2 and m <= len(music): #checking for left click, mouse over previous song circle, and if m is less than the number of items in music list
                if m >= 0: #checking if m is greater than or equal to zero
                    m -= 1 #whenever it is clicked, m decreases by 1

                elif m == -1: #checking if m is equal to -1
                    m += 1 #whenevr is is clcicked when m is -1, m increases by 1 to the first track

                mixer.music.load (music[m]) #loads the song
                mixer.music.play (-1) #plays song



            if evt.button == 1 and (mx-((782+819)//2))**2+(my-921)**2 <= 20**2 and m <= len(music): #checking for left click, mouse over next song circle, and if m is less than number of items in music list
                if m >= 0: #checking if m is greater than or equal to 0
                    m += 1 #whenever it is clicked, m increases by 1

                if m == int(len(music)): #checking if m is equal to number of items in list
                    m = 0 #m is set to original song, 0

                mixer.music.load (music[m]) #loads song
                mixer.music.play (-1) #plays song


            if evt.button == 4 and th <= 30: #check for scroll up
                th += 1 #increases thickness/size by 1 for every scroll

            if evt.button == 5 and th > 0: #checks for scroll down
                th -= 1 #decreases thickness/size by 1 for every scroll



        if evt.type == MOUSEBUTTONUP: #when the user releases the mouse

            if evt.button == 1 and bottom_Rects[0].collidepoint (mx, my) or keys[K_LCTRL] and keys[K_z] or keys[K_RCTRL] and keys[K_z]: #checks for undo click or control z (undo function)
                if len (undo) > 1: #checks i fht eundo list is greater than 1
                    redo.append (undo[-1]) #adds the last undo function to the redo list
                    undo.pop() #deletes last item from undo
                    screen.blit (undo[-1], (500, 25)) #blits the last item from undo


            if evt.button == 1 and bottom_Rects[1].collidepoint (mx, my) or keys[K_LSHIFT] and keys[K_LCTRL] and keys[K_z] or keys[K_RSHIFT] and keys[K_RCTRL] and keys[K_z]: #checks for redo button
                if len (redo) >= 1: #checks if the redo list has more than one item
                    undo.append(redo[-1]) #adds last redo item to undo
                    redo.pop() #deletes last item from redo
                    screen.blit (undo[-1], (500, 25)) #blits last itme from undo


            if evt.button == 1 and canvasRect.collidepoint (mx, my): #checks if the user clicked the canvas
                undo.append (screen.subsurface(canvasRect).copy()) #adds to the undo list


            if evt.button == 1 and shapeRects[5].collidepoint (mx, my): #checks if the clear tool was clicked
                draw.rect (screen, WHITE, canvasRect) #draws white canvas
                canvas = screen.subsurface(canvasRect).copy() #takes a screenshot of the canvas 


            if canvasRect.collidepoint (mx, my) and evt.button == 1: #checks if canvas was clicked 
                screen.set_clip(canvasRect) #you can only update the canvasd


                if tool == "unfilled rectangle": #checks if tool is unfilled rectangle          
                    screen.blit (canvas, canvasRect) #blits screenshot
                    dxr = mx-sx #distance between intiial click pos and current position (x axis)
                    dyr = my-sy #distance berween initial click pos and current position (y-axis)

                    draw.rect(screen,cols,(sx,sy,dxr,dyr),th) #draws the rectangle

                    #adding 4 squares to solve problem with rectangle corners
                    draw.rect(screen,cols,(sx-(th/2)+1,sy-(th/2)+1,th,th))
                    draw.rect(screen,cols,((sx+dxr)-(th/2)-(1/2),sy-(th/2)+1,th,th))
                    draw.rect(screen,cols,(sx-(th/2)+1,(sy+dyr)-(th/2)-(1/2),th,th))
                    draw.rect(screen,cols,((sx+dxr)-(th/2),(sy+dyr)-(th/2),th,th))

                    canvas = screen.subsurface(canvasRect).copy() #takes a screenshot of the canvas # #takes a screenshot of canvas



                if tool == "filled rectangle": #checks if tool is filled rectangle
                    screen.blit(canvas,canvasRect) #blits screenshot right when mouse button was clicked
                    dxr = mx-sx #distance between intiial click pos and current position (x axis)
                    dyr = my-sy #distance berween initial click pos and current position (y-axis)
                    draw.rect(screen,cols,(sx,sy,dxr,dyr)) #draws rectangle
                    canvas = screen.subsurface(canvasRect).copy() #takes a screenshot of the canvas 


                if tool == "line": #checks if tool is line
                    screen.blit(canvas,canvasRect) # blits screenshot
                    draw.line(screen,cols,(sx,sy),(mx,my),th) #draws the line
                    canvas = screen.subsurface (canvasRect).copy() #takes a screenshot of the canvas 


                if tool == "filled ellipse": #checks if the filled ellipse is selected
	                screen.blit(canvas,(500,25)) #blits screenshot
	                dxc = mx-sx #dist between mx and sx
	                dyc = my-sy #dist between my and sy

	                try: #try and except for errors
	                    ellipse_Rect = Rect(sx,sy,dxc,dyc) #rect dimensions of ellipse
	                    ellipse_Rect.normalize() #fixes neg #'s
	                    draw.ellipse(screen,cols,ellipse_Rect) #draws ellipse

	                except:
	                    pass
	                    
	                canvas = screen.subsurface (canvasRect).copy() #takes a screenshot of the canvas #)


                if tool == "unfilled ellipse": #checks for unfilled ellipse t
                    screen.blit(canvas,(500,25))
                    dxc = mx-sx
                    dyc = my-sy

                    try:
                        for i in range(4): ## drawing 4 seperate ellipses in a loop
                        #each of these ellipsses are moved a bit
                            ellipse_Rect = Rect(sx+i,sy,dxc,dyc)
                            ellipse_Rect = Rect(sx-i,sy,dxc,dyc)
                            ellipse_Rect = Rect(sx,sy+i,dxc,dyc)
                            ellipse_Rect = Rect(sx,sy-i,dxc,dyc)
                            ellipse_Rect.normalize() #This will flip the width or height of a rectangle if it has a negative size. The rectangle will remain in the same place, with only the sides swapped.     

                            draw.ellipse(screen,cols,ellipse_Rect,th) #draws the ellipse
                            canvas = screen.subsurface(canvasRect).copy() #takes a screenshot of the canvas 

                    except:
                        pass

                   

                if tool == "soccer ball stamp": #checking for soccer ball stamp
                    screen.blit(canvas,(500,25)) #blits screen cap
                    x = mx-(stamps_loaded_large[0].get_width()//2) #gets the width of the stamp, subtracted by mx
                    y = my-(stamps_loaded_large[0].get_height()//2) #gets the height of the stamp, subtracted by my
                    screen.blit(stamps_loaded_large[0],(x,y)) #blits the stamp to the screen
                    canvas = screen.subsurface(canvasRect).copy() #takes a screenshot of the canvas 


                if tool == "ronaldo stamp": #checking for ronaldo stamp
                #same process as above
                    screen.blit (canvas,(500,25))
                    x = mx-(stamps_loaded_large[1].get_width()//2) 
                    y = my-(stamps_loaded_large[1].get_height()//2) 
                    screen.blit(stamps_loaded_large[1],(x,y)) 
                    canvas = screen.subsurface(canvasRect).copy() 


                if tool == "ea logo stamp": #checks for ea logo stamp
                #same process as above
                    screen.blit (canvas,(500,25)) 
                    x = mx-(stamps_loaded_large[2].get_width()//2) 
                    y = my-(stamps_loaded_large[2].get_height()//2) 
                    screen.blit (stamps_loaded_large[2],(x,y)) 
                    canvas = screen.subsurface(canvasRect).copy() 


                if tool == "player kicking ball stamp": #checks for player kicking ball stamp
                #same process as above
                    screen.blit (canvas,(500,25))
                    x = mx-(stamps_loaded_large[3].get_width()//2) 
                    y = my-(stamps_loaded_large[3].get_height()//2) 
                    screen.blit (stamps_loaded_large[3],(x,y)) 
                    canvas = screen.subsurface(canvasRect).copy() 


                if tool == "manchester united stamp": #checks for Manchester United stamp
                #same process as above
                    screen.blit (canvas,(500,25))
                    x = mx-(stamps_loaded_large[4].get_width()//2) 
                    y = my-(stamps_loaded_large[4].get_height()//2) 
                    screen.blit (stamps_loaded_large[4],(x,y))
                    canvas = screen.subsurface(canvasRect).copy() 


                if tool == "fifa text stamp": #checks for next stamp
                #same process as above
                    screen.blit (canvas,(500,25))
                    x = mx-(stamps_loaded_large[5].get_width()//2) 
                    y = my-(stamps_loaded_large[5].get_height()//2) 
                    screen.blit (stamps_loaded_large[5],(x,y))  #blits
                    canvas = screen.subsurface(canvasRect).copy() 


                screen.set_clip (None)  #goes back to normal          




############## DRAWING SOME SHAPES ##################

    for a in toolRects: #this loop draws the rectangles that would be behind the top tools
        draw.rect (screen, DARK_BLUE, a, 2) #draws rectangules from list
    

    for i in range (4):
    	screen.blit (basictoolsimg[i], toolRects[i])


    for s in shapeRects: #displays the rectangular dimensions for the shapes
        draw.rect(screen, DARK_BLUE,s, 2) 


    for i in range (7): #this loop blits the images for the shape tools
    	screen.blit (shapetool_list[i], shapeRects[i])


    #draws all rectangles for stamps 
    for i in stampsRects:
        draw.rect (screen, DARK_BLUE, i, 2)

#blits images for stamps
    for i in range (6):
    	screen.blit (stamps_loaded_small[i], stampsRects[i])

 
 	#draws background rects
    for i in background_Rects:
    	draw.rect (screen, DARK_BLUE, i, 5)

	#blits the small background in the rects     	
    for i in range (3):
    	screen.blit (background_loaded_small[i], background_Rects[i])

    #blits the second row
    for i in range (3):
    	screen.blit (background_loaded_small[i+3], background_Rects[i+3])

    #draws the bottom rectangles
    for i in bottom_Rects:
        draw.rect (screen,DARK_BLUE,i)

    #blits the bottom tool pictures
    for i in range (8):
        screen.blit (bottom_tools_loaded[i],(115*i+720,840))
        

    #draws the rectangles for the canvas outline
    for i in canvas_outline:
    	draw.rect (screen, cols, i)

    #circles for music box
    draw.circle (screen, DARK_BLUE, (770, 876), 36, 1)
    draw.circle (screen, DARK_BLUE, (738, 921), 20, 1)
    draw.circle (screen, DARK_BLUE, ((782+819)//2, 921), 20, 1)




    if tool == "no tool": # checking if there is not tool selected
        screen.blit (desc_loaded[0], (50, 745)) #blits intro description


    for i in range(4): #hovering, selecting tool  for top tools
        if toolRects[i].collidepoint (mx, my): #checking if the cursor is over the top tools
            if mb[0] == 1: #checking if the user clicked the mouse in that area

                tool = tool_list[i] #tool is the index of the shape clicked ex. pencil
                draw.rect (screen, GREEN, toolRects[i], 1) #draws green rectangle (for hovering)
                screen.blit (desc_loaded[i+1], (50, 745)) #displays description


            else: #if the user did not click the mouse

                draw.rect (screen, RED, toolRects[i], 1) #draws red rectangle for hovering
                screen.blit (desc_loaded[i+1], (50, 745)) #blits description

        elif tool == tool_list[i]: #if a tool is selected
            draw.rect (screen, WHITE, toolRects[i], 1) #draws white rectangle over tool to indicate which tool is being used
            screen.blit (desc_loaded[i+1], (50, 745)) #blits description


    for i in range (7): #hovering and selecting over shape tools
        if shapeRects[i].collidepoint (mx, my): #if the cursor is over the shape rectangles...

            if mb[0] == 1: #checking if the left mouse button was checked

                tool = tool_list[i+4] #tool is the index of the shape clicked on. 4 is added because it is in the same list as all other tools
                draw.rect (screen, GREEN, shapeRects[i], 1) #hovering - rectangle turns green when clicked
                screen.blit (desc_loaded[i+5], (50, 745)) #displays description

            else: #anything else (if mouse button was not clicked)
                draw.rect (screen, RED, shapeRects[i], 1) #red outline over rectangle
                screen.blit (desc_loaded[i+5], (50, 745)) #displays description

            if tool == "clear": #if the tool selected was the clear tool
                draw.rect (screen, WHITE, canvasRect) #draws a white rectangle over the canvas
                fillcol = WHITE #changes eraser colour to white
                prev_eraser.append ("clear") #adds to the previously used list for eraser


        elif tool == tool_list[i+4]: #checks if the tool selected for the object

            draw.rect (screen, WHITE, shapeRects[i], 1) #draws a white outlime
            screen.blit (desc_loaded[i+5], (50, 745)) #displays description



    for i in range (6): #hovering and selecting over stamp tools
        if stampsRects[i].collidepoint (mx, my): #checks if the cursor is over the stamp rectangles

            if mb[0] == 1: #if the mouse button was clicked over one of the rectangles

                tool = tool_list[i+11] #tool is the index of the stamp clicked on, + 11 because there were other items in the list before stamps
                draw.rect (screen, GREEN, stampsRects[i], 1) #hovering - highlights in green when stamps are clicked
                screen.blit (desc_loaded[12], (50, 745)) #blits the descriptions

            else: #anythin else (if mouse button was not clicked)
                draw.rect (screen, RED, stampsRects[i], 1) #highlights red when hovered over
                screen.blit (desc_loaded[12], (50, 745)) #blits the descriptions

        elif tool == tool_list[i+11]: #checking if the tool selected for the object clicked on

            draw.rect (screen, WHITE, stampsRects[i], 1) #draws a white outline over tool
            screen.blit (desc_loaded[12], (50, 745)) #blits the descriptions 



    for i in range (7): #fix errors #hovering and selecting over bottom tools
        if bottom_Rects[i].collidepoint (mx, my): #if the cursor is over the tools on the bottom

            if mb[0] == 1: #if the left mouse button was clicked

                tool = tool_list[i+17] #takes the tool of the index, added to 16 because there were previous items in the list
                screen.blit (desc_loaded[i+17], (50, 745)) #blits description
                draw.rect (screen, GREEN, bottom_Rects[i], 1) #draws the green outline for hovering

                if tool == "load": #checking if the tool selected is the load tool

                    try:
	                    filename = filedialog.askopenfilename(filetypes = [("images","*.png")]) #asks the user to load a pciture from their files

	                    if filename!="": #if the filename is not equal to an empty string
	                        canvas_img = image.load(filename) #loads the image imported
	                        cw=canvas_img.get_width() #width of loaded image
	                        ch=canvas_img.get_height() #height of loaded image

	                        if cw > 1125 and ch > 800: #checks if the height and width of the image are greater than the canvas size
	                            canvas_img = transform.scale (canvas_img, (1125, 800)) #makes it fit to canvas

	                        elif cw > 1125: #checks if the width is too big for canvas
	                            canvas_img = transform.scale (canvas_img, (1125, ch)) #fixes for canvas

	                        elif ch > 800: #checks if height is too big for canvas
	                            canvas_img = transform.scale (canvas_img, (ch, 800)) #fixes for canvas

	                        draw.rect (screen, WHITE, canvasRect) #draws white canvas
	                        screen.blit(canvas_img, canvasRect) #blits the image loaded onto the canvas #blits loaded images

                    except: #if any errors
                    	print ("Load Error") #tells in console theres a load error

                    canvas = screen.subsurface(canvasRect).copy() #takes a screenshot of the canvas 



                if tool == "save": #issue with complete fill selection

                    try: #here, the user will be saving the canvas
                        fname = filedialog.asksaveasfilename(defaultextension=".png") #asks the user to save the canvas, makes sure the file type is a png
                        image.save(canvas, fname) #saves the image

                    except: #if there is any sort of error saving the image, the program will tell the user in the python shell there was a saving error
                        print ("Saving Error") #tells the user there is a saving error


                if tool == "filter": #checks if the tool is filter
                    for x in range (500, 1625): #gets x values for canvas
                        for y in range (25, 825): #gets y values for canvas

                            r,g,b,a = screen.get_at((x,y)) #gets the rbga colours
    
    						#formula for sepia tool
                            nr = min(255,0.393*r + 0.769*g + 0.189*b) #min function: takes the smallest number
                            ng = min(255,0.349*r + 0.686*g + 0.168*b) #ex. 300 will go to 255
                            nb = min(255,0.272*r + 0.534*g + 0.131*b) 
                            
                            screen.set_at ((x, y), (nr, ng, nb))  #gets the colour value for a single pixel                  

                        if x%5 == 0:
                            display.update(canvasRect) #instead of doing display.flip(), i used display.update() to only update the area, its also better for hardware processing

                    canvas = screen.subsurface(canvasRect).copy() #takes a screenshot of the canvas #


            else: #anything else (if the mouse button was not clicked)
                draw.rect (screen, RED, bottom_Rects[i], 1) #draws a red outline when cursor is over rectangle
                screen.blit (desc_loaded[i+17], (50, 745))

        elif tool == tool_list[i+17]: #checks if the tool selected over the object is clicked on
            draw.rect (screen, WHITE, bottom_Rects[i], 1) #highlights it with a white rectangle
            screen.blit (desc_loaded[i+17], (50, 745))


    for i in range (3): #selecting and hovering over the background tools (top background tools)
        if background_Rects[i].collidepoint (mx, my): #checking if the cursor is over the tools

            if mb[0] == 1: #checks if a left  click was present
                tool = tool_list[i+24] #takes the tool of the object selected, added by 24 because there were previous items in the list

                screen.blit (desc_loaded[13], (50, 745)) #desc

                screen.blit (background_loaded_large[i], (500, 25))  #displays the background selected

                canvas = screen.subsurface(canvasRect).copy() #takes a screenshot of the canvas
                undo.append(canvas) #adds to undo list

                pos = i  #pos for the eraser
                draw.rect (screen, GREEN, background_Rects[i], 1) #highlights when clicked with green
                prev_eraser.append ("background") #adds to list for eraser that backgrounds was used


            else: #anything else (left mouse button wasn't clicked)
                draw.rect (screen, RED, background_Rects[i], 1) #draws rectangle for hovering 
                screen.blit (desc_loaded[13], (50, 745))

        elif tool == tool_list[i+24]: #checks if the tool selected over the object is clicked on, with the tool being defined
            draw.rect (screen, WHITE, background_Rects[i], 1) #draws white rectangle to indicate its the tool
            screen.blit (desc_loaded[13], (50, 745)) #blits desc


    #exact same process as above, only difference is if the tool index and background index is being added by 3
    for i in range (3): #loop for background
        if background_Rects[i+3].collidepoint (mx, my): #checks if the bottom row of background was hovered over

            if mb[0] == 1: #checks if the mouse was clicked
                tool = tool_list[i+27] #the tool is the one of index i+27

                screen.blit (desc_loaded[13], (50, 745)) #description

                screen.blit (background_loaded_large[i+3], (500, 25)) #blits the background onto the canvas

                canvas = screen.subsurface(canvasRect).copy() #takes a screenshot of the canvas 
                undo.append(canvas) #adds to undo list

                draw.rect (screen, GREEN, background_Rects[i+3], 1) #hovering
                pos = i+3 #gets the position for the list

                prev_eraser.append ("background") #adds that a background was used for eraser

            else: #anything else:
                draw.rect (screen, RED, background_Rects[i+3], 1) #hovering
                screen.blit (desc_loaded[13], (50, 745)) #desc

        elif tool == tool_list[i+27]: #checks if the tool is on the right background
            draw.rect (screen, WHITE, background_Rects[i+3], 1) #hovering
            screen.blit (desc_loaded[13], (50, 745)) #desc



#music player circles
    if (mx-770)**2+(my-876)**2 <= 36**2: #checking if over the play/pause circle
        draw.circle (screen, RED, (770, 876), 36, 1) #highlights with red circle
        screen.blit (desc_loaded[14], (50, 745))


    if (mx-770)**2+(my-876)**2 <= 36**2 and mb[0] == 1: #checkig if over the play/plause circle and left button is clicked
        draw.circle (screen, GREEN, (770, 876), 36, 1) #highlights with green circle
        screen.blit (desc_loaded[14], (50, 745))



    if (mx-738)**2+(my-921)**2 <= 20**2:  #checking if over previous music box
        draw.circle (screen, RED, (738, 921), 20, 1) #draws red circle to highlight
        screen.blit (desc_loaded[15], (50, 745))

    if (mx-738)**2+(my-921)**2 <= 20**2 and mb[0] == 1: #checking of over the previous music box and left button is clicked
        draw.circle (screen, GREEN, (738, 921), 20, 1) #draws green circle to highlight
        screen.blit (desc_loaded[15], (50, 745))



    if (mx-((782+819)//2))**2+(my-921)**2 <= 20**2: #checking if over next song box
        draw.circle (screen, RED, ((782+819)//2, 921), 20, 1)   #draws red circle to highlight
        screen.blit (desc_loaded[16], (50, 745))
        

    if (mx-((782+819)//2))**2+(my-921)**2 <= 20**2 and mb[0] == 1: #checking of over next song box and left button is clicked
        draw.circle (screen, GREEN, ((782+819)//2, 921), 20, 1)     #draws green circle to highlight 
        screen.blit (desc_loaded[16], (50, 745)) 





########## PIXEL COUNTER ###########
    if canvasRect.collidepoint (mx, my): #checking if mouse is over canvas
        draw.rect (screen, (68, 194, 101), (500,840,205,100)) #rectangle for pixel location
        screen.blit (pixelloaction_title, (500, 840)) #text for pixel location

        bracket_left = arial_font.render ("(", True, BLACK) #bracket
        bracket_right = arial_font.render (")", True, BLACK) #bracket
        px = eaFont.render (str(mx-500),True,BLACK) #Turning coordinates into text, for the x value
        comma = arial_font.render (",",True,BLACK) #comma
        py = eaFont.render (str(my-25),True,BLACK) #y-coord
        
        #blits the text
        screen.blit (bracket_left, (517, 888)) 
        screen.blit (px, (530, 890))
        screen.blit (comma, (595, 890))
        screen.blit (py, (615, 890))
        screen.blit (bracket_right, (677, 888))


    else: #anything else
        draw.rect (screen, (68, 194, 101), (500,840,205,100))  #rectangle for pixel location
        screen.blit (pixelloaction_title, (500, 840)) #blits the title

        n_a = eaFont.render ("N  A", False, RED) #text for N/A
        slash = arial_font.render ("/", True, RED) #slash

        #blits the text
        screen.blit (slash, (597, 890))
        screen.blit  (n_a, (570, 890)) #blits N/A




########## USING THE TOOLS THAT REQUIRE YOU TO CLICK ON CANVAS ##############



    if mb[0] == 1: #checks if the user clicked the left button

        if canvasRect.collidepoint(mx,my): #checks if the user clicked in the canvas area
            # undo.append (screen.subsurface(canvasRect).copy())

            screen.set_clip(canvasRect) #only the canvas can be updated

            if tool == "pencil":  #checking if the tool selected is the pencil
                draw.line(screen,cols,(omx,omy),(mx,my),3) #draws a line for the pencil
                canvas = screen.subsurface(canvasRect).copy() #takes a screenshot of the canvas #

                
            if tool == "eraser": #checking if the tool selected is the eraser

                # if prev_eraser[-1] == "complete fill" or prev_eraser[-1] == "clear" or prev_eraser[-1] == "none": #checking if there is no background
                if prev_eraser[-1] != "background": #checking if the background is not the last thing in the previous list
                    if prev_eraser[-1] == "none": #checkis if nothing was selected
                        fillcol = WHITE #makes eraser colour white
                        
                    dx = mx-omx #run, takes the distance between old mouse position and current mouse pos (horizontal direction)
                    dy = my-omy #rise, takes the distance betweent the old mouse pos and current mouse pos (vertic direction)
                    dist = int(sqrt(dx**2+dy**2)) #gets total distance

                    for i in range(1,dist): #while i is between 1 and the total dist
                        cx = int(omx+i*dx/dist) #calculating the center if the circle (x-value)
                        cy = int(omy+i*dy/dist) #calculatin the center of the circle (y-value)
                        draw.circle (screen,fillcol,(cx,cy),th) #fillcol is the colour used for the fill, draws circular motion for eraser
                        
                    canvas = screen.subsurface(canvasRect).copy() #takes a screenshot of the canvas 


                if prev_eraser[-1] == "background": #checking if there is a background placed, needs to be fixed
                    try: #try and accept for errors
                        dx = mx-omx #gets distance between mx and omx
                        dy = my-omy #gets dist btwn my and omy
                        dist = int(sqrt(dx**2+dy**2)) #calculates distance

                        for i in range (1, dist): #loop for calculating midpoiints
                            cx = int(omx+i*dx/dist) #mid of x
                            cy = int(omy+i*dy/dist) #mid of y
                      
                            eraser_back = background_loaded_large[pos].subsurface((cx-500, cy-25, th, th))## taking the exact location of the background
                            screen.blit (eraser_back, (cx, cy))

                    except: #except for errors
                        pass
                    
                    canvas = screen.subsurface(canvasRect).copy() #takes a screenshot 
            


            if tool == "brush": #checking if the current tool selected is the brush
            #same procedure as circle, just in different colour
                dx = mx-omx #run
                dy = my-omy #rise
                dist = int(sqrt(dx**2+dy**2)) #gets distance
                for i in range(1,dist):
                    cx = int(omx+i*dx/dist) #calculating the center if the circle (x-value)
                    cy = int(omy+i*dy/dist) #calculatin the center of the circle (y-value)
                    draw.circle (screen,cols,(cx,cy),th)
                canvas = screen.subsurface(canvasRect).copy() #takes a screenshot of the canvas #

                
            if tool == "fill": #checking if the current tool selected is the fill tool
                pixel = screen.get_at((mx,my)) #Colour of current pixel
                pixel_List = [(mx,my)] #Creates a list of coordinates

                if pixel != cols: #checking if the pixel colour is not equal to the current colour
                    while len(pixel_List) > 0: #Stops errors and only goes until list is empty
                        if canvasRect.collidepoint(pixel_List[0]) and screen.get_at(pixel_List[0]) == pixel:  #checking if the cursor was over the canvas when checking for different colours and if the current position was equal to the pixel colour
                            screen.set_at(pixel_List[0],cols) #set the color value for a single pixel
                            
                            #adds the locations for the pixels to the list
                            pixel_List.append ((pixel_List[0][0],pixel_List[0][1]+1))  
                            pixel_List.append ((pixel_List[0][0],pixel_List[0][1]-1))
                            pixel_List.append ((pixel_List[0][0]+1,pixel_List[0][1]))
                            pixel_List.append ((pixel_List[0][0]-1,pixel_List[0][1]))

                        del (pixel_List[0]) #deletes the first pixel location 

                canvas = screen.subsurface(canvasRect).copy() #takes a screenshot of the canvas 


            if tool == "filled rectangle": #checking if the current tool selected is the filled rectangle tool
                screen.blit(canvas,(500,25)) #blits screenshot right when mouse button was clicked
                dxr = mx-sx #distance between intiial click pos and current position (x axis)
                dyr = my-sy #distance berween initial click pos and current position (y-axis)
                draw.rect(screen,cols,(sx,sy,dxr,dyr)) #draws rectangle
                
                
            if tool == "unfilled rectangle": #using this tool is complete
                screen.blit(canvas,(500,25))
                dxr = mx-sx #distance between intiial click pos and current position (x axis)
                dyr = my-sy #distance berween initial click pos and current position (y-axis)

                draw.rect(screen,cols,(sx,sy,dxr,dyr),th)

                #adding 4 squares to solve problem with rectangle corners
                draw.rect(screen,cols,(sx-(th/2)+1,sy-(th/2)+1,th,th))
                draw.rect(screen,cols,((sx+dxr)-(th/2)-(1/2),sy-(th/2)+1,th,th))
                draw.rect(screen,cols,(sx-(th/2)+1,(sy+dyr)-(th/2)-(1/2),th,th))
                draw.rect(screen,cols,((sx+dxr)-(th/2),(sy+dyr)-(th/2),th,th))



            
            if tool == "line": #using this tool is complete
                screen.blit (canvas,(500,25)) #blits screenshot
                draw.line (screen,cols,(sx,sy),(mx,my),th) #draws the line

            if tool == "filled ellipse": #using this tool is complete; possibly change name of ellipse_rect
                screen.blit (canvas,(500,25)) #blits ss
                dxc = mx-sx #dist btwn mx and sx
                dyc = my-sy #dist btwn mx and sy
                
                try: #try and except to bypass errors 
                    ellipse_Rect = Rect(sx,sy,dxc,dyc) #makes a rect for elliose
                    ellipse_Rect.normalize() #fixes neg values
                    draw.ellipse(screen,cols,ellipse_Rect) #draws the ellipse
                    
                except: #except for errors
                    pass #bypasses


            if tool == "unfilled ellipse": #using this tool is complete; possibly change name of ellipse_rect
                screen.blit(canvas,(500,25))
                dxc = mx-sx #dist btwn mx and sx
                dyc = my-sy #dist btwn my and sy

                try:  #try and except to bypass errors
                    for i in range(4): ## drawing 4 seperate ellipses in a loop
                        
                        ellipse_Rect = Rect(sx+i,sy,dxc,dyc)
                        ellipse_Rect = Rect(sx-i,sy,dxc,dyc)
                        ellipse_Rect = Rect(sx,sy+i,dxc,dyc)
                        ellipse_Rect = Rect(sx,sy-i,dxc,dyc)
                        ellipse_Rect.normalize() #This will flip the width or height of a rectangle if it has a negative size. The rectangle will remain in the same place, with only the sides swapped.     

                        draw.ellipse(screen,cols,ellipse_Rect,th) #draws the ellipse

                except: #for errors
                    pass


            if tool == "spray paint":  #checks if the tool selected is spray paint
                for i in range (30): #this loop is for creating random circles
                    spray_x = randint(-th,th) #gets random spots for spray paint: x
                    spray_y = randint(-th,th) #y
                    if hypot(spray_x,spray_y) <= th: #this is so the spray paint does not go into a rectangle
                        draw.circle(screen,cols,(mx+spray_x,my+spray_y),0) #draws the circles for spray paint
                canvas = screen.subsurface(canvasRect).copy() #takes a screenshot of the canvas 


            if tool == "soccer ball stamp": #checks for this stamp selected
                screen.blit(canvas,(500,25)) #blits screenshot
                x = mx-(stamps_loaded_large[0].get_width()//2) #takes width of stamp, subtracted by mx
                y = my-(stamps_loaded_large[0].get_height()//2) #takes height of stamp, subtracted by my
                screen.blit(stamps_loaded_large[0],(x,y)) #blits the stamp


            if tool == "ronaldo stamp": #checks if ronaldo stamp is selected
            #same process as above
                screen.blit (canvas,(500,25))
                x = mx-(stamps_loaded_large[1].get_width()//2)
                y = my-(stamps_loaded_large[1].get_height()//2)
                screen.blit(stamps_loaded_large[1],(x,y))


            if tool == "ea logo stamp": #checks if ea logo stamp is selected
            #same process as above
                screen.blit (canvas,(500,25))
                x = mx-(stamps_loaded_large[2].get_width()//2)
                y = my-(stamps_loaded_large[2].get_height()//2)
                screen.blit (stamps_loaded_large[2],(x,y))


            if tool == "player kicking ball stamp": #checks if player kicking ball stamp is selected
            #same process as above
                screen.blit (canvas,(500,25))
                x = mx-(stamps_loaded_large[3].get_width()//2)
                y = my-(stamps_loaded_large[3].get_height()//2)
                screen.blit (stamps_loaded_large[3],(x,y))


            if tool == "manchester united stamp": #checks if machester united stamp is selected
            #same process as above
                screen.blit (canvas,(500,25))
                x = mx-(stamps_loaded_large[4].get_width()//2)
                y = my-(stamps_loaded_large[4].get_height()//2)
                screen.blit (stamps_loaded_large[4],(x,y))


            if tool == "fifa text stamp": #checks if fifa stamp is selected
            #same process as above
                screen.blit (canvas,(500,25))
                x = mx-(stamps_loaded_large[5].get_width()//2)
                y = my-(stamps_loaded_large[5].get_height()//2)
                screen.blit (stamps_loaded_large[5],(x,y))


            if tool == "complete fill": #checks if complete fill tool us selected
                draw.rect (screen,cols,canvasRect) #draws the colour of choice over the canvas
                fillcol = screen.get_at((mx,my)) #sets the eraser colour to the colour of the canvas
                canvas = screen.subsurface(canvasRect).copy() #takes a screenshot of the canvas 
                prev_eraser.append ("complete fill") #adds that this was previously used for the eraser


            if tool == "marker":
                dx = mx-omx #run
                dy = my-omy #rise
                dist = int(sqrt(dx**2+dy**2)) #gets distance

                for i in range(dist):
                    cx = int(omx+i*dx/dist) #calculating the center if the circle (x-value)
                    cy = int(omy+i*dy/dist) #calculatin the center of the circle (y-value)

                    marker_surface = Surface((th,th),SRCALPHA) #makes a marker surface for the transparency
                    draw.circle (marker_surface,(cols[0], cols[1], cols[2], 15),(th//2,th//2),th//2) #draws the transparent circle
                    screen.blit(marker_surface,(cx-th//2,cy-th//2)) #blits the marker surface

                canvas = screen.subsurface(canvasRect).copy() #takes a screenshot of the canvas #


            screen.set_clip(None) #goes back to normal

         
    #choosing the colour from the palette
    if mb[0] == 1 and paletteRect.collidepoint(mx,my):
        #cols,tuple = askcolor(title='Pick your colour!')
        #cols = screen.get_at((mx,my))
        cols = screen.get_at((mx,my)) #gets the colour from the colour palette
        draw.rect (screen, cols, col_previewRect) #colour preview 
   

    print (prev_eraser[-1])
    display.flip()
    omx,omy = mx,my
            
quit()



