## Guess a Word
# Drawing inspiration from the spelling bee contest, you need to create a Python-based computer game prototype which allows a player to guess the correct word through observing the jumbled letters of a word.
import random
import time
leaderboard = []
my_words = (("questionnaire", "noun", "a list of questions survey"),
            ("unconscious", "adjective", "not conscious or without awareness"),
            ("precocious", "adjective", "usually mature, especially in mental development"),
            ("liaison", "noun", "a person who maintains a connection between people or groups"),
            ("surveillance", "noun", "continuous observation of a person, place, or activity in order to gather information"),
            ("malfeasance", "noun", "conduct by a public official that violates the publi trust or is against the law"),
            ("irascible", "adjective", "irritable, quick-tempered"),
            ("idiosyncrasy", "noun", "a tendency, habit, or mannerism that is peculiar to an individual; a quirk"),
            ("foudroyant", "adjective", "sudden and overwhelming or stunning"),
            ("eudemonic", "adjective", "pertaining to or conductive to happiness"))
records={"name":"", "guess count":0, "time taken":0}
print(my_words, records)
# Jumbles the letters of a word
def shuffler(word):
  word = list(word)
  random.shuffle(word)
  word= "".join(word)
  return word

# Gameplay
def gameplay():
  print("GUESS A WORD GAME".rjust(12,"-"))
  name=input("Enter Name: ")
  guesses=0
  tt=time.time()
  score=0
  print("To stop the game, enter s")
  for i in range(0,4):
    index = random.randint(0,9)
    real_word=my_words[index][0].upper()
    wordy=shuffler(real_word)
    pos=my_words[index][1].upper()
    means=my_words[index][2].upper()
    toplay=f"""Jumbled Letters: {wordy}
    Part of speech: {pos}
    Meaning: {means}"""
    print(toplay)
    guess = input("Guess the word:")
    if (guess.lower()==real_word.lower()):
      print("CORRECT!")
      guesses+=1
    else:
      print("""WRONG!
      Correct word is""",real_word)
  tt=time.time()-tt
  if tt>60:
    print("You took "+str(tt//60)+" minute(s) and "+str(tt%60)+" seconds to guess "+str(guesses)+" words correctly.")
  else:
    print("You took "+str(tt)+" seconds to guess "+str(guesses)+" words correctly.")
  my_score = f"""Name: {name}
Guess Count: {guesses}
Time Taken: {tt}"""
  leaderboard.append(my_score)
  for i in leaderboard:
    print(i+"\n")

gameplay()