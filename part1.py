import sys
import json
import pandas as pd

if __name__ == '__main__':
    path = sys.argv[1]

    d = []
    for l in open(path + 'tip.json').readlines():
        d.append(json.loads(l))  # from json str to dict
    df = pd.DataFrame.from_records(d)
    print('Q1: ' + str(len(df.index)))
    print('Q2: ' + str(len(df[df.text.map(len) == df.text.map(len).max()])))
    user_reviews = df.groupby("user_id").count()[["text"]]
    print('Q3: ' + str(len(user_reviews[user_reviews.text >= user_reviews.text.mean() + user_reviews.text.std()])))
