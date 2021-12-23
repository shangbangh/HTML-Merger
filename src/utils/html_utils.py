import bs4;

def make_soup(file):
    return bs4.BeautifulSoup(file.read(), features="html.parser");