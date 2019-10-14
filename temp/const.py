#settings
WIDTH=900
HEIGHT=600
player_width=50
player_height=50

#for jump
PLAYER_ACC=2
PLAYER_FRICTION=-0.2
PLAYER_GRAVITY=0.8

#충돌검사 위함
#(x,y,w,h)
PlatformList=[(0,0,100,30,1),(100,0,100,30,1),(200,0,100,30,1),(300,0,100,30,1),
(400,0,100,30,1),(500,0,100,30,1),(600,0,100,30,1),(700,0,100,30,1),(800,0,100,30,1),
(0,570,100,30,1),(100,570,100,30,1),(200,570,100,30,1),(300,570,100,30,1),
(400,570,100,30,1),(500,570,100,30,1),(600,570,100,30,1),(700,570,100,30,1),(800,570,100,30,1),

(0,490,100,30,1),(100,490,100,30,1),(200,490,100,30,1),
(300,470,100,30,1),(400,450,100,30,1),(700,480,100,30,1),
(800,480,100,30,1),

(470,350,30,100,4),(470,350,100,30,1),(470,250,100,30,6),(540,250,30,100,4),

(0,380,100,30,1),(100,350,100,30,1),(200,350,100,30,1),
(270,250,30,100,4),(270,250,100,30,1),(0,350,30,30,7),
(300,275,70,70,5),(370,250,30,100,4),
(370,250,100,30,1),(600,420,100,30,1),(600,400,100,20,3),

(800,320,100,30,1),(800,300,100,20,3),(700,320,100,30,1),(700,300,100,20,3),(670,250,30,100,4),

(350,110,100,30,1),(250,110,100,30,1),(450,30,30,100,4),(450,180,30,100,4),
(450,150,30,100,4),(450,50,30,100,4),(0,200,100,30,1),(100,200,100,30,1),

(600,100,100,30,1),(700,100,100,30,1),(620,70,30,30,7),(520,180,100,30,1)]

#for sprite animation-walk
EVENT=4
RIGHT=0
LEFT=1
WALKRIGHT=2
WALKLEFT=3
