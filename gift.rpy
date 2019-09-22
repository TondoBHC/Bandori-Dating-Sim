label fd_gift:
    "Starting"
    Call screen gift
    #tried to implement an if statement where if you clicked on a gift you would get a confirmation menu - doesnt work for some reason - needs fix 
    If _return == True:
	menu:
	    "Is this the gift you want?"
	    "Yes":
		     "Okay dokey"
		"No":
			Call screen gift
