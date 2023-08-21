import os
from datetime import date, datetime, timedelta
from typing import Any, List, Optional

import pandas as pd
from pandas.core.frame import DataFrame

from models.settings import settings


def strip_dataframe_empty_string(df: DataFrame) -> DataFrame:
    df_obj = df.select_dtypes(["object"])
    df[df_obj.columns] = df_obj.apply(lambda x: x.str.strip())
    return df
