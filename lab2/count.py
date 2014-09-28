import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import pandas as pd
import numpy as np


reader = DataFileReader(open("countries.avro", "r"), DatumReader())
my_list = list()
for user in reader:
    my_list.append(user)
df = pd.DataFrame(my_list)
reader.close()

#######database manipulation#########
print np.sum(df.population>10000000)

