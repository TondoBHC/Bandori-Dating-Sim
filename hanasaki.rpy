label fd_hanasakigawa: # First day at Hanasakigawa (Tae, Arisa, Sayo)
#SAYO START
    principal "Oh [user] , such a deep reason! Surely Hanasakigawa is a school with many loving memories from past generations!"
    "Hopefully I\'ll get to make some loving memories of my own."
    principal "Now then, let me get some paperwork sorted out and you can be on your way."
    user "Is it okay if I explore the school a bit, to familiarize myself with it that is."
    principal "Actually, we have a volunteer student who\'s very excited to show you around the school, hopefully, she could be your first friend."
    principal "Her name is Sayo Hikawa, and she should be arriving here any moment now."
    s "Excuse me, sorry for being late, I was caught up doing some work."
    principal "Oh don\'t worry about that, I was just telling [user]  here about you."
    s "I see, [user]  is it?"
    user "Ah yes, I\'m [fullName]. It\'s a pleasure to meet you."
    principal "Marvelous, I can tell you two are going to be great friends!"
    principal "Now then, [s], why don\'t you take [user]  on a tour of the school while I finish up some work of my own."
    s "Of course, [last_name], after you."
    "We step outside of the teachers lounge and into the empty hallway, presumably because everyone is in class."
    "For a, not-so-brief, moment we stare each other down like lions in a pit."
    user"…"
    s"…"
    s"Did you even bother to look neat for a new school? All your buttons are done up the wrong way."
    user"S-sorry...ma’am?"
    s"Drop the honorific, it’s Hikawa to you. We’ve wasted enough time here, please pay more attention to your appearance in the future."
    "Something about how I’ve already let someone down on my first day here ties my guts in a knot."
    "Hopefully that was nothing to her…?"
    "Our first stop is what looks like their school library."
    s"This is the library. The books range from print to electronic, all books arranged according to the Dewey Decimal…"
    "The poster on the other wall reads 'Literature Club: Making Poetry Lovers Doki Doki Since 2017'."
    "It looks very familiar."
    "My thoughts drown out her voice, and it’s too late when I realise this. Sayo looks as if she’s going to eat me alive."
    "She merely sighs and shakes her head."
    s"Try to pay more attention when other people speak to you."
    "We leave the library."
    "The Hanasakigawa campus is a good bit fancier than what I’m used to. Hanasakigawa has everything I imagined would be in a posh school, like a heated swimming pool."
    if pronoun == sheHer:
        "Otonokizaka didn’t even have a heating system."
    else:
        pass
    user"Hikawa-san, should we go up the staircases to the rooftop?"
    s"T-There’s no reason not to…"
    "So we did."
    "There’s two telescopes too expensive for my civilian hands. I instinctively stuff my hands in the pockets of my uniform."
    s"Astronomy club. Joint club with Haneoka Girls’ High School. "
    "Her spat response came with a withering glance at one of the telescopes."
    user"Huh?"
    "Before I could say anything else she spins aggressively towards the staircase, running far away from the offending telescope."
    "Her long legs far outpace me, but I manage to catch up."
    user"Hikawa-san, are you alright? I’m sorry-"
    s"Who are you to care? You don’t even know me."
    user"I-"
    "What’s with her?"
    "The bell rings, and she leaves without looking back."
    "I trudge to my class, 2A on the second floor. There’s a poster tacked up in the corridor next to a room I’ve never seen."
    "It says Hanasakigawa Host Club. There’s three girls on the poster, two of them dressed as french maids, and --"
    "Sayo?"
    "Poster Sayo’s dressed as a butler, her turquoise hair pulled back into a ponytail. It’s the first time I’ve ever seen her smile, and it’s not unattractive."
    "There’s a clipboard next to the poster with a blank sheet of paper and a stubby pencil."
    "Cheery letters sprawl across the top. ‘Hanasakigawa Host Club :^) Sign up to be a host here!’"
    "Then neat and formal cursive just below it. ‘Meet new people without feeling apprehensive. Free food at times. Duties include entertaining guests and maintaining the club room.’"
    "Then, in small, awkward handwriting, ‘Please be a host. If we don’t have at least 4 members, the school will make us close down.’"
    "Under that was two columns labelled ‘Name’ and ‘Class’."
    user"I’ll eventually have to meet new people and join an extracurricular, right? I’ll check this out I guess."
    "I fill in my details on the clipboard and head to class."
    jump arisa
    return

