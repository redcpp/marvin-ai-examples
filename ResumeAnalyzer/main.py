import os
import json
from pdf_utils import PdfUtils
from resume_analyzer import ResumeAnalyzer

async def main():
    with open("job_position.json", "r") as file:
        job_position = json.load(file)
    directory_path = "./resumes"
    pdf_files = PdfUtils.get_pdf_files_in_directory(directory_path)
    resumes = [PdfUtils.read_pdf_resume(os.path.join(directory_path, pdf_file)) for pdf_file in pdf_files]
    analyzer = ResumeAnalyzer()
    resumes_scores = await analyzer.analyze_resumes(job_position['description'], resumes)
    print("Resumes scores:", resumes_scores)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
