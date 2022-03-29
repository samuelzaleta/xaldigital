import json
import requests
import pandas as pd
from datetime import datetime

if __name__ == '__main__':
    url = requests.get("https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow")
    text = url.text
    data = json.loads(text)

    #json_object = json.dumps(data, indent=4)
    #print(json_object)

    Df = pd.DataFrame.from_dict(data['items'])
    print(Df.columns)

    Df2 = Df['is_answered']
    print("Contestados", Df2[Df2 == True].count())
    print("No contestados", Df2[Df2 == False].count())

    Df3 = Df[Df['view_count'] == Df['view_count'].min()]
    print(Df3.values)

    Df4 = Df.sort_values(by=['last_activity_date'], ascending=False)
    Df4['last_activity_date'] = pd.to_datetime(Df4['last_activity_date'],unit='s')
    print(Df4)

    Df6 = pd.json_normalize(Df['owner'])
    print(Df6[Df6['reputation'] == Df6['reputation'].max()])
