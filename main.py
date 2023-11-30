import gmaps
import gmaps.datasets

gmaps.configure(api_key='AI...') # Fill in with your API key

earthquake_df = gmaps.datasets.load_dataset_as_df('earthquakes')
earthquake_df.head()