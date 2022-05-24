from bs4 import BeautifulSoup
import requests
# import openpyxl


# Accesses website and return a response object that is stored in a variable
# Contains source variable contains HTML source code of requested webpage
# Inorder to capture error from response object use try

try:
    source = requests.get("https://www.imdb.com/search/keyword/?keywords=superhero%2Cmarvel-comics&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=a581b14c-5a82-4e29-9cf8-54f909ced9e1&pf_rd_r=24367EM19WS382QMFF9K&pf_rd_s=center-5&pf_rd_t=15051&pf_rd_i=genre&ref_=kw_ref_key&sort=moviemeter,asc&mode=detail&page=1")
    
    # Sends an error to the console if the requested webpage is unavailable
    source.raise_for_status()


    # Takes the content of the source website and converts it to text
    soup = BeautifulSoup(source.text,"html.parser")
    

    # Goes to each of the 50 movie boxes
    movie_containers = soup.find("div", class_="lister-item mode-detail")
    
    # print(movie_containers)

    # Iterate with for loop through each part of the container for certain content
    # Use find to search for first tag that meets search criteria
    # Tag class cannot be named class or else error occurs. Use class_
    # Use .get_text(strip=True) to remove spaces, tabs, and enters
    # Use .split(".")[0] to split a string between periods and index into the seperate splits

    for movie in movie_containers:

        name = movie.find("a").text

        release_year = movie.find("span", class_="lister-item-year text-muted unbold").text.strip("()")

        age_rating = movie.find("span", class_="certificate").text

        length = movie.find("span", class_="runtime").text

        genre = movie.find("span", class_="genre").text

        imdb_score = movie.find("strong").text

        print(f"{name}, {release_year}, {imdb_score}, {age_rating}, {length}, {genre}.")

        # Use break inorder to stop for loop after first loop

except Exception as e:
    # Catches exceptions of type Exception. Inside except: block, the raised expection(the actual object, not the exception class) is bound to the variable e.
    print(e)
