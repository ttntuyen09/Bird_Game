from bird import *

new_bird = Bird()

user_input = input("Do you want to play game? yes/no ").strip().lower()

if user_input == "no":
    quit()

elif user_input == "yes":
    while True:
        player_input = input("Your command for the bird: hop/turn/location/exit ")
        match player_input:
            case "hop":
                new_bird.hop()
            case "turn":
                new_bird.turn()
            case "location":
                new_bird.location()
            case "exit":
                break
            case _:
                continue


