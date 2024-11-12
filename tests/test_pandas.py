import pandas as pd
import pytest
from pandas_modules.dataframes import FrameXRC

def test_create_df():
    #ARRANGE
    frame = FrameXRC()
    #ACT
    df = frame.create_frame()
    #ASSERT
    assert df.dtypes['column1'] == int
    assert df.dtypes['column2'] == object

def test_sort_frame():
    frame = FrameXRC()
    df = frame.sort_df()
    #series = df['Date']

    assert df['Date'][0] == '2023-09-01'
    #assert series.iloc(-1) == '2023-09-30'
    assert df.iloc[-1]['Date'] == '2023-09-30'
    # assert df.tail(-1)['Date'] == '2023-09-30'assert df.iloc[0]['Date'] == '2023-09-01


