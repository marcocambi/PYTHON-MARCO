import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#1. Prezzi di chiusura
tickers = ["AAPL", "MSFT", "TSLA", "GOOGL", "AMZN", "NVDA", "AMD", "META", "SPY", "QQQ", "AVGO"]
data = yf.download(tickers, start = "2020-01-01", end = "2026-01-01", auto_adjust=True)["Close"]

# 2. Calcolo dei rendimenti e della matrice di correlazione
returns = data.pct_change().dropna()
corr_matrix = returns.corr()

# 3. Elimina il triangolo superiore
# mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

# 4. Rendering visivo della Heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(
    corr_matrix, 
    annot=True, 
    cmap="coolwarm", 
    vmin=-1, 
    vmax=1, 
    fmt=".2f",
   # mask=mask,
    annot_kws={"size": 9}
)

plt.title("Stock Return Correlation Heatmap", fontsize=14, pad=12)
plt.tight_layout()

# Invece di plt.show(), salva il grafico come immagine
plt.savefig("heatmap.png", dpi=300)
print("Grafico salvato con successo!")
plt.show