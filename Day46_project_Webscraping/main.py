
import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
website = response.text
soup = BeautifulSoup(website, "html.parser")
movie_headings_tags = soup.find_all(name="h3", class_="title")

movie_titles = [title.getText() for title in movie_headings_tags]
movie_titles.reverse()

with open(r"C:\python_course_projects\Day46_project_Webscraping\movies.txt", mode="w", encoding="utf-8") as file:
    for movie_title in movie_titles:
        file.write(f"{movie_title}\n")