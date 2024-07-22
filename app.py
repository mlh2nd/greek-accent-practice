import streamlit as st
from annotated_text import annotated_text
import GreekAccents as ga

textoptions = {"SBL GNT":"sblgnt.txt"}

sourcetext = textoptions[st.selectbox("Source text:", textoptions.keys())]

col1, col2 = st.columns(2)
with col1:
    practicelength = st.number_input("Number of words to practice per verse:", min_value=1, max_value=5)
with col2:
    attempts = st.number_input("Number of attempts per verse:", min_value=1, max_value=5)

text_data = ga.generate_book_data(sourcetext)
reference, verse, wordlist = ga.choose_verse(text_data, practicelength)
before, after, test, answer = ga.generate_practice_text(wordlist, practicelength)
annotated_text(before, (test, ""), after, f"\n({reference})")

@st.experimental_fragment
def quiz_instance(correct_answer, attempts):
    with st.form("input_form"):
        useranswer = st.text_input("Type the highlighted word with correct accents: ")
        submitted = st.form_submit_button("Check answer")
        if submitted:
            result = ga.check_answer(useranswer, correct_answer)
            st.write(result)

quiz_instance(answer, attempts)


st.button("New Verse")
st.divider()
st.write("The SBLGNT is licensed under a Creative Commons Attribution 4.0 International License.")
st.write("Copyright 2010 by the Society of Biblical Literature and Logos Bible Software.")
st.divider()
st.write("This app is CC0-1.0 (Public domain, no copyright)")