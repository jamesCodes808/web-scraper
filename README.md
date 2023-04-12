# Web Scraper
Uses Python's BeautifulSoup to webscrape for citations needed on Wikipedia pages 

Examples:

git clone repo to local 

start virtual environment
```python
source .venv/bin/activate
```

edit urls in functions
```python
    print(get_citations_needed_count('https://en.wikipedia.org/wiki/Hedgehog'))
    print(get_citations_needed_report('https://en.wikipedia.org/wiki/Hedgehog'))
```

run script
```python
python3 -m web_scraper.scraper
```