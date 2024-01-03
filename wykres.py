import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_excel('bmi.xlsx', usecols=['osoba', 'waga', 'wzrost'])
sns.color_palette("Spectral", as_cmap=True)


sns.set_theme()


sns.relplot(
    data=data,
    x="wzrost", y="waga", hue="osoba", style="osoba"
)
plt.show() 
