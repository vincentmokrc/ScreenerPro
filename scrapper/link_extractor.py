from urllib.request import urlopen, urljoin , urlparse
import re
import requests

def download_page(url):
    try:
        return requests.get(url).text
    except:
        print('error in the url', url)

def extract_links(page):
    if not page:
        return []
    link_regex = re.compile('<a[^>]+href=["\'](.*?)["\']',re.IGNORECASE)
    return [urljoin(page,link) for link in link_regex.findall(page)]

def get_links(page_url):
    host = urlparse(page_url)[1]
    page = download_page(page_url)
    print(page)
    links = extract_links(page)
    return[link for link in links if urlparse(link)[1] == host]

def depth_first_search(start_url):
    from collections import deque
    visited = set()
    queue = deque()
    queue.append(start_url)
    while queue:
        url = queue.popleft()
        if url in visited:
            continue
        visited.add(url)
        for link in get_links(url):
            queue.appendleft(link)
        print(url)

def breadth_first_search(start_url):
    from collections import deque
    visited = set()
    queue = deque()
    queue.append(start_url)
    while queue:
        url = queue.popleft()
        if url in visited:
            continue
        visited.add(url)
        queue.extend(get_links(url))
        print(url)

if __name__ == '__main__':
    target_url = 'https://www.bursamalaysia.com/'
    get_links(target_url)
