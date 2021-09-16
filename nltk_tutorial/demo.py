import validators
import logging
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from urllib.request import Request, urlopen
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# Global Variable
news = {}
intel_web = 'https://circuit.intel.com/content/news/home/circuithome.html'

def _initialize_log():
    format = '%(asctime)s [%(levelname)s]: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')


def intel_news_links(choice='header'):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-erros')
    options.add_argument('--test-type')
    driver = webdriver.Chrome(executable_path=r'C:\bat\chromedriver_win32\chromedriver.exe', chrome_options=options)
    driver.get(intel_web)
    sleep(5)
    data = driver.page_source
    driver.close()
    html = BeautifulSoup(data, 'lxml')
    li_list = []
    if choice == 'header':
        li_list = html.findAll(name='li', attrs={'class': 'swiper-pagination-bullet'})
    elif choice == 'all':
        li_list = html.findAll(name='li', attrs={'class':'article-preview type-separate-text'})
    news_link = [f"https://circuit.intel.com{li.find(name='a').attrs['href']}" for li in li_list]
    return news_link


def news_content(news_links):
    for i, link in enumerate(news_links):
        if validators.url(link):
            logging.info(f'{link}: is Valid')
            content = {}
            req = Request(url=link, headers={'user-agent':'my-app'})
            data = urlopen(req)
            html = BeautifulSoup(data, 'html.parser')
            try:
                # header = html.find(name='h1', id='article-header', attrs={'class': 'page-title'}).text
                header = html.title.text
                logging.info(f'No {i}. Header: {header}')
                # paragraph = html.find(name='div', attrs={'class': 'imgTextBulletsClass block-quote-fix template-editorial-table-container white-font-bg'}).text
                body_content = html.find(name='div', attrs={'class': 'content_article_body_par parsys'})
                page_content = body_content.find_all(text=True)
                paragraph = []
                for cont in page_content:
                    if cont.parent.name in ['p']:
                        paragraph.append(cont.replace(u'\xa0', ' '))
                paragraph = ' '.join(para.rstrip() for para in paragraph)
                content['header'] = header
                content['paragraph'] = paragraph
            except:
                logging.warning(f'No {i}: None News webpage')
                content['header'] = ''
                content['paragraph'] = ''
            news[i] = content
        else:
            logging.error(f'{link}: INVALID !!!')
    return news


def text_analysis(i):
    if i > len(news):
        return f'Total Number of news: {len(news)}'
    vader = SentimentIntensityAnalyzer()
    news_c = news[i]

    # Header
    if not news_c['header']:
        return 'None News Webpage'
    header = news_c['header']
    header_score = vader.polarity_scores(header)
    logging.info(f'HEADER: {header}\nScore: {header_score}')

    # Paragraph
    paragraph = news_c['paragraph']
    if not paragraph:
        logging.warning(f'Visiting non-news webpage')
    # Search for keyword
    stopword = stopwords.words('english')
    words = [word for word in word_tokenize(paragraph) if word.isalpha() if word not in stopword]
    fdist = FreqDist(words)
    logging.info(f'Paragraph:\n KEYWORD{fdist.most_common(10)}')
    sentences = sent_tokenize(paragraph)
    min_compound = max_compound = 0
    min_sentence = max_sentence = ''
    for index, sentence in enumerate(sentences):
        sentence_score = vader.polarity_scores(sentence)
        if sentence_score['compound'] > max_compound:
            max_sentence = sentence
        if sentence_score['compound'] < min_compound:
            min_sentence = sentence
    logging.info(f'Score :{vader.polarity_scores(paragraph)}')
    logging.info(f'Most neg sentence: {min_sentence}')
    logging.info(f'Most pos sentence: {max_sentence}')
    return 0


if __name__ == '__main__':
    _initialize_log()
    news_link = intel_news_links()
    news = news_content(news_link)
    text_analysis(1)
    print()