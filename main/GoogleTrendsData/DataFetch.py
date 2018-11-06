from pytrends.request import TrendReq


pytrend = TrendReq()
kw_list = ['Google Stock','Facebook Stock']
# Create payload and capture API tokens. Only needed for interest_over_time(), interest_by_region() & related_queries()
pytrend.build_payload(kw_list)

# # Interest Over Time
# interest_over_time_df = pytrend.interest_over_time()
# print(interest_over_time_df.head())
#
# # Interest by Region
# interest_by_region_df = pytrend.interest_by_region()
# print(interest_by_region_df.head())
#
# # Related Queries, returns a dictionary of dataframes
# related_queries_dict = pytrend.related_queries()
# print(related_queries_dict)
#
# # Get Google Hot Trends data
# trending_searches_df = pytrend.trending_searches()
# print(trending_searches_df.head())
#
# # Get Google Top Charts
# top_charts_df = pytrend.top_charts(cid='actors', date=201611)
# print(top_charts_df.head())
#
# # Get Google Keyword Suggestions
# suggestions_dict = pytrend.suggestions(keyword='pizza')
# print(suggestions_dict)
# # a = dir(pytrends.dailydata)
# # print(a)

hourly_histoical_data = pytrend.get_historical_interest(kw_list, year_start=2018, month_start=6, day_start=1, hour_start=1, year_end=2018, month_end=7, day_end=9, hour_end=5,sleep=0)
print(hourly_histoical_data)

