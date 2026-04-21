define H = Character("Hina")
define A = Character("Airi")

define centerOffsetLeft = Position(xpos=0.6)
define droppedCenterOffsetLeft = Position(xpos=0.6, ypos=1.1)
define droppedLeft = Position(xpos=1, ypos=1.1)

transform up:
    ypos 0.8

transform new:
    fit "contain"
    xysize (900,900)
    xoffset 0

transform standard:
    fit "contain"
    xysize (1000,1000)
    xoffset 38

transform bg_standard:
    fit "cover"
    size (1920, 1080)

label start:
    play music "audio/bgm_hina_room.mp3" volume 0.5
    scene bg hina_room at bg_standard with fade
    "The clock strikes midnight"
    "July 26, 00:00."
    "Hina's birthday."
    "A bright message flashes on Hina's phone."
    show hina stand_1_2 at standard, center with easeinleft
    H "A notification?"
    "Hina glances over at her screen. The text reads..."
    hide hina stand_1_2 with easeoutleft
    show airi cross_1_2 at standard, center with easeinright
    A "Hina, Happy birthday!"
    A "Sorry, we haven't been able to spend much time together recently! How about today we go out on a date to celebrate? ⭐︎"
    hide airi cross_1_2 with easeoutright
    show hina cross_1_2 at new, center with easeinleft
    H "..."
    H "Ai-chan is really thinking about me…"
    H "A date…?" 
    extend "I want to go…"
    H "I wonder how I should reply…"
    H "Spending time on my birthday with Ai-chan is more than I could ever ask for."

    stop music fadeout 1.0


    jump daylight

label daylight:

    scene bg daylight at bg_standard with fade
    play music "audio/bgm_daylight.mp3" volume 0.4
    show hina stand_1_2 at standard, left with easeinleft
    ""
    A "Hina!"
    show airi stand_1_5 at standard, right with easeinright
    A "Sorry, I just got here. Did you wait?"
    show hina stand_1_4 at standard, left with dissolve
    H "No, I just got here as well."
    show hina think_1_7 at new, left with dissolve
    "Hina had, in fact, shown up at the meeting location an hour earlier."
    show airi stand_1_4 at standard, right with dissolve
    A "..."
    "Airi knew."
    "Hina's bangs were drenched in sweat from the summer's heat. It was so blatantly obvious."
    "She was also still hesitating on what kind of present to get Hina, hoping that the two of them would find something along the way, but a handkerchief would have been really good right now."
    show hina stand_1_1 at standard, left with dissolve
    H "......"
    show airi cross_1_8 at standard, right with dissolve
    A "Hina, you look kind of feverish. Are you okay?"
    show hina cross_1_15 at new, left with dissolve
    H "Ah- yeah. It's nothing. It's just really hot…"
    A "...Are you sure you don't need to rest at home?"

    menu:
        "Stay home":
            jump homestay
        "Go out anyway":
            jump outdoors

