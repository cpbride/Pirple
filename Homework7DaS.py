SongStats = {"song" :"Pull Me Under",
"genre" :"Progressive Rock",
"artist" :"Dream Theater",
"album" :"Images & Words",
"composer" :"Petrucci, John",
"year" :"1991",
"length" :"4.6 minutes",
"key" :"a minor"}

print(SongStats)
while True:
    SongGuess = input("what song am I thinking of?\n")
    if SongGuess == "Pull Me Under":
        print("Good guess!")
    else:
        print("Try again")