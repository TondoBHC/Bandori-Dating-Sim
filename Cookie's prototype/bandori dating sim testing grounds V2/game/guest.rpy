# #written by cookie - referred to renpy doc and this: https://lemmasoft.renai.us/forums/viewtopic.php?t=23071
# $ import variables as var
#
#
# 
# screen guestscreen():
#     $guestPerformance = 0 #this variable is used for tracking your progress with the guest you are working with...i swear it will make more sense
#     #later on
#     #choosing the guest
#     $ranGuest = [] #empty list to put guests for random selection inS
#     if False in guests:
#         for i in guests:
#             if not i.visitTimes:
#                 ranGuest.append(i)
#         $chosenGuest = renpy.random.choice(ranGuest)#fetches a random guest that has not yet visited
#         chosenGuest.visitTimes = True#sets their visit variable to true
#     else:
#         for i in guests:
#             i.visitTimes = False#if all the guests have visited, all the visitTimes are reseted back to False
#
#     add "[chosenGuest.image]"
#     #okay going with the assumption that the guest is a linear progress.....
#     #we will have a little message here for the guest saying hello! ill put in the statements after it is decided whether or not we are going to
#     #have guest personality types or not
#     #time to give the gift to the guest!
#     call screen giftscreenGuest
#     for x in chosenGuest.giftPref:
#         if _return == giftPref:
#             guestPerformance+=1 #get points if gift chosen is in guest gift pref
#             break
#     #put call for minigame for making sweets/tea in here when ready! the result of the minigame should be stored in _return variable (going with assumption that
#     #_return is a boolean and true is a a good result for minigame
#     if _return:
#         guestPerformance+=1#get points if do well in minigame
#     #put call for convo here
#     for x in chosenGuest.convoPref:
#         if _return == convoPref:
#             guestPerformance+=1 #get points if chosen convo is in guest convo pref
#             #call for convo advancement(when the guest asks more on the topic - if they like the topic, they wanna talk more!)
#             #new if for the result of the convo. if the player chooses right option, _return is assumed true.
#             if _return:
#                 guestPerformance+=1
#             break
#     #evaluating guest performance
#     hostPerf += guestPerformance
