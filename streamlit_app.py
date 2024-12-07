import streamlit as st

# タイトル
st.title("英文法学習アプリ（解説付き）")

# 問題1: 現在形と過去形の選択肢問題
st.subheader("問題 1: 次の文を正しく完成させてください。")
question_1 = "I ___ (eat) lunch at 12:00 every day."
options_1 = ["eat", "eats", "ate", "eating"]
answer_1 = "eat"  # 正解は "eat"
explanation_1 = (
    "現在形を使うべきです。'every day' のように、習慣や普段の行動を表すときは "
    "現在形の動詞を使います。'eat' が正しいです。"
)

# ユーザーの選択を取得
user_answer_1 = st.radio(question_1, options_1, key="q1")

# 解答結果と解説（ユーザーが選択後に表示される）
if user_answer_1:
    if user_answer_1 == answer_1:
        st.success("正解です！")
    else:
        st.error("間違いです。正しい答えは 'eat' です。")
    st.write(explanation_1)

# 問題2: 一般動詞の使い方
st.subheader("問題 2: 次の文を正しく完成させてください。")
question_2 = "She ___ (go) to school every day."
options_2 = ["go", "goes", "gone", "going"]
answer_2 = "goes"  # 正解は "goes"
explanation_2 = (
    "'She' のように三人称単数の主語がある場合、動詞に 's' をつける必要があります。"
    "したがって、'goes' が正解です。"
)

# ユーザーの選択を取得
user_answer_2 = st.radio(question_2, options_2, key="q2")

# 解答結果と解説（ユーザーが選択後に表示される）
if user_answer_2:
    if user_answer_2 == answer_2:
        st.success("正解です！")
    else:
        st.error("間違いです。正しい答えは 'goes' です。")
    st.write(explanation_2)

# 問題3: 助動詞の使い方
st.subheader("問題 3: 次の文を正しく完成させてください。")
question_3 = "You ___ (can) swim very fast."
options_3 = ["can", "could", "be", "will"]
answer_3 = "can"  # 正解は "can"
explanation_3 = (
    "'can' は能力を表す助動詞です。'You can swim very fast.' は「あなたはとても速く泳げる」という意味です。"
    "他の選択肢（'could', 'be', 'will'）は文の意味に合いません。"
)

# ユーザーの選択を取得
user_answer_3 = st.radio(question_3, options_3, key="q3")

# 解答結果と解説（ユーザーが選択後に表示される）
if user_answer_3:
    if user_answer_3 == answer_3:
        st.success("正解です！")
    else:
        st.error("間違いです。正しい答えは 'can' です。")
    st.write(explanation_3)

# 総合的な学習の進捗を表示する
st.sidebar.title("学習の進捗")
st.sidebar.write("このアプリは、簡単な英文法問題を解きながら、学習を進めていく形式です。")
