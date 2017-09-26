x=0
y=600
flag = 0
dis = []
keyEvent = False

# SET THE VALUE FOR ANGLE HERE (< 85 degrees) AND OTHER PARAMETERS
vel = 90

angle = 30

steps = 5

gravity = 9.8

Res = 0.12

# If you want to see just one projection, replace False by True here:
stopAtOne = True


vel = float(vel)
angle = float(angle)
rads = (angle/180.0)*(3.14)
vx = vel*cos(rads)
vy = vel*sin(rads)
i = Res
angles = []

def setup():
    size(1000,600)
    strokeWeight(2)
    background(173,221,252)
    frameRate(90)
    textFont(createFont('San Serif', 17))
    textAlign(CENTER)
    fill(0)
    text('Enter a value for velocity(<=500) and angle(<=90).', width/2, 50)

def draw():
    global keyEvent
    if keyEvent == True:
        global flag
        if flag == 1:
            stroke(255,0,0)
        else:
            stroke(0)
        global x
        global angles
        global vx
        global vy
        global rads
        global Res
        global i
        global y
        global gravity
        global angle
        global dis
        global steps
        global stopAtOne
        prevx = x
        prevy = y
        x = vx*i
        y = height - (vy*i - 0.5*gravity*(i**2))
        line(prevx,prevy,x,y)
        i += Res
        if y<=height:
            pass
        else:
            dis.append(x)
            x=0
            y=600
            i = Res
            angles.append(angle)
            angle+=steps
            rads = (angle/180.0)*(3.14)
            vx = vel*cos(rads)
            vy = vel*sin(rads)
            if flag == 1:
                noLoop()
            elif(angle>85 or stopAtOne):
                for i in range(len(dis)):
                    if dis[i] == max(dis):
                        angle = angles[i]
                rads = (angle/180.0)*(3.14)
                vx = vel*cos(rads)
                vy = vel*sin(rads)
                x = 0
                y = 600
                i = Res
                strokeWeight(3)
                text("Best Distance travelled = %.2f at angle = %d degrees" %(max(dis), angle), width/2, 70)
                flag = 1

s = ''
param = vel
paramValue = 'Velocity'
params = 2

def checkKey():
    global s, param, paramValue, params, keyEvent
    global vel, angle, rads, vx, vy 
    if key >= '0' and key <= '9':
        fill(173,221,0)
        noStroke()
        rect(width/3, 0, 300, 30)
        s = s + key
        fill(255,0,0)
        text( paramValue +' = '+s, width/2,20)
    elif key == 's' and s !=None:
        print(int(s))
        print(params)
        if int(s) > 500 or ((params==1 and int(s)>=90)):
            s = ''
        else:
            params -=1
            if params==1:
                vel = int(s)
                vx = vel*cos(rads)
                vy = vel*sin(rads)
                paramValue = 'Angle'
            else:
                angle = int(s)
                rads = (angle/180.0)*(3.14)
                vx = vel*cos(rads)
                vy = vel*sin(rads)
                keyEvent = True
            s = ''
            


def keyPressed():
    global params
    if params>0:
        checkKey()     