#ARISA Start
#I think there are other expressions of Arisa that can be used. Not sure on hunch
#Not sure on how to add this within the script
label arisa:
    user "Man... I hope I can get some good food from the cafeteria. At least I hope I have enough money to buy something."
    "I exit the classroom into the hallway. There are a couple of other students out here too but they were travelling to different classrooms to eat with their friends."
    "I take out my wallet to check how much money I have on me when I drop it."
    "I bend down to pick it up when I notice a couple of pieces of paper."
    "Upon closer inspection, they weren’t paper but rather photos."
    "Picking one up, I see it’s a picture of a small tree. It’s really cute! All right, all safe and sound. I pat my pocket to make sure it doesn’t fall."
    "Before I could pick the other pictures up, someone swipes them off from the floor."
    user "Hey! You can’t just take these!"
    "There she was, a light chestnut-haired beauty with a blushing red face."
    #(CG of Arisa blushing and holding the pictures)
    a "What do you mean? These pictures are mine"
    a "If anything, it looks like you were gonna keep them yourself."
    "These photos are hers?"
    "Wait... back up a bit. She thinks I tried to take them. I should clear that up first."
    user "No, I just saw them and wanted to return them."
    user "I wasn’t gonna take them. I swear."
    #(End of CG)
    a "Is that so?"
    a "Then I guess you won’t mind if I count them."
    "Uh-oh. She’ll notice that there’s one missing."
    show old_arisa_angry
    "Before I could even think about pulling the photo out, her glaring eyes had told me it was too late."
    a "Where’s Tamagawa?"
    hide old_arisa_angry
    "Tamagawa? That’s a weird way to ask for the photo."
    user "Is that the name of the photo?"
    show old_arisa_cross
    a "It’s not the name of the photo, it’s the name of my bonsai tree in that photo"
    hide old_arisa_cross
    user "So this tree is named Tamagawa?"
    "I took out the photo and gave it back to her."
    user "Do the other trees have names?"
    "Her face reddened as though she realized she said something embarrassing when I asked her my question."
    a "It’s just the one that has the name. I certainly didn’t name one of my trees Yodogawa."
    "So they do have another names. That reminds me..."
    user "What’s your name?"
    a "Huh? My name? I’m Ichigaya Arisa."
    a "What about you?"
    user "What about me?"
    a "Your name?"
    user "Ah... I’m [fullName]. I’m new here"
    a "Is that so? Well, I have my photos now. I better hurry and spend the rest of the lunch period with my friends."
    user "Ok. I’ll see you around I guess."
    "With a hesitant farewell, she left."
    "She seemed pretty interesting."
    "I wonder if I’ll see her around."
    "Now what was I going to do?"
    "…"
    "Ah! That’s right! I was supposed to buy lunch."
    "Hopefully there’s still to time to get something."
    "And with that, I sprinted towards the cafeteria."
    jump Tae

