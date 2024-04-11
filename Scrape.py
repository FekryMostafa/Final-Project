"""
Author: Patrick Schools
File: Scraper.py
Descrtiption: Scrapes all links connected to mywlu.edu index and writes text to txt files
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, unquote
import os
from tqdm import tqdm
import re

# Function to scrape text from a webpage
def scrape_text_from_page(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract text from <p> elements
        paragraphs = soup.find_all('p')
        text = '\n'.join([p.get_text() for p in paragraphs])
        return text.strip()  # Strip whitespace from the text
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return ""

# Function to sanitize a string for use as a filename
def sanitize_filename(filename):
    # Remove invalid characters
    sanitized = re.sub(r'[\\/:*?"<>|]', '_', filename)
    # Remove leading and trailing whitespace
    sanitized = sanitized.strip()
    return sanitized

# Function to scrape linked pages iteratively
def scrape_linked_pages(starting_url, output_dir='output'):
    # List of forbidden items
    forbidden_items = ["flickr", "youtube", "instagram", "joinhandshake",
                       "facebook", "twitter", "pinterest", "reddit", 
                       "tiktok", "snapchat", "tumblr", "whatsapp", 
                       "linkedin", "netflix", "amazon", "ebay", 
                       "craigslist", "etsy", "spotify", "twitch", 
                       "discord","@",".jpg",".mov"]

    visited_urls = set()
    starting_url_links = []

    print("Finding all links within the specified section of the starting URL...")
    # Find all links within the specified section of the starting URL
    response = requests.get(starting_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    starting_url_links.extend([urljoin(starting_url, link['href']) for link in soup.select('div.tax-index.component.position-1 ul li a') if 'href' in link.attrs][20:])  # Exclude the first 20 links
    urls_to_visit = starting_url_links
    print("Scraping started...")
    with tqdm(desc="Progress", unit=" URLs visited") as pbar:
        for url in urls_to_visit:
            if url not in visited_urls:
                visited_urls.add(url)
                # Check if any forbidden item is present in the URL
                if any(item in url for item in forbidden_items):
                    continue
                # Scrape text from the current page
                text = scrape_text_from_page(url)
                # Check if text is empty
                if text:
                    # Generate a sanitized filename from the URL
                    filename = os.path.join(output_dir, sanitize_filename(unquote(urlparse(url).path[1:])) + '.txt')
                    # Save text to the file
                    with open(filename, 'w', encoding='utf-8') as f:
                        f.write(text)
                # Find all links on the current page
                try:
                    response = requests.get(url)
                    soup = BeautifulSoup(response.content, 'html.parser')
                    page_links = [urljoin(url, link['href']) for link in soup.find_all('a', href=True)]
                    for link in page_links:
                        if link not in visited_urls:
                            urls_to_visit.insert(0,link)
                except Exception as e:
                    print(f"Error processing links on {url}: {e}")
                pbar.update(1)  # Update the progress bar

    print("Scraping finished!")

# Starting URL
starting_url = "https://my.wlu.edu/a-z-index"

# Create output directory if it doesn't exist
output_directory = 'TextFiles2'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Begin scraping
scrape_linked_pages(starting_url, output_dir=output_directory)
