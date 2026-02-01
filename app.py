import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 日本語フォント設定（文字化け対策）
plt.rcParams['font.family'] = 'MS Gothic'

st.title('日本の平均寿命')
st.subheader('年号・性別を選択して平均寿命の推移を確認できます')

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

# 見出し表示（st.metric使用）
col1, col2 = st.columns(2)

if '男性' in gender:
    col1.metric(
        '男性の平均寿命（選択期間平均）',
        f"{df_filtered['man'].mean():.2f} 歳") # 選択したデータ範囲によって表示を変化

if '女性' in gender:
    col2.metric(
        '女性の平均寿命（選択期間平均）',
        f"{df_filtered['woman'].mean():.2f} 歳")

# タブ表示（st.tab使用）
tab1, tab2 = st.tabs(['表', 'グラフ'])

# 表
with tab1:
    st.subheader('日本における平均寿命')

    df_display = df_filtered.rename(columns={
        'year':'年',
        'man':'男性',
        'woman':'女性',
        'era':'年号'
    })

    columns = ['年','年号']
    if '男性' in gender:
        columns.append('男性')
    if '女性' in gender:
        columns.append('女性')

    st.dataframe(
        df_display[columns],
        use_container_width=True
    )
    
    # ダウンロード機能（st.download_button使用）
    st.download_button(
        '表示中のデータをCSVファイルでダウンロード',
        df_display[columns].to_csv(index=False),
        'average_lifespan_filtered.csv',
        'text/csv'
    )

# グラフ表示
with tab2:
    st.subheader('平均寿命の推移')

    fig, ax = plt.subplots()

    if '男性' in gender:
        ax.plot(df_filtered['year'], df_filtered['man'], label='男性')

    if '女性' in gender:
        ax.plot(df_filtered['year'], df_filtered['woman'], label='女性')

    ax.set_xlabel('年')
    ax.set_ylabel('平均寿命（歳）')
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)