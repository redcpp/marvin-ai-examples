# **Resume Analyzer**

Resume Analyzer is a powerful AI-driven tool that helps you analyze and score resumes for specific job positions using the @AskMarvinAI bot and @OpenAI ChatGPT. Automate the resume screening process and focus on the top candidates, saving time and energy!

## **Features**

- Analyze resumes in PDF format
- Extract relevant information from resumes
- Assign scores to resumes based on a specific job position
- Rank resumes by score
- Read job positions from JSON files

## **Getting Started**

### **Prerequisites**

Make sure you have Python 3.9 and the following libraries installed:

- marvin
- PyPDF2

You can install them with the following command:

```bash
pip install marvin PyPDF2
```

### **Usage**

1. Clone the repository:

```bash
git clone https://github.com/redcpp/marvin-ai-examples.git
```

2. Move to the project directory:

```bash
cd marvin-ai-examples/ResumeAnalyzer/
```

3. Add your resumes in PDF format to the **`resumes`** folder.
4. Create or modify the JSON file for the job position in the **`job_positions`** folder.
5. Run the **`main.py`** file:

```
python main.py
```

The Resume Analyzer will process the resumes and display the ranked list of candidates based on their scores.

## Known Issues

- Large PDF files could cause a too many tokens exception.

## **Contributing**

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## **License**

**[MIT](https://choosealicense.com/licenses/mit/)**

## **Acknowledgments**

- Special thanks to @AskMarvinAI and @OpenAI for their amazing AI-powered tools.