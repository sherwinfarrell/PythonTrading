from newsapi import newsapi_client
import datetime
import json
api = newsapi_client.NewsApiClient(api_key='d022b69b02b3488ebd2508c2b3972734')

date = datetime.datetime(2018,9,20)
# print(date.strftime('%Y-%m-%d'))

all_articles =[]


for i in range(30):
    all_articles.append(api.get_everything(q='Google',from_param=date.strftime('%Y-%m-%d'),to=date.strftime('%Y-%m-%d'),

                                      language='en',
                                      sort_by='relevancy',
                                      page=2))
    with open('JsonFile{}.json'.format(i),'w') as fp:
        json.dump(all_articles[i],fp)
    print(date)
    print(all_articles[i])
    date += datetime.timedelta(days=1)



# with open('JsonFile1.json','w') as fp:
#     jsonString = json.dump(all_articles,fp)



