import streamlit as st
import pandas as pd
import streamlit as st

st.title('日本の平均寿命')

df = pd.read_csv('JP_AverageLifespan.csv')

with st.sidebar:
    branch = st.multiselect('年号を選択してください（複数選択可）',
                            df['era'].unique())


