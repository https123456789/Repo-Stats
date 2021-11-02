import datetime

readmeData = """
# Repo Stats

Stats for each repository owned by [https123456789](<https://github.com/https123456789>).

![test.svg](<https://github.com/https123456789/Repo-Stats/raw/main/test.svg>)
"""

currentDate = datetime.datetime.now()
date = currentDate.strftime("%m-%d-%Y %I:%M")
readmeData += "# Last Time Run\n" + str(date)

# Create SVG Image

img = {
  "header": '<svg xmlns="http://www.w3.org/2000/svg" width="200px" height="100px">\n',
  "content": '<rect x="0" y="0" width="100%" height="100%" rx="15" fill="rgb(255, 255, 255)"></rect>\n',
  "footer": '</svg>'
}

img["content"] += '<rect x="10%" y="10%" width="80%" height="80%" fill="rgb(0, 0, 0)"></rect>\n'

imgFile = open("test.svg", "w")
imgFile.write(img["header"])
imgFile.write(img["content"])
imgFile.write(img["footer"])
imgFile.close()

# Write to README.md
readmeFile = open("README.md", "w")
readmeFile.write(str(readmeData))
readmeFile.close()
print(date)
