import streamlit as st

# セッション状態の初期化
if 'question_number' not in st.session_state:
    st.session_state.question_number = 1
    st.session_state.score = 0
    st.session_state.selected_answer = None  # 解答選択をリセット

# 問題1: 現在形と過去形の選択肢問題あ
def question_1():
    st.subheader("問題 1: 次の文を正しく完成させてください。")
    question = "I ___ (eat) lunch at 12:00 every day."
    options = ["eat", "eats", "ate", "eating"]
    correct_answer = "eat"
    explanation = (
        "現在形を使うべきです。'every day' のように、習慣や普段の行動を表すときは "
        "現在形の動詞を使います。'eat' が正しいです。"
    )
    
    # 解答選択
    user_answer = st.radio(question, options, key="q1")
    
    # 決定ボタン
    if st.button("決定", key="q1_button"):
        if user_answer:
            st.session_state.selected_answer = user_answer  # 解答をセッションに保存
            if user_answer == correct_answer:
                st.session_state.score += 1
                st.success("正解です！")
            else:
                st.error(f"間違いです。正しい答えは '{correct_answer}' です。")
            st.write(explanation)
            # 次の問題へ進むボタンを表示
            if st.button("次の問題へ"):
                st.session_state.question_number += 1

# 問題2: 一般動詞の使い方
def question_2():
    st.subheader("問題 2: 次の文を正しく完成させてください。")
    question = "She ___ (go) to school every day."
    options = ["go", "goes", "gone", "going"]
    correct_answer = "goes"
    explanation = (
        "'She' のように三人称単数の主語がある場合、動詞に 's' をつける必要があります。"
        "したがって、'goes' が正解です。"
    )
    
    # 解答選択
    user_answer = st.radio(question, options, key="q2")
    
    # 決定ボタン
    if st.button("決定", key="q2_button"):
        if user_answer:
            st.session_state.selected_answer = user_answer  # 解答をセッションに保存
            if user_answer == correct_answer:
                st.session_state.score += 1
                st.success("正解です！")
            else:
                st.error(f"間違いです。正しい答えは '{correct_answer}' です。")
            st.write(explanation)
            # 次の問題へ進むボタンを表示
            if st.button("次の問題へ"):
                st.session_state.question_number += 1

# 問題3: 助動詞の使い方
def question_3():
    st.subheader("問題 3: 次の文を正しく完成させてください。")
    question = "You ___ (can) swim very fast."
    options = ["can", "could", "be", "will"]
    correct_answer = "can"
    explanation = (
        "'can' は能力を表す助動詞です。'You can swim very fast.' は「あなたはとても速く泳げる」という意味です。"
        "他の選択肢（'could', 'be', 'will'）は文の意味に合いません。"
    )
    
    # 解答選択
    user_answer = st.radio(question, options, key="q3")
    
    # 決定ボタン
    if st.button("決定", key="q3_button"):
        if user_answer:
            st.session_state.selected_answer = user_answer  # 解答をセッションに保存
            if user_answer == correct_answer:
                st.session_state.score += 1
                st.success("正解です！")
            else:
                st.error(f"間違いです。正しい答えは '{correct_answer}' です。")
            st.write(explanation)
            # 結果表示ボタン
            if st.button("結果を見る"):
                st.session_state.question_number += 1

# 問題の表示
if st.session_state.question_number == 1:
    question_1()
elif st.session_state.question_number == 2:
    question_2()
elif st.session_state.question_number == 3:
    question_3()

# 結果の表示
if st.session_state.question_number > 3:
    st.subheader("お疲れ様でした！")
    st.write(f"最終得点: {st.session_state.score} / 3")
    if st.button("再挑戦"):
        st.session_state.question_number = 1
        st.session_state.score = 0
