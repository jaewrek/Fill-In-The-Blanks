# IPND Stage 2 Final Project
# Jerrik Neri
# Intro to Programming ND
# Udacity



# Strings for different quiz levels
easy = """Heroes of the Storm is a game made by __1__ Entertainment. __1__ Entertainment is owned by their parent company __2__. Heroes of the Storm, 
or HotS for short, is a __3__ type game, like DOTA2 and League of Legends. __3__s actually started in WC3 as user made map mods, that eventually gained 
popularity and became their own game. __1__ Entertainment makes various other games like the Starcraft series, the (for now) Diablo trilogy, and their most 
well-known game __4__, the most successful MMORPG of all time. """

medium = """World of Warcraft, or WoW for short, is Blizzard Entertainment's most popular and successful game. The two main factions that are 
constantly at war are the __1__, consisting of the Humans, Night Elves, Dranei, Gnomes, Worgen, and Dwarves, and the __2__, made up of the
war-driven Orcs, displaced Trolls, nature-seeking Tauren, magic-enriched Blood Elves, and money-hungry Goblins. There is also a newly added 
netural race known as the __3__. Fun fact, the __3__ were actually subtetly joked at in WC3 in an April Fool's video and gained enough popularity
to become reality! This game released in 2004 and at it's peak had over 12 million players. The game itself takes place in the world of __4__ a few 
years after thelore of WarCraft 3 The Frozen Throne. Throughout the years, Blizzard Entertainment has added several expansions, including more levels, zones, and 
even other planets!"""

hard = """Blizzard Entertainment has not released a new IP for almost over a decade. They have continued on with their Starcraft, Diablo, and Warcraft series. 
They have just recently stepped foot into the FPS scene with their latest and extremely successful game, __1__. __1__ is set in a futuristic world where
Humans and robots known as Omnics, were once at war. A team of heroes named __1__ was created to help win the war against the Omnics, and eventually
find peace for the world. One of the most well known heroes from this game is __2__, with her ability to bend time at her will, flashing forward, slowing 
it down, or recalling back in time altogether. This game was released in 2016 and in just 2 weeks, gained over 10 million players and generated over 280
million dollars of revenue. It quickly knocked out League of Legends as the most played game in __3__, a country well known for dominating the competitive
electronic gaming market. 
        
__1__ in some ways is the redemption game for Blizzard Entertainment. It is not well-known that for almost a decade they were working on another IP called
__4__ that never came to fruition. In fact, __2__'s abilities are taken from one of the characters meant to be in __4__. In the height of success from WoW,
they believed they could create another very successful MOBA, the never released __4__. It is both fortunate and unfortunate that they were able to fail
and yet persever through and create another wildly successful game like __1__!"""

answer_key = ["__1__", "__2__", "__3__", "__4__"]

easy_answers = ["Blizzard", "Activision", "MOBA", "World of Warcraft"]
medium_answers = ["Alliance", "Horde", "Pandaren", "Azeroth" ]
hard_answers = ["Overwatch", "Tracer", "South Korea", "Titan"]




"""def correct_answer takes in which string difficulty to use as string difficulty, the list of answers, and what index quiz currently is in
loops through every word changing blanks to correct answer and returning string """
def correct_answer(stringdifficulty, answers_list, index):
    splitquiz = stringdifficulty.split()
    replaced = []

    # for every word in splitquiz check if answer key index, ex. __1__ is in that word
    # if it is equal, replace with answer of corresponding index
    for word in splitquiz:
        if answer_key[index] in word:
            word = word.replace(answer_key[index], answers_list[index])
            replaced.append(word)
        else:
            replaced.append(word)
        

    replaced = " ".join(replaced)
    return replaced

def show_intro_message():
    print "\nSo you think you're a " + game_difficulty +"?!?! EH?!\n"
    print "You get 5 lives ADVENTURER, I hope you know your games!\n"

# Runs the game taking in the string and answer set as parameters
# Prints out to user to interact with them
# Answer Key index to ensure the blanks and answer set are coordinated
def play_game(quizstring, answers):
    lives, answer_key_index = 5, 0  
    show_intro_message()
    while lives > 0:
        print quizstring + "\n"
        guess = raw_input("ADVENTURER, what is the answer for "+answer_key[answer_key_index]+"?  \n")
        if guess == answers[answer_key_index]:
            print "\nGRATZ ADVENTURER! That's the correct answer. You advance! DING!\n"
            lives = 5
            quizstring = correct_answer(quizstring, answers, answer_key_index)
            answer_key_index+=1
        else:
            lives-=1
            print "\nIncorrect ADVENTURER, try again! You have "+str(lives)+" lives remaining! Tread carefully!"
            if lives == 0:
                print "\nGAME OVER ADVENTURER!!! You've run out of lives.\n"      
        if answer_key_index == len(answer_key):
            print quizstring + "\n\nCONGRATULATONS ADVENTURER. GG YOU'VE WON!\n"
            break

print "\nHELLO, welcome to my game about GAMES!\n"
game_difficulty = "unselected"
#Loop through until difficulty level typed appropriately
while game_difficulty == "unselected":
    game_difficulty = raw_input("What kind of adventurer are you?! Please enter below: (NOVICE, INTERMEDIATE, VETERAN) \n").lower()
    if game_difficulty == "novice":
        play_game(easy, easy_answers)
        break
    if game_difficulty == "intermediate":
        play_game(medium, medium_answers)
        break
    if game_difficulty == "veteran":
        play_game(hard, hard_answers)
        break
    else:
        print "\nAdventurer! Please provide correct difficulty level!\n"
        game_difficulty = "unselected"


