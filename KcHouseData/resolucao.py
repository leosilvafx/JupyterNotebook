import pandas as pd
import numpy as np

data = pd.read_csv( 'kc_house_data.csv' )

#1
print( len( data['id'].unique() ) )

#2
print( len( data.drop( ['id','date'], axis=1).columns ) )

#3
print( data.drop( ['id','date'], axis=1 ).columns )

#4
print( data['id'][data.price == (data['price'].max())]  )

#5
print( data['id'][data.bedrooms == (data['bedrooms'].max())]  )

#6
print( data.bedrooms.sum() )

#7
print( len( data['bathrooms'][data.bathrooms == 2]) )

#8
print( np.round( data['price'].mean(), 2 ) )

#9
print( np.round( data['price'][data.bathrooms == 2].mean(), 2) )

#10
print( data['price'][data.bedrooms == 3].min() )

#11
print( 
len( data['sqft_living'][data.sqft_living > 3229.17] ) )

#12
print( len( data['floors'][data.floors > 2] ) )

#13
print( len( data['sqft_lot'][data.sqft_lot > 3229.17] ) )

#14
print( len( data['bedrooms'][data.bedrooms > 2] ) )

#15
print( len( data['waterfront'][data.waterfront == 1] ) )

#16
print( len( data['waterfront'][data.waterfront == 1][data.bedrooms == 3] ) )

#17
print( len( data['sqft_living'][data.sqft_living > 3229.17][data.bathrooms > 2] ) )
