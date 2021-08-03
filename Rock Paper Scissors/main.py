# This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player
from unittest import main


play(player, abbey, 1000)
play(player, kris, 1000)
play(player, mrugesh, 1000)
play(player, quincy, 1000)  # I keep getting different results if these are uncommented. Theoretically, the percentages should match perfectly. Why?

# Okay, figured out why. The learned patterns list doesn't reset for each player, so the program thinks its playing 4000 matches instead of 4 different people. Fixed rps.py so this no longer occurs.

# Uncomment line below to run unit tests automatically
main(module='test_module', exit=False)