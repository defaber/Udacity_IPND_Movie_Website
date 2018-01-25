# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# import two python files
import media
import fresh_tomatoes

# Define the dark knight instance - added launch date
the_dark_knight = media.Movie('The Dark Knight',
                            'An epic battle between batman and the joker.',
                            'July 18, 2008',
                            'https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg',
                            'https://www.youtube.com/watch?v=EXeTwQWrcwY'
                            )
# Define the Ace instance - added launch date
ace_ventura_pet_detective = media.Movie('Ace Ventura: Pet Detective',
                                        'A pet detective that is deteremine to find a killer and a dolphin snatcher.',
                                        'February 4, 1994',
                                        'https://upload.wikimedia.org/wikipedia/en/8/84/Ace_ventura_pet_detective.jpg',
                                        'https://www.youtube.com/watch?v=QzxDlS6QY1s'
                                        )
# Define the Eeemy of the State instance - added launch date
enemy_of_the_state = media.Movie('Enemy of the State',
                            'A story of a lawyer thats at the wrong place at the wrong time.',
                            'November 20, 1998',
                            'http://www.deltastate.edu/images/DSU_Events/enemy_of_the_state.jpg',
                            'https://www.youtube.com/watch?v=AoNT6u3mQew'
                            )

# List movies
movies = [the_dark_knight, ace_ventura_pet_detective, enemy_of_the_state]

# Call Fresh Tomatoes open movies page function
fresh_tomatoes.open_movies_page(movies)
