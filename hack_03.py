import pandas as pd

df = pd.DataFrame({"price": ["R$ 46.550,25"]})

# Remove o símbolo de real e as vírgulas
df["price"] = df["price"].str.replace("R$", "").str.replace(".", "").str.replace(",", "")

# Imprime o dataframe
print(df)