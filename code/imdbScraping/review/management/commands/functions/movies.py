def get_movie_info(movie_containers):
    names = []
    urls = []
    years = []
    imdb_ratings = []
    metascores = []
    votes = []

    for container in movie_containers:

        if container.find('div', class_='ratings-metascore') is not None:
            name = container.h3.a.text
            names.append(name)

            url = container.h3.a['href']
            urls.append(url.split('?')[0])

            year = container.h3.find('span', class_='lister-item-year').text
            years.append(year)

            imdb = float(container.strong.text)
            imdb_ratings.append(imdb)

            m_score = container.find('span', class_='metascore').text
            metascores.append(int(m_score))

            vote = container.find('span', attrs={'name': 'nv'})['data-value']
            votes.append(int(vote))

    return names, urls, years, imdb_ratings, metascores, votes
