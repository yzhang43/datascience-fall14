
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
import pandas as pd
import numpy as np


reader = DataFileReader(open("countries.avro", "r"), DatumReader())
for user in reader:
    print user
reader.close()
