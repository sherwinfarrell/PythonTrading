import json
import eventregistry as ER
er = ER.EventRegistry('569a0bbd-eb92-4249-9434-c401f4d2c4cc')
analytics = ER.Analytics(er)

sum = []

for i in range(30):
    with open('JsonFile{}.json'.format(i),'r') as fp:
            jsonObj = json.load(fp)
            print(jsonObj)
            newList = []
            for article in jsonObj['articles']:
                title = article['title']
                if(title.find('Google')!=-1):
                    newList.append(article)
            print(newList)
            newJsonString = json.dumps(newList)
            newJsonString2 = json.loads(newJsonString)
            sum1 =0
            for article in newJsonString2:
                print(article['description'])
                text = article['description']
                if(text!=None):
                    sentiment = analytics.sentiment(text = text)
                    sum1 = sum1 + sentiment['avgSent']
                else:sum1=sum1+0

            sum.append(sum1)
# newList = []
# for article in jsonObj['articles']:
#     title = article['title']
#     if(title.find('Apple')!=-1):
#        newList.append(article)
#
# print(newList)
# newJsonString = json.dumps(newList)
# # for article in jsonObj['articles']:
# #     title = article['title']
# #     if(title.find('Apple')==-1):
# #         print(article['title'])
# #         del article
# newJsonString2=json.loads(newJsonString)
# sum=0
# for article in newJsonString2:
#     print(type(article['description']))
#     text = article['description']
#     sentiment = analytics.sentiment(text=text)
#     sum =sum+sentiment['avgSent']
#     #print(Analytics.sentiment(article['description']))


# print(sum)

# newJsonString  =  json.dumps(jsonObj)
# print(newJsonString)
# newJsonObj = json.loads(newJsonString)
#
# for articles in newJsonObj['articles']:
#     print(articles['title'])
print(sum)