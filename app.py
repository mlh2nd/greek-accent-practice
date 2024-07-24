import streamlit as st
from annotated_text import annotated_text
import GreekAccents as ga

st.title("Polytonic Greek Accent Practice")

textoptions = {"SBL GNT":"sblgnt.txt"}

col1, col2 = st.columns(2)
with col1:
    sourcetext = textoptions[st.selectbox("Source text:", textoptions.keys())]
with col2:
    practicelength = st.number_input("Number of words to practice per verse:", min_value=1, max_value=5)

text_data = ga.generate_book_data(sourcetext)
reference, verse, wordlist = ga.choose_verse(text_data, practicelength)
before, after, test, answer = ga.generate_practice_text(wordlist, practicelength)
annotated_text(before, (test, "", "#ffa"), after, f"\n({reference})")

@st.experimental_fragment
def quiz_instance(correct_answer):
    useranswer = st.text_input("Add the correct accents: ", value=test)
    st.write("(Note: On mobile devices you may need to press Enter on the keyboard before pressing the \"Check answer\" button)")
    submitted = st.button("Check answer")
    if submitted:
        correct = ga.check_answer(useranswer, correct_answer)
        if correct:
            annotated_text(("Ὀρθῶς ἀπεκρίθης!","", "#afa"))
        else:
            annotated_text((f"Try again!", "", "#faa"))
    with st.expander("Show answer"):
        st.write(f"Correct answer: {correct_answer}")

quiz_instance(answer)


st.button("New verse")
with st.expander("Review accent rules"):
    st.write("Accent rule review to be added later")
st.divider()

with st.expander("Copyright notices"):
    st.write("The SBLGNT is licensed under a Creative Commons Attribution 4.0 International License.")
    st.write("Copyright 2010 by the Society of Biblical Literature and Logos Bible Software.")
    st.divider()
    st.write("This web app is CC0-1.0 (Public domain, no copyright)")