import streamlit as st
import sqlite3

# Function to create SQLite database and table
def create_table():
    conn = sqlite3.connect('qa_database.sqlite')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS questions_answers
                 (question TEXT PRIMARY KEY, answer TEXT)''')
    conn.commit()
    conn.close()

# Function to insert question and answer into SQLite database
# def insert_question_answer(question, answer):
#     conn = sqlite3.connect('qa_database.db')
#     c = conn.cursor()
#     c.execute('''INSERT OR REPLACE INTO questions_answers (question, answer)
#                  VALUES (?, ?)''', (question, answer))
#     conn.commit()
#     conn.close()

# Function to get all questions from SQLite database
def get_questions():
    conn = sqlite3.connect('qa_database.sqlite')
    c = conn.cursor()
    c.execute('''SELECT question FROM questions_answers''')
    result = c.fetchall()
    conn.close()
    return [row[0] for row in result]

# Function to get answer from SQLite database based on question
def get_answer(question):
    conn = sqlite3.connect('qa_database.sqlite')
    c = conn.cursor()
    c.execute('''SELECT answer FROM questions_answers WHERE question = ?''', (question,))
    result = c.fetchone()
    conn.close()
    if result:
        return result[0]
    else:
        return "Sorry, I don't have an answer to that question."

# Custom CSS for textured theme
custom_css = """
<style>
body {
    background-color: #f0f0f0;
}

.stTextInput > div > div > div > input {
    background-color: #ffffff;
    border-radius: 25px;
}

.stTextInput > div > div > div > input:focus {
    border-color: #3366ff;
    box-shadow: 0 0 0 0.2rem rgba(51, 102, 255, 0.25);
}

.stButton>button {
    background-color: #3366ff;
    color: #ffffff;
    border-radius: 25px;
}

.stButton>button:hover {
    background-color: #254eda;
}

.stTextArea>div>textarea {
    background-color: #ffffff;
    border-radius: 15px;
}

.stTextArea>div>textarea:focus {
    border-color: #3366ff;
    box-shadow: 0 0 0 0.2rem rgba(51, 102, 255, 0.25);
}

.stText>div>span {
    color: #333333;
}
</style>
"""

# Streamlit app
def main():
    st.title('Attendance Chatbot !!!!')
    st.markdown(custom_css, unsafe_allow_html=True)

    # Create table if it doesn't exist
    create_table()

    # Get all questions
    all_questions = get_questions()

    # Dynamic search box
    # user_input = st.text_input('You: ', '')
    related_questions = [q for q in all_questions]
    
    # if user_input.lower() in q.lower()]
    
    selected_question = st.selectbox("you:", related_questions)

    # Display answer
    if st.button('Ask') and selected_question:
        response = get_answer(selected_question)
        st.text_area('Bot:', response, height=150)

if __name__ == "__main__":
    main()
