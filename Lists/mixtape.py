# Task: 
# Back in the good ol' days, a mixtape is a compilation of music, a playlist, recorded onto a cassette tape or a CD.
# Create a mixtape.py program and think of a theme for the songs.
# Make a list called playlist and throw in some songs.
# For example:
# # 💿 Theme: Indie Travel Songs

# playlist = [
 # 'Porches - rangerover',
 # 'Mount Eerie - You Swan, Go On',
 # 'Carolyn Polachek - Look at Me Now',
 # 'Pinegrove - Darkness',
 # 'LVP UP - Spirit Was',
 # 'Mitski - First Love / Late Spring'
#]
# Now loop over the list and print everything out! 📻

# Code: 
# 💿 Theme: Indie Travel Songs

playlist = [
  'Porches - rangerover',
  'Mount Eerie - You Swan, Go On',
  'Carolyn Polachek - Look at Me Now',
  'Pinegrove - Darkness',
  'LVP UP - Spirit Was',
  'Mitski - First Love / Late Spring'
]
print(playlist)
for i in range(len(playlist)):
  print(playlist[i])

# Or 

for i in playlist:
  print(i)
