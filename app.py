import streamlit as st
import pandas as pd

st.title('日本の平均寿命')

# CSVファイル読み込み
df = pd.read_csv('JP_AverageLifespan.csv')

# サイドバー
with st.sidebar:
    st.header('表示条件')

    era = st.multiselect('年号を選択してください（複数選択可）',
                            df['era'].unique(),
                            default=['平成','令和'])
    
    gender = st.multiselect('性別を選択してください（複数選択可）',
                            ['男性','女性'],
                            default=['男性','女性'])

# データ抽出
df_filtered = df[df['era'].isin(era)]

# 見出し表示
col1, col2 = st.columns(2)

if '男性' in gender:
    col1.metric(
        '男性の平均寿命（選択期間平均）',
        f"{df_filtered['man'].mean():.2f} 歳")

if '女性' in gender:
    col2.metric(
        '女性の平均寿命（選択期間平均）',
        f"{df_filtered['woman'].mean():.2f} 歳")

# タブ表示
tab1, tab2 = st.tabs(['表', 'グラフ'])







