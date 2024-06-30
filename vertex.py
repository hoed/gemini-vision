import streamlit as st
from vertexai.preview.generative_models import GenerativeModel, Image # importing GenerativeModel and Image Classes
import vertexai # Importing Vertex AI SDK
import tempfile # for creating temporary files and directories
import os # for interacting with operating system


PROJECT_ID = "YOUR GOOGLE CLOUD PROJECT" # Your Vertex AI project ID
REGION = "us-central1" # Region where your Vertex AI resource are located

#initialize Vertex AI SDK
vertexai.init(project=PROJECT_ID, location=REGION)

def generate_response(prompt, image_file):
    """
    Function to generate response based on a prompt and image.

    Parameters:
    - prompt: The Text Prompt for generating the response.
    - image_file: The Image file to be used in generating the response.

    Returns:
    - The generated response.
    """

    # Load the image from file
    image = image.load_from_file(image_file)

    # Initialize the generative model with specific model
    generative_multimodal_model = GenerativeModel("gemini-1.0-pro-vision")

    # Generate content based on the prompt and image
    response = generative_multimodal_model.generate_content([prompt, image])

    # Return the generated response
    return response.candidates(0).content.text


def main():

    """
    Main function for running the streamlit web application
    """
    # Set the title and logo
    st.title("Vertex AI")
    st.image("https://1000logos.net/wp-content/uploads/2024/02/Gemini-Logo.png", width=100)

    # Allow users to upload an image
    img = st.file_uploader("Upload an image")

    # If an image is uploaded
    if img:
        # Create a temporary directory
        temp_dir = tempfile.mkdtemp()
        #Define a path to save the uploaded image
        path = os.path.join(temp_dir, img.name)
        # Write the uploaded image to the specified path
        with open(path, "wb") as f:
            f.write(img.getvalue())
    
    # Input area for user's question
    st.header(":violet[Question]")
    question = st.text_area(label="Enter your question")
    submit = st.button("Submit")

    # If question is entered and submitted
    if question and submit:
        # Generate a response based on the question and uploaded image
        response = generate_response(question, path)
        # Display the generated response
        st.header("Answer")
        st.write(response)

# Entry point of the script
if __name__ == "__main__":
    main()
