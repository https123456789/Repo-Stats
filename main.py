import datetime

# Get contents of README.md
#readmeFile = open("README.md", "r")
readmeData = """
# Repo Stats

Stats for each repository owned by [https123456789](<https://github.com/https123456789>)
"""
#readmeFile.read()
#readmeFile.close()

currentDate = datetime.datetime.now()
date = currentDate.strftime("%Y %m %d %I:%M")
readmeData += "# Last Time Run\n" + str(date)

# Write to README.md
readmeFile = open("README.md", "w")
readmeFile.write(str(readmeData))
readmeFile.close()
print(date)
