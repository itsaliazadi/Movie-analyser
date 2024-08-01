import Scraper
import matplotlib.pyplot as plt


data = Scraper.ExtractData()
quantity_dict = dict()

for genre_list in data.values():
    for genre in genre_list:
        if genre in quantity_dict.keys():
            quantity_dict[genre] += 1
        else:
            quantity_dict[genre] = 1


genres = list(quantity_dict.keys())
quantities = list(quantity_dict.values())

plt.bar(genres, quantities)
plt.xlabel('Genre')
plt.ylabel('Quantity')
plt.title('Genre Distribution')
plt.xticks(rotation=45, ha='right')
plt.show()

