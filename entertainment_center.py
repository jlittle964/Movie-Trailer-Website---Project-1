import fresh_tomatoes
import media

lion_king = media.Movie("The Lion King",
                        "A story about a lion excepting his place as king",
                        "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg", # noqa
                        "https://www.youtube.com/watch?v=4sj1MT05lAA")
star_wars_the_force_awakens = media.Movie("Star Wars: The Force Awakens",
                                          "Follow Ray as she doscevers powers",
                                          "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg", # noqa
                                          "https://www.youtube.com/watch?v=sGbxmsDFVnE") # noqa
intersteller = media.Movie("Intersteller",
                           "A pilot goes in search of liveable planet",
                           "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg", # noqa
                           "https://www.youtube.com/watch?v=0vxOhd4qlnA&t=3s")
# intersteller.show_trailer ()
iron_man = media.Movie("Iron Man",
                       "A Genius invents a suit and fights crime",
                       "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG", # noqa
                       "https://www.youtube.com/watch?v=8hYlB38asDY")

inception = media.Movie("Inception",
                        "A story about a thief that can enter people's dream\
                         and steal their secrets",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", # noqa
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

batman_the_killing_joke = media.Movie("Batman: The Killing Joke",
                                      "Joker is back for one last joke",
                                      "https://upload.wikimedia.org/wikipedia/en/1/11/Batman-The_Killing_Joke_%28film%29.jpg", # noqa
                                      "https://www.youtube.com/watch?v=VeNi4PfNMqI") # noqa
# Defiens movies
movies = [lion_king, star_wars_the_force_awakens, intersteller,
          iron_man, inception, batman_the_killing_joke]
# Uses movies to generate an html file and open it in the browser
fresh_tomatoes.open_movies_page(movies)
