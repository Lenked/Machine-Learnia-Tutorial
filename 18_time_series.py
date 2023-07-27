import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

bitcoin = pd.read_csv('data_game/BTC-EUR.csv', index_col='Date', parse_dates=True)

# bitcoin['Close'].plot(figsize=(9, 6))
bitcoin.loc['2022':'2023', 'Close'].plot()
plt.show()


