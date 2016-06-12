import pandas as pd
from models import most_common

import data

most_common.predict(data.train, data.test)
