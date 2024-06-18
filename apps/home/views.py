# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
import numpy as np
from .buisness.buisness import before_data, predict_next_n_month, predict_sales, previous_n_month, \
    previous_six_month_improve, last_year, compare_monthly_sales

past_data = before_data()
# calculate months day and dates for predicting and show labels on chart
next_month, list_dates_month = predict_next_n_month(n=1)
next_two_month, listdates_two_month = predict_next_n_month(n=2)
next_three_month, listdates_three_month = predict_next_n_month(n=3)
# calculate previous 6 month sales
sale_6m_sum, start_date, end_date = previous_n_month()
# calculate last 6 month improvements
improvements, _ = list(previous_six_month_improve())
# calculate last year sales
last_year_sales = last_year(start_date=start_date, end_date=end_date)
compare_monthly_sales_values = compare_monthly_sales()

print(f"Improvements mean: {np.round(np.mean(compare_monthly_sales_values), 1)}")

@login_required(login_url="/login/")
def index(request):
    # values, labels = past_data
    predictions_month = list(predict_sales(next_month))
    predictions_two_month = list(predict_sales(next_two_month))
    predictions_three_month = list(predict_sales(next_three_month))

    context = {'segment': 'index', 'values_month': predictions_month, 'labels_month': list_dates_month,
               'values_two_month': predictions_two_month, 'labels_two_month': listdates_two_month,
               'values_three_month': predictions_three_month, 'labels_three_month': listdates_three_month,
               'prev_six_month_sale': list(sale_6m_sum), 'sum_prev_six_month_sale': f'{int(sum(sale_6m_sum)):,}',
               'improvements': improvements, 'improvements_mean': np.round(np.mean(compare_monthly_sales_values), 1),
               'compare_monthly_sales': compare_monthly_sales_values,
               'last_year_sales': list(last_year_sales), 'sum_last_year_sales': f'{int(sum(last_year_sales)):,}',
               }

    # html_template = loader.get_template('home/index.html')
    # return HttpResponse(html_template.render(context, request))
    return render(request, 'home/index.html', context)


@login_required(login_url="/login/")
def rtl_support(request):
    predictions_month = list(predict_sales(next_month))
    predictions_two_month = list(predict_sales(next_two_month))
    predictions_three_month = list(predict_sales(next_three_month))

    context = {'segment': 'index', 'values_month': predictions_month, 'labels_month': list_dates_month,
               'values_two_month': predictions_two_month, 'labels_two_month': listdates_two_month,
               'values_three_month': predictions_three_month, 'labels_three_month': listdates_three_month,
               'prev_six_month_sale': list(sale_6m_sum), 'sum_prev_six_month_sale': f'{int(sum(sale_6m_sum)):,}',
               'improvements': improvements, 'improvements_mean': np.round(np.mean(compare_monthly_sales_values), 1),
               'compare_monthly_sales': compare_monthly_sales_values,
               'last_year_sales': list(last_year_sales), 'sum_last_year_sales': f'{int(sum(last_year_sales)):,}',
               }

    # html_template = loader.get_template('home/index.html')
    # return HttpResponse(html_template.render(context, request))
    return render(request, 'home/rtl.html', context)


@login_required(login_url="/login/")
def icons(request):
    return render(request, 'home/icons.html')


@login_required(login_url="/login/")
def table_list(request):
    return render(request, 'home/tables.html')


@login_required(login_url="/login/")
def typography(request):
    return render(request, 'home/typography.html')


def login(request):
    return render(request, 'home/login.html')


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
