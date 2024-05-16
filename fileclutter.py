
import os
def func(name):
    ext=os.listdir()
    if name not in ext:
        os.mkdir(name)
ext1=os.listdir()
ext1.remove("fileclutter.py")
func("Images")
func("Docs")
func("Media")
func("PythonFiles")
images=[".jpg",".jpeg",".png"]
imagecheck=[file for file in ext1 if os.path.splitext(file)[1].lower() in images ]
# print(imagecheck)
docs=[".pdf",".doc",".docx",".txt"]
docscheck=[file for file in ext1 if os.path.splitext(file)[1].lower() in docs]
# print(docscheck)
media=[".mp4",".mp3",".mp2"]
mediacheck=[file for file in ext1 if os.path.splitext(file)[1].lower() in media]
# print(mediacheck)

others=[]
for files in ext1:
    ext1 = os.path.splitext(files)[1].lower()
    if (ext1 not in images) and (ext1 not in docs) and (ext1 not in media) and os.path.isfile(files):
        others.append(files)
print(others)
def adding(file,name):
    for files in name:
        os.replace(files,f"{file}/{files}")
adding("Docs",docscheck)
adding("Images",imagecheck)
adding("Media",mediacheck)
adding("PythonFiles",others)



# func("Images")
# func("Docs")
# func("Media")
# func("PythonFiles")