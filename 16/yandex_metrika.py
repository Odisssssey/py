import requests

TOKEN = 'AQAAAAAMO8PjAAQMTDTQlh_t-0Delpv87dk27xc'
class YandexMetrika(object):
    views = None
    page_depth = None
    review_min = None

    def __init__(self, token):
        params = {'preset': 'sources_summary',
                  'id': '42720824',
                  'oauth_token': token}

        response = requests.get('https://api-metrika.yandex.ru/stat/v1/data', params)
        self.page_depth = response.json()['totals'][3]
        self.views = int(response.json()['totals'][1])
        self.review_min = int((response.json()['totals'][4]/60))



    def print_views(self):
        #print(self.views)
        pass


metrika = YandexMetrika(TOKEN)
print(metrika.__dict__)
