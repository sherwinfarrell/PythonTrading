# from eventregistry import *
# import json
# er = EventRegistry(apiKey = '569a0bbd-eb92-4249-9434-c401f4d2c4cc')
# q = QueryArticlesIter(conceptUri = er.getConceptUri("George Clooney"))
# with open('data.json','w') as fp:
#     for art in q.execQuery(er, sortBy = "date"):
#         print(art)
#         json.dump(art,fp)
#



from eventregistry import *
er = EventRegistry(apiKey = '569a0bbd-eb92-4249-9434-c401f4d2c4cc')
# q=QueryArticlesIter(
#     keywords="Facebook",
#     dateStart='2018-09-02',
#     dateEnd='2018-10-03'
# )
# for article in q.execQuery(er,sortBy="rel",maxItems=10):
#     print(article)
q = QueryArticles(
    # set the date limit of interest
    dateStart = datetime.date(2018, 6, 16), dateEnd = datetime.date(2018, 10, 4),
    # find articles mentioning the company Apple
    conceptUri = er.getConceptUri("Apple"))
# return the list of top 30 articles, including the concepts, categories and article image
q.setRequestedResult(RequestArticlesInfo(page = 1, count = 100,
    returnInfo = ReturnInfo(articleInfo = ArticleInfoFlags(concepts = True, categories = True, image = True))))
res = er.execQuery(q)

print(res)


#569a0bbd-eb92-4249-9434-c401f4d2c4cc