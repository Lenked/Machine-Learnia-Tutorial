import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

bitcoin = pd.read_csv('data_game/BTC-EUR.csv', index_col='Date', parse_dates=True)

# bitcoin['Close'].plot(figsize=(9, 6))
bitcoin.loc['2022':'2023', 'Close'].plot()
plt.show()

bitcoin.loc['2023', 'Close'].resample('2W').mean().plot()
plt.show()

bitcoin.loc['2023', 'Close'].resample('2W').std().plot()
plt.show()

m = bitcoin.loc['2023', 'Close'].resample('W').agg(['mean', 'std', 'min', 'max'])

plt.figure(figsize=(12, 8))
m['mean']['2023'].plot(label='moyenne par semaine')
plt.fill_between(m.index, m['max'], m['min'], alpha=0.2, label='min-max par semaine')

plt.legend()
plt.show()

plt.figure(figsize=(12, 8))
bitcoin.loc['2023', 'Close'].plot()
for i in np.arange(0.2, 1, 0.2):
    bitcoin.loc['2023-07', 'Close'].ewm(alpha=i).mean().plot(label=f'ewm {i}', ls='--', alpha=0.8)
plt.legend()
plt.show()

ethereum = pd.read_csv('data_game/ETH-EUR.csv', index_col='Date', parse_dates=True)
ethereum.loc['2023', 'Close'].plot()

pd.merge(bitcoin, ethereum, on='Date', how='inner', suffixes=('_btc', '_eth'))
