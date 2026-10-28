"""Small, offline BeautifulSoup warm-up adapted from the course lesson."""
from bs4 import BeautifulSoup

html = """
<html><body><h1>A Ghibli reading list</h1>
<p>Start with these community wiki pages:</p>
<a href="https://nausicaa.net/wiki/My_Neighbor_Totoro">My Neighbor Totoro</a>
<a href="https://nausicaa.net/wiki/Spirited_Away">Spirited Away</a>
</body></html>
"""
soup = BeautifulSoup(html, "html.parser")
for link in soup.find_all("a", href=True):
    print(link.get_text(" ", strip=True), link["href"])
