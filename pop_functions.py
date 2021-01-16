import pandas as pd

def categorize_ages(df):
    age_cat = pd.DataFrame()
    for k, v in df.iteritems():
        if int(k) % 10 == 0:
            age_cat[k//10] = v
        elif int(k) % 10 == 9:
            age_cat[k//10] += v
            rename_dict = {(k//10): f"{k-9}-{k}"}
            age_cat.rename(rename_dict, axis = 1, inplace = True)
        else:
            age_cat[k//10] += v
    age_cat["90+"] = age_cat["90-99"] + age_cat["100-109"] + age_cat[11]
    age_cat.drop(["90-99", "100-109", 11], axis = 1, inplace = True)
    return age_cat