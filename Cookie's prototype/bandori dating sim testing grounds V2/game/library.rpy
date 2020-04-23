$ import variables as var

label library():
    "At the library, you can either study for school or a convo topic."
    menu:
        "Study for school.":
            "You studied for school."
            "Your study points are now up by 1!"
            $ studyPoints += 1
            "Your study points are now [studyPoints]!"
        "Study a conversation topic.":
                call screen convo
                $topicChosen = _return
                $ topicChosen.level += 1
                "I learned more about [topicChosen.topic]!"
                "My knowledge levelled up by 1!"
                "My knowledge on the topic is now [topicChosen.level]!"
    jump endDay
    return
