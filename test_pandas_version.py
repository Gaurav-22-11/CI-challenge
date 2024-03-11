import pandas as pd

PANDAS_VERSION = "2.2.1"

def test_pandas_version():
  assert pd.__version__ in [PANDAS_VERSION]

if __name__=="__main__":
  test_pandas_version()
  print("Pandas version is correct!")
