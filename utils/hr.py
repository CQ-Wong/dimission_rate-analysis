from datetime import date, datetime
from math import ceil


def cal_working_month(enroll_date: date, resign_date: date) -> int:
    enroll_date_year = enroll_date.year
    resign_date_year = resign_date.year
    enroll_date_month = enroll_date.month
    resign_date_month = resign_date.month

    if enroll_date_year == resign_date_year:
        working_month = resign_date_month - enroll_date_month + 1

    else:
        working_month = (
            (resign_date_year - enroll_date_year - 1) * 12
            + enroll_date_month
            + resign_date_month
        )
    if enroll_date.day >= 16:
        return working_month - 1
    else:
        return working_month


def cal_working_month_level(working_month: int) -> int:
    if working_month == 0:
        return 0
    if working_month >= 32:
        return 12
    return ceil((working_month + 2) / 3)