#TAE START
#tae is said to start after school so put code here. added variable so this is triggered if player is in hanasakigawa (COOKIE)
#ALIGNMENT IS OFF BUT NOT CORRECTED SINCE PLACEHOLDER (COOKIE)
label Tae:
    "I think I should make my way home now."
    "Huh…?"
    "Walking past it I notice a girl in the middle school pet room."
    show tae w_smile
    "Draped over the Hanasakigawa high school uniform is waist-length dark hair."
    "I don’t know many people with waist-length hair in high school, yet on this girl it works like a charm."
    hide tae w_smile
    show tae w_glad
    $ ta = "Dark-haired girl"
    ta "mn… you are so cute..."
    "For some reason I’ve been seized by an urge to take this girl into my arms and protect her from all the evils in the world."
    ta "So cute.. I want to take you home so bad..must..resist..but..."
    "I watch as she sets a rabbit free from its cage, then two --{w}Wait… Is she trying to steal!?"
    "I can’t just leave the rabbits at her mercy and go home!"
    "I rush towards her."
    with hpunch
    user "Stop! Thief!"
    hide tae w_glad
    show tae w_curious
    ta "Huh? I’m not a thief."
    "She looks as if she has more to say, but trails off at the sight of a lop eared rabbit snuffling her hand."
    hide tae w_curious
    show tae w_smile
    "She ignores me altogether and pets the creature."
    user "You know stealing is bad right?"
    hide tae w_smile
    show tae w_serious
    ta "Who doesn’t?"
    "She still goes to get more rabbits out of the cage."
    user "What if the middle school kids knew you were stealing their rabbits? Worse still, the teachers? You could get suspended, you could get expelled, you could-"
    hide tae w_serious
    show tae w_smile
    ta "They know."
    "She cuddles the rabbit, not seeming concerned with my accusations." #adding new monologe for the ** parts (COOKIE)
    user "What? And they are okay with that?"
    #made if statement to try and tidy things up (COOKIE)
    #IF STATEMENT DOES NOT WORK. INTENDED PURPOSE IS THAT WHEN PRONOUNS ARE HEHIM THEN SPECIAL DIALOUGE APPEARS, AND IF NOT THE DIALOUGE IS SKIPPED AND IGNORED WITH THE IF. (COOKIE)
    #The reason it wasn't working is becuase you were using one = instead of 2, when using 1 = then you're assigning a value to a variable (see lines 9-37)
    #when using 2 == you're checking if the variable is has that value (see line 94) -Tondo
    if pronoun == heHim:
        "I guess I transferred to a different planet. Girls’ schools are an ...experience. If I slapped myself this will all be my imagination and whoever this girl is will not be stealing bunny rabbits from 13 year olds."
    else:
        pass
    ta "Yeah, You can feed them too, you know?"
    user "That’s why i sai- huh? What?"
    "She fumbles around in her pocket to reveal carrot sticks."
    hide tae w_smile
    show tae w_serious
    ta "Now hold him for me."
    "The lop eared rabbit in my lap is brown. Fluffy. Surprisingly warm, and a good bit heavier than I imagined."
    user "Eh? So you are not going to steal them?"
    "It sniffs the air and snuggles close to me as if in response."
    hide tae w_serious
    show tae w_curious
    ta "Why would i do that? How could I do such a cruel thing to them?"
    "So she isn’t stealing them…?"
    "She wanted to take them home. I saw her open the cages with my own two eyes. I saw her taking them from the cages. She has carrot sticks with her. There’s only one reason she could be doing th-"
    "How has it never occured to me that she didn’t actually mean to take the rabbits home?{p}...Fuck me. "
    "It’s an age-old habit of mine, jumping to conclusions and embarrassing myself."
    "Maybe I should’ve listened to my thirteen-year-old self and gone through with my plans to disappear into some uncharted cave and die."
    hide tae w_curious
    show tae w_serious
    ta "There, there. Eat up, Fluffycheeks!"
    user "...Fluffycheeks?"
    "I watch in a trance as Fluffycheeks eats up."
    "I wish I was anywhere but right in front of this girl."
    hide tae w_serious
    show tae w_smile
    ta "Good boy."
    "I gingerly reach out a hesitant finger to pet Fluffycheeks on its head."
    with fade
    "Long minutes tick by, and eventually she returns all the rabbits to their hutch with a kiss on their foreheads."
    hide tae w_smile
    show tae w_glad
    ta "Good boy."
    "She puts the last rabbit in its cage and closes it."
    hide tae w_glad
    show tae w_smile
    ta "Thank you for helping me feed them."
    user "Eh? Ah... You’re welcome."
    hide tae w_smile
    show tae w_thinking
    ta "Hmm.. By the way..."
    "Is she going to make fun of me for what happened?"
    hide tae w_thinking
    show tae w_smile
    $ ta = "Tae"
    ta "My name is Hanazono Tae."
    ta "Hope we meet again."
    hide tae w_smile
    user "Ah...yes..."
    "I come to my senses, but Hanazono Tae has disappeared without a trace."
    jump hostClubIntroHanasaki
    return

