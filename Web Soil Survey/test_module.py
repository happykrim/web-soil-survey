def find_highest_percent_aoi(data_list):
    # Convert 'Percent of AOI' to numeric and find the max
    highest = max(data_list, key=lambda x: float(x['Percent of AOI'].strip('%')))
    return highest["Map Unit Symbol"], highest["Map Unit Name"], highest["Rating"]

data_in_soil_moisture_class_table = [
    {'Map Unit Symbol': '38A', 'Map Unit Name': 'Hinckley loamy sand, 0 to 3 percent slopes', 'Rating': 'Udic', 'Acres in AOI': '0.0', 'Percent of AOI': '0.7%'},
    {'Map Unit Symbol': '73C', 'Map Unit Name': 'Charlton-Chatfield complex, 0 to 15 percent slopes, very rocky', 'Rating': 'Udic', 'Acres in AOI': '2.7', 'Percent of AOI': '74.7%'},
    {'Map Unit Symbol': '73E', 'Map Unit Name': 'Charlton-Chatfield complex, 15 to 45 percent slopes, very rocky', 'Rating': 'Udic', 'Acres in AOI': '0.9', 'Percent of AOI': '24.6%'}
]

test_data = [{'Map Unit Symbol': '17', 'Map Unit Name': 'Timakwa and Natchaug soils, 0 to 2 percent slopes', 'Rating': 'Peraquic', 'Acres in AOI': '0.3', 'Percent of AOI': '8.7%'}, 
 {'Map Unit Symbol': '38A', 'Map Unit Name': 'Hinckley loamy sand, 0 to 3 percent slopes', 'Rating': 'Udic', 'Acres in AOI': '2.6', 'Percent of AOI': '86.1%'}, 
 {'Map Unit Symbol': '38C', 'Map Unit Name': 'Hinckley loamy sand, 3 to 15 percent slopes', 'Rating': 'Udic', 'Acres in AOI': '0.2', 'Percent of AOI': '5.2%'}]

symbol, name, rating =  find_highest_percent_aoi (data_in_soil_moisture_class_table)
print(f"Symbol: {symbol}")
print(f"Name: {name}")
print(f"Rating: {rating}")