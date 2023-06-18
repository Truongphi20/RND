import streamlit as st
import pandas as pd
import numpy as np

import static as stt


st.set_page_config(page_title="HPV_overview" ,layout='wide')
st.title("""
**Tìm hiểu về *papillomavirus* và phương pháp xét nghiệm DNA virus**
""")

st.header("1. Số lượng bài báo công bố hằng năm về HPV")
data1 = stt.gettb.table1
fig1 = stt.draw.DrawYear(data1)
st.write(fig1)


st.header("2. Tình hình nghiên cứu các chủng HPV")
st.write(stt.gettb.table2)




col1, col2 = st.columns([1,2])

with col1:
    cutoff_val = st.slider('Cut-off value: ', 1, 1000, 300, key='slidebar')
    table_sum = stt.gettb.TableSum(cutoff_val)
    table_sum_show = table_sum.copy()
    table_sum_show = table_sum_show.set_index('Type')
    st.write(table_sum_show)
    

with col2:
    graph_com = stt.draw.DrawCom(table_sum)
    st.write(graph_com)
    

st.header("3. Mức độ nghiên cứu ở các chủng theo mỗi năm")
col1, col2 = st.columns([1,4])
with col1:
    cutoff_val2 = st.slider('Cut-off value: ', 1, 1000, 300, key='slidebar2')

with col2:
    table_ey = stt.gettb.TableEy(cutoff_val2)
    graph_ey = stt.draw.DrawEy(table_ey)
    st.write(graph_ey)
