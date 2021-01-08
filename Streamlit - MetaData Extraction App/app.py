import streamlit as st 
import streamlit.components.v1 as stc 

# EDA Pkgs
import pandas as pd
import numpy as np

# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib 
matplotlib.use('Agg')

# Opening Files/Forensic MetaData Extraction
# For Images
from PIL import Image
import exifread
# For Audio
import mutagen

# For PDF
from PyPDF2 import PdfFileReader

# HTML 
metadata_wiki = """
Metadata is defined as the data providing information about one or more aspects of the data; it is used to summarize basic information about data which can make tracking and working with specific data easier
"""

HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px">
    <h1 style="color:white;text-align:center;">MetaData Extractor App </h1>
    </div>
    """


# App Structure
def main():
	"""Meta Data Extraction App"""
	st.title("MetaData Extraction App")
	stc.html(HTML_BANNER)


	menu = ["Home","Image","Audio","DocumentFiles","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == 'Home':
		st.subheader("Home")
		st.write(metadata_wiki)

	elif choice == "Image":
		st.subheader("Image MetaData Extraction")

	elif choice == "Audio":
		st.subheader("Audio MetaData Extraction")

	elif choice == "DocumentFiles":
		st.subheader("DocumentFiles MetaData Extraction")	

	elif choice == "About":
		st.subheader("MetaData Extraction App")
		


					

if __name__ == '__main__':
	main()