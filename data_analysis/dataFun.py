import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
import plotly.express as px




############################################Pandas notes############################################

# how to check elements in data set
# df = pd.read_csv("14er.csv")
# df.head()
# df.tail()

# print(df.head())
# print(df.tail())


# how to read specific columns
# df = pd.read_csv("14er.csv", usecols= ["Do you attend religious services"])
# print(df.head())

# how to use .describe, .info, and .dtypes
df = pd.read_csv("14er.csv", encoding='cp1252')
# # df.describe()
# # df.info()
# # df.dtypes
# df.sort_values("Distance_mi").head(10)
# print(df.head())

# check names of columns
# print(df.columns)

# count rows
# row_count = df['Elevation_ft].count()

####################################################################################################

## Purpose:     To analyze trends and patterns in the dataset and return useful observations
## Questions:   How does elevation correlate with the difficulty of climbing each 14er?
##              Which 14ers have the highest elevation gain compared to their overall elevation?
##              How does elevation gain compare to difficulty of the climb?
##              
## You must demonstrate the ability to do one or more of the following to achieve each answer: filter, sort, aggregate (sum, average, count), or data conversion.       



# Average elevation of 14er
# average_elevation = df['Elevation_ft'].mean()
# print(f"The average elevation of the 14ers in this set is {average_elevation} feet high.")


# Elevation vs Difficulty
# matplotlib.pylot version

# plt.scatter(df['Elevation_ft'], df['Difficulty'], alpha=0.5)
# # plt.yticks([1, 2, 3, 4, 5, 6, 7], ['Class 1', 'Class 2', 'Hard Class 2' 'Easy CLass 3', 'Hard Class 3', 'Class 4'])
# plt.title('Elevation vs Difficulty of Climbing 14ers')
# plt.xlabel('Elevation (ft)')
# plt.ylabel('Difficulty (class)')
# plt.show()

# plotly.express version

# custom_order =  ['Class 1', 'Class 2', 'Hard Class 2' 'Easy Class 3', 'Hard Class 3', 'Class 4']
fig = px.scatter(
    df,
    x='Elevation_ft',
    y='Difficulty',
    hover_name='Mountain Peak',  # This is the column that will display on hover
    # category_orders={'Difficulty': custom_order},
    labels={
        'Elevation_ft': 'Elevation (ft)',
        'Difficulty': 'Difficulty (class)',
    },
    title='Elevation vs Difficulty of Climbing 14ers'

)

# Update y-axis formatting
# fig.update_layout(
#     yaxis=dict(
#         tickvals=[13000, 13500, 14000, 14500],  # Custom tick positions
#         ticktext=["13k ft", "13.5k ft", "14k ft", "14.5k ft"],  # Labels for the ticks
#         title="Difficulty (ft)"
#     )
# )



fig.show()
# Correlation: ranges from -1 (perfect negative correlation) to +1 (perfect positive correlation), and 0 (no correlation)
# df['Difficulty'] = df['Difficulty'].replace('unknown', 0).astype(int)
# df['Difficulty'] = pd.to_numeric(df['Difficulty'], errors='coerce')

# correlation = df['Elevation_ft'].corr(df['Difficulty'])
# print(f"Correlation between Elevation and Difficulty: {correlation}")


# Elevation gain compared to total elevation
# matplotlib.pylot version
# plt.scatter(df['Elevation_ft'], df['Elevation Gain_ft'], alpha=0.5)
# plt.title('Elevation vs Elevation Gain')
# plt.xlabel('Elevation (ft)')
# plt.ylabel('Elevation Gain (ft)')
# plt.show()

# plotly.express version
fig2 = px.scatter(
    df,
    x='Elevation_ft',
    y='Elevation Gain_ft',
    hover_name='Mountain Peak',  # This is the column that will display on hover
    labels={
        'Elevation_ft': 'Elevation (ft)',
        'Elevation Gain_ft': 'Elevation Gain (ft)',
    },
    title='Elevation vs Elevation Gain'
)

fig2.show()

# Elevation Gain compared to difficulty


fig3 = px.scatter(
    df,
    x='Elevation Gain_ft',
    y='Difficulty',
    hover_name='Mountain Peak',  # This is the column that will display on hover
    # category_orders={'Difficulty': custom_order},
    labels={
        'Elevation Gain_ft': 'Elevation Gain (ft)',
        'Difficulty': 'Difficulty (class)',
    },
    title='Difficulty vs Elevation Gain'
)

fig3.show()
