import os
from PyPDF2 import PdfReader

class PdfUtils:
    @staticmethod
    def read_pdf_resume(file_path):
        with open(file_path, "rb") as file:
            pdf_reader = PdfReader(file)
            resume_text = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                resume_text += page.extract_text()
            return resume_text

    @staticmethod
    def get_pdf_files_in_directory(directory):
        files_in_directory = os.listdir(directory)
        pdf_files = [file for file in files_in_directory if file.endswith(".pdf")]
        return pdf_files
