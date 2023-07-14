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
    data = pd.read_csv(data_url, encoding='utf8')
    return data


data_load_state = st.text('导入数据...')
data = load_data()
data_load_state.text('数据导入完成')

st.subheader('城南与城北地区历年常住人口（万人）')
st.write(data)
