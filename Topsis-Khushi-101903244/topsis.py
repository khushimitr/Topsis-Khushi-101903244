import pandas as pd
import sys
import numpy as np

def topsis_score():
    filename = pd.read_excel('data.xlsx')
    filename.to_csv ("101903244-data.csv", 
                    index = None,
                    header=True)

    df = pd.read_csv("101903244-data.csv")
    ndf = df.drop('Fund Name', axis=1)
    row = len(ndf)
    cols = len(ndf.iloc[0,:])

    den = ndf.apply(np.square).apply(np.sum,axis = 0).apply(np.sqrt)

    weights = [1,1,1,2,1]
    impact = ['+','+','-','+','+']
    for i in range(cols):
        for j in range(row):
            ndf.iat[j, i] = (ndf.iloc[j, i] / den[i]) * weights[i]

    ideal_best = (ndf.max().values)
    ideal_worst = (ndf.min().values)
    for i in range(cols):
        if impact[i] == '-':
            ideal_best[i], ideal_worst[i] = ideal_worst[i], ideal_best[i]

    score = []
    for i in range(row):
        p,n = 0, 0
        for j in range(cols):
            p += (ideal_best[j] - ndf.iloc[i, j])**2
            n += (ideal_worst[j] - ndf.iloc[i, j])**2
        p, n = p**0.5, n**0.5
        score.append(n/(p + n))

    df['Topsis Score'] = score
    df['Rank'] = (df['Topsis Score'].rank(method='max', ascending=False))
    df.to_csv("101903244-result.csv")


if __name__ == "__main__":
    topsis_score()
