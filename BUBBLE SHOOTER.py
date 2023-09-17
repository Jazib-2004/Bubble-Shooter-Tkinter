from tkinter import *
import random,time

window=Tk()
speed=1 #accounts for delay of .after() function and ball movement


height = 700
width = 1363

#INTRO WINDOW
def configure_window():
    window.title("BUBBLE SHOOTER")
    window.configure(height = height, width = width)
    window.minsize(width, height)
    window.maxsize(width, height)
    window.iconphoto(False,icon)

cvs = Canvas(height = height,width = width)

icon=PhotoImage(file='icon.png')
img=PhotoImage(file='bubbleshooter.png')
image_label = Label(cvs,image=img)
image_label.grid()

play_button= Button(cvs, text="PLAY",font=("helvetica",20,"bold"),bg="maroon2",fg="white",width=10,command = lambda: game_window())
play_button.place(x = 550, y = 400)

ins_button= Button(cvs, text="INSTRUCTIONS",font=("helvetica",17,"bold"),bg="maroon2",fg="white",width=12,command = lambda: instruction())
ins_button.place(x = 550, y = 470)


def instruction():
    ins_window = Toplevel(window,height = height, width = width,bg= "pink3")
    title_label = Label(ins_window,text = "BUBBLE SHOOTER", font = "helvetica 30 bold italic",bg= "pink3",fg = "black")
    title_label.place(x = 150, y = 10)
    ins_label = Label(ins_window,text = "INSTRUCTIONS:",font ="helvetica 20 bold",bg= "pink3",fg = "black")
    ins_label.place(x = 10, y = 100)

    # --------------------game instructions--------------
    instruction_1 = '''1. THE ENDPOINT OF THE AIM!,To aim a target, use LEFT and RIGHT arrow keys, these keys take your shooter line to the respective direction.'''
    label_ins = Label(ins_window, text = instruction_1, font = "helvetica 15",bg= "pink3",fg = "white")
    label_ins.place(x = 10, y = 150)
    instruction_2 = '''2. FOLLOW AND SHOOT AS PER THE POINTER OF THE AIM!'''
    label_ins_2 = Label(ins_window, text=instruction_2, font="helvetica 15",bg= "pink3",fg = "white")
    label_ins_2.place(x=10, y=180)
    instruction_3 = '''3. To shoot the ball at your desired aim, use SPACE key button.'''
    label_ins_2 = Label(ins_window, text=instruction_3, font="helvetica 15", bg="pink3", fg="white")
    label_ins_2.place(x=10, y=210)
    instruction_4 = '''4. Hitting each same coloured ball will increment score by 1'''
    label_ins = Label(ins_window, text = instruction_4, font = "helvetica 15",bg= "pink3",fg = "white")
    label_ins.place(x = 10, y = 240)

    # -----------------cheat codes------------------
    cheat_code_label = Label(ins_window, text = "CHEAT CODES",font="helvetica 20 bold",bg="pink3",fg="black")
    cheat_code_label.place(x = 10, y = 270)
    cheat_code_1 = "red----------All the red balls will be banged."
    cheat_1_label = Label(ins_window,text = cheat_code_1, font = "helvetica 15",bg = "pink3",fg = "white")
    cheat_1_label.place(x = 10, y = 310)
    cheat_code_2 = "yellow------All the yellow balls will be banged."
    cheat_2_label = Label(ins_window,text = cheat_code_2, font = "helvetica 15",bg = "pink3",fg = "white")
    cheat_2_label.place(x = 10, y = 340)
    cheat_code_3 = "green-------All the green balls will be banged."
    cheat_3_label = Label(ins_window,text = cheat_code_3, font = "helvetica 15",bg = "pink3",fg = "white")
    cheat_3_label.place(x = 10, y = 370)
    cheat_code_4 = "blue---------All the blue balls will be banged."
    cheat_4_label = Label(ins_window,text = cheat_code_4, font = "helvetica 15",bg = "pink3",fg = "white")
    cheat_4_label.place(x = 10, y = 400)
