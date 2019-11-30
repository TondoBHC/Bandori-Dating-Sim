#written by cookie - referred to renpy doc and this: https://lemmasoft.renai.us/forums/viewtopic.php?t=23071
$ import variables as var

#gift screen
screen giftscreen():

    modal True #used so player cant click on anything outside the screen

    frame:
        xpadding 10
        ypadding 10
        xalign 0.5
        yalign 0.5
        xysize(500,557)


        vpgrid:
            #grid define + spacing
            cols 2
            spacing 10

            #scrollbar - wanna move this to the side a bit but couldnt really find out how - will continue to investigate in the future or tondo. (eyes emoji)
            draggable True
            mousewheel True
            scrollbars "vertical"
            side_xalign 0.5

            #for each gift - do this
            for i in gifts:
                    vbox:
                        add "[i.image]" xalign 1.0 yalign 0.0 #image added
                        hbox:
                            textbutton "[i.name]": #name of gift and button to select/buy
                                xysize(100,20)
                                action Confirm("Is this the gift you want? It will cost [i.cost].",Return(i),NullAction()) #for some reason, [i.cost] displays instead of the variable - ?
                            add im.Scale("gui/coin.png",20,20)#rescaling money image so it corresponds to the cost text
                            text "[i.cost]"#cost
                        text "[i.desc]":#desc
                            xysize (300,10)




## example use:
#
# label start:
#
#     call screen giftscreen # calling the screen
#
# #the usual bing-bong that i couldnt be bothered to remove
#     scene bg room
#
#     show eileen happy
#
#     e "You've created a new Ren'Py game."
#
#     e "Once you add a story, pictures, and music, you can release it to the world!"
#
#     $inventory.buy(_return)#when you buy something - not ideal but i'll fix when moving to the code {:
#
#
#     return
