# using constructor in python

class movie:
    def __init__(self,title, director, year):
        self.title = title
        self.director = director
        self.year = year
    def info(self):
        print(f"{self.title} film is directed by {self.director} and release in a {self.year}.")


list_of_movies=[]
while True:
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = int(input("Enter the movie release year: "))
    m = movie(title, director, year)
    list_of_movies.append(m)
    cont = input("Do you want to add another movie? (yes/no): ")
    if cont.lower() != "yes":
        break
print("\nList of Movies:")
for m in list_of_movies:
    m.info()

#m1= movie("RRR", "Rajamouli", 2022)
#m1.info()