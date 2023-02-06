#Map navigation screen

screen mapbuttonUI: #alignment for the UI icon
    imagebutton: 
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        auto "UI/map_%s.png" #PLACEHOLDER LOCATION
        action ShowMenu("MapUI") #refers to MapUI function

screen dictbuttonUI: #alignment for the UI icon
    imagebutton: 
        xalign 1.0
        yalign 0.1
        xoffset -30
        yoffset 30
        auto "UI/map_%s.png" #PLACEHOLDER LOCATION
        action ShowMenu("DictUI") #refers to function




transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
screen pointandclick:

    $teleport = renpy.random.random() 
    imagebutton:
        xalign 1.0
        yalign 1.0
        xoffset -30
        yoffset 30
        auto "UI/Target_%s.png" #TARGET LOCATION
        action Hide("pointandclick")

init: #setting up timer variables
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0
    #$ click_success = 0
    
screen timer:
    timer 1 repeat True action If(time > 0, true = SetVariable('time', time -1), false =[Hide('countdown'),Jump(timer_jump)])
    #time decreases by 0.01 seconds and when it goes below 0, then it stops and jumps to a lose state
    if time <= 2:
        text str(time) xpos .5 ypos .1 color "#FF0000" at alpha_dissolve
    else:
        text str(time) xpos .5 ypos  .1 at alpha_dissolve





    



init python: #uses python
        def drag_placed(drags,drop): #function calling drag and drop vars
            if not drop:
                return #if no drop var then quit the game
            store.object = drags[0].drag_name #reference draggable from the drag group to drag var
            store.goalpiece = drop.drag_name #reference droppable from the drag group to drop var
            return True

screen draganddrop(): #for drag and drop mini game
    draggroup: #define the set of objects in one group. it's like an array in which the drag objects are part of this drag group
        drag: #object format must follow like this
            drag_name "obj" #name of obj
            child "catprofile.png" #source of img
            xpos 100 #position
            ypos 100 #position
            drag_raise True #can it be layered on top of another draggable? 
            draggable True #can it be draggable?
            droppable False #can it be dropped on?
            dragged drag_placed
        drag: #even droppable objects aka objects that dont need to be dragged on for goal puposes need the same format
            drag_name "Goal"
            child "catbruh.png"
            xpos 600
            ypos 600
            draggable False
            drag_raise False
            droppable True

init python:
        import random
    







#Map UI
screen MapUI(): #function to display map
    tag mapsUI
    add "Map/bg map.jpg" #PLACEHOLDER LOCATION

    imagebutton: #this is for the location
        xpos 618
        ypos 566
        idle "Map/house1_idle.png" #location for idle image
        hover "Map/house1_hover.png" #location for hover image
        action Jump("location1") #Jump allows to search for function in bracket from other scripts

screen DictUI(): #shows the dictionary picture
    tag magicdict
    add "images/Minigames/Memory_dict_placeholder.png" 

screen clicked(): 
    tag clickedon
"clicked on"
