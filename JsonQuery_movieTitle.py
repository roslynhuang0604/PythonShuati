'''
- query all movies with the parameter: substring from database
- there are multiple pages
- sort the result in ascending order
'''


import urllib, json

def getPageNumber(substr):
    url = "https://jsonmock.hackerrank.com/api/movies/search/?Title={}".format(substr)
    response = urllib.urlopen(url)
    json_data = json.loads(response.read())
    return json_data['total_pages']


def fetchURLPage(substr, curPage):
    url = "https://jsonmock.hackerrank.com/api/movies/search/?Title={}&page={}".format(substr, curPage)
    response = urllib.urlopen(url)
    json_data = json.loads(response.read())
    return json_data['data'] # a list

def movieTitle(substr):
    total_pages = getPageNumber(substr)
    titles = []
    # check for all pages
    for curPage in range(1, total_pages + 1):
        movies = fetchURLPage(substr, curPage)
        for i in range(len(movies)):
            title = str(movies[i]['Title'])
            titles.append(title)
    return list(sorted(titles, key = str.lower))


print movieTitle("spiderman")
