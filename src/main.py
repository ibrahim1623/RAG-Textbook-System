import textract

# Load the PDF document
text = textract.process("./inputs/macbeth_PDF_FolgerShakespeare.pdf")

# Write the extracted text to a .txt file
with open("./outputs/stat305_course_pack.txt", 'wb') as file:  # Use 'wb' for binary writing
    file.write(text)
