import sys
import json
import pandas as pd

if __name__ == '__main__':
    path = sys.argv[1]

    d = []
    for l in open(path + 'business.json').readlines():
        d.append(json.loads(l))  # from json str to dict
    df = pd.DataFrame.from_records(d)
    daz = pd.Series([x.city] for x in df.state["AZ"])
    print(daz)
    
#     da = []
#     for business in df:
#       if df.state[business] == "AZ": 
#         da.append(df.city[business]
#     print(da)
    
