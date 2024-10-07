# Overview

{Data set of 14ers mountains.
https://www.kaggle.com/datasets/mikeshout/14erpeaks}

{My purpose for writing this software for this specific data set was to find connections in difficulty of hikes and elevation compared to elevation gained. I also wanted to learn more about using the Plotly library and Pandas.}


[Software Demo Video](https://youtu.be/TNSmQ513Zis)

# Data Analysis Results

{Questions:
How does elevation correlate with the difficulty of climbing each 14er?
Which 14ers have the highest elevation gain compared to their elevation?  
How does elevation gained compare to the climb difficulty?

Answers:
Elevation looks like it may correlate with the difficulty of climbing 14ers. The result was unexpected. It seems like the taller the mountain, the easier the climb is. Perhaps this dataset included this skew specifically to show that some mountains, though high in elevation, can be easier to climb than lower elevation mountains.
The 14ers with the highest elevation gain compared to their elevation gain told us that there is no clear pattern for how high a mountain is and how quickly it will gain elevation. It does tell us perhaps the relative difficulty of how the hike might be per mountain.
The difficulty of the hike compared to how much elevation was gained throughout showed that there are definitely other factors contributing to difficulty besides elevation gain. The general trend line is that the higher the elevation gain, the harder the hike is but we would need more of what goes into the difficulty class to make a conclusion.

Other Observations:
We can learn that Pikes Peak is often an outlier in the scatter plots. In both the Elevation vs Elevation Gain chart and the Difficulty vs Elevation Gain chart it stood alone.
}

# Development Environment

{This program was made in Python. I used Pandas, the Matplotlib, and the Plotly libraries to work with the dataset I choose. Pandas allowed me to easily retrieve information from the data set and do operations with it. The Matplotlib library allowed me to display a graph to summarize my data visually and have conclusions be apparent according to the visual. I later found the Plotly library easier to work with so this library is used in the final version, but in the comments you will find a version using the Matplotlib library. }

# Useful Websites

* [Towards Data Science ](https://towardsdatascience.com/getting-started-to-data-analysis-with-python-pandas-with-titanic-dataset-a195ab043c77)
* [Pandas Pydata](https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Item 1: I had a difficult time working with the "Difficulty" column in this data set. When displaying it on the Y axis in my charts it is out of order. I tried to input a custom order for the graphs but it seemed that broke it more. I would want to find the best way to take the values and put them in numerical order instead of "Easy Class 3 and Hard Class 3." I think this would help me move "Class 4" Difficulty to where it was supposed to be on the axis.
* Item 2: I would want to make use of the "Pictures" column in the dataset. In the future I would add pictures when you hover over the points on the scatter plots.
* Item 3: I could improve the look of the charts with better spacing. If possible I would want to figure out how to put all three charts on the same page for readability.
* Item 4: Since I was trying to determine the actual difficulty of the hikes and what went into a 14er being more difficult than another I would do more charts plotting the difference between difficulty and the other data points given in the dataset like prominence, isolation, and distance.
