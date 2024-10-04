# MAZE GAME
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
window.fullscreen  = True

# 1. buat entity lantai
ground = Entity(model='plane', 
                scale=(50,1,50), 
                color=color.white.tint(-.2), 
                texture='white_cube', 
                texture_scale=(50,50), 
                collider='box')

# 2. buat entity player
player = FirstPersonController(model='cube',
                               collider = 'box', 
                               position=(0,0,-2))

# 3. set lokasi random finish
locations = set()
for i in range(0,300):
    x = random.randrange(-24,24,2)
    y = 0
    z = random.randrange(-24,24,2)
    locations.add((x,y,z))
finish_location = random.choice(list(locations))
locations.remove(finish_location)

# 4. buat entity finish
finish = Entity(model = 'cube', 
                scale=(2,2,1), 
                color=color.green, 
                collider = 'box', 
                position = finish_location)

# 5. buat looping untuk random maze
for loc in locations:
    cube_width = 2
    cube_height = random.randrange(2,8,1)
    cube_depth = 2
    obstacle = Entity(model='cube', 
                    scale=(cube_width,cube_height,cube_depth),
                    position= loc,
                    texture='brick',
                    color=color.yellow.tint(.4),
                    collider='box')
#6. update finish jika found cube finish
def update(): 
    hit_info = player.intersects()
    if hit_info.hit:
        if hit_info.entity == finish:    
            message = Text(text = 'You WON', scale=2, origin=(0,0), background=True, color=color.blue)
            application.pause()
            mouse.locked = False 

# waktu menemukan cube finish
countdown=15
def timedown():
    global countdown
    count = Text(text = 'Countdown: '+str(countdown), origin=(0,-6),color=color.white)
    count.fade_out(0,0.5)
    countdown-=1
    seq = invoke(timedown, delay=1)
    if countdown == -1:
        end = Text(text = 'You LOST', scale=2, origin=(0,0), background=True, color=color.blue)
        application.pause()
        mouse.locked = False
        seq.kill()
timedown()

def input(key):
    if key == 'q':
        quit()
app.run()