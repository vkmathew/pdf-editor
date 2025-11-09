# 🧩 Simple PDF Editor (Python)

A lightweight command-line tool to **merge, remove, or add pages** to PDF files using Python.  
Built using [PyPDF2](https://pypi.org/project/PyPDF2/), this project provides a simple way to perform common PDF editing tasks directly from the terminal — no GUI or web app required.

---


[![Live Demo in Google Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vkmathew/pdf-editor/blob/main/pdf_editor_demo.ipynb)

---

## 🚀 Features
- 🧠 **Merge PDFs** — Combine multiple PDF files into one.
- ✂️ **Remove Page** — Delete a specific page from a PDF.
- ➕ **Add Page(s)** — Insert pages from another PDF at any position.
- 💡 **No Internet Required** — Works completely offline.
- 🪶 **Minimal Dependencies** — Uses only one Python library.

---

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/pdf-editor.git
   cd pdf-editor
2. Install the required dependency:
    pip install PyPDF2

📘 Usage

Run the script:
python pdf_editor.py

You’ll be presented with a simple menu:
PDF Editor Options:
1. Merge PDFs
2. Remove Page
3. Add Page
Choose an option (1/2/3):

🧠 Examples
1. Merge PDFs
Choose an option (1/2/3): 1
Enter PDF filenames separated by space: file1.pdf file2.pdf
Output filename: merged.pdf

2. Remove a Page
Choose an option (1/2/3): 2
Enter PDF filename: document.pdf
Page number to remove: 3
Output filename: trimmed.pdf

3. Add a Page
Choose an option (1/2/3): 3
Enter base PDF filename: base.pdf
Enter PDF to insert: insert.pdf
Insert after page #: 2
Output filename: combined.pdf