label homestay:

    H "Actually, I might have to after all."
    show airi think_1_3 at standard, right with dissolve
    "There goes Airi's plans to acquire Hina's present. She's in a pinch!"
    H "Well, my house is also nearby. Do you want to come over?"
    show hina stand_1_3 at standard, left with dissolve
    A "Is that okay?"
    H "Of course. Once we get there, we can spend the time however we want."
    show airi think_1_1 at standard, right with dissolve
    A "???"
    show hina cross_1_5 at new, left with dissolve
    H "Haha, forget that. Let's just get going."
    
    scene bg hina_room_day at bg_standard with fade
    # Find music
    show hina stand_1_2 at standard, left with easeinright
    show airi cross_1_1 at standard, right with easeinright
    A "Pardon for intruding!"
    show hina stand_1_4 at new, left with easeinright
    H "No need to be so uptight. Come sit."
    show airi cross_1_2 at standard, right with dissolve
    A "You must be tired from being in the heat. I'll pour us some water."
    H "Okay!"
    hide airi cross_1_2 with easeoutright
    show hina think_1_1 at new, left with dissolve
    H "..."
    H "What should I do..."

    menu:
        "Look around the room":
            scene bg photo at bg_standard with fade # Change to photograph later
            H "Oh? What's this?"
            H "How nostalgic…"
            H "I remember when Airi and I first went to the beach…"
            H "Times were much simpler then… and she would still talk to me in school…"
            H "Ai-chan, how I wish we could go back."
            "The door clicks."

    scene bg hina_room_day at bg_standard with fade
    show hina stand_1_2 at standard, left with dissolve
    show airi stand_1_3 at standard, right with easeinright
    A "..." # Make sure this is a smile sprite
    show airi stand_1_5 at standard, right with easeinright
    A "I got us juice."
    show hina stand_1_14 at new, left with dissolve
    H "Thanks."
    show hina stand_1_2 at standard, left with dissolve
    "Hina fiddles with her straw."
    show airi stand_1_5 at standard, right with dissolve
    A "...Were you looking at something?"
    show hina cross_1_7 at new, left with dissolve
    H "Ah, just the photo…"
    show airi think_1_6 at standard, right with dissolve
    show hina cross_1_3 at new, left with dissolve
    "Airi takes a sip of her drink."
    A "Hmm…"
    show airi think_1_8 at standard, right with dissolve
    A "Never mind that, we can have fun indoors, too."
    A "Like this."
    show airi stand_1_3 at standard, right with dissolve
    "Airi inches closer to Hina and reaches out for her hair."
    show airi stand_1_3 at standard, centerOffsetLeft with dissolve
    A "Don't move."
    show hina cross_1_12 at new, left with dissolve
    "She runs her fingers through the white fluff, separating it as she moves along."
    show airi think_1_5 at standard, centerOffsetLeft with dissolve
    A "Hina, aren't you supposed to look more special on your birthday?"
    show hina cross_1_11 at new, left with dissolve
    H "…" 
    show airi think_1_8 at standard, centerOffsetLeft with dissolve
    A "Let's do something cute for you."
    show hina cross_1_13 zorder 10 at new, droppedLeft with dissolve
    "Hina looks down, letting Airi take control."
    show airi think_1_2 at standard, centerOffsetLeft with dissolve
    "Airi continues to do her delicate fingerwork on Hina's hair. The two sit in silence."
    "♫"
    "Airi begins humming a tune."
    show hina cross_1_14 zorder 10 at new, droppedLeft with dissolve
    H "…"
    H "I know where this is from!"
    H "Ai-chan, this is a song that Yoshimi likes."
    show airi cross_1_5 at standard, centerOffsetLeft with dissolve
    A "Ah… Oh, her?"
    show hina cross_1_11 zorder 10 at new, droppedLeft with dissolve
    "Airi fails to remember the significance of Hinako's social circle."
    show airi cross_1_8 at standard, centerOffsetLeft with dissolve
    A "Is that so?"
    "She isn't too fond of Hinako's mentioning of a plain-looking girl."
    show airi cross_1_3 at standard, centerOffsetLeft with dissolve
    A "I'm sick of humming, let's put on a fun song instead."
    A "Give me your phone."
    show hina stand_1_5 zorder 10 at new, droppedLeft with dissolve
    H "Alright."
    "Hina hands over her phone."
    "It unlocks to Hina's photo album, left wide open on display for Airi to see."
    "One of the albums titled 'Ai-chan' with a heart contained 312 items."
    "Out of curiosity, Airi taps on it."
    show airi cross_1_1 at standard, droppedCenterOffsetLeft with dissolve
    A "Uwa, what is this? It's all…"
    A "Me."
    show hina think_1_11 zorder 10 at new, droppedLeft with dissolve
    H "It's not what it looks like-"
    A "Is that so?"

    scene bg closeness_1 at bg_standard with fade
    "Airi reaches her hand out to caress Hina, just to see her reaction."
    "She didn't exactly know how to feel about all this, but she did know that she found it cute how much Hina seemed to need her presence."
    scene bg closeness_2 at bg_standard
    A "Did I misunderstand?"
    H "…!"
    A "I'll take that as a no."
    scene bg closeness_9 at bg_standard
    "For a second, the air felt light."
    "Hina felt as if her dream had come true."
    "Airi inches her face close to Hina's…"
    scene bg closeness_2 at bg_standard
    "…only to pull it away."
    scene bg closeness_4 at bg_standard
    "Hina's face flushes."
    A "Ahaha! What were you thinking just now?"
    "Hina grumbles."
    scene bg closeness_6 at bg_standard
    H "Ai-chan, don't play with me like that!"
    scene bg closeness_8 at bg_standard
    A "I don't know what you mean…"
    scene bg hina_room_day at bg_standard with fade
    show hina stand_1_10 at new, left with dissolve ### This is bugged and have to settle with basic positioning instead of dropped for haircut
    show airi cross_1_1 at standard, right with dissolve
    "Airi lies back and searches for a 'better' song on Hina's phone."
    "The tune plays until the completion of Hina's hairdo — it falls with a sudden stop."
    show airi cross_1_3 at standard, right with dissolve
    show hina stand_1_2 at standard, left with dissolve
    A "Haah! I'm bored. Think of something you want to do, Hina."
    "Hina wants to get closer to Airi."
    "Give her an experience where she's closer than she's been with anyone else."
    show hina stand_1_3 at standard, left with dissolve
    H "How about we… bake something together?"
    "Good enough."
    show airi stand_1_8 at standard, right with dissolve
    A "Alright."
    H "We can make pancakes, since you already made me a cake last year for my birthday. It'll be more enjoyable together."
    show airi think_1_7 at standard, right with dissolve
    A "Do you already have ingredients?"
    show hina think_1_13 at new, left with dissolve
    H "Uhh… I ran out of eggs recently."
    show airi cross_1_1 at standard, right with dissolve
    A "I'll go get them."
    show hina think_1_4 at new, left with dissolve
    H "I'll come with-"
    show airi cross_1_2 at standard, right with dissolve
    A "You can stay put. It's too hot for you anyway."
    show hina think_1_12 at new, left with dissolve
    H "Oh, right."
    A "I'll be back, Hina."
    show hina cross_1_2 at new, left with dissolve
    H "Mhm!"
    hide airi cross_1_2 with easeoutright

    scene bg store at bg_standard with fade
    show airi think_1_2 at standard, center with dissolve
    "Supermarket Airi is ready to buy eggs."
    show airi think_1_5 at standard, left with dissolve
    "Oho? But what's this?"
    show plush lamb at standard, right, up with dissolve
    "Sheep plushies. On sale for 15 percent off."
    "Meek, docile-looking, fluffy creatures staring into her."
    "For a second, they seemed to resemble her companion."
    show airi think_1_8 at standard, left with dissolve
    "The perfect gift!"
    "Mission complete. All that's left is to return."

    scene bg hina_room_day at bg_standard with fade
    show hina cross_1_2 at new, left with dissolve
    show airi stand_1_8 at standard, right with easeinright
    A "I got the eggs."
    show hina cross_1_4 at new, left with dissolve
    H "I prepared some ingredients while waiting for you."
    show airi stand_1_8 at standard, right with dissolve
    A "And here are the rest."
    H "Thank you, Ai-chan!!!"
    "Hina goes to hug Airi."

    scene bg closeness_9 at bg_standard with fade
    A "Hina…"
    A "Don't get so close all of a sudden…"
    scene bg closeness_7 at bg_standard
    H "I'm just excited to see you again."
    H "Sometimes it feels like you'll completely free yourself from me."
    "Airi chuckles."
    scene bg closeness_6 at bg_standard
    A "You're always saying weird things."
    scene bg closeness_8 at bg_standard
    "Airi notices sugar on Hina's nose."
    A "Hold still."
    A "You have something on your face."
    scene bg closeness_9 at bg_standard
    "She wipes the white powder off Hina's face, cleaning her finger by licking the sugar off."
    A "If you keep being so careless, you'll end up a mess eventually."
    scene bg closeness_8 at bg_standard
    "Not that she minded to see Hina in a humiliating state."
    H "A-A-A-Ai-chan..!"
    "Hina faints."

    scene bg hina_room_day at bg_standard with fade
    show airi think_1_1 at standard, center with dissolve
    A "Oh dear."
    A "Are you okay, Hina?"
    H "I'm… just a little dazed, that's all…"
    "She couldn't let Airi find out that her little act sent her into a trance."
    show airi think_1_3 at standard, center with dissolve
    A "As long as you're sure."
    show airi think_1_7 at standard, center with dissolve
    A "How about you rest for a while? The heat was also pretty harsh on you."
    A "Don't worry about the pancakes, I'll take care of them. It's my treat."
    show airi think_1_3 at standard, right with dissolve
    show hina stand_1_8 at new, left with dissolve
    H "I was looking forward to making them together so much though~!"
    "A sigh escapes Hina's mouth."
    show hina cross_1_12 at new, left with dissolve
    H "Okay…"
    A "Good. Let me know if you need anything."
    hide airi think_1_3 with easeoutright
    show hina cross_1_14 at new, left with dissolve
    H "Alright…"
    show hina stand_1_12 at new, left with dissolve
    "ZZZ"
    "5:30 p.m."
    show airi cross_1_4 at standard, right with easeinright
    A "Hina! Wake up."
    show hina stand_1_9 at new, left with dissolve
    A "The pancakes are done."

    scene bg kitchen at bg_standard with fade
    show airi cross_1_1 at standard, right with dissolve
    show hina stand_1_2 at standard, left with dissolve
    "Airi brings a fork with a piece of pancake up to Hina's mouth."
    A "Say 'aah'."
    show hina stand_1_4 at standard, left with dissolve
    H "Aah~."
    show hina cross_1_4 at new, left with dissolve
    "Hina's eyes light up after taking a bite of the dessert."
    H "It's so fluffy !!!!"
    show airi cross_1_2 at standard, right with dissolve
    A "Right?"
    A "And here,"
    "Airi lights up a candle nearby, revealing a bigger pancake stack, placing the candle upon it."
    show airi cross_1_1 at standard, right with dissolve
    A "Make a wish, Hina."
    show hina think_1_4 at new, left with dissolve
    "Hina's eyes well up. She instinctively closes them to mask her teary expression, wishing upon this makeshift birthday cake that she and Airi could stay together forever in this life and beyond."
    "The light goes out as Hina blows the candle out, but her yearning does not vanish with it."
    show airi think_1_2 at standard, right with dissolve
    A "Oh, it's getting quite late, isn't it?"
    A "I should get going soon…"

    menu:
        "Ask Airi to stay":
            jump homestay_good
        "Wish her off":
            jump homestay_bad

