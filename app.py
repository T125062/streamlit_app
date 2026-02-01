import streamlit as st
import pandas as pd
import streamlit as st

st.title('日本の平均寿命')

# CSVファイル読み込み
df = pd.read_csv('JP_AverageLifespan.csv')

# サイドバー
with st.sidebar:
    branch = st.multiselect('年号を選択してください（複数選択可）',
                            df['era'].unique(),
                            default=['平成','令和'])
    gender = st.multiselect('性別を選択してください（複数選択可）',
                            ['男性','女性'],
                            default=['男性','女性'])
    option = st.radio('表示形式を選択してください',
                  ['表','グラフ'])
    
# 表示




