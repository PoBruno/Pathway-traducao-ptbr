import pandas as pd
from googletrans import Translator as T
import time
import tqdm.notebook as tq

CNAE = pd.read_excel('/content/correspondecia_CPV_CNAE.xlsx', 'CNAE', dtype=str)
CPV = pd.read_excel('/content/correspondecia_CPV_CNAE.xlsx', 'CPV2003', dtype=str)
CNAE.head()





