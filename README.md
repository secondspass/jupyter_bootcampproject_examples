This repo contains Jupyter and excel examples that will be useful when putting together the bootcamp
projects. We will make our actual projects in different locations. This will just hold
useful examples that we can all consult when we need something.

This includes examples of how to do things with Geopandas, widgets, making plots and maps.

In order to set up the environment, run `conda env create -f environment.yml`

Or if that is not working, pip installing the following should be sufficient
`pip install pandas geopandas geodatasets scipy matplotlib openpyxl`

Add any data that needs to read for the examples in `data`. (And if github won't allow you
to upload that data, then just leave some instructions in this README for your particular
example

## Info about each example

### us_choropleth_map.ipynb
This gives a nice interactive map of the US where you can hover over counties to see the 
Jun average temperature and the number of medicare benificiaries in that county.

No special instructions. Just make sure that the `CtyAvTemp62016.csv` and
`2016_HHSemPOWERMapHistoricalDataset.xlsx` files are in the `data` directory.

### aggregate_poweroutage_data.ipynb
This shows how to use Pandas groupby and aggregate functions to get mean and median
(and other stuff too) of a time series data. In this example I use the
`eaglei_outages_2016.csv` which is a time series data. I show how to aggregate the 
data for the date 2016-06-20 to get mean and median of the number of people who are out of
power that day.

Make sure the `eaglei_outages_2016.csv` file is in the data directory. Github will not
allow it to be pushed so you'll have to copy it in to the data directory.

### Geo_project_widgets.ipynb
This shows how to apply widgets to a given Pandas/GeoPandas plot.
Each Notebook cell can be run individually without depending on the others.
The first cell just shows a normal GeoPandas plot.
The second cell introduces a lot of widgets that update the plot (e.g., variable changing and colorbar limit changing)
The third cell is a simplified version of the second cell that only allows the changing of variables

Switching variables via the dropdown box will switch the variable that is plotted (and reset the colorbar limits to default min/max values).
This allows viz-ing plots for different variables very simple without having to swap code around.

> Note: Sometimes the notebook widgets bug out and don't produce a plot, or it ends up producing multiple plots on accident
This is usually because the kernel hiccuped when executing the notebook and usually restarting the kernel and clearing
all output will help this.

> Note 2: Although switching variables resets the colorbar limits to the default min/max values for that variable, currently
the text in the widget itself for ``c_min`` and ``c_max`` don't update. Just a quality of life bug. A workaround can be done
that fixes this by uncommenting the ``c_min.value`` and ``c_max.value`` lines in the ``update`` function, but then this generates
two additional plots as updating c_min and c_max "regenerates" the plot.
