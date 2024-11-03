import requests
from bs4 import BeautifulSoup
import re
from pick import pick

class LinkFilter:
    def filter(self, response):
        soup = BeautifulSoup(response.text, "html.parser")
        audio_links = []

        for link_tag in soup.find_all("a", href=True):
            href = link_tag["href"]
            if re.search(r"\.(mp3|wav|aac|ogg|m4a)$", href):
                audio_links.append(href)

        if len(audio_links) > 1:
            print("There are multiple links in your url.")
            link, _ = pick(audio_links, "Select from the links:")
        else:
            link = audio_links[0]

        return requests.get(link)

class AudioFileGetter:
    def __init__(self):
        self.link_filter = LinkFilter()

    def get_audio_file(self, url: str = ""):
        links: [] = []
        response = requests.get(url)
        if response.status_code == 200:
            filtered_response = self.link_filter.filter(response)
            with open("temp_audio_file", "wb") as audio_file:
                audio_file.write(filtered_response.content)
        else:
            print(f"Impossible to get content from given link")