cvs.place(x = 0, y = 0)


game_canvas=Canvas(height = height,width = width,bg="pink3")
colors=["red","yellow","green","blue"]

Boss_img=PhotoImage(file='Boss.PNG').subsample(1,1)
Boss_label = Label(game_canvas,image=Boss_img,height=height,width=width,)
Boss_click=0

WIN=PhotoImage(file="WIN1.PNG")
WIN_Label=Label(game_canvas,image=WIN,height=height,width=width,)

# GAME WINDOW BELOW
def game_window():
    """
    Destroys Intro Window and Creates a New Game Window
    """
    cvs.destroy()
    game_canvas.place(x = 0, y = 0)

balls=[]
def create_balls():
    """
    Creates Ball along width and height of the game window
    """
    dia = 30
    global width,height,colors,balls_and_coords,ball_no
    for j in range(0,round(0.25*height),dia+1):
        for i in range(0,width,dia+1):
            choice=random.choice(colors)
            ball=game_canvas.create_oval(i,j,i+dia,j+dia,fill=choice)
            balls.append(ball)
create_balls()

destroyed = False 
end = 0.1 
added = False

def create_shooter():
    """
    Creates Shooter at the beginning of game
    and after each collison
    or if ball hits the upper boundary
    """
    global end,line,direction,shooter,temp_color,shooter_coords,pointer
    shooter_coords = [width/2-30,height-108,width/2,height-78]
    temp_color=random.choice(colors)
    shooter=game_canvas.create_oval(shooter_coords,fill=temp_color)
    direction = width/2-15
    line = game_canvas.create_line(width/2-15,height-108,direction,end,fill="black", width=1,dash=(4, 2))
    pointer=game_canvas.create_polygon(direction-10,5,direction+10,5,direction,20,fill="black")
create_shooter()

def shooting(event=None):
    """
    Shoots our shooter
    """
    global line,direction,shooter,temp_color,shooter_coords,destroyed,end,added,pointer
    game_canvas.delete(line)
    game_canvas.delete(pointer)
    if shooter_coords[1]==0 or destroyed or added:
        if not added:
            game_canvas.delete(shooter)
        end = 0.1
        destroyed = False
        added = False
        create_shooter()
        
    else:
        if direction-15 - shooter_coords[0] > 0:
            shooter_coords[0]+=speed
            shooter_coords[2]+=speed
        elif direction-15 - shooter_coords[0] < 0:
            shooter_coords[0]-=speed
            shooter_coords[2]-=speed
        shooter_coords[1]-=speed
        shooter_coords[3]-=speed
        game_canvas.delete(shooter)
        shooter = game_canvas.create_oval(shooter_coords,fill=temp_color) 
        collision(event)
        game_canvas.after(speed,shooting)

def laim(event=None):
    """
    aims on left
    """
    global line,direction,shooter_coords,end,pointer
    if shooter_coords[1]==height-108 and direction-15 >= 0:
        game_canvas.delete(line)
        game_canvas.delete(pointer)
        direction-= 30
        line = game_canvas.create_line(width/2-15,height-93,direction,end,fill="black", width=1,dash=(4, 2)) 
        pointer=game_canvas.create_polygon(direction-10,5,direction+10,5,direction,20,fill="black")
def raim(event=None):
    """
    aims on right
    """
    global line,direction,shooter_coords,end,pointer
    if shooter_coords[1]==height-108 and direction-15 <= width:
        game_canvas.delete(line)
        game_canvas.delete(pointer)
        direction+= 30
        line = game_canvas.create_line(width/2-15,height-93,direction,end,fill="black", width=1,dash=(4, 2)) 
        pointer=game_canvas.create_polygon(direction-10,5,direction+10,5,direction,20,fill="black")
