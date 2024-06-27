import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the CSV file with specified column names
file_path = '/mnt/data/Word Cloud - Attributes PalBot - Sheet2.csv'
data = pd.read_csv(file_path, header=None, names=['Phrase', 'Frequency'])

# Create a dictionary of phrases and their frequencies
phrase_freq = dict(zip(data['Phrase'], data['Frequency']))

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(phrase_freq)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
