#PLEASE CHECK THE RENPY DOCUMENTATION BEFORE ASKING SOMETHING OVER HERE, IT'S EASY TO UNDERSTAND HOW TO WORK WITH THIS

define myst =Character("Mysterious Man", image = "mystprofile") #myst is how we will refer to this character in code. In-game he is currently called Mysterious Man
define you =Character("Player", image = "playerprofile") #same goes for player. 
define fade = Fade(1.0,4.0,3.0) #if you want to change transition speed, change values here. (FADEINTIME,HOLDTIME,FADEOUTTIME)
image magic1 = Movie(play="magappear.webm", side_mask=False, loop = False, image = "prologuemag.png")
image magic2 = Movie(play="magmove.webm", side_mask=False, loop = True)
image magic3 = Movie(play="magdim.webm", side_mask=False, loop = True)

image side mystprofile normalface = "mystprofile.png"
image side playerprofile catdefault = "catprofile.png"

# The game starts here.
label start: #this starts the game
with fade #this is a transition effect
#scene blackplaceholder


play music "magetheme.mp3" fadein 2.0 #song composed by MAOU on https://opengameart.org/content/mage-theme fadein allows for transition
#NOTE: ALL sound files must be kept in game folder and don't put it in a subfolder. Ren'py won't recognize it.


scene cg1 #to insert a sprite, type show filename. KEEP ALL IMAGES IN IMAGES FOLDER OF THE GAME
#NOTE: FILES NAMES SHOULD START WITH LOWER CASE
myst "“Welcome, chosen one - you might be confused about the circumstances you’re in but fret not, all will be revealed to you in due time.”" # put "" for dialogue 

"I wake up on a desk feeling confused and disoriented."

"My head throbs at the sudden view of the light across the room." 

myst "Welcome, chosen one." # put "" for dialogue 

you "........"

"I feel out of place."
"I look around at my surroundings and It seems that I am in a library..?" 
"Levitating candles, the tall dark bookshelves.."
"And wait.."

"Why does everything look much bigger than they usually do?"
"I tried to get up on the…desk?"


you "Why am I on a desk? Wait, who even are you?!" 
you "What exactly am I doing here? I don’t understand-"

scene cg2

"You lift your hand to point a finger at the mysterious char in front of you but you’re met with a paw." 
"A tiny, black paw, to be exact."

myst normalface "Calm down, little one - you’ve taken the form of a cat."

you catdefault "A CAT?! How is this possible? HOW am I able to speak?"

myst "Do not worry. The answers that you seek, will soon be revealed to you"

"Wow, that totally sounds reassuring."

scene prologuelib
"Waking up in a unfamilliar place. Meeting a complete stranger."
"Realising that I'm a talking cat... I should definitely not worry about this."

myst "“Well, can you feel that?”"

show magic1
"The presence of magic can be felt in the air."
"It feels quite heavy."
show magic2
"I feel a deep tug somewhere in the depths of my being."
"Something is pushing me to step forward and to accept this…energy."

myst "“What you’ve felt just now is a subtle force, or in other words, magic."
myst "It flows through everyone's veins, just as blood would, regardless of your societal status or your ancestral history."
show magic3
myst "It exists because your heart beats fervently."
myst "Careful now, magic isn’t something you can lightly wield because it can be it can be volatile and dangerous."
myst "If your emotional state is not in the right place." 
myst "But this is the primary reason why you and I can communicate well despite our differences in species."

you "...Is that right..?"
scene prologuelib

"I tried to wrack my head to recall any answers for this."
"Anything that could explain how all of this had happened in the first place."
"But nothing comes to mind" 


myst "Magic flows through your veins because you are also a familiar."
myst "A mystical companion that forms a deep bond with its chosen witch or wizard." 
myst "This allows the companion to gain certain skills and strengthens their magic through the shared bond."

you "If that’s the case then where is my partner? How did I get here?" 
you "I can’t remember anything before this…"

myst "“I know you have many questions but for starters, The place we are at is called TOWN NAME, found in the centre of COUNTRY NAME and we’re currently at our grand library."
myst "We are a quaint town and home to some of the best schools in magic - so you may find the answers that you seek if you stay long enough. "

myst "Prior to this conversation, I found you unconscious in front of the library three days ago."  
myst "You must’ve had a long journey from your origins, and hence I’ve ensured that you were taken…care of, per se."
myst "But you say you cannot recall anything? That is quite unfortunate. As for your chosen partner, that is another matter we will arrive at in the near future.”"

"Mysterious character lifts a finger and a flying thick book comes towards them. Immediately, its pages open and flips through several pages before landing on a single one. "
 #TO SHOW A SPRITE AGAIN OF THE SAME CHARACTER LATER ON, TRY TO HIDE IT using hide filename
"They quietly murmur something and look thoughtfully at the book."
"My cat hearing seems to be quite handy."

