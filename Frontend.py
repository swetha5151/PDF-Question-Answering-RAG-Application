import streamlit as st
from tempfile import NamedTemporaryFile

# Import backend functions
from Backend import generate_answer

def main():
    """
    PDF question-answering using Retrieval-Augmented Generation (RAG).

    This application allows users to upload a PDF document and ask questions 
    related to its content.
    
    Usage:
        - Users should upload a PDF file and type their question in the provided input box.
        - Upon clicking the "Get Answer" button, the application will process the input and display the answer based on the content of the PDF.

    """
    st.title("PDF Question-Answering")
    st.write("Upload a PDF and ask questions related to its content.")

    # File upload widget
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    # Question input
    question = st.text_input("Enter your question")

    # Button to generate an answer
    if st.button("Get Answer"):
        if uploaded_file and question:
            with NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
                temp_pdf.write(uploaded_file.getbuffer())
                temp_pdf_path = temp_pdf.name

            # Generate answer
            answer = generate_answer(temp_pdf_path, question)

            # Display the answer
            st.write("Answer:")
            st.write(answer)
        else:
            st.write("Please upload a PDF file and enter a question.")

if __name__ == "__main__":
    main()
