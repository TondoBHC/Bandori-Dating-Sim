label fd_haneoka: # First day at Haneoka (Kaoru, Tomoe, Hina)
    #KAORU START

    principal "How diligent of you, [user]! We are proud of our students here in Haneoka, I trust you'll excel in all your classes."
    "I sure hope so."

    #scene for hallway
    "The principal told me I would find my tour guide ‘Seta Kaoru’ upstairs in the drama club room, so I guess that’s my next stop."
    "I walk down the hallway to find the staircase. As I climb up each step, I count out loud out of mere curiosity."
    user "One {w}Two{w=1.0} Three {w}Four{w=1.0}"
    user "Five {w}Six{w=1.0} Seven {w}Eight{w=1.0}"
    user "Nine {w}Ten{w=1.0} Eleven {w}Twelve{w=1.0}"
    "Just as I was about to bring my other foot up..."
    #defining karou as unknown (as player does not yet know them)
    #All the girls can be defined as ??? when first defined up top, and later redefined with their proper names as the player gets to know them, to avoid
    #multiple redefinings. -Tondo
    $ k = "???"
    k "Thirteen!"
    "An alluring voice called out. Startled by the voice, I lose my balance and start to stumble backwards."
    user "Crap!"
    with vpunch
    "This is it."
    "I’m going to die by stairs."
    "I close my eyes and brace for the painful impact of the hard floor until something- or rather, someone- grabbed my waist."
    show old_karou_smile
    k "Are you alright, my little kitten?"


    #image will show without and the player can admire it as much as they want until they click to move on
    hide old_karou_smile
    window hide
    show placeholder_karou_cg with fade
    $ renpy.pause ()

    #game continues when player clicks
    window show
    "My eyes open to see a purple haired girl gripping the railing of the staircase to prevent the both of us from falling."
    user "U-um... yeah..."
    "Flustered by the intimate contact, I couldn’t help but blush. It didn’t help that her crimson eyes stared into my own."
    $ k = "Purple haired girl"
    k "I’m relieved. It would be an injustice if a cute little kitten such as yourself were to be harmed."
    "She pulled me up and guided me safely to the top of the staircase."
    hide placeholder_karou_cg

    show old_karou_idle
    "Her voice sounded familiar though{w}...Ah."
    #There was a new paragraph created just for the closing parenthesis, I don't know if that's what you intended but it looked kinda odd, so I removed it.
    #Thank for editing - was supposed to be wait. Changed. (COOKIE)
    "I remember that someone said "Thirteen" which surprised me and made me lose my balance. Her voice was the same voice."
    user "Although I wouldn’t have tripped if you didn’t surprise me by calling out ‘Thirteen’ like that..."
    hide old_karou_idle
    show old_karou_suprised
    k "What?"
    k "I haven’t uttered a word."
    hide old_karou_suprised
    show old_karou_pride2
    k "Perchance I was on my way downstairs that I’ve come across you, my damsel,  in a moment of distress and risked life and limb to save you."
    "Eeehhh?"
    "I did hear rushing footsteps and there’s no one else here. If that’s true..."
    user "If you didn’t say that then who did? There isn’t anyone else here."
    hide old_karou_pride2
    show old_karou_suprised
    "The purple haired girl froze. Her face paled at my words."
    hide old_karou_suprised
    show old_karou_scared
    k "I-it might have been nothing."
    hide old_karou_scared
    show old_karou_idle
    k "Well if you look at the time, I must be going to the principal’s office. I have to pick up what I’ve forgotten for a new student."
    "She forgot something? And it’s something for a new student? {w}Could she be..?"
    user "Are you Seta Kaoru?"
    $ k = "Kaoru"
    k "Why yes, I am."
    hide old_karou_idle
    show old_karou_pride
    k "Now that you know my name, may I have the honor of knowing yours, my little kitten?"
    user "I’m [fullName], the new student. The principal gave me what you left behind and told me to meet you in the drama club room."
    hide old_karou_pride
    show old_karou_pride2
    k "Ah yes, as leader of the host club, it’s my duty as a prince to show a lovely little kitten like you around the school."
    hide old_karou_pride2
    show old_karou_scared
    k "If I may, I believe what I forgot was your schedule."
    "I hand over my schedule and she looks over it."
    hide old_karou_scared
    show old_karou_pride2
    k "Ah I see. How fleeting."
    "She hands my schedule back to me."
    hide old_karou_pride2
    show old_karou_pride
    k "Let us embark now on a journey around the school."
    "We began the tour of the school."
    hide old_karou_pride

    "We stopped by the gym"
    #here we would use scene x with fade. this will be done when all backgrounds are done
    #Which would work better, 4 lines each with it's own scene or 1 line split into 4 paragraphs and a scene for each paragraph with the pause/wait function? -Tondo
    #I think 4 lines (COOKIE)
    "We stopped by the auditorium"
    "We stopped by the classrooms"
    "We stopped by the the drama club"


    #scene should return to hallway after tour
    user "Are there other clubs here at the school?"
    show old_karou_idle
    k "Yes. Off the top of my head, there’s the enthusiastic dance club, the dedicated student council, and the vigorous tennis club."
    "I don’t think I can deal with the busy work the student council is given. The dance club and tennis club seems to be really active given what Kaoru said. And I don’t think I have it in me to act so dramatic or act realistically."
    user "Are there any other clubs?"
    k "Of course, there are other clubs. In fact, I myself am a part of another club."
    "Oh yeah, that’s right."
    user "You mentioned being the leader of the host club. But what is this ‘host club’?"
    hide old_karou_idle
    show old_karou_pride2
    k "The host club is-"
    "Before she could finish, the bell rang."
    hide old_karou_pride2
    show old_karou_smile
    k "I guess this is the end of the tour. It’s best if we head to class."
    hide old_karou_smile
    show old_karou_pride
    k "Adieu, my little kitten."
    hide old_karou_pride
    "She flashed a princely smile before she left. I decide to head to class too but one thing on my mind remains unanswered."
    "What the hell is the host club?"

    jump hostClubIntroHaneoka
    return

