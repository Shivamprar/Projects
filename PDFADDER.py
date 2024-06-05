import PyPDF2
print(dir(PyPDF2))
addinfiles=PyPDF2.PdfMerger()
listvalue=["Directdepositpayroll.pdf","licenceandSIn.pdf","Shivam_AroraCPR!.pdf","Shivam_AroraCPR2.pdf","SmartServeOntario_Certificate_4451411.pdf","Workpermit.pdf"]
newvalue="Importantdocument.pdf"
files=[file for file in listvalue if file.endswith(".pdf")]
for pdfs in files:
    with open(pdfs,"rb") as file:
        pdfread=PyPDF2.PdfReader(file)
        addinfiles.append(pdfread)
    # print(pdfread)
addinfiles.write(newvalue)
addinfiles.close()