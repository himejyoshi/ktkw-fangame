define H = Character("Hina")
define A = Character("Airi")

label start:

    "The clock strikes midnight"
    "July 26, 00:00."
    "Hina's birthday."
    "A bright message flashes on Hina's phone."
    H "A notification?"
    "Hina glances over at her screen. The text reads..."
    A "Hina, Happy birthday!"
    A "Sorry, we haven't been able to spend much time together recently! How about today we go out on a date to celebrate? ⭐︎"
    H "..."
    H "Ai-chan is really thinking about me…"
    H "A date…?" 
    extend "I want to go…"
    H "I wonder how I should reply…"
    H "Spending time on my birthday with Ai-chan is more than I could ever ask for."

    jump daylight

label daylight:

    A "Hina!"
    A "Sorry, I just got here. Did you wait?"
    H "No, I just got here as well."
    "Hina had, in fact, shown up at the meeting location an hour earlier."
    A "..."
    "Airi knew."
    "Hina's bangs were drenched in sweat from the summer's heat. It was so blatantly obvious."
    "She was also still hesitating on what kind of present to get Hina, hoping that the two of them would find something along the way, but a handkerchief would have been really good right now."
    H "......"
    A "Hina, you look kind of feverish. Are you okay?"
    H "Ah- yeah. It's nothing. It's just really hot…"
    A "...Are you sure you don't need to rest at home?"

    menu:
        "Stay home":
            jump homestay
        "Go out anyway":
            jump outdoors

label homestay:

    H "Actually, I might have to after all."
    "There goes Airi's plans to acquire Hina's present. She's in a pinch!"
    A "Well, my house is also nearby. Do you want to come over? ♡"
    H "Eh? Is that okay?"
    A "Of course. Once we get there, we can spend the time however we want."
    H "???"
    A "Haha, forget that. Let's just get going."
    
    # Load Airi's room and add more dialogue

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
