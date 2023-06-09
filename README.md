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

