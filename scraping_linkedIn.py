from bs4 import BeautifulSoup
import requests
import re

job_count = 0

def contains_keywords(text, keywords):
    return any(re.search(keyword, text, re.IGNORECASE) for keyword in keywords)

# List of keywords to filter for new grad AND intern positions
new_grad_keywords = ["new grad", "recent grad", "graduate"]
intern_keywords = [ "intern", "internship", "co-op"]

page_to_scape = requests.get("https://www.linkedin.com/jobs/")
soup = BeautifulSoup(page_to_scape.text, "html.parser")

titles = soup.findAll("span", attrs={"class":"job-details-jobs-unified-top-card__job-title-link"})
location = soup.findAll("span", attrs={"class":"white-space-pre"})
dates_posted = soup.findAll("time")


for title, date_posted, in zip(titles, dates_posted):
    if contains_keywords(title.text, new_grad_keywords) or contains_keywords(title.text, intern_keywords):
      print(f"Job Title: {title.text} \n Date posted: {date_posted.text})")
      job_count += 1

      if job_count >= 20:
        break