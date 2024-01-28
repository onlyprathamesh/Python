from pypdf import PdfReader


reader = PdfReader("E:\Persnol Information\Income Tax Return\FY22-23, AY 23-24\Dad\Statement_XXXXXXXXXXX9999_20Jul2023_22_39.pdf")

if reader.is_encrypted:
    reader.decrypt("PRAK0207")

page = reader.pages[2]
str = " "
str += page.extract_text()



with open("text.text", "w") as f:
    f.write(str)