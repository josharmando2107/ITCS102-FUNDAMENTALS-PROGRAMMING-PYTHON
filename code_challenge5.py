print("Welcome to the Manga Reader Recommender")
genre = input("What genre are you looking for?(action, romance, horror):")

if genre.lower() == "action":
               print("You have choosen action")
               manga_year = input("What year?(2000-2010):")
               if manga_year == "2000":
                       duration = input("long or short: ")
                       if duration == "long":
                                 print("Here are long action manga's in 2000 ")
                                 print("1. Dragon Ball Z\n2. Naruto\n3. One Piece")
 
                       elif duration == "short":
                                 print("Here are short action manga's in 2000 ")
                                 print("1. Solo Leveling\n2. One punch Man\n3. Unordinary")

               elif manga_year == "2010" :
                       duration = input("long or short: ")
                       if duration == "long":
                                 print("Here are long action manga's in 2010 ")
                                 print("1. Demon Slayer\n2. Mob Psycho\n3. Hero Academia")

                       elif duration == "short":
                                 print("Here are short action manga's in 2010 ")
                                 print("1. Bleach\n2. Black Clover\n3. Jujutsu Kaisen")
if genre.lower() == "romance":
              print("You have choosen Romance")
              manga_year = input("What year?(2000-2010):")
              if manga_year == "2000":
                       duration = input("long or short: ")
                       if duration == "long":
                              print("Here are long manga's in 2000 ")
                              print("1. Horimiya\n2. Fruits Basket\n3. Say I Love you")
                       elif duration == "short":
                              print("Here are short manga's in 2000 ")
                              print("1. Ao Haro Ride\n2. Angel Beats\n3. Toradora")
              if manga_year == "2010" :
                       duration = input("long or short: ")
                       if duration == "long":
                              print("Here are long manga's in 2010 ")
                              print("1. Skip Beat\n2. My Little Monster\n3. Bakuman")
                       elif duration == "short":
                              print("Here are short manga's in 2010 ")
                              print("1. Silent Voice\n2. Golden Time\n3. Your Name")
if genre.lower() == "horror":
             print("You have choosen Horror")
             manga_year = input("What year?(2000-2010):")
             if manga_year == "2000":
                       duration = input("long or short: ")
                       if duration == "long":
                              print("Here are long manga's in 2000 ")
                              print("1. Parasyte\n2. Hellsing\n3. Junji Ito Collection")
                       elif duration == "short":
                              print("Here are short manga's in 2000 ")
                              print("1. Death Note\n2. Another\n3. Tokyo Ghoul")
             if manga_year == "2010" :
                       duration = input("long or short: ")
                       if duration  == "long":
                              print("Here are long manga's in 2010 ")
                              print("1. Gantz\n2. Shiki\n3. Berserk")
                       if duration == "short":
                              print("Here are short manga's in 2010 ")
                              print("1. Gyo\n2. Dark Gathering\n3. Mononoke")
                           
