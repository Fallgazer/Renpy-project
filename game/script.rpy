# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")

define myst =Character("Mysterious Man")
define you =Character("Player")

# The game starts here.
label start:
#
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

   # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

  #  show eileen happy

    # These display lines of dialogue.

 #   e "You've created a new Ren'Py game."

#    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

myst "“Welcome, chosen one - you might be confused about the circumstances you’re in but fret not, all will be revealed to you in due time.”"

"You look around feeling a bit out of place. 
Confusion and wonder flickers across your eyes as you take in what is before you. "

"Levitating candles, the bubbling smoke of potions from the cauldron beside the fireplace and..Wait a second- 
why does everything look much bigger than they usually do? You quickly scramble on the….wait..desk…?"

you "“Uhm…why am I on a desk? Wait, who even are you?! What exactly am I doing here? I don’t understand-”"

"You lift your hand to point a finger at the mysterious char in front of you but you’re met with a paw. A tiny, black paw, to be exact."

myst "*chuckles* Calm down, little one - you’ve taken the form of a cat."

you "“A CAT?! How is this possible? HOW am I able to speak?”"

myst "“Well, can you feel that?”"

"The presence of magic can be felt in the air and it feels quite heavy. You feel a tug somewhere in 
the depths of your being, as if it’s beckoning you to step forward and to accept it immediately."

myst "“What you’ve felt just now is a subtle force, or in other words, magic. It flows through everyone's veins, just as blood would, regardless of your societal status or your ancestral history. "
"It exists because your heart beats fervently. Careful now, magic isn’t something you can lightly wield or summon into existence. It can be volatile and dangerous if your emotional state is not in the right place. 
But this is the primary reason why you and I can communicate well despite our differences in species.”"

you "“...Is that right..?”"

"You look at your outstretched paws - opening and closing them, you can feel something electric flowing through them. 
You held your breath and tried to recall any events before this - nothing comes to mind."

myst "“Indeed, magic flows through your veins because you are also a familiar. A mystical companion that forms a deep bond with its chosen witch or wizard. 
This allows the companion to gain certain skills and strengthens their magic through the shared bond. ”"

you " “If that’s the case then where is my partner? How did I get here? I can’t remember anything before this…”"

myst "“I know you have many questions but for starters, The place we are at is called TOWN NAME, found in the centre of COUNTRY NAME and we’re currently at our grand library.
We are a quaint town and home to some of the best schools in magic - so you may find the answers that you seek if you stay long enough. "

myst "Prior to this conversation, I found you unconscious in front of the library three days ago.  
You must’ve had a long journey from your origins, and hence I’ve ensured that you were taken…care of, per se.
But you say you cannot recall anything? That is quite unfortunate. As for your chosen partner, that is another matter we will arrive at in the near future.”"

"Mysterious character lifts a finger and a flying thick book comes towards them. Immediately, its pages open and flips through several pages before landing on a single one. "

myst "*Reads the page and whispers*  “Hmm..loss of memory…this might be a side effect.”"

"The book closes with a thud and the mysterious character faces you once more."

myst "“It seems that you’ll be under my care for as long as you’ll gain your memory back.  Do you have any questions for me in the meantime?”"


menu:

    "Who the hell are you?!":
        jump question1
    "Will you eventually turn me back to what I was?":
        jump question2
    "I’ve got no more questions to ask":
        jump alldone

label question1:
    myst "*chuckles* I see the cat has bared its claws. That’s quite rude of you don’t you think? 
    After all, I was the one that had saved you. If you ask nicely, I might give away some information about myself.”"
    menu:
        "I’m sorry, but you look suspicious. Why is your face covered?":
            jump question1A
        "I woke up in an unknown place with no recollection of my memories! It’s only natural that I don’t trust you.":
            jump question1B
    label question1A:
        myst "“That’s better! This robe does seem intimidating doesn’t it? Don’t worry, I have no interest in causing harm towards you. 
        Well, if you must know I’m the head librarian of this town - I ensure that the state of our knowledge is being kept up to date in our records.”"
    label question1B:
        myst "“Touché. I do not blame you - but I can assure you that I have no interest in harming you. 
        It is your decision whether to trust me or not, but I only wish to help you. After all, I did take care of you all this time.”"
        you "((They are right..they did help me…if they wanted me gone, they would’ve killed me off immediately or left me to die in the streets..)) 
        Alright, I’ll be under your care but only because I wish to know who I am, and how I’ve come to be. "
        myst "Thank you. If it helps to ease your worries, I am the head librarian of this town. I make sure that our current knowledge of magic, our world and state of affairs are kept up to date in our records."

label question2:
    myst " “I will try my best to help you change back to your original form, however to do that we would have to acquire a memento of yours from your original form. 
    This could be a treasured trinket or something that you would have used often. Then only would we be able to trace out your roots and transform you back. “"

    you "“But..I have nothing on me..right now. How am I supposed to find something from the past when I can’t even remember? I don’t even know if I was a cat this whole time or not.”"

    "Mysterious Character paused and looks at you with a thoughtful look."
    myst "“Familiars are often made from normal, unmodified animals. So you wouldn’t be wrong in thinking that you were technically a cat this whole time but your lack of memory and connection with being a cat is what's troubling.”"

    "Mysterious Character beckons a finger and several books come flying towards them again and opens simultaneously. The sound of turning pages echoed throughout the room."

    myst "“To successfully transform back, I would need you to have a strong bond with your magic - to be able to have a connection with yourself. 
    I suppose, this is where I would tell you that you must find a partner you can bond with to strengthen your magic.”"

    you "”What?! I don’t even know anyone in this town. Let alone, I’ve never dealt with witches and wizards before.”"

    myst "“Perhaps this will be a good starting point then. After all, you must remember that the strength of your magic lies within your heart and is linked with your partner’s potential. 
    Once the connection between you and your partner is strong enough, your magic will be stable enough to give you glimpses of your past, of your original self and then only can we establish a direct link to your original form along with your memento."

    "You sighed deeply and looked at the mysterious character wearily."

    you "((This sounds like a lot to handle and do. Not only am I dealing with my lack of memory but now I must find someone to link with.))"

    myst "“I know what you’re thinking but as I’ve said, I’m here to help you. You will not be doing this alone, I will provide aid when necessary and I will guide you to the right person that will be able to bond with you.”"

    you "“So how do I know whether a person is good enough to bond with?”"

    "Mysterious Character looks at you with a small smile. "

    myst " “That my dear companion, is up to you. As you once judged me and checked whether I was worthy of your trust or not, the same concept applies. 
    Once close enough to a person, you will be able to feel a slight tug of magic in yourself but to unlock its full potential you will have to know the person better. Just as you would with a new face, just as you have tried with me.”"


label alldone:
    myst "*chuckles* My apologies, that was quite a lot of info splurged on there but I hope this has given you an idea of what you’re about to face. 
    Before you head off to the town and explore for yourself, I want to give you this map. "
    "Take it, you’ll need it to navigate the area. And please don’t forget, your magic is only as strong as the connection you have with yourself and with your partner. "







return

