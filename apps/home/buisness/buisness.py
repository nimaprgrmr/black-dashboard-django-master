import numpy as np
import pickle
import warnings
from .data_preprocessing import make_all_process
from datetime import timedelta
import datetime
from dateutil import relativedelta
import jdatetime

warnings.filterwarnings("ignore")

# import models from paths we saved before.
filename_count = '/home/asltoghiri/asltoghiri/Django_Projects/black-dashboard-django-master/black-dashboard-django-master/apps/home/buisness/models/count_model.pkl'
filename_sale = '/home/asltoghiri/asltoghiri/Django_Projects/black-dashboard-django-master/black-dashboard-django-master/apps/home/buisness/models/sale_model.pkl'

# load the model from disk
model_count = pickle.load(open(filename_count, 'rb'))
model_xgb = pickle.load(open(filename_sale, 'rb'))
print("Models uploaded successfully!")


def before_data(df=make_all_process()) -> (np.ndarray, np.ndarray):
    last_3_months = df[-30:]
    last_3_months_data = last_3_months['total_price'].values.tolist()
    last_3_months_label = np.arange(1, len(last_3_months_data) + 1)
    return last_3_months_data, last_3_months_label


class MakeDetail:
    """
    این کلاس برای اجرای بعضی از تبدیلات و استخراج اصلاعات از مقادیر دیگر مانند تبدیل سال میلادی به شمسی و همچنین محاصبه فصل از ماه میلادی تعریف شده است.
    """

    def __init__(self, date):
        self.date = date

    def make_prd_to_plc(self):
        year = self.date.year
        id_prd = {'2018': 1397, '2019': 1398, '2020': 1399, '2021': 1400, '2022': 1401, '2023': 1402, '2024': 1403,
                  '2025': 1404, '2026': 1405}
        id_prd_to_plc = id_prd[str(year)]
        return id_prd_to_plc

    def make_season(self):
        month = self.date.month
        if month in (1, 2, 12):
            return 4
        elif month in (3, 4, 5):
            return 1
        elif month in (6, 7, 8):
            return 2
        else:
            return 3


def predict_next_n_month(df=make_all_process(), n: int = 1):
    """
    این تابع روز های n ماه آینده را میسازد برای ارجاع به تابع پیشبینی فروش.
    Parameters
    ----------
    df
    n : تعداد ماه درخواستی برای ساخته شدن

    Returns   است x خروجی این تابع ۲ مقدار است: که مقدار اول مشخصات روزهای تعداد ماه وارد شده برای پیشبینی و مقدار دوم تاریخ روزها برای نمایش در بردار
    -------

    """
    last_day_info = df.iloc[-1][['date', 'year', 'month', 'day', 'series']]
    # take the last day there is in dataframe
    last_day_date = (datetime.date(int(last_day_info['year']), int(last_day_info['month']), int(last_day_info['day']))
                     + timedelta(days=1))
    # take last series
    last_series = last_day_info['series']

    # calculate next month date
    nextmonth_date = (datetime.date(int(last_day_info['year']), int(last_day_info['month']), int(last_day_info['day']))
                      + relativedelta.relativedelta(months=n))

    list_information = []
    list_dates = []
    while last_day_date <= nextmonth_date:
        now = MakeDetail(last_day_date)
        last_series = last_series + 1

        new_info = [last_day_date.year, last_day_date.month, last_day_date.day, now.make_prd_to_plc(),
                    now.make_season(), last_series, 1]

        amount = int(np.round(model_count.predict([new_info]))[0])

        new_record = [last_day_date.year, last_day_date.month, last_day_date.day, now.make_prd_to_plc(),
                      now.make_season(), last_series, 1, amount]

        list_information.append(new_record)
        # convert miladi date to shamsi date with this library
        shamsi_date = jdatetime.date.fromgregorian(day=last_day_date.day, month=last_day_date.month,
                                                   year=last_day_date.year)
        # convert it to datetime fields
        shamsi_date = datetime.date(shamsi_date.year, shamsi_date.month, shamsi_date.day)
        # append to the list of dates
        list_dates.append(str(shamsi_date))
        last_day_date = last_day_date + timedelta(days=1)

    return list_information, list_dates


def predict_sales(days):
    """
    این تابع به عنوان ورودی ویژگی های چندین روز را میگیرد و پیشبینی های فروش این روز هارا به دست میآورد.
    Parameters
    ----------
    days

    Returns خروجی این تابع آرایه ای از پیشبینیها میباشد.
    -------

    """
    predictions = model_xgb.predict(days)
    predictions = [x/10 for x in predictions]
    return predictions


def previous_n_month(df=make_all_process(), n=6):
    """
    این تابع فروش ۶ ماه گذشته را حساب میکند و نمایش میدهد. برای مثال اگر امروز 1402/12/26 باشد
    این تابع مجموع فروش ۶ ماه گذشته یعنی برج ۶ تا 11 را محاصبه میکند
    Parameters
    ----------
    df
    n: تعداد ماه های درخواستی
    Returns  خروجی تابع ۶ عدد حاصل مجموع قروش ۶ ماه گذشته است.
    -------

    """
    last_day = df.iloc[-1]
    previous_n_month_date = (datetime.date(int(last_day['year']), int(last_day['month']), 1)
                             - relativedelta.relativedelta(months=n))
    max_date = previous_n_month_date + relativedelta.relativedelta(months=n)
    df_6m = df[(df['date'] >= str(previous_n_month_date)) & (df['date'] < str(max_date))]
    sale_6m_sum = df_6m[['month', 'total_price']].groupby(df_6m['month']).sum()['total_price']/10
    return sale_6m_sum.values, previous_n_month_date, max_date


def previous_six_month_improve(sale_7m_sum=previous_n_month(n=7)[0]):
    improvements = []
    for i, sale in enumerate(sale_7m_sum):
        try:
            improve = np.round(((sale_7m_sum[i+1]*100) / sale_7m_sum[i]) - 100, 2)
            improvements.append(improve)
        except:
            pass
    improvements_mean = np.round(np.mean(improvements), 2)
    return improvements, improvements_mean


def last_year(df=make_all_process(), start_date=None, end_date=None):
    try:
        start_ly = datetime.date(year=start_date.year - 1, month=start_date.month, day=start_date.day)
        end_ly = datetime.date(year=end_date.year - 1, month=end_date.month, day=end_date.day)
    except AttributeError:
        raise ValueError("You enetered None values for start_date and end_date for last_year function")
    
    df_6m_ly = df[(df['date'] >= str(start_ly)) & (df['date'] < str(end_ly))]
    sale_6m_sum = df_6m_ly[['month', 'total_price']].groupby(df_6m_ly['month']).sum()['total_price']/10
    return sale_6m_sum.values


def compare_monthly_sales(this_year_sales=None, last_year_sales=None):
    improvements = []
    if this_year_sales or last_year_sales is None:    
        this_year_sales, start_date, end_date = previous_n_month()
        last_year_sales = last_year(start_date=start_date, end_date=end_date)
    try:
        len(this_year_sales) == len(last_year_sales)
        for i in range(len(this_year_sales)):
            this_year_sale = this_year_sales[i]
            last_year_sale = last_year_sales[i]
            improve = np.round(((this_year_sale*100) / last_year_sale) - 100, 2)
            improvements.append(improve)
    except:
        raise ValueError("The lenght of entered values aren't the same!")
    
        
    return improvements
    

# next_30_days = predict_next_30_days()
# predictions = predict_sales(next_30_days)
# print(len(predictions))
# print(predictions)