myst "Hmm..loss of memory…this might be a side effect."

"The book closes with a thud and the mysterious character faces you once more."


myst "“It seems that you’ll be under my care for as long as you’ll gain your memory back."  
myst "Do you have any questions for me in the meantime?"



label tutorialquestions: #labels are used to refer to certain events in the game, in this case it's the questions choice menu
    menu: #declare this if you want to make a choice selection
    
        "Who the hell are you?!": #option 1
            jump question1 #to go to answer of option 1, type jump and then a label name for reference
        "Will you eventually turn me back to what I was?": #option 2
            jump question2
        "I’ve got no more questions to ask": #option 3
            jump alldone

label question1: #option 1 answer
    myst "*chuckles* I see the cat has bared its claws. That’s quite rude of you don’t you think?"
 
    myst "After all, I was the one that had saved you. If you ask nicely, I might give away some information about myself."
   
    menu: #this is another choice selection. labels are only necessary if you wanna refer to them repeatedly or for something important
        "I’m sorry, but you look suspicious. Why is your face covered?":
            jump question1A
        "I woke up in an unknown place with no recollection of my memories! It’s only natural that I don’t trust you.":
            jump question1B
    label question1A:

        myst "“That’s better! This robe does seem intimidating doesn’t it?"
        myst  "Don’t worry, I have no interest in causing harm towards you."
        myst "Well, if you must know I’m the head librarian of this town - I ensure that the state of our knowledge is being kept up to date in our records."
        jump tutorialquestions #this goes back to the choices again

    label question1B:
       
        myst "Touché. I do not blame you - but I can assure you that I have no interest in harming you." 
    
        myst "It is your decision whether to trust me or not, but I only wish to help you. After all, I did take care of you all this time."
    
        "They are right..they did help me…if they wanted me gone, they would’ve killed me off immediately or left me to die in the streets.."
        you  "Alright, I’ll be under your care but only because I wish to know who I am, and how I’ve come to be."
        myst "Thank you. If it helps to ease your worries, I am the head librarian of this town." 
        myst "I make sure that our current knowledge of magic, our world and state of affairs are kept up to date in our records."
        jump tutorialquestions

label question2:#option 2

    myst "I will try my best to help you change back to your original form, however to do that we would have to acquire a memento of yours from your original form."
    myst "This could be a treasured trinket or something that you would have used often. Then only would we be able to trace out your roots and transform you back."

    you "But..I have nothing on me..right now. How am I supposed to find something from the past when I can’t even remember?" 
    you "I don’t even know if I was a cat this whole time or not."

    "Mysterious Character paused and looks at you with a thoughtful look."
    myst "“Familiars are often made from normal, unmodified animals. So you wouldn’t be wrong in thinking that you were technically a cat this whole time."
    myst "But your lack of memory and connection with being a cat is what's troubling."

    "Mysterious Character beckons a finger and several books come flying towards them again and opens simultaneously. The sound of turning pages echoed throughout the room."

    myst "“To successfully transform back, I would need you to have a strong bond with your magic - to be able to have a connection with yourself." 
    myst "I suppose, this is where I would tell you that you must find a partner you can bond with to strengthen your magic."

    you "”What?! I don’t even know anyone in this town. Let alone, I’ve never dealt with witches and wizards before.”"

    myst "“Perhaps this will be a good starting point then. After all, you must remember that the strength of your magic lies within your heart and is linked with your partner’s potential. "
    myst "Once the connection between you and your partner is strong enough, your magic will be stable enough to give you glimpses of your past, of your original self and then only can we establish a direct link to your original form along with your memento."

    "I sighed deeply and looked at the mysterious character wearily."
    "This sounds troublesome."
    "Not only am I dealing with my lack of memroy but now I must find someone to link with."

    myst "I know what you’re thinking but as I’ve said, I’m here to help you." 
    myst "You will not be doing this alone, I will provide aid when necessary and I will guide you to the right person that will be able to bond with you."

    you "“So how do I know whether a person is good enough to bond with?”"

    "Mysterious Character looks at you with a small smile."

    myst "That my dear companion, is up to you. As you once judged me and checked whether I was worthy of your trust or not, the same concept applies."
    myst "Once close enough to a person, you will be able to feel a slight tug of magic in yourself."
    myst "But to unlock its full potential you will have to know the person better. Just as you would with a new face, just as you have tried with me."
    jump tutorialquestions

label alldone: #option 3
    myst "My apologies, that was quite a lot of info splurged on there but I hope this has given you an idea of what you’re about to face."
    myst "Before you head off to the town and explore for yourself, I want to give you this map."
    myst "Take it, you’ll need it to navigate the area."
    myst "And please don’t forget, your magic is only as strong as the connection you have with yourself and with your partner."







return #return ends the game

