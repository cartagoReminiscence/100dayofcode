import requests
import collections
import csv

movies_data = "https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv"
movies_csv = "movies.csv"

def retrieve_csv_from_url(url=movies_data):
    r = requests.get(url)

    with open(movies_csv, 'w') as f:
        f.write(r.text)

Movie = collections.namedtuple('Movie', 'title year score')

def get_movies_by_director(data=movies_csv):
    directors = collections.defaultdict(list)
    with open(data, encoding='utf-8') as f:
        for line in csv.DictReader(f):
            try:

                director = line['director_name']
                movie = line['movie_title'].replace('\xa0', '')
                year = int(line['title_year'])
                score = float(line['imdb_score'])
            except ValueError:
                continue

            m = Movie(title=movie, year=year, score=score)
            directors[director].append(m)

    return directors

def get_directors_by_num_of_movies(directors):
    cnt = collections.Counter()
    for director, movies in directors.items():
        cnt[director] = len(movies)
    
    return cnt

if __name__ == "__main__":
    #retrieve_csv_from_url()

    directors = get_movies_by_director()
    # print(directors['Christopher Nolan'])
    # [print(m) for m in directors['Stanley Kubrick']]

    num_of_movies_counter = get_directors_by_num_of_movies(directors)
    print(num_of_movies_counter.most_common(5))