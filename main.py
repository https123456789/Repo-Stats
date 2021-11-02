import datetime
import svgwrite

readmeData = """
# Repo Stats

Stats for each repository owned by [https123456789](<https://github.com/https123456789>)
"""
#readmeFile.read()
#readmeFile.close()

currentDate = datetime.datetime.now()
date = currentDate.strftime("%m-%d-%Y %I:%M")
readmeData += "# Last Time Run\n" + str(date)

drawing = svgwrite.Drawing('test.svg', profile='tiny')
drawing.add(drawing.line((0, 0), (10, 10), stroke=svgwrite.rgb(10, 10, 16, "%"))
drawing.save()

# Write to README.md
readmeFile = open("README.md", "w")
readmeFile.write(str(readmeData))
readmeFile.close()
print(date)
