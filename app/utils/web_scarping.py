import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


def testUrl(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False

def fetchAndParse(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
        print(f"Failed to retrieve {url}")
        return None
    
def fetchAndParseBySelenium(url):
    chrome_options = Options()
    # Opens the browser up in background
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--incognito")
    with Chrome(options=chrome_options) as browser:
        browser.get(url)
        html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def textCleaning(soup: BeautifulSoup) -> str:
    for menu in soup.find_all('nav'):
        menu.decompose()
    for menu in soup.find_all('header'):
        menu.decompose()
    for menu in soup.find_all('footer'):
        menu.decompose()
    content = soup.text
    content = re.sub(r'\{\{.*?\}\}', '', content)
    content = re.sub(r'[\r]?[\n]?[-]?[ \t]?', '', content)
    content.strip()
    return content


travelled_url = set()
full_url_list = set()
url_base = ''
page_contents = []


def scrape(url):
    url_base = urlparse(url).netloc
    print(url_base)
    recursiveScrape(url, url_base)
    return page_contents


def getLinksByTag(soup: BeautifulSoup) -> set:
    urls = set()
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href and href.startswith('http'):
            pure_url = re.search(
                r'(https?:\/\/[www\.]?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b[-a-zA-Z0-9()@:%_\+.~?&//=]*)', href)
            if pure_url is not None:
                urls.add(pure_url[0])
    return urls


def getLinksFromScript(soup: BeautifulSoup) -> set:
    urls = set()
    script = soup.find_all('script')
    for s in script:
        if s.string == None:
            continue
        links = re.findall(
            r'(https?:\/\/[www\.]?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b[-a-zA-Z0-9()@:%_\+.~#?&//=]*)', s.string)
        urls.update(links)
    return urls


def discoverLinks(url: str, base_url: str) -> set:
    soup = fetchAndParse(url)
    all_links = set()

    if soup is not None:
        # Get the links from JS script
        links = getLinksFromScript(soup)
        for l in links:
            if base_url in l:
                all_links.add(l)
        links = getLinksByTag(soup)
        for l in links:
            if base_url in l:
                all_links.add(l)
    return all_links

def scrapeContent(url):
    soup = fetchAndParseBySelenium(url)
    if soup is not None:
        travelled_url.add(url)
        if soup.find('title') is None:
            return
        title = soup.find('title').string
        main_content = soup.find('body')
        content = textCleaning(main_content)
        page_content = {
            'url': url,
            'title': title,
            'content': content
        }
        return page_content
    else:
        return None

def recursiveScrape(url, base_url, depth=0, max_depth=3):
    if depth > max_depth:
        return

    if url in travelled_url:
        return

    print(f"Scraping depth {depth}: {url}")
    if testUrl(url) is False:
        return
    page_content = scrapeContent(url)
    if page_content is not None:
        for c in page_contents:
            if page_content['title'] in c['title']:
                print(
                    f'Duplicate Header: {page_content['url']}, {page_content['title']}')
                return
        page_contents.append(page_content)
    links = discoverLinks(url, base_url)
    if len(links) > 0:
        for l in links:
            if l is not None:
                recursiveScrape(l, base_url, depth + 1, max_depth)
