import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import time
import random
import re

def get_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0.4472.124",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/91.0.4472.114",
        "Mozilla/5.0 (Linux; Android 10) Chrome/91.0.4472.101",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:89.0) Gecko/20100101 Firefox/89.0"
    ]
    return random.choice(user_agents)

def print_banner():
    print("=== SQLi Dork Finder - 0X1955 - HACKO ===")

def is_valid_id_param(url):
    parsed = urlparse(url)
    query = parsed.query
    return re.search(r'(^|&)id[a-zA-Z0-9_]*=', query)

def search_for_potential_targets(dorks_list, max_pages_per_dork=3, min_delay_seconds=8):
    found_urls = set()
    bing_base_url = "https://www.bing.com/search?q="

    print("\n--- Mulai pencarian target SQL Injection Global (param id=) ---\n")

    for dork in dorks_list:
        for page_num in range(max_pages_per_dork):
            query_url = f"{bing_base_url}{dork}&first={page_num * 10 + 1}"
            try:
                headers = {"User-Agent": get_random_user_agent()}
                response = requests.get(query_url, headers=headers, timeout=20)
                soup = BeautifulSoup(response.text, 'html.parser')
                results = soup.find_all('li', class_='b_algo')

                for result in results:
                    link = result.find('a', href=True)
                    if not link:
                        continue
                    url = link['href']

                    if "bing.com" in url or not url.startswith("http"):
                        continue

                    parsed = urlparse(url)
                    if not parsed.query:
                        continue
                    if not is_valid_id_param(url):
                        continue

                    if url not in found_urls:
                        found_urls.add(url)
                        print(url)

                time.sleep(min_delay_seconds)

            except Exception as e:
                
                break

    print("\n--- Selesai ---")
    print(f"Total ditemukan: {len(found_urls)} URL")

# Dork global fokus ke param id=
dorks_list = [
    "inurl=index.php?id=",
    "inurl=view.php?id=",
    "inurl=detail.php?id=",
    "inurl=read.php?id=",
    "inurl=profile.php?id=",
    "inurl=news.php?id=",
    "inurl=artikel.php?id=",
    "inurl=page.php?id=",
    "inurl=berita.php?id=",
    "inurl=info.php?id=",
    "inurl=product.php?id=",
    "inurl=content.php?id=",
    "inurl=show.php?id=",
    "inurl=more.php?id=",
    "inurl=info-detail.php?id=",
    "inurl=item.php?id=",
    "inurl=viewnews.php?id=",
    "inurl=viewitem.php?id=",
    "inurl=post.php?id=",
    "inurl=event.php?id=",
    "inurl=report.php?id=",
    "inurl=download.php?id=",
    "inurl=service.php?id=",
    "inurl=ticket.php?id=",
    "inurl=display.php?id=",
    "inurl=watch.php?id=",
    "inurl=record.php?id=",
    "inurl=detail_news.php?id=",
    "inurl=show_news.php?id=",
    "inurl=gallery.php?id=",
    "inurl=viewphoto.php?id=",
    "inurl=announce.php?id=",
    "inurl=ad.php?id=",
    "inurl=sport.php?id=",
    "inurl=doc.php?id=",
    "inurl=announcement.php?id=",
    "inurl=result.php?id=",
    "inurl=viewfile.php?id=",
    "inurl=event_detail.php?id=",
    "inurl=view_article.php?id=",
    "inurl=view.php?record_id=",
    "inurl=product.php?item_id=",
    "inurl=display.php?content_id=",
    "inurl=profile.php?user_id=",
    "inurl=shownews.php?id=",
    "inurl=doc_read.php?id=",
    "inurl=showimage.php?id=",
    "inurl=more_news.php?id=",
]

if __name__ == "__main__":
    print_banner()
    search_for_potential_targets(
        dorks_list=dorks_list,
        max_pages_per_dork=5,
        min_delay_seconds=5
    )
