import time

print("welcome to the amazing world of life, who are you?")
name = input("i am..")
print("hello", name, "before we continue this is a rated r game continue with caution")
print("please respond with yes if you wish to continue anything else will be considered no")
response = input("")

if response == "yes":
    print("well without furtherado here we go!")
else:
    print("good choice")
    exit()

time.sleep(5)

print("your name is", name, "you live in a fantasy town where your neighbor has something.. wrong with him..")
time.sleep(5)

print("one day you are walking your dog and you notice your neighbors house is awfully quiet")
decision1 = input("""what do you do?
                     1, you knock on his door to check on him
                     2, you keep walking because its not your buisness

                     """)

if decision1 == "1":
    print("""as you knock you catch something out of the corner of your eye..
             something dark when you look its gone then suddenly a big green figure
             aka your neighbor opens the door he seems like hes in a really good mood
             which is unusual you quickly say "oh hello mr robbinson i saw it seemed
             pretty darn diddly dark! are you ok neigboroony?" mr robbinson replies with his
             deep heavy voice "yeah of course im ok! we are all ok.. and soon we will all always be ok.."
             you of course get creeped out by that so you walk away but you cant shake the feeling""")
elif decision1 == "2":
    print("you say to yourself i AM not going to die because i got a bit to curious CONGRATS you got the smart ending!")
    exit()
else: print("Error")

time.sleep(30)
print("as you start to turn around you see the door swing back open and you feel something go into your neck.. everything goes dark..")
time.sleep(5)
print("w-what.. (your fading in and out of conciousness) i.. i cant feel anything..")
time.sleep(6)
print("as you fade in and out of conciousness you see something.. something undescrribable standing in the corner")
time.sleep(6)
print("the last thing you see is a tall pale figure standing in the corner staring at you like your food")
time.sleep(10)
print("...")
time.sleep(5)
print("Subject 002 please wake-up i repeat Subject 002 please wake-up")
time.sleep(5)
print("thank you for playing part 1 of THE IT more is to come")