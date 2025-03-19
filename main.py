import streamlit as st

def main():
    st.title("Fun Mad Libs Game!")
    st.write("Fill in the blanks to create your own hilarious story!")

    # Get inputs from user
    noun1 = st.text_input("Enter a noun:")
    adjective1 = st.text_input("Enter an adjective:")
    verb1 = st.text_input("Enter a verb (present tense):")
    adverb1 = st.text_input("Enter an adverb:")
    noun2 = st.text_input("Enter another noun:")
    adjective2 = st.text_input("Enter another adjective:")
    

    if st.button("Generate Story!"):
        if noun1 and adjective1 and verb1 and adverb1 and noun2 and adjective2:
            
            story = f"""
            Once upon a time, there was a {adjective1} {noun1} who loved to {verb1} {adverb1}.
            One day, while {verb1}ing, they found a {adjective2} {noun2}!
            It was the most extraordinary day of their life.
            """
            
            st.success("Your Mad Libs Story:")
            st.write(story)
            

            print("Story generated:")
            print(story)
        else:
            st.error("Please fill in all the blanks!")

if __name__ == "__main__":
    main()