#Day 2
label hostClubIntroHanasaki:
    "Classes are still a drag, and I can’t help but slam my head onto the table when the teacher leaves. Realising that I’m being too dramatic, my head shoots up, and I smile, trying to make myself look better. Like I didn’t just bang my head against my desk."
    "I look around the classroom for those colourful characters from yesterday but they are nowhere in sight. Instead, my eyes are met with a poster. Wait a moment, are those girls in the dresses Arisa and Tae?"
    "Arisa’s lips are tugged into a polite smile, and she is looking over to Tae, who is serving a cup of tea, beaming at nothing in what seems like a daydream. Sayo, like before, reflects great authority. The girls are surrounded by roses and in the midst of these roses, is the title."
    "The host club."
    ga "Gah, it’s a shame the host club is closed up this week."
    gb "Yeah, I really wanted to see Tae again. She’s always so cool."
    "Like clockwork, two girls behind me begin talking about the host club. I perk up with curiosity."
    ga "Not just Tae, they’re all really charming."
    gb "Yeah, even Arisa’s become really popular!"
    "I glance at the poster again, and think on the girls’ words. Does being a hostess…make you popular around here? I turn back on the classroom to be faced with unfamiliar faces, all in their own friend groups. And me, alone."
    "A light bulb goes off in my head and I rush towards the host club. I beam at the clubroom door, and yank it open."
    "Arisa and Tae are at the doorway, and they are arguing over something. I slink behind the door, not wanting to get involved."
    a "Are you stupid? You can’t bring your rabbits into the host club?"
    ta "I don’t see why not. They’ll be a cute addition to the host club."
    a "But they’ll make a mess! And what about allergies, have you thought about that?"
    ta "No one is allergic to rabbits."
    s "Hey, you know we’re closed. We did put up a sign, didn’t we?"
    "Sayo intensely stares straight at me, attracting Tae’s and Arisa’s attention to me too. I fumble into the clubroom, and clear my throat. Sayo looks more annoyed."
    s "Why are you coming in, we’re closed. We’ll be open again this Friday so there’s no reason for you to be here."
    user "Actually…I wanted to help."
    s "Trust me, we have enough help here. Don’t we?"
    "Sayo launches her laser eyes towards Arisa and Tae. Tae remains unchanged, but Arisa visibly shakes. She laughs it off, but her laughter is a bit too high to be genuine."
    a "Y-Yes, we’re fine. We appreciate your help though, now, too-da-loo!"
    user "No, no! I mean…I want to be a host too?"
    "They all go silent. Sayo closes her eyes and beckons me over to a sofa. She sits down, and folds her leg over her knee, her hands over her legs. I go to sit next to her, but she halts me with a raised hand. "
    "When she opens her eyes, she looks furious."
    #**cg time
    #hide sprites
    hide old_karou_idle
    hide hina w1_idle
    window hide
    #(CG OF SAYO DOING WHAT IS DESCRIBED ABOVE)
    show placeholder_karou_cg with fade
    $ renpy.pause ()
    #game continues when player clicks
    window show
    s "We don’t accept new hosts, it isn’t something you just walk into it. This is a privilege, do you understand?"
    "Sayo’s tone is as cold as her icy eyes, and she practically spits out frost."
    s "To think, that after your presentation yesterday, that you have the cheek to barge in here, demanding to be a host. This isn’t a game, you know!"
    user "I know this isn’t a game!"
    #cg time end
    hide placeholder_karou_cg
    "I have to stand my ground. I hold my chin high and clutch my fists together. Sayo looks at me expectantly; she does not falter."
    user "I…I want to be as popular as you! I came here with no other reason to find my place, and if the host club can make me popular, then I can finally make friends! I’ve…I’ve been alone my entire life, and I’m not going to go by this opportunity!"
    unk "Then I see no problem."
    "I spin around to see Tae, who is still smiling in her absent-minded way. However, her face is gentle."
    ta "It’s been the three of us for a long time, I think a new student would mix things up. We don’t want our guests getting bored, no? What do you think, Arisa?"
    "Tae nudges Arisa, who is red with either anger or embarrassment – I can’t really tell. She huffs to the side. Tae beams at her reaction."
    #**cg time
    #hide sprites
    hide old_karou_idle
    hide hina w1_idle
    window hide
    #(CG of Tae and Arisa)
    show placeholder_karou_cg with fade
    $ renpy.pause ()
    #game continues when player clicks
    window show
    a "W-Well, I mean…your story was too mopey! You didn’t need to give us your life story! But…yeah. I think Tae may, er, be making a…good…point."
    ta "See, Arisa thinks so too. She may not admit it, but she really agrees with me."
    a "N-No I’m not! Really, I’m on the verge of disagreeing now!"
    #cg time end
    hide placeholder_karou_cg
    "Tae narrows her eyes towards Sayo, who tries to maintain her hostility."
    ta "Now, Sayo, I understand your disagreement, but it’s two against one here. And I am the leader."
    "Sayo looks shaken up, bewildered. She pauses, like a deer in headlights. Eventually, she sighs, defeated."
    s "Fine, but only because it’s my responsibility as disciplinary committee member to make sure no student is isolated. And, I believe in democracy, so if you two want it that way…"
    "Sayo glares at me, severely, momentarily, before turning her attention back on Tae and Arisa."
    s "…I guess it will be that way. Welcome to the host club, [user] ."
    ta "Okay, say it too Arisa."
    a "Eh? Jeez, fine, welcome to the host club, [user] ."
    ta "’Kay, my go. Welcome to the host club, [user] . I’m glad to have you with us."
    call showAffection
    jump day5hansaki
    return