deleted_balls=[]
def collision(event):
    """
    Checks for Collision with any hit ball
    """
    global deleted_balls,cnvlist,destroyed,shooter,added,balls
    i=balls[-1]
    if shooter_coords[1] <= height:

        def explosion(ball):
            """
            Checks if same balls are connected
            """
            def left(ball):
                """
                checking color for balls on left
                """
                if game_canvas.coords(ball)[0]==0 or game_canvas.itemcget(ball-1,"fill") != game_canvas.itemcget(ball,"fill") :
                    pass
                else:
                    if game_canvas.itemcget(ball-1,"fill") == game_canvas.itemcget(ball,"fill"):
                        left(ball-1)
                        game_canvas.delete(ball-1)
                        deleted_balls.append(ball-1)
                        score_label.configure(text = "Score:"+str(len(deleted_balls)))
                        checkwin()

            def right(ball):
                """
                checking color for balls on right
                """
                if game_canvas.coords(ball)[3]==width or game_canvas.itemcget(ball+1,"fill") != game_canvas.itemcget(ball,"fill") :
                    pass
                else:
                    if game_canvas.itemcget(ball+1,"fill") == game_canvas.itemcget(ball,"fill"):
                        right(ball+1)
                        game_canvas.delete(ball+1)
                        deleted_balls.append(ball+1)
                        score_label.configure(text="Score:" + str(len(deleted_balls)))
                        checkwin()

            def top(ball):
                """
                Checking color for balls on top
                """
                if game_canvas.coords(ball)[1]==0 or game_canvas.itemcget(ball-44,"fill") != game_canvas.itemcget(ball,"fill"):
                    pass
                else:
                    if game_canvas.itemcget(ball-44,"fill") == game_canvas.itemcget(ball,"fill"):
                        top(ball-44)
                        game_canvas.delete(ball-44)
                        deleted_balls.append(ball-44)
                        score_label.configure(text="Score:" + str(len(deleted_balls)))
                        checkwin()

            def top_right(ball):
                """
                checking color for balls at top right
                """
                if (game_canvas.coords(ball)[1]==0 and game_canvas.coords(ball)[3]==width) or game_canvas.itemcget(ball-43,"fill") != game_canvas.itemcget(ball,"fill") :
                    pass
                else:
                    if game_canvas.itemcget(ball-43,"fill") == game_canvas.itemcget(ball,"fill"):
                        top_right(ball-43)
                        game_canvas.delete(ball-43)
                        deleted_balls.append(ball-43)
                        score_label.configure(text="Score:" + str(len(deleted_balls)))
                        checkwin()
            
            def top_left(ball):
                """
                checking color for balls at top left 
                """
                if (game_canvas.coords(ball)[1]==0 and game_canvas.coords(ball)[0]==0) or game_canvas.itemcget(ball - 45, "fill") != game_canvas.itemcget(ball, "fill"):
                    pass
                else:
                    if game_canvas.itemcget(ball - 45, "fill") == game_canvas.itemcget(ball, "fill"):
                        top_left(ball-45)
                        game_canvas.delete(ball - 45)
                        deleted_balls.append(ball - 45)
                        score_label.configure(text="Score:" + str(len(deleted_balls)))
                        checkwin()
            
            def bottom_right(ball):
                """
                checking color for balls on bottom right
                """
                if (game_canvas.coords(ball)[2]==width and game_canvas.coords(ball)[3]==round(0.25*height)) or game_canvas.itemcget(ball+45,"fill") != game_canvas.itemcget(ball,"fill"):
                    pass
                else:
                    if game_canvas.itemcget(ball+45,"fill") == game_canvas.itemcget(ball,"fill"):
                        bottom_right(ball+45)
                        game_canvas.delete(ball+45)
                        deleted_balls.append(ball+45)
                        score_label.configure(text="Score:" + str(len(deleted_balls)))
                        checkwin()
            
            def bottom_left(ball):
                """
                checking color for balls on bottom left
                """
                if (game_canvas.coords(ball)[2]==30 and game_canvas.coords(ball)[3]==round(0.25*height)):
                    pass
                else:
                    if game_canvas.itemcget(ball+43,"fill") == game_canvas.itemcget(ball,"fill"):
                        bottom_left(ball+43)
                        game_canvas.delete(ball+43)
                        deleted_balls.append(ball+43)
                        score_label.configure(text="Score:" + str(len(deleted_balls)))
                        checkwin()

            left(ball)
            right(ball)
            top(ball)
            top_right(ball)
            top_left(ball)
            bottom_right(ball)
            bottom_left(ball)

        while i>=1:
            if i not in deleted_balls:               
                try:
                    if abs(game_canvas.coords(i)[3] - shooter_coords[1])<5 and abs(game_canvas.coords(i)[0] - shooter_coords[0])<15:
                        if game_canvas.itemcget(i,"fill") == game_canvas.itemcget(shooter,"fill"):
                            explosion(i)
                            game_canvas.delete(shooter)
                            game_canvas.delete(i)
                            destroyed = True
                            deleted_balls.append(i)
                            score_label.configure(text="Score:" + str(len(deleted_balls)))
                            checkwin()
                            break
                        else:
                            score_label.configure(text='Score: ' + str(len(deleted_balls) - 1))
                            added = True
                            balls.append(shooter)
                            break
                except IndexError:
                    i-=1
                    continue
            i-=1

