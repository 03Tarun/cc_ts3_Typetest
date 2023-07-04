#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time

def calculate_typing_speed(total_characters, total_time):
    # Calculate typing speed in words per minute (WPM)
    words_typed = total_characters / 5  # Assuming an average word length of 5 characters
    minutes = total_time / 60
    speed = words_typed / minutes
    return speed

def run_typing_test(sentence):
    print("Welcome to the Speed Typing Test!")
    print(f"Type the following sentence: '{sentence}'")
    starttime = time.time()  # Record the start time
    typedtext = input("Your sentence: ")  # Prompt the user to type the sentence
    endtime = time.time()  # Record the end time
    
    totaltime = endtime - starttime  # Calculate the total time taken
    totalcharacters = len(typedtext)  # Count the total characters typed
    typingspeed = calculate_typing_speed(totalcharacters, totaltime)  # Calculate the typing speed
    
    # Display the results
    print(f"\nTotal time taken: {totaltime:.2f} seconds")
    print(f"Total characters typed: {totalcharacters}")
    print(f"Typing speed: {typingspeed:.2f} words per minute")

custom_sentence = input("Enter a sentence for the typing test: ")
run_typing_test(custom_sentence)  # Run the typing test with the custom sentence


# In[ ]:




