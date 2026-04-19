define H = Character("Hina")
define A = Character("Airi")

image bg hina_room:
    "images/bg hina_room.jpg"
    size (1920, 1080)

image bg airi_room:
    "images/bg airi_room.jpg"
    size (1920, 1080)

image bg daylight:
    "images/bg daylight.jpg"
    size (1920, 1080)

define centerOffsetLeft = Position(xpos=0.6)
define centerMoreOffsetLeft = Position(xpos=0.58)
define droppedCenterOffsetLeft = Position(xpos=0.6, ypos=1.1)
define droppedLeft = Position(xpos=1, ypos=1.1)

label start:
    jump homestay
    play music "audio/bgm_hina_room.mp3" volume 0.5
    scene bg hina_room with fade
    "The clock strikes midnight"
    "July 26, 00:00."
    "Hina's birthday."
    "A bright message flashes on Hina's phone."
    show hina stand_1_2 at center with easeinleft:
        zoom 0.8
    H "A notification?"
    "Hina glances over at her screen. The text reads..."
    hide hina stand_1_2 with easeoutleft
    show airi cross_1_2 at center with easeinright:
        zoom 0.8
    A "Hina, Happy birthday!"
    A "Sorry, we haven't been able to spend much time together recently! How about today we go out on a date to celebrate? ⭐︎"
    hide airi cross_1_2 with easeoutright
    show hina stand_1_2 at center with easeinleft:
        zoom 0.8
    H "..."
    H "Ai-chan is really thinking about me…"
    H "A date…?" 
    extend "I want to go…"
    H "I wonder how I should reply…"
    H "Spending time on my birthday with Ai-chan is more than I could ever ask for."

    stop music fadeout 1.0


    jump daylight

label daylight:

    scene bg daylight with fade
    play music "audio/bgm_daylight.mp3" volume 0.4
    show hina stand_1_2 at left with easeinleft:
        zoom 0.8
    ""
    A "Hina!"
    show airi stand_1_5 at right with easeinright:
        zoom 0.8
    A "Sorry, I just got here. Did you wait?"
    show hina stand_1_4 at left with dissolve:
        zoom 0.8
    H "No, I just got here as well."
    "Hina had, in fact, shown up at the meeting location an hour earlier."
    show airi stand_1_4 at right with dissolve:
        zoom 0.8
    A "..."
    "Airi knew."
    "Hina's bangs were drenched in sweat from the summer's heat. It was so blatantly obvious."
    "She was also still hesitating on what kind of present to get Hina, hoping that the two of them would find something along the way, but a handkerchief would have been really good right now."
    show hina stand_1_1 at left with dissolve:
        zoom 0.8
    H "......"
    show airi cross_1_8 at right with dissolve:
        zoom 0.8
    A "Hina, you look kind of feverish. Are you okay?"
    show hina stand_1_3 at left with dissolve:
        zoom 0.8
    H "Ah- yeah. It's nothing. It's just really hot…"
    A "...Are you sure you don't need to rest at home?"

    menu:
        "Stay home":
            jump homestay
        "Go out anyway":
            jump outdoors

label homestay:

    H "Actually, I might have to after all."
    show airi think_1_3 at right with dissolve:
        zoom 0.8
    "There goes Airi's plans to acquire Hina's present. She's in a pinch!"
    show airi think_1_4 at right with dissolve:
        zoom 0.8
    A "Well, my house is also nearby. Do you want to come over? ♡"
    show hina stand_1_3 at left with dissolve:
        zoom 0.8
    H "Eh? Is that okay?"
    A "Of course. Once we get there, we can spend the time however we want."
    show hina stand_1_1 at left with dissolve:
        zoom 0.8
    H "???"
    show airi stand_1_8 at right with dissolve:
        zoom 0.8
    A "Haha, forget that. Let's just get going."
    
    scene bg airi_room with fade
    # Find music

    show hina stand_1_4 at left with easeinright:
        zoom 0.8
    show airi cross_1_1 at right with easeinright:
        zoom 0.8
    H "Pardon for intruding!"
    A "No need to be so uptight. Come sit."
    show airi cross_1_2 at right with dissolve:
        zoom 0.8
    A "I'll go get us something to drink."
    H "Okay!"
    hide airi cross_1_2 with easeoutright
    show hina stand_1_2 at left with dissolve:
        zoom 0.8
    H "..."
    H "What should I do..."

    menu:
        "Look around the room":
            scene bg hina_room with fade # Change to photograph later
            H "Oh? What's this?"
            H "How nostalgic…"
            H "I remember when Airi and I first went to the beach…"
            H "Times were much simpler then… and she would still talk to me in school…"
            H "Ai-chan, how I wish we could go back."
            "The door clicks."

    scene bg airi_room with fade
    show hina stand_1_2 at left:
        zoom 0.8
    show airi stand_1_3 at right with easeinright:
        zoom 0.8
    A "..." # Make sure this is a smile sprite
    show airi stand_1_5 at right with easeinright:
        zoom 0.8
    A "I got us juice."
    H "Thanks."
    "Hina fiddles with her straw."
    show airi stand_1_5 at right with dissolve:
        zoom 0.8
    A "...Were you looking at something?"
    show hina stand_1_3 zorder 10 at left with dissolve:
        zoom 0.8
    H "Ah, just the photo…"
    show airi think_1_6 at right with dissolve:
        zoom 0.8
    show hina stand_1_1 at left with dissolve:
        zoom 0.8
    "Airi takes a sip of her drink."
    A "Hmm…"
    show airi think_1_8 at right with dissolve:
        zoom 0.8
    A "Never mind that, we can have fun indoors, too."
    A "Like this."
    show airi stand_1_3 at right with dissolve:
        zoom 0.8
    "Airi inches closer to Hina and reaches out for her hair."
    show airi stand_1_3 at centerOffsetLeft with dissolve:
        zoom 0.8
    A "Don't move."
    "She runs her fingers through the white fluff, separating it as she moves along."
    show airi think_1_5 at centerOffsetLeft with dissolve:
        zoom 0.8
    A "Hina, aren't you supposed to look more special on your birthday?"
    H "…" 
    show airi think_1_8 at centerOffsetLeft with dissolve:
        zoom 0.8
    A "Let's do something cute for you."
    show hina stand_1_2 zorder 10 at droppedLeft with dissolve:
        zoom 0.8
    "Hina looks down, letting Airi take control."
    show airi think_1_2 at centerOffsetLeft with dissolve:
        zoom 0.8
    "Airi continues to do her delicate fingerwork on Hina's hair. The two sit in silence."
    "♫"
    "Airi begins humming a tune."
    show hina stand_1_4 zorder 10 at droppedLeft with dissolve:
        zoom 0.8
    H "…"
    H "I know where this is from!"
    H "Ai-chan, this is a song that Yoshimi likes."
    show airi cross_1_5 at centerOffsetLeft with dissolve:
        zoom 0.8
    A "Ah… Oh, her?"
    "Airi fails to remember the significance of Hinako's social circle."
    show airi cross_1_8 at centerOffsetLeft with dissolve:
        zoom 0.8
    A "Is that so?"
    "She isn't too fond of Hinako's mentioning of a plain-looking girl."
    show airi cross_1_3 at centerOffsetLeft with dissolve:
        zoom 0.8
    A "I'm sick of humming, let's put on a fun song instead."
    A "Give me your phone."
    show hina stand_1_5 zorder 10 at droppedLeft with dissolve: 
        zoom 1.0
    H "Alright."
    "Hina hands over her phone."
    "It unlocks to Hina's photo album, left wide open on display for Airi to see."
    "One of the albums titled 'Ai-chan' with a heart contained 312 items."
    "Out of curiosity, Airi taps on it."

    # bg change
    show airi cross_1_1 at droppedCenterOffsetLeft with dissolve:
        zoom 0.8
    A "Uwa, what is this? It's all…"
    A "Me."
    show hina stand_1_5 zorder 10 at droppedLeft with dissolve
    H "It's not what it looks like-"
    A "Is that so?"
    "Airi reaches her hand out to caress Hina, just to see her reaction."
    "She didn't exactly know how to feel about all this, but she did know that she found it cute how much Hina seemed to need her presence."
    show airi think_1_2 at droppedCenterOffsetLeft with dissolve:
        zoom 0.8
    A "Did I misunderstand?"
    H "…!"
    show airi cross_1_1 at centerOffsetLeft with dissolve:
        zoom 0.8
    A "I'll take that as a no."
    "For a second, the air felt light."
    show hina stand_1_2 zorder 10 at droppedLeft with dissolve:
        zoom 0.8
    "Hina felt as if her dream had come true."
    show airi stand_1_3 at centerMoreOffsetLeft with dissolve:
        zoom 0.8
    "Airi inches her face close to Hina's…"
    show airi stand_1_3 at center with dissolve:
        zoom 0.8
    "…only to pull it away."
    "Hina's face flushes."
    show airi stand_1_5 at center with dissolve:
        zoom 0.8
    A "Ahaha! What were you thinking just now?"
    show hina stand_1_5 zorder 10 at droppedLeft with dissolve:
        zoom 1.0
    "Hina grumbles."
    H "Ai-chan, don't play with me like that!"
    show airi stand_1_3 at left with dissolve:## temp
        zoom 0.8
    A "I don't know what you mean…"
    show airi think_1_6 at left with dissolve:## temp
        zoom 0.8
    "Airi lies back and searches for a 'better' song on Hina's phone."
    "The tune plays until the completion of Hina's hairdo — it falls with a sudden stop."
    show airi cross_1_3 at right with dissolve:
        zoom 0.8
    show hina stand_1_2 at left with dissolve
    A "Haah! I'm bored. Think of something you want to do, Hina."
    "Hina wants to get closer to Airi."
    "Give her an experience where she's closer than she's been with anyone else."
    show hina stand_1_3 at left with dissolve: 
        zoom 0.8
    H "How about we… bake something together?"
    "Good enough."
    show airi stand_1_8 at right with dissolve:
        zoom 0.8
    A "Alright."
    H "We can make pancakes, since you already made me a cake last year for my birthday. It'll be more enjoyable together."
    show airi think_1_7 at right with dissolve:
        zoom 0.8
    A "Do you already have ingredients?"
    show hina stand_1_2 at left with dissolve: 
        zoom 0.8
    H "Uhh… I ran out of eggs recently."
    show airi cross_1_1 at right with dissolve:
        zoom 0.8
    A "I'll go get them."
    show hina stand_1_4 at left with dissolve:
        zoom 0.8
    H "I'll come with-"
    show airi cross_1_2 at right with dissolve:
        zoom 0.8
    A "You can stay put. It's too hot for you anyway."
    show hina stand_1_2 at left with dissolve: 
        zoom 0.8
    H "Oh, right."
    A "I'll be back, Hina."
    show hina stand_1_4 at left with dissolve:
        zoom 0.8
    H "Mhm!"

    # bg change 

    "Supermarket Airi is ready to buy eggs."
    "Oho? But what's this?"
    "Sheep plushies. On sale for 15 percent off."
    "Meek, docile-looking, fluffy creatures staring into her."
    "For a second, they seemed to resemble her companion."
    "The perfect gift!"

    "Mission complete. All that's left is to return."

    # back to Hina's house

    A "I got the eggs."

    H "I prepared some ingredients while waiting for you."

    A "And here are the rest."

    H "Thank you, Ai-chan!!!"

    "Hina goes to hug Airi."

    # bg change

    A "Hina…"
    A "Don't get so close all of a sudden…"

    H "I'm just excited to see you again."
    H "Sometimes it feels like you'll completely free yourself from me."

    "Airi chuckles."

    A "You're always saying weird things."

    "Airi notices sugar on Hina's nose."

    A "Hold still."
    A "You have something on your face."

    "She wipes the white powder off Hina's face, cleaning her finger by licking the sugar off."

    A "If you keep being so careless, you'll end up a mess eventually."

    "Not that she minded to see Hina in a humiliating state."

    H "A-A-A-Ai-chan..!"

    "Hina faints."

    A "Oh dear."
    A "Are you okay, Hina?"

    H "I'm… just a little dazed, that's all…"

    "She couldn't let Airi find out that her little act sent her into a trance."

    A "As long as you're sure."
    A "How about you rest for a while? The heat was also pretty harsh on you."
    A "Don't worry about the pancakes, I'll take care of them. It's my treat."

    H "I was looking forward to making them together so much though~!"

    "A sigh escapes Hina's mouth."

    H "Okay…"

    A "Good. Let me know if you need anything."

    H "Alright…"

    "ZZZ"
    "7:00 p.m."

    A "Hina! Wake up."
    A "The pancakes are done."

    "Airi brings a fork with a piece of pancake up to Hina's mouth."

    A "Say 'aah'."

    H "Aah~."

    "Hina's eyes light up after taking a bite of the dessert."

    H "It's so fluffy !!!!"

    A "Right?"
    A "And here,"

    "Airi lights up a candle nearby, revealing a bigger pancake stack, placing the candle upon it."

    A "Make a wish, Hina."

    "Hina's eyes well up. She instinctively closes them to mask her teary expression, wishing upon this makeshift birthday cake that she and Airi could stay together forever in this life and beyond."
    "The light goes out as Hina blows the candle out, but her yearning does not vanish with it."

    A "Oh, it's getting quite late, isn't it?"
    A "I should get going soon…"

    menu:
        "Ask Airi to stay":
            jump homestay_good
        "Wish her off":
            jump homestay_bad

label homestay_good:
    return

label homestay_bad:
    return

label outdoors:

    H "It's okay, I'm fine. I've been wanting to enjoy the summer atmosphere together with Ai-chan."
    A "Okay then, let's go somewhere! Did you have anywhere in mind?"

    menu:
        "Beach":
            jump beach
        "Cafe":
            jump cafe
        "Let's just walk around":
            jump shops