cheat_code=""
def Cheat(event):
    """
    Functions of cheat codes
    """
    global cheat_code,colors, deleted_balls
    cheat_code+=event.char
    if cheat_code == colors[0]:
        cheat_code=""
        for j in game_canvas.find_all():
            if game_canvas.itemcget(j,"fill")==colors[0]:
                deleted_balls.append(j)
                game_canvas.delete(j)
                score_label.configure(text="Score:" + str(len(deleted_balls)))
                checkwin()
    if cheat_code==colors[1]:
        cheat_code=""
        for j in game_canvas.find_all():
            if game_canvas.itemcget(j,"fill")==colors[1]:
                deleted_balls.append(j)
                game_canvas.delete(j)
                score_label.configure(text="Score:" + str(len(deleted_balls)))
                checkwin()
    if cheat_code==colors[2]:
        cheat_code=""
        for j in game_canvas.find_all():
            if game_canvas.itemcget(j,"fill")==colors[2]:
                deleted_balls.append(j)
                game_canvas.delete(j)
                score_label.configure(text="Score:" + str(len(deleted_balls)))
                checkwin()
    if cheat_code==colors[3]:
        cheat_code=""
        for j in game_canvas.find_all():
            if game_canvas.itemcget(j,"fill")==colors[3]:
                deleted_balls.append(j)
                game_canvas.delete(j)
                score_label.configure(text="Score:" + str(len(deleted_balls)))
                checkwin()
    if cheat_code not in "redyellowgreenblue":
        cheat_code=""

score_label = Label(game_canvas,text="SCORE :" + str(len(deleted_balls)), font=("Arial Bold", 40, "bold"),bg="pink3")
score_label.place(x=10, y= 570)




def Boss(event):
    """
    Displays a quick window for pretention
    """
    global Boss_click,Boss_label,height,width
    if Boss_click==0:
        Boss_label.place(anchor=CENTER,relx=0.5,rely=0.4)
        score_label.place_forget()
        Boss_click=1
    else:
        score_label.place(x=10, y= 640)
        Boss_label.place_forget()
        Boss_click=0

def checkwin():
    """
    Checks if all balls are deleted
    """
    global WIN_Label,deleted_balls
    if len(deleted_balls)==309:
        score_label.place_forget()
        WIN_Label.place(anchor=CENTER,relx=0.5,rely=0.4)

game_canvas.bind_all('<Key>',Cheat)
window.bind('<Return>',Boss)
window.bind('<space>', shooting)
window.bind('<Left>', laim)
window.bind('<Right>', raim)

configure_window()
window.mainloop()





