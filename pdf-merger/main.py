import PyPDF2 as pd

pdFiles = ["1.pdf", "2.pdf", "sample.pdf"]
merger = pd.PdfMerger()

for file in pdFiles:
    pdFile = open(file, "rb")
    pdfReader = pd.PdfReader(pdFile)
    merger.append(pdfReader)

pdFile.close()
merger.write('merger.pdf')