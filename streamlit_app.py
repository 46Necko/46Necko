import streamlit as st

# セッション状態の初期化
if 'question_number' not in st.session_state:
    st.session_state.question_number = 1
    st.session_state.score = 0
    st.session_state.selected_answer = None  # 解答選択をリセット

# 問題の定義
questions = [
    {
        "question": "I ___ (eat) lunch at 12:00 every day.",
        "options": ["eat", "eats", "ate", "eating"],
        "correct_answer": "eat",
        "explanation": (
            "現在形を使うべきです。'every day' のように、習慣や普段の行動を表すときは "
            "現在形の動詞を使います。'eat' が正しいです。"
        )
    },
    {
        "question": "She ___ (go) to school every day.",
        "options": ["go", "goes", "gone", "going"],
        "correct_answer": "goes",
        "explanation": (
            "'She' のように三人称単数の主語がある場合、動詞に 's' をつける必要があります。"
            "したがって、'goes' が正解です。"
        )
    },
    {
        "question": "You ___ (can) swim very fast.",
        "options": ["can", "could", "be", "will"],
        "correct_answer": "can",
        "explanation": (
            "'can' は能力を表す助動詞です。'You can swim very fast.' は「あなたはとても速く泳げる」という意味です。"
            "他の選択肢（'could', 'be', 'will'）は文の意味に合いません。"
        )
    },
    {
        "question": "I ___ (watch) TV every evening.",
        "options": ["watch", "watches", "watched", "watching"],
        "correct_answer": "watch",
        "explanation": (
            "現在形を使うべきです。'every evening' のように繰り返しの動作を表すときは "
            "現在形の動詞を使います。'watch' が正しいです。"
        )
    },
    {
        "question": "She ___ (study) English at school.",
        "options": ["study", "studies", "studied", "studying"],
        "correct_answer": "studies",
        "explanation": (
            "'She' のように三人称単数の主語がある場合、動詞に 's' をつける必要があります。"
            "したがって、'studies' が正解です。"
        )
    }
]

# 現在の問題を表示
def display_question(question_data):
    st.subheader(f"問題 {st.session_state.question_number}: 次の文を正しく完成させてください。")
    st.write(question_data["question"])
    user_answer = st.radio("選択肢", question_data["options"], key=f"q{st.session_state.question_number}")
    
    # 決定ボタン
    if st.button("決定", key=f"q{st.session_state.question_number}_button"):
        if user_answer:
            st.session_state.selected_answer = user_answer  # 解答をセッションに保存
            if user_answer == question_data["correct_answer"]:
                st.session_state.score += 1
                st.success("正解です！")
            else:
                st.error(f"間違いです。正しい答えは '{question_data['correct_answer']}' です。")
            st.write(question_data["explanation"])
            
            # 次の問題へ進むボタンを表示
            if st.button("次の問題へ"):
                st.session_state.question_number += 1

# 問題の表示
if st.session_state.question_number <= len(questions):
    display_question(questions[st.session_state.question_number - 1])
else:
    st.subheader("お疲れ様でした！")
    st.write(f"最終得点: {st.session_state.score} / {len(questions)}")
    if st.button("再挑戦"):
        st.session_state.question_number = 1
        st.session_state.score = 0
