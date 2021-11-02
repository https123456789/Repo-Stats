import datetime

currentDate = datetime.datetime.now()

readmeFile = open("README.md", "w")
readmeFile.write(str(currentDate))
readmeFile.close()
print(currentDate)
