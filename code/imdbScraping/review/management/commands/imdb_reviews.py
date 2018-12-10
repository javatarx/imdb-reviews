from django.core.management import BaseCommand, CommandError

from review.management.commands.functions.movies import get_movie_info
from review.management.commands.functions.reviews import get_reviews


class Command(BaseCommand):
    help = 'Get reviews for a url of IMDB movie'

    def add_arguments(self, parser):
        parser.add_argument('url', nargs='+', type=str)

    def handle(self, *args, **options):
        from bs4 import BeautifulSoup as BS
        from requests import get
        from warnings import warn

        try:
            _base_url = 'http://www.imdb.com'
            requests = 0
            _url = options['url']
            url = _base_url + '/search/title?release_date=2018&sort=num_votes,desc&page=1'

            response = get(url)

            if response.status_code != 200:
                warn('Request: {}; Status code: {}'.format(requests, response.status_code))

            html_soup = BS(response.text, 'html.parser')
            movie_containers = html_soup.find_all('div', class_='lister-item mode-advanced')

            names, urls, years, imdb_ratings, metascores, votes = get_movie_info(movie_containers)

            for i, n in enumerate(names[:30]):
                nro_reviews = get_reviews(_base_url + urls[i] + 'reviews', n)
                print('Se encontraron %s reviews de %s' % (nro_reviews, n))

            self.stdout.write(self.style.SUCCESS('Obtain review of %s' % _url))
        except Exception as e:
            raise CommandError('Error al obtener review: %s', e)

        self.stdout.write(self.style.SUCCESS('Successfully closed'))