#day 5 - written by cookie
label day5hansaki:
    "When I go to the host club this time, it’s different. I can hear the guests from just outside the door. They making a lot of noise, but I can tell it’s because of all the fun they’re having. I have to take a deep breath before entering."
    "As expected, the host club is swarming with guests, but more than I expected. Without realising, I have shuffled back towards the door and closed myself in to watch the crowds and crowds of guests."
    "I am absorbed by how well my fellow members are doing."
    "Tae is chitchatting with the guests, although she looks like she is still in a daydream. I assume she must be talking about something silly, as Arisa has that cynical charm in her face when she is looking at Tae. Sayo’s expertise is shining through, and the crowd of guests surrounding her bring out her elegance."
    "To think, I used to feel good about calling them my fellow members. I never knew that they were this much of a big deal."
    ta "Hey, [user]!"
    "I jump at Tae’s voice, and she dashes across the room to meet me."
    ta "You okay?"
    user "Y-Yeah, great!"
    ta "…Oh, okay! Look, I can you do me another favour?"
    user "Uh, sure! Sure! It’s, er, to do with your rabbits."
    #fast text occurs here - supposed to be unreadable for user. need help to do this.
    ta "Yeah, you see, Oddie has been a really good this week so I wanted to treat him to a big meal! So, I want you to {nw}feedhimcarrotslettucecorianderbasilpizzayogurtdropsohandsomebrocoliifthereisanyandmaybesomecelerythat’sgoodtheylikeceleryyouknowchocolatemaysoundgoodbutrabbitsdon’tlikethatsoisupposenothuh.{fast}"
    ta "Did you get that?"
    "Not at all!"
    user "Do you mind running it by me again. Argh, I guess it’s just noisy in here or something…"
    gu "O-Tae! You didn’t finish your story about Oddie! I want you tell my friend, please?"
    ta "I’m afraid I can’t. I trust that you can do it though!"
    user "Wait, Tae, the thing is-!"
    "Crap, she’s already away. Well, the least I can do is try my best."
    "On the bright side, the walk to the rabbit pet room relaxes me from the hectic host club. But now, I only can guess what Tae was trying to say."
    #(MINIGAME – NO WAY TO WIN. CONCEPT: PLAYER GETS FOOD OPTIONS TO FEED RABBIT AND DRAGS IT INTO PEN)
    "I head back to the host club to see that it still hasn’t calmed down. Sayo beckons me over."
    s "Deal with these guests, please."
    "She directs me over to a group of girls. I see a faint smile on her face before she returns to her group. At least that smile gives me the confidence to deal with these guests. I face them with a beam."
    "But I only see they are glaring at me."
    gu1 "Ugh, are we really with the newbie?"
    gu2 "Tchah, I wanted Sayo. I was getting excited then."
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
    "I fumble for a conversation topic. I guess this is why Arisa, Tae and Sayo have their charm and I don’t. Really, I’m a boring person and they’re so interesting."
    gu2 "Jeez, this is what you get with newbies, not knowing what to say."
    gu1 "You know there is a reason they don’t let in members usually-!"
    user "How about some tea?"
    gu3 "Tea made by Arisa sounds good."
    gu1 "Alright, go ahead. Impress me, you host!"
    "The guests burst into a rude laughter. I pick up the tea blend left on the table and begin pouring the guests a cup."
    gu1 "Gross, are you using the one left out?"
    gu2 "Those are the worst ones!"
    gu1 "I’ve had enough, let’s just go!"
    user "No, wait!"
    "I rush up to hold up my hand, but instead…"
    gu3 "Argh! Crap! You…You just spilled tea over my uniform!"
    "The guest is so loud that every turns to us. Including Tae. Including Arisa. Including Sayo."
    gu1 "Let’s go already!"
    gu2 "Good idea."
    "The guests leave, still glaring at me. It feels like everyone is glaring at me now. It feels like everyone knows that I am not a good host. So, I stay sitting down, defeated."
    "Before I know it, the event is over and I’ve only interacted once. I’ve stay seated for most of the time, my head down. My head doesn’t rise when I hear footsteps."
    a "What the hell was that? You know how much of an idiot you looked?"
    s "I agree with Arisa. Your performance was humiliating!"
    a "Didn’t you say you were serious about this? Didn’t you say-!"
    ta "[user], you didn’t give Oddie the right treats. Hmm, what a shame."
    s "So, not only can’t you talk with guests, but you can’t follow Tae’s orders. You know we’re all above you, and therefore…"
    "Sayo’s angry rambling pauses. I look up, to see that Tae, Arisa, and Sayo are looking gloomy and miserable – all their anger has disappeared."
    s "…I think we have the right to remove you as a host."
    a "W-We can’t afford that embarrassment again, er, you know?"
    ta "…What a shame."
    user "Wait a moment! I need to explain some things."
    "I stand up, shoving all the spotlight onto me."
    user "You see, I know as a host I should be ready to deal with anything, but those guests were really rude to me!"
    "I explain myself to the others. When I’m done, they exchange glances, not knowing how to take in the information. Tae closes her eyes, and nods."
    ta "I guess it was unfair to throw that chore on you without much information."
    s "I should mention that I saw [user] rush out of the room too. I can’t really get how someone so earnest would mess up a chore on purpose. Your efforts were clear, [user]."
    a "Although, uh, you really REALLY should be ready for those guests…I suppose it was unlucky bad guests happened to you first time though."
    "Tae, who has actually been uncharacteristically frowning this entire time, suddenly smiles."
    ta "I think you need more experience."
    user "More experience? I’m sorry but I thought I’ve already been trained?"
    ta "You see though, maybe you should get a deeper understanding of the hearts of the guests. Starting with our hearts."
    a "Our hearts?"
    s "Tae, this isn’t the time to be messing around."
    ta "Messing around? Nah, I wouldn’t do that. I’m saying though that perhaps this weekend one of us should go on a date with [user]."
    user "A date?"
    a "Nuh-huh! No way! T-That’s too embarrassing!"
    s "I-It’s shameful!"
    t "Well, [user] would get to know our hearts better. If we let them train with our hearts, then they’ll understand the guests’ hearts! Afterall, you two are pretty much like difficult guests!"
    a "I am NOT difficult! You’re the one being difficult with this idiot idea!"
    s "…I-I suppose though that Tae is making sense here."
    ta "So, it’s two against one! Okay, [user], which one of us would you like to date?"
    a "HUH?! What about my say? Hello?"
    menu:
        "Tae":
            user "Well, I guess, you then, Tae."
            ta "Mmm, me? I wouldn’t consider myself that difficult but I suppose you want to go for easy level first…I don’t blame you, Arisa and Sayo are toughies!"
            a "Hey! You’ve insulted me enough today!"
            jump afterMenu1
        "Arisa":
            user "Um, Arisa?"
            a "E-Ehh? What do you mean, you...!"
            ta "Arisa, what did I say? It’s not really a real date, it’s an experience date!"
            a "…Still my first date…"
            ta "Huh? What was that?"
            a "NOTHING! I was just saying that I’ll have to do it then!"
            jump afterMenu1
        "Sayo":
            user "I’ll go with…Sayo."
            s "O-Oh, sure. But like Tae said, this isn’t a real date."
            ta "Yeah, it’s an experience date!"
            s "…Right, yes, just an experience date if you will."
            jump afterMenu1

    label afterMenu1:
        ta "Then it’s decided! I hope you’re free this weekend!"
        user "Y-Yeah, I am."
        ta "So the date will be this Sunday!"
        user "Uh, yes."
        ta "Great! I hope this works!"
    return
return
