from PyPDF2 import PdfMerger, PdfReader, PdfWriter

def merge_pdfs(file_list, output):
    merger = PdfMerger()
    for pdf in file_list:
        merger.append(pdf)
    merger.write(output)
    merger.close()
    print(f"Merged PDF saved as: {output}")

def remove_page(input_pdf, page_to_remove, output):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    for i, page in enumerate(reader.pages):
        if i != page_to_remove - 1:
            writer.add_page(page)
    with open(output, "wb") as f:
        writer.write(f)
    print(f"Page {page_to_remove} removed → Saved as: {output}")

def add_pdf_page(base_pdf, insert_pdf, position, output):
    reader_base = PdfReader(base_pdf)
    reader_insert = PdfReader(insert_pdf)
    writer = PdfWriter()
    for i, page in enumerate(reader_base.pages):
        if i == position - 1:
            for p in reader_insert.pages:
                writer.add_page(p)
        writer.add_page(page)
    with open(output, "wb") as f:
        writer.write(f)
    print(f"Inserted pages from {insert_pdf} after page {position} → Saved as: {output}")

if __name__ == "__main__":
    print("PDF Editor Options:")
    print("1. Merge PDFs")
    print("2. Remove Page")
    print("3. Add Page")
    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        files = input("Enter PDF filenames separated by space: ").split()
        output = input("Output filename: ")
        merge_pdfs(files, output)
    elif choice == "2":
        inp = input("Enter PDF filename: ")
        page = int(input("Page number to remove: "))
        out = input("Output filename: ")
        remove_page(inp, page, out)
    elif choice == "3":
        base = input("Enter base PDF filename: ")
        insert = input("Enter PDF to insert: ")
        pos = int(input("Insert after page #: "))
        out = input("Output filename: ")
        add_pdf_page(base, insert, pos, out)
    else:
        print("Invalid choice.")
