import pandas as pd
import numpy as np

#D = pd.read_exel/csv ("lokacijafajla/naziv fajla  ")
dates = pd.date_range("20130101", periods=6) #<-- random datumi

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

print(df)

print("*****************")
df2 = pd.DataFrame(    #<-- razliciti tipovi podataka
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
       
    }
)
""""
print(df2)
print("****************")
print(df2.dtypes) #<== tipovi podataka

"""

print(df.head)   #prikazati vrh
print("*****************")
print(df.tail(3)) #prikazati kraj
print("*****************") 
print(df.index)  # prikazati indeks 
print("*****************")
print(df.columns) #prikazati kolone
print("*****************")
print(df.to_numpy()) #dajete numpy-u prikaz osnovnih podataka(što se svodi na fundamentalnu razliku između pandas i NumPi: NumPi nizovi imaju jedan dtipe za ceo niz, dok pandas DataFrames imaju jedan dtipe po kolon)
print("*****************")
print(df.describe()) #kratak statisticki rezime nasih podataka
print("*****************")
print(df.T) #transponovane matrice
print("*****************")
print(df.sort_values(by="B")) #sortiraj vrijednosti( kolona B)
print("*****************")

print("*****************")
df3 = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)
print(df3)