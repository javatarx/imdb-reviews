from review.models import Review


def get_reviews(url, movie, base=None):
    from requests import get
    from bs4 import BeautifulSoup as BS
    from time import sleep
    from random import randint

    reviews = 0

    try:
        response = get(url)

        html_soup = BS(response.text, 'html.parser')
        review_containers = html_soup.find_all('div', class_='imdb-user-review')

        for review in review_containers:
            title, comment, date, rating = get_review_info(review)

            review = Review()
            review.title = title
            review.comment = comment
            review.date = date
            review.movie = movie
            review.rating = rating
            review.url = url

            review.save()

        if html_soup.find('div', class_='load-more-data') is not None:
            if base is None:
                base = url

            _key = html_soup.find('div', class_='load-more-data')['data-key']
            _url = base + '/_ajax?paginationKey=' + _key
            sleep(randint(3, 8))
            get_reviews(_url, movie, base)
    except Exception as e:
        print('ERROR: ', e)
        print(movie, url)

    return reviews


def get_review_info(review):
    title = ''
    comment = ''
    date = ''
    rating = '0'

    if review.find('a', class_='title') is not None:
        title = review.find('a', class_='title').text

    if review.find('div', class_='text show-more__control') is not None:
        comment = review.find('div', class_='text show-more__control').text

    if review.find('span', class_='spoiler-warning') is not None:
        comment = review.find('span', class_='spoiler-warning').text

    if review.find('span', class_='review-date') is not None:
        date = review.find('span', class_='review-date').text

    if review.find('span', class_='rating-other-user-rating') is not None:
        rating = review.find('span', class_='rating-other-user-rating').find('span').text

    return title, comment, date, rating
