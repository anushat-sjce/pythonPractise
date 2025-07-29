import pandas as pd
import matplotlib.pyplot as plt

dict1 = {"a":[1,2,3], "b":[4,5,6],"c":[7,8,9]}
df = pd.DataFrame(dict1)
type(df)
df.head()


!pip install nba_api

from nba_api.stats.static import teams
import matplotlib.pyplot as plt

def one_dict(list_dict):
    keys= list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict


dict_nba_team = one_dict(nba_teams)
df_teams = pd.DataFrame(dict_nba_team)
df_teams.head()
