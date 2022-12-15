# Author: Daniel Kruze
# Document: Python 3.9 (Edited with IDLE)
# Title: High Low Black Belt Lab
# Date: Oct 14 2021

#import mathematical capabilities
import random
#set variables for highest and lowest possible guesses, as well as attempts
hi = 100
lo = 1
attempts = 1

#set a variable that determines when the loop will close
x = True
while x:
#generate a random number inclusively from 1 to 100, print it
    g = (random.randint(lo, hi))
    print(g)
#ask the user for an input that determines the conditions for the next guess
    y = str(input("So what is it? High, low, or correct? Come on big boy. "))
#if the guess is correct, judging by the amount of attempts print the particular message
    if y.lower() == "correct":
        if attempts == 1:
            print("Looks like I got it immediately. Wow, great work. Come up with a better @$%!ing number next time you donut. @$%! me.")
            x = False
        elif attempts != 1:
            print("I got it, finally, after {} @$%!ing attempts. Wow, unbelievable. @$%! off out of here." .format(attempts))
            x = False
#if the guess is too high, make the highest guess smaller and guess again, while incrementing the attempts counter
    elif y.lower() == "high":
        hi = g - 1
        attempts += 1
#if the guess is too low, make the lowest guess bigger and guess again, while incrementing the attempts counter
    elif y.lower() == "low":
        lo = g + 1
        attempts += 1
#If the user doesn't comply with the provided prompts, ask them to do so and guess again
    else:
        print("What was that? You stupid idiot. Give me a real @$%! answer for god's sake. ")


