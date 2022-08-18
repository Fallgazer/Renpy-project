screen choose_route: #declare the screen for its use
    add "placeholder_for_route.png" #adds background
    hbox: #invisible horizontal box that adds items side by side. below are dimensions for how each box should be placed
        xalign 0.5
        yalign 0.5
        yoffset 30 #probably offset from bottom screen
        spacing 20 #maybe spacing between each item


        imagebutton: #allows the image to be clickable
            auto "choice1.png"
            action Jump("gotochoice1") #if this choice is selected then go to this route
            
        imagebutton:
            auto "choice2.png"
            action Jump("gotochoice2") #if this choice is selected then go to this route

        imagebutton:
            auto "choice1.png"
            action Jump("gotochoice3") #if this choice is selected then go to this route
