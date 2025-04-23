import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the cleaned CSV file
file_path = 'oscar_final_attributes.csv'
data = pd.read_csv(file_path)

# Drop any rows where 'Attribute' column is empty or NaN
data = data.dropna(subset=['Attribute'])

# Count occurrences of each attribute
attribute_freq = data['Attribute'].value_counts().to_dict()

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(attribute_freq)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
