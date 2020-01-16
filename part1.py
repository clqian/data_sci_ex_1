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
    print('Q3: ' + str(len(user_reviews[user_reviews.text >= user_reviews.text.mean() + 6 * user_reviews.text.std()])))
    biz_id = df['business_id'].value_counts().idxmax()
    d = []
    for l in open(path + 'business.json').readlines():
        d.append(json.loads(l))  # from json str to dict
    biz = pd.DataFrame.from_records(d)
    # df_biz = df.set_index('business_id').join(biz.set_index('business_id'))
    print('Q4: ' + biz[biz.business_id == biz_id].name.iloc[0])
    df['date'] = pd.to_datetime(df['date'])
    df['time_hour'] = df['date'].dt.hour
    print('Q5: ' + str(df[df.business_id == biz_id]['time_hour'].value_counts().index[-1]))

