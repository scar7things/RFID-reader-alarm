#!/usr/bin/env python3
import RPi.GPIO as GPIO
import RFID
import pygame
import pandas as pd
# Initialize the RFID reader
reader = RFID.RFIDReader()
# Create a DataFrame with id numbers from 1 to 100
df = pd.DataFrame({
  "id": range(1, 100)
})
# Create a function to alert when an RFID tag is read
def alert():
    print("RFID tag readed!  alarm on")
    pygame.mixer.music.load("alert.wav")
    pygame.mixer.music.play()
# Set up the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
# Start the main loop
while True:
    # Read the RFID tag's ID number
    id_number = reader.read_id()

 # Check if the ID number is in the DataFrame
    if id_number in df["id"].values:
        alert()
