import requests
import re
from bs4 import BeautifulSoup

site1 = "https://en.wikipedia.org/wiki/History_of_Islam"
site2 = 'https://en.wikipedia.org/wiki/History_of_the_iPhone'
site3 = 'https://en.wikipedia.org/wiki/History_of_Amazon#:~:text=Amazon%20was%20founded%20in%20the,with%20World%20Wide%20Web%20access.'
site4 = 'https://en.wikipedia.org/wiki/Amazon_rainforest#:~:text=The%20rainforest%20likely%20formed%20during,climate%20to%20the%20Amazon%20basin.'


# req = requests.get(url)
# markup = req.text
#
# soup = BeautifulSoup(markup, 'html.parser')

# print(soup.prettify())


def get_citations_needed_count(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    citations_needed = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    return len(citations_needed)


def get_citations_needed_report(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    citations_needed = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    passages = []
    for citation in citations_needed:
        passage = citation.find_parent('p').text
        sentences = passage.split('.')
        for index, sentence in enumerate(sentences):
            if citation.text.strip() in sentence:
                prev_sentence = sentences[index - 1].strip()
                if prev_sentence.endswith('['):
                    prev_sentence = prev_sentence[:-1]
                passages.append(prev_sentence)
                break
    report = "\n\n".join(passages)
    return report



# print(get_citations_needed_count(site1))
# print(get_citations_needed_count(site2))
# print(get_citations_needed_count(site3))
# print(get_citations_needed_count(site4))

print(get_citations_needed_report(site4))

