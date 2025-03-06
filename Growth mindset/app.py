import streamlit as st

st.title("🌱 Growth Mindset App")

st.write("""
Welcome to the Growth Mindset App! Here, you can learn about the power of a growth mindset and track your progress.
""")

# User input for goals
goal = st.text_input("What is your learning goal for today?")
if st.button("Submit"):
    st.success(f"Great! You're working on: {goal}. Keep going!")

# Display a motivational quote
st.header("💡 Motivational Quote")
st.write("""
"The only limit to our realization of tomorrow is our doubts of today." – Franklin D. Roosevelt
""")

# Progress tracker
st.header("📊 Progress Tracker")
progress = st.slider("How much progress have you made today?", 0, 100)
st.write(f"You've completed {progress}% of your goal. Keep pushing!")