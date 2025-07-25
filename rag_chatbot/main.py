from retriever_qa import retriever_qa
import gradio as gr

if __name__ == "__main__":
    # Create Gradio interface
    rag_application = gr.Interface(
        fn=retriever_qa,
        allow_flagging="never",
        inputs=[
            # Drag and drop file upload
            gr.File(label="Upload PDF File",
                    file_count="single",
                    file_types=['.pdf'], type="filepath"),
            gr.Textbox(label="Input Query",
                       lines=2,
                       placeholder="Type your question here...")
        ],
        outputs=gr.Textbox(label="Output"),
        title="RAG Chatbot",
        description="""
            Upload a PDF document and ask any question.
            The chatbot will try to answer using the provided document.
        """
    )

    # Launch the app
    rag_application.launch(server_name="0.0.0.0", server_port= 7860)