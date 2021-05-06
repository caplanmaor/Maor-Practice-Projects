#Create dictionary
name_for_id = {
	265: "Maor",
	452: "Agam",
	134: "Haim",
}

#Print name function
def greeting(userid):
	print("Hi %s !" % name_for_id.get(userid, "there"))

#This is a bug, implement a default statement if the number is not in the dictionary
greeting(266)