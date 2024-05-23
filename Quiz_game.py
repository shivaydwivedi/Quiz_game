# Prompting the User
print("Welcome to our Quiz!!")

# Permission from the user
playing = input("wanna  play the game: ").strip().lower()

# Logic
if playing != "yes":
    quit()

print("OK,  Let's play!!")

# maintaing score
score = 0

answer = input("full form of UN: ").strip().lower()
if answer == "united nations":
    print("Correct")
    score += 1
else : print("Incorrect")


answer = input("full form of CPU: ").strip().lower()
if answer == "central processing unit":
    print("Correct")
    score += 1

else : print("Incorrect")

answer = input("full form of RAM: ").strip().lower()
if answer == "random acces memory":
    print("Correct")
    score += 1

else : print("Incorrect")

answer = input("full form of ROM: ").strip().lower()
if answer == "read only memory":
    print("Correct")
    score += 1

else : print("Incorrect")

# displaying Result
print("Your final score is", score )