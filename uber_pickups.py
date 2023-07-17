# -*- coding: utf-8-*-
# conding:utf-8
import streamlit as st
import pandas as pd
import numpy as np

st.title('北京市数据')

data_url = (
    'https://github.com/tyut2018/laomiao_app/blob/main/uber-raw-data-sep14.csv')


# @st.cache_data
def load_data():
    data = pd.read_csv(data_url,encoding='utf-8')
    return data


data_load_state = st.text('导入数据...')
data = load_data()
data_load_state.text('数据导入完成')

st.subheader('城南与城北地区历年常住人口（万人）')
data = pd.DataFrame(data)
st.write(data)

columns = ['2010', '2011', '2012', '2013',
           '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
rows = ['全市', '丰台区', '房山区', '大兴区', '城南地区',
        '城南占比(%)', '朝阳区', '海淀区', '顺义区', '昌平区', '城北地区', '城北占比(%)']

st.subheader('按照时间浏览常驻人口')
chart_data = pd.DataFrame(data)
chart_data = chart_data[1:12]
st.write(chart_data)
st.line_chart(chart_data, y=columns)

st.subheader('按照区浏览常驻人口')
chart_data = pd.DataFrame(data.T)
st.write(chart_data)
chart_data = chart_data[1:13]
st.line_chart(chart_data)
