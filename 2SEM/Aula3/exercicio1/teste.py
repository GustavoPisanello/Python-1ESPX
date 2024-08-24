import pandas as pd
import numpy as np

df_track = pd.read_csv(r'./Track_202408231944.csv')

""" print(df_track)
print(df_track.groupby('Name')['Milliseconds'].sum())
print(df_track['Milliseconds']) """

""" vetor = np.array([10, 20, 30, 40 , 50])
print(vetor)

matriz_2d = np.array([[10, 20, 20], [30, 40, 6]])
print(matriz_2d)
 """

# Estrutura unidimensionais - pandas series

s1 = pd.Series([10, 20, 30, 40, 50], name = "Serie 1")
s2 = pd.Series([1, 2, 3, 4, 5], name = "Serie 2")
s3 = pd.Series(['A', 'B', 'C', 'B','A'], name = "Serie 3")

s_soma = s1 + s2
s_sub = s1 - s2
s_mult = s1 * s2
s_div = s1 / s2

print(s1)

df = pd.DataFrame({'Serie 1': s1, 'Serie 2': s2, 'Serie 3': s3})

df['soma'] =  df['Serie 1'] + df['Serie 2']
df['sub'] =  df['Serie 1'] - df['Serie 2']

""" df['max'] = df.groupby('Serie 3')['soma'].max() """
df.groupby('Serie 3')['soma'].min()
df.groupby('Serie 3')['soma'].mean()

print(df)
print(df.groupby("Serie 3")['soma'])

