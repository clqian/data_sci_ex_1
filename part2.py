import sys
import json
import pandas as pd

if __name__ == '__main__':
    path = sys.argv[1]

    d = []
    for l in open(path + 'business.json').readlines():
        d.append(json.loads(l))  # from json str to dict
    df = pd.DataFrame.from_records(d)
    # daz = pd.Series([x.city] for x in df.state["AZ"])
    # daz = pd.Series([x.city] for x in df.query('state == ["AZ"]'))
    daz = df.query('state == ["AZ"]').city
    daz = daz.str.upper()  # account for different lettering
    daz = daz.dropna(axis=0)  # account for missing entries
    daz = daz.str.replace('NORTH|SOUTH|EAST|WEST', '', case=False).str.strip()  # account for directions and whitespace

    # print(daz[0:10])
    print(len(daz))
    print(len(daz.unique()))

#     da = []
#     for business in df:
#       if df.state[business] == "AZ":
#         da.append(df.city[business]
#     print(daz)
