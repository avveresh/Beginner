import pandas
trips_data = pandas.read_excel('trips_data.xlsx')
print (trips_data["city"].value_counts())