#****DAY 2****
label hostClubIntroHaneoka:
#written by cookie
    "Classes are still a drag, and I’m relieved when the bell rings. The hallways are loud and swarming with people, so I just try and blend in."
    "I look around the hallway for those colourful characters from yesterday but they are nowhere in sight."
    "Oh right! I almost forgot that there was a library, so I can camp out there for the rest of break until I meet new people."
    "I trail along to the library and see a colourful poster on the door."
    "For a poster made by high schoolers, it’s surprisingly full of spirit and creativity. It’s so detailed that the drawings remind me of something, but what?"
    "The host club! I clap my hands and rush over to the club room specified on the poster, the jolt in my body resounding in my footsteps. I beam at the clubroom door, and yank it open."
    user "Holy shit."
    "It’s official, Haneoka is made of money if they can support THIS kind of room. It must’ve costed a fortune."
    "My eyes hunt the room for Tomoe and her blazing red hair, but I’m instead met with electric blue hair."
    show hina w1_idle
    "Hina drifts around the room, humming blissfully. It’s almost like she isn’t carrying a heavy box; it’s impressive that she can move so weightlessly. She seem to do everything so effortlessly..."
    "She seems oblivious to my presence, and I begin to wonder if it would be best if I just left. Afterall, I feel like I’ve just rushed into this, I haven’t even planned on what to say."
    "But just as I was about to leave..."
    hide hina w1_idle
    #need suprised hina sprites - more hina expressions
    show hina w2_idle
    h "Wah! Hey, hey! Do we have a guest?"
    "Hina’s box dives to the ground, the items knocked out messily. She stares at me, incredulously, before her eyes twinkle wildly."
    hide hina w2_idle
    show hina w1_idle
    "In a fever, she swings herself over to me, and snatches my hands up, grinning. She dances maniacally around the room, spinning me around, beaming brightly all the way."
    "I slump onto the couch she swivels me onto and catch my breath – does she greet every guest this way? Hina is still breathless, but is bouncing on her like nothing ever happened."
    $ k = "???"
    k "Ah, what’s this? A guest you say?"
    "Hina veers toward the captivating voice. A familiar voice."
    hide hina w1_idle
    show hina w1_idle at right
    #only using this kaoru sprite to show her presence (will change when artist finishes kaoru sprites)
    show old_karou_idle at left
    $ k = "Kaoru"
    "My head shoots up, and my glance meets the tall, suave Kaoru yet again. She slides next to me, brushing herself against me."
    "Strangely, my dizziness seems stronger with Kaoru’s allure than with Hina spiralling me around the room, but I digress."
    user "Actually, I’m not here as a, er..., guest. I’m here to -!"
    "A squirm slips out of my mouth as I feel warm hands enveloping in mine. Shakily, my head slowly shifts to Kaoru, who winks at me as she caresses my hand."
    user "Gak!"
    "I whimper out, as Kaoru boldly sneaks a kiss at my hand. My face must be as red as a tomato. Kaoru laughs at my reaction."
    k "I’m glad you came to the host club, my little kitten."
    #**cg time
    hide old_karou_idle
    hide hina w1_idle
    window hide
    # (CG OF KAORU KISSING MC’S HAND WITH HINA NEXT TO MC)
    show placeholder_karou_cg with fade
    $ renpy.pause ()
    #game continues when player clicks
    window show
    h "Aha! You’re totally boppin’ too, aren’t you, Kaoru?"
    "Hina’s voice thunders in my ears, reminding me of her presence. Her hands bounce onto my thigh, and I yelp yet again, not being used to all this flirting and attention."
    k "I feel it, this boppin’-ness. Ah, how fleeting!"
    "Hina’s hands crush into my thighs further and my whole body becomes impossibly hot."
    h "Hey, are you boppin’ too?"
    user "I, um…yes?"
    hide placeholder_karou_cg
    #**cg time ended
    show hina w2_idle at right
    show old_karou_idle at left
    "Hina’s arms rocket into the air in celebration. Thank god, I had a feeling that I was about to go on fire!"
    h "Woo-hoo! Now, all we need is Tomoe…Huh? She’s not here?"
    k "Tomoe is still working. My, what a hard worker."
    hide hina w2_idle
    hide old_karou_idle
    show tomoe s_idle3
    t "Hey, aren’t we not supposed to be accepting guests right now?"
    "I look up to see Tomoe. When our eyes meet, she bats her eyes before apologetically smiling at me, realising the situation."
    hide tomoe s_idle3
    show tomoe s_idle1
    t "Ah, [user]-san! I didn’t expect you to take up the offer that quickly!"
    hide tomoe s_idle1
    show old_karou_idle at left
    show tomoe s_idle1 at right
    k "Ah, was this little kitten prompted to come here by dear Tomoe?"
    hide tomoe s_idle1
    show tomoe s_idle3 at right
    t "Er, yes and no. Yes, I prompted them to come here because I thought we could use a few extra hands."
    hide old_karou_idle
    show hina w2_mad at left
    h "Jeez, who just wants to lift heavy boxes all the time. I’m sooo bored tidying up! Wah, when can we start the guest thing again?"
    user "Er, can I just say that actually, I’m here to help out."
    hide tomoe s_idle3
    hide hina w2_mad
    show hina w2_idle at left
    show old_karou_idle at right
    "Kaoru and Hina halt, and dart their eyes towards me. Kaoru presses her hand against her throat and chuckles heartily, although Hina’s eyebrows squish together, confounded."
    k "A host, I see…I see…"
    "Kaoru’s smile fades and she rubs her chin, thoughtfully…"
    k "Well, welcome to the club!"
    "Just like that? I smirk to myself, happy that it was easier to get in than I expected."
    hide hina w2_idle
    show hina w1_idle at left
    h "Uh, I don’t have a problem or anything, but why do you want to join?"
    "Hina tilts her head and inquisitively watching at me, grinning eagerly. I fumble, fidgeting with my tie."
    user "Well, I want to make friends!"
    h "Hmm, but why the host club?"
    user "You see, I’ve…I’ve always been kind of a nobody. I never really knew how to make friends, so being a host, to me, is like…a chance to meet new people?"
    "The room falls silent, and I feel everyone staring at me. I cringe and break the silence with a bark of nervous giggles."
    user "Gah, I know it’s weird, but…I want to do this."
    "This pause is killing me, when is anyone going to speak?"
    #**cg time
    hide old_karou_idle
    hide hina w1_idle
    window hide
    #(CG of Tomoe showing her hand to the player)
    show placeholder_karou_cg with fade
    $ renpy.pause ()
    #game continues when player clicks
    window show
    t "Welcome to the host club, [user]-san!"
    user "Eh? Really?"
    k "What tragic yet endearing reasoning, but as they say, ‘catastrophe is the gift of allure.’"
    "I subtly roll my eyes, did anyone really say that?"
    h "Uh-huh, I think I get it now. Man, people are so interesting! It’s so totally zappin’!"
    hide placeholder_karou_cg
    #**cg time ended
    call showAffection
    jump day5
    return
    #NEED HELP WITH: PLACING SPRITES. RIGHT NOW THE PLACEMENT IS PRETTY BAD SO I NEED HELP DO IT EFFECTIVELY. THE IF STATEMENTS MESSED UP AGAIN SO I NEED THOSE FIXED.
    #EVERYTHING ELSE IS FINE(?) I THINK.

    #day 5 start
    #written by cookie
    label day5:
        "When I go to the host club this time, it’s different. I can hear the guests from just outside the door. They're making a lot of noise, but I can tell it’s because of all the fun they’re having. I have to take a deep breath before entering."
        "As expected, the host club is swarming with guests, but more than I expected. Without realising, I have shuffled back towards the door and closed myself in to watch the crowds and crowds of guests."
        "I am absorbed by how well my fellow members are doing."
        "Tomoe is talking with such engagement and heart to her guests. Hina’s gestures are vivid and full of energy with her guests; Kaoru is courteous and confident as always.
        To think, I used to feel good about calling them my fellow members. I never knew that they were this much of a big deal."
        h "Hi hi, [user]!"
        "I jump at Hina’s voice, and she dashes across the room to meet me."
        h "What’s up, what’s up? Isn’t it boppin’ in here!"
        user "I-I guess!"
        h "Mm-hmm! Yo, can you do something for me real quick!"
        user "Uh, sure! Sure! Er, what is it exactly?"
        #there is supposed to be fast text here
        h "So did you know I like astronomy? I need you to clean the lenses of my telescope, it’s on the rooftop! {nw}TheschooldoesntreallycaresoIjustleaveituptherebytheway.Thestarsaretotallyzappin’andmyheartrusheswheneverIseethemsothatiswhyineedmylensescleanedlistencloselythoughtheyneedspecialwipesorthey’llgetmuckysoilefttheminmylockermylockercodeis0320,mybirthdaybutthat’sasecretmybirthdayisn’tthoughitbeboppinifwecouldcelebrateitsomedayathehostclub!{fast}"
        h "I hope you got all that!"
        "Not at all!"
        user "Do you mind running it by me again. Argh, I guess it’s just noisy in here or something…"
        gu "Hina! Hina! I wanna hear about your sister more!"
        h "Guh! I wanna go and talk about sister again! See you, (USER)!"
        user "Wait, Hina, the thing is-!"
        "Crap, she’s already away. Well, the least I can do is try my best."
        "On the bright side, the walk to the rooftop relaxes me from the hectic host club. But now, I only can guess what Hina was trying to say. I can only really use my glasses wipes to clean the lenses, I suppose."
        #(MINIGAME – NO WAY TO WIN. CONCEPT: PLAYER HAS TO WIPE IN CERTAIN MOTIONS BY FOLLOWING A PATTERN WITH THEIR MOUSE. EACH PATTERN COULD BE TOO COMPLICATED)
        "I head back to the host club to see that it still hasn’t calmed down. Tomoe beckons me over."
        t "Hey! I was hoping that you could deal with these guests! I’m sure it’ll be great for you!"
        "She directs me over to a group of girls. I see a friendly smile on her face before she returns to her group. At least that smile gives me the confidence to deal with these guests. I face them with a beam."
        "But I only see they are glaring at me."
        gu1 "Ugh, are we really with the newbie?"
        gu2 "Tchah, I wanted Tomoe. I was getting excited then."
        gu3 "Pff, let’s just go."
        user "Excuse me!"
        "The girls, who were leaving, spin around to look at me, with faces of disgust."
        user "I really think you should give me a chance! I won’t disappoint!"
        gu2 "Gak, so desperate."
        gu1 "I mean, I suppose though?"
        user "Mm-hmm! I’ll find a good seat!"
        "I search the room for a seat. Weirdly enough, I find a tranquil corner by the window. Perfect! However, the guests still looked distain by my presence."
        gu3 "So, ugh, what is it?"
        user "Well, is there anything in particular you all would like to talk about?"
        gu1 "No way. We came here to be charmed, not quizzed."
        user "Oh, well, let me take the lead."
        "I fumble for a conversation topic. I guess this is why Hina, Kaoru and Tomoe have their charm and I don’t. Really, I’m a boring person and they’re so interesting."
        gu2 "Jeez, this is what you get with newbies, not knowing what to say."
        gu1 "You know there is a reason they don’t let in members usually-!"
        user "How about some tea?"
        gu3 "Tea made by Hina sounds good."
        gu1"Alright, go ahead. Impress me, you host!"
        "The guests burst into a rude laughter. I pick up the tea blend left on the table and begin pouring the guests a cup."
        gu1 "Gross, are you using the one left out!"
        gu2 "Those are the worst ones!"
        gu2 "I’ve had enough, let’s just go!"
        user "No, wait!"
        "I rush up to stop them, but instead…"
        gu3 "Argh! Crap! You…You just spilled tea over my uniform!"
        "The guest is so loud that every turns to us. Including Kaoru. Including Hina. Including Tomoe."
        gu1 "Let’s go already!"
        gu2 "Good idea."
        "The guests leave, still glaring at me. It feels like everyone is glaring at me now. It feels like everyone knows that I am not a good host. So, I stay sitting down, defeated.
        Before I know it, the event is over and I’ve only interacted once. I’ve stay seated for most of the time, my head down. My head doesn’t rise when I hear footsteps."
        t "[user], are you okay? Is anything up?"
        k "Hmm, that was…unexpected. Do you have a cold, kitten?"
        "Hina barges into the conversation after running back into the room."
        h "I thought I told you to use the special wipes, [user]. I didn’t think it was that hard!"
        t "Come on, Hina, I’m sure it’s not that bad."
        h "It is! My lenses are really blurry! But I’ll fix them later on!"
        k "Hmm, I guess then…"
        "I look up to see the others looking at each, apprehensive. I know what they are thinking, so I stand up, shoving all the spotlight onto me."
        user "Wait, I need to explain somethings. You see, I know as a host I should be ready to deal with anything, but those guests were really rude to me!"
        "I explain myself to the others. When I’m done, they exchange glances, not knowing how to take in the information. Tomoe closes her eyes, and nods."
        t "Hina, perhaps you were too quick with your instructions. It was busy and I’m sure [user] didn’t mess up your lenses on purpose!"
        h "Yeah, I’m sorry, but I didn’t really see that."
        k "Aha, you see, Hina, every kitten is different and deal with things differently! We can’t be as, uh, 'boppin’' as you!"
        h "Yeah, you’re right. Sorry, [user], but you’re not really like me!"
        t "That’s not much of an apology, but I suppose it will do. [user], I’m sorry I paired you up with such rude guests. I promise I’ll do everything in my power to prevent that happening to you again."
        k "…Oh, Tomoe? Do you not get it?"
        t "Er, get what?"
        "Kaoru crosses her arm, and thoughtfully smirks to herself."
        k "Every kitten is different. And the guests, there are kittens too. Kittens can be kind but others can be mean. But they’re still kittens. And this little kitten should learn to play with other kittens."
        "Kaoru opens her eyes and draws herself closer to me. Damnit, my face is on fire again!" "When will Kaoru ever give me a break?"
        k "Are you free this weekend?"
        user "Um, I do have…er, I guess?"
        k "Perfect, so how about…I teach you about my heart!"
        user "E-Eh?"
        t "Um, Kaoru, don’t do that to [user]!"
        k "Pff, I’m suppose I’m being unfair. [user] should have a choice who they go on a date with!"
        user "A-A date?"
        t "Hold up, none of us have agreed to this. Um, expect…Hina?"
        h "Wow! I’ve never been on a date before! It sounds really…zappin’! I wanna go, I wanna go!"
        k "Haha, don’t get too excited now. It’s only a date for experience, so [user] can appreciate the hearts of all kittens, starting with ourselves."
        t "I mean, if it’s alright with [user], I guess it’s alright. I mean, we’ll just be hanging out…like with our guests?"
        k "It’s only a learning experience, precisely, but it will help [user] understand the mysteries of the heart. So, [user], who do you choose?"
        #**
        menu:
            k "It’s only a learning experience, precisely, but it will help [user] understand the mysteries of the heart. So, [user], who do you choose?"
            "Kaoru":
                #Choice 1: Kaoru
                user "Well, since you suggested it, I think you, Kaoru."
                k "M-Me? Uh, I mean, good choice! Who’s better than me to teach you about the wonders of the heart?"
            "Hina":
                    #Choice 2: Hina
                    user "I choose you, Hina!"
                    h "Yay! I’ve always wanted to go on a date! We could go to the zoo, or the park, or to the amusement park! Wow, so many options! My heart is zappin’ out of my chest!"
            "Tomoe":
                        #Choice 3: Tomoe
                        user "I hope you don’t mind, but I think Tomoe would be…best."
                        t "Er, yeah, I don’t really mind. I hope this is not too embarrassing for you, [user]. If it is, just think of it as hanging out! Yeah! Just two friends hanging out!"
                        #after choices
                        label afterMenu:
                            k "It is decided that the date will meet this Sunday! Fufu, this will truly be an interesting lesson for our little kitten here!"
                            user "I-I suppose it will be."
                            return
