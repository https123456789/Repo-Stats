import sys

repoName = sys.argv[1]

import datetime

# Create SVG Image

img = {
  "header": '<svg xmlns="http://www.w3.org/2000/svg" width="400px" height="200px">\n',
  "content": '<rect x="0" y="0" width="100%" height="100%" rx="15" fill="rgb(200, 200, 200)"></rect>\n',
  "footer": '</svg>'
}

# Add body of image
img["content"] += '<rect x="5%" y="10%" width="90%" height="80%" rx="15" fill="rgb(255, 255, 255)"></rect>\n'
# Add title
img["content"] += '<text x="10%" y="20%" height="5%" width="80%">' + repoName + ' Stats</text>'
# Add line under title
img["content"] += '<line x1="10%" y1="21%" x2="90%" y2="21%" stroke="black"></line>'

# Main Content

# Add Total Commits
img["content"] += '<text x="10%" y="30%">Total Commits:</text><text x="70%" y="30%">18203912</text>'

imgFile = open("docs/" + repoName + "/main.svg", "w")
imgFile.write(img["header"])
imgFile.write(img["content"])
imgFile.write(img["footer"])
imgFile.close()
