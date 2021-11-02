import sys, os

import datetime

readmeData = """
# Repo Stats

Stats for each repository owned by [https123456789](<https://github.com/https123456789>).

![test.svg](<https://github.com/https123456789/Repo-Stats/raw/main/test.svg>)
"""

currentDate = datetime.datetime.now()
date = currentDate.strftime("%m-%d-%Y %I:%M")
readmeData += "# Last Time Run\n" + str(date)

os.system("python generate.py " + sys.argv[1])

# Write to README.md
readmeFile = open("README.md", "w")
readmeFile.write(str(readmeData))
readmeFile.close()
print(date)
