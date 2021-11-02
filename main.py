import datetime

readmeData = """
# Repo Stats

Stats for each repository owned by [https123456789](<https://github.com/https123456789>).

![test.svg](<test.svg>)
"""

currentDate = datetime.datetime.now()
date = currentDate.strftime("%m-%d-%Y %I:%M")
readmeData += "# Last Time Run\n" + str(date)

# Create SVG Image

img = {
  "header": '<svg xmlns="http://www.w3.org/2000/svg" width="100px" height="100px">',
  "content": '<rect x="0" y="0" width="10px" height="10px"></rect>',
  "footer": '</svg>'
}

imgFile = open("test.svg", "w")
imgFile.write(img["header"])
imgFile.write(img["content"])
imgFile.write(img["footer"])

# Write to README.md
readmeFile = open("README.md", "w")
readmeFile.write(str(readmeData))
readmeFile.close()
print(date)
