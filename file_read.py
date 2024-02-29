import h5py
from pandas import (
    DataFrame, HDFStore
)
import numpy as np
import pandas as pd
import numpy as np
import os
#df = DataFrame(np.random.randn(5,3), columns=['A', 'B', 'C',])
#store = HDFStore('temp1.h5')
# adding dataframe to the HDF5 file
#store.put('d1', df, format='table', data_columns=True)
#store['d1']
#store.append('d1', DataFrame(np.random.randn(5,3), columns=['A', 'B', 'C']))
#store.close()
store = HDFStore('temp1.h5')
#df = pd.read_hdf('temp1.h5')
store.put('d2', DataFrame(np.random.randn(7,4)))
store.put('d3', DataFrame(np.random.randn(14,3)))
df = store['d1']
df1 = store['d2']
print(df)
print(df1)
store.close()
