import requests
from bs4 import BeautifulSoup

def fetch_headlines(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    headline_tags = soup.select('h2') or soup.select('.title')
    headlines = [tag.get_text(strip=True) for tag in headline_tags if tag.get_text(strip=True)]
    return headlines

def save_headlines(headlines, filename='headlines.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        for idx, line in enumerate(headlines, start=1):
            f.write(f"{idx}. {line}\n")

def main():
    url = 'https://www.indiatoday.in/'
    print(f"Fetching headlines from: {url}")
    headlines = fetch_headlines(url)
    if headlines:
        print(f"Found {len(headlines)} headlines. Saving to file...")
        save_headlines(headlines)
        print("Headlines saved successfully!")
    else:
        print("No headlines found. You may need to refine the selector.")

if __name__ == '__main__':
    main()
