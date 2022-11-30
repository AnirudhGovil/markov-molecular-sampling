import requests
import streamlit as st
from PIL import Image
import os
import subprocess
import sys

def save_uploaded_file(uploadedfile):
  with open(os.path.join("MARS/data",uploadedfile.name),"wb") as f:
     f.write(uploadedfile.getbuffer())

st.title("MARS")

image = Image.open('Schema.png')
st.image(image, caption='What the Code is doing')

st.header('Preprocessing')

st.text("Upload the Vocabulary File from which the fragments will be generated")
# Upload the Vocabulary txt file
uploaded_file = st.file_uploader("Choose a file", type="txt")

# Button for preprocessing
if st.button("Preprocess"):
    if uploaded_file is not None:
        save_uploaded_file(uploaded_file)
        st.write("File Uploaded")
        # Pre-processing the Vocabulary
        with st.spinner('Pre-processing the Vocabulary'):
            subprocess.call(["python", "-m", "MARS.datasets.prepro_vocab"])
        st.success('Pre-processing the Vocabulary Completed',icon="✅")

st.header('Sampling')

# Sample the Fragments and generate the molecules
st.text("Sample the Fragments and generate the molecules")

# Drop down to select the number of molecules to be generated
num_molecules = st.selectbox("Number of Molecules", [i for i in range(10, 210, 10)])

# Drop down to select the number of iterations per epoch
num_iterations = st.selectbox("Number of Iterations per Epoch", [i for i in range(5, 55, 5)])

# Drop down to select the number of epochs
num_epochs = st.selectbox("Number of Epochs", [i for i in range(2, 11)])

# Button to generate the molecules
if st.button('Generate Molecules'):
    with st.spinner('Generating Molecules'):
        # delete the previous generated molecules
        subprocess.call(["python", "-m", "MARS.main", "--train", "--run_dir", "runs/RUN_DIR", "--num_mols", str(num_molecules), "--num_step", str(num_iterations), "--num_runs", str(num_epochs)])
    st.success('Molecules Generated',icon="✅")