label homestay_good:
    show hina cross_1_14 at new, left with dissolve
    H "Ai-chan, wait-"
    show airi stand_1_3 at standard, right with dissolve
    A "Hm?"
    show hina think_1_15 at new, left with dissolve
    H "Would you like to just… stay over for tonight?"
    show airi think_1_10 at standard, right with dissolve
    "Airi ponders to herself."
    show airi think_1_4 at standard, right with dissolve
    A "If you don't mind."
    show hina cross_1_4 at new, left with dissolve
    "Hina lights up."
    "The two of them enjoy pancakes before nightfall, then comfortably tuck themselves into bed."

    scene bg hina_room at bg_standard with fade
    show airi stand_1_6 at standard, left with easeinright
    show hina think_1_10 at new, right with easeinright
    "Airi climbs into Hina's bed."
    show hina think_1_14 at new, right with dissolve
    H "Ai-chan??"
    show airi cross_1_1 at standard, left with dissolve
    A "This is fine, right?"
    show hina cross_1_12 at new, right with dissolve
    H "…Yeah."
    A "Oh, I almost forgot."
    "Airi takes out the lamb plushie from her shopping bag from earlier."
    show plush lamb at standard, center, up with dissolve
    show airi cross_1_2 at standard, left with dissolve
    A "Happy Birthday, Hina."
    show hina cross_1_14 at new, right with dissolve
    "Hina gasps."
    show hina cross_1_4 at new, right with dissolve
    H "It's so cute—!"
    H "Thank you, Ai-chan, thank you!"
    H "I couldn't be happier..."
    show airi cross_1_1 at standard, left with dissolve
    A "I'm glad. Goodnight, Hina."
    H "Goodnight!"

    scene bg homestay_good_end at bg_standard with fade
    "Under one roof, the two share dreams and slumber."
    "For this night, Airi belongs to Hina."
    "If only it were her birthday every day. Would it be too much to ask?"

    return

label homestay_bad:
    show hina cross_1_5 at new, left with dissolve
    H "...yeah. Thanks for today, Ai-chan."
    show airi think_1_4 at standard, right with dissolve
    A "It's my pleasure."
    show airi think_1_5 at standard, right with dissolve
    A "Oh, I almost forgot."
    show airi cross_1_1 at standard, right with dissolve
    A "Here's something for you."
    show plush lamb at standard, center, up with dissolve
    "Airi hands Hina the sheep plushie from the grocery store."
    A "This is a little something for you."
    show hina cross_1_3 at new, left with dissolve
    "A weak smile forms on Hina's face."
    show hina cross_1_2 at new, left with dissolve
    H "I appreciate it, Ai-chan."
    H "Goodnight, see you tomorrow."
    A "Goodnight, Hina."

    scene black with fade
    "As much as Hina wanted to, she could not bring herself to call out to Airi."
    "The weight was crushing. She was well aware that she and Airi would go back to normal once school commences, no interaction occurring between them."
    "Maybe if she kept staring into the little lamb, she could preserve the feeling of Airi's presence a little longer."

    return

label outdoors:

    H "It's okay, I'm fine. I've been wanting to enjoy the summer atmosphere together with Ai-chan."
    A "Okay then, let's go somewhere! Did you have anywhere in mind?"

    menu:
        "Beach":
            jump beach

label beach:
    return
