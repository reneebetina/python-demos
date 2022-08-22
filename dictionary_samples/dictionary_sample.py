toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}

# Add: Epilogue starts on page 39
toc["Epilogue"] = 39     
# Update: Chapter 3 now starts on page 24
toc["Chapter 3"] = 24
# What are the current contents of the dictionary?
print(toc)               
# Is there a Chapter 5?
print("Chapter 5" in toc)     



#Listing all items in DICTIONARY TYPE
wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for clothing,colorlist in wardrobe.items():
	#print(clothing)
	for color in colorlist:
		print("{} {}".format(color,clothing))
    
#Here is your output:
#red shirt
#blue shirt
#white shirt
#blue jeans
#black jeans
