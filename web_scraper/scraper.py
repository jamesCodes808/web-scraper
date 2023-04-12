import requests
import re
from bs4 import BeautifulSoup


def get_citations_needed_count(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    citations = soup.find_all(title=re.compile('Wikipedia:Citation needed', re.IGNORECASE))
    return len(citations)

def get_citations_needed_report(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    report = ''
    for citation in soup.find_all('p'):
        if 'citation needed' in citation.text:
            report += citation.text
    return report

if __name__ == '__main__':
    print(get_citations_needed_count('https://en.wikipedia.org/wiki/Hedgehog'))
    print(get_citations_needed_report('https://en.wikipedia.org/wiki/Hedgehog'))
