from bs4 import BeautifulSoup
import requests

page_to_scape = requests.get("https://realpython.github.io/fake-jobs/")
soup = BeautifulSoup(page_to_scape.text, "html.parser")
titles = soup.findAll("h2", attrs={"class":"title is-5"})
dates_posted = soup.findAll("time")
apply_links = soup.findAll("a", attrs={"href": "Apply"})

# Find all footers with class 'card-footer'
footers = soup.findAll("footer", attrs={"class": "card-footer"})
# Extract the 'Apply' links from each footer
apply_links = [footer.find_all("a", class_="card-footer-item")[1]['href'] for footer in footers]


for title, date_posted, apply_link in zip(titles, dates_posted, apply_links):
    print(f"*{title.text} -> {date_posted.text} ( {apply_link} )")