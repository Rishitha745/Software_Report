import os
import random
import pygame
import time
from mutagen.mp3 import MP3
import sys
import select


while True:
    directory = './Songs'
    mp3_files = [file for file in os.listdir(directory) if file.endswith('.mp3')]
    mp3_files_with_numbers = [(random.randint(1, 100), file) for file in mp3_files]
    mp3_files_with_numbers.sort(key=lambda x: x[0])
    playlist = [file for _, file in mp3_files_with_numbers]

    pygame.mixer.init()
    print("Press")
    print("next  :To play the next song")
    print("Enter :To pause the song")
    print("quit  :To quit the program")
    for file in playlist:
        file_path = os.path.join(directory, file)
        pygame.mixer.music.load(file_path)
        # Get the audio file length
        audio = MP3(file_path)
        audio_length = audio.info.length
        timeout = audio_length
        pygame.mixer.music.play()

        start_time = time.time()
        user_input = None
        current_pos=0

        while pygame.mixer.music.get_busy():        
                if sys.stdin in select.select([sys.stdin], [], [], timeout-current_pos)[0]:
                    user_input = input(" ")
                    if user_input == "next":
                        print("Playing the next song")
                        break
                    elif user_input =='':
                        pygame.mixer.music.pause()
                        current_pos = pygame.mixer.music.get_pos() // 1000 
                        print("Press Enter to resume")
                        user_input2 = input(" ")
                        if user_input2=='':
                            pygame.mixer.music.unpause()
                    elif user_input == "quit":
                        print("You are exiting the playlist")
                        exit(0)  
                else:
                    print("Playing the next song")
                    break

                time.sleep(0.1)
        
