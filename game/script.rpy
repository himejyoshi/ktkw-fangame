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

label start:
    
    play music "audio/bgm_hina_room.mp3" volume 0.5
    scene bg hina_room
    with fade
    "The clock strikes midnight"
    "July 26, 00:00."
    "Hina's birthday."
    "A bright message flashes on Hina's phone."
    show hina_1_2_stand at center with easeinleft:
        zoom 0.8
    H "A notification?"
    "Hina glances over at her screen. The text reads..."
    hide hina_1_2_stand with easeoutleft
    show airi cross_1_2 at center with easeinright:
        zoom 0.8
    A "Hina, Happy birthday!"
    A "Sorry, we haven't been able to spend much time together recently! How about today we go out on a date to celebrate? ⭐︎"
    hide airi cross_1_2 with easeoutright
    show hina_1_2_stand at center with easeinleft:
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

    scene bg daylight
    with fade
    play music "audio/bgm_daylight.mp3" volume 0.4
    show hina_1_2_stand at left with easeinleft:
        zoom 0.8
    ""
    A "Hina!"
    show airi stand_1_5 at right with easeinright:
        zoom 0.8
    A "Sorry, I just got here. Did you wait?"
    show hina_1_4_stand at left with dissolve:
        zoom 0.8
    H "No, I just got here as well."
    "Hina had, in fact, shown up at the meeting location an hour earlier."
    show airi stand_1_4 at right with dissolve:
        zoom 0.8
    A "..."
    "Airi knew."
    "Hina's bangs were drenched in sweat from the summer's heat. It was so blatantly obvious."
    "She was also still hesitating on what kind of present to get Hina, hoping that the two of them would find something along the way, but a handkerchief would have been really good right now."
    show hina_1_1_stand at left with dissolve:
        zoom 0.8
    H "......"
    show airi cross_1_8 at right with dissolve:
        zoom 0.8
    A "Hina, you look kind of feverish. Are you okay?"
    show hina_1_3_stand at left with dissolve:
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
    show hina_1_3_stand at left with dissolve:
        zoom 0.8
    H "Eh? Is that okay?"
    A "Of course. Once we get there, we can spend the time however we want."
    show hina_1_1_stand at left with dissolve:
        zoom 0.8
    H "???"
    show airi stand_1_8 at right with dissolve:
        zoom 0.8
    A "Haha, forget that. Let's just get going."
    
    # Load Airi's room and add more dialogue

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

label beach:
    # Beach route

label cafe:
    # Cafe route

label shops:
    # Shops route
