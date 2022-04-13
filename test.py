
import pandas as pd
from pmaw import PushshiftAPI
import datetime as dt

api = PushshiftAPI()
before = int(dt.datetime(2022,4,12,0,0).timestamp())
after = int(dt.datetime(2022,4,11,0,0).timestamp())
subreddit = "conspiracy"
limit = 200
comments = api.search_comments(subreddit = subreddit, limit = limit, before = before, after = after)
print(f'Retrieved {len(comments)} comments for r/{subreddit}')

dataframe = pd.DataFrame(comments)
dataframe.to_csv('./wsb_comments.csv', header=True, index=False, columns=list(dataframe.axes[1]))