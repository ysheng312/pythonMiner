#import json
from collections import Counter
from prettytable import PrettyTable

from ys_twitter import TWTR_OAUTH


__author__ = 'ysheng'

# XXX: Set this variable to a trending topic,
# or anything else for that matter. The example query below
# was a trending topic when this content was being developed
# and is used throughout the remainder of this chapter.

q = "#stocks"

count = 200

# See https://dev.twitter.com/docs/api/1.1/get/search/tweets

search_results = TWTR_OAUTH.twitter_api.search.tweets(q=q, count=count)

statuses = search_results['statuses']

# Iterate through 5 more batches of results by following the cursor

#for _ in range(5):
#    print "Length of statuses", len(statuses)
#    try:
#        next_results = search_results['search_metadata']['next_results']
#    except KeyError, e: # No more results when next_results doesn't exist
#        break

# Create a dictionary from next_results, which has the following form:
# ?max_id=313519052523986943&q=NCAA&include_entities=1
#    kwargs = dict([kv.split('=') for kv in next_results[1:].split("&")])

#    search_results = TWTR_OAUTH.twitter_api.search.tweets(**kwargs)
#    statuses += search_results['statuses']

# Show one sample search result by slicing the list...
#print json.dumps(statuses[0], indent=1)

status_texts = [status['text']
                for status in statuses]

screen_names = [user_mention['screen_name']
                for status in statuses
                for user_mention in status['entities']['user_mentions']]

hashtags = [hashtag['text']
            for status in statuses
                for hashtag in status['entities']['hashtags']]

# Computer a collection of all words from all tweets
words = [w
         for t in status_texts
         for w in t.split()]

# Explore the first 5 items for each...
#print 'status texts: ' + json.dumps(status_texts[0:5], indent=1)
#print 'screen names: ' + json.dumps(screen_names[0:5], indent=1)
#print 'hashtags: ' + json.dumps(hashtags[0:5], indent=1)
#print 'words: ' + json.dumps(words[0:5], indent=1)

#for item in [words, screen_names, hashtags]:
#    c = Counter(item)
#    print c.most_common()[:10] # top 10
#    print

for label, data in (('Word', words),
                    ('Screen Name', screen_names),
                    ('Hashtag', hashtags)):
    pt = PrettyTable(field_names=[label, 'Count'])
    c = Counter(data)
    [pt.add_row(kv) for kv in c.most_common()[:10]]
    pt.align[label], pt.align['Count'] = 'l', 'r' #Set column alignment
    print pt
