import sys, os, datetime, requests, json

readmeData = """
# Repo Stats

Stats for each repository owned by [https123456789](<https://github.com/https123456789>).

![test.svg](<https://github.com/https123456789/Repo-Stats/raw/main/test.svg>)
"""

currentDate = datetime.datetime.now()
date = currentDate.strftime("%m-%d-%Y %I:%M")
readmeData += "# Last Time Run\n" + str(date)

# Get all repo names

repos = []
repoNames = []

r1 = requests.get("https://api.github.com/users/https123456789/repos")
r1.raise_for_status()
reposFile = open("repos.json", "wb")
#json.dump(r1.json, reposFile, indent=4)
reposFile.write(r1.content)
reposFile.close()
reposFile = open("repos.json", "r")
data = json.load(reposFile)
reposFile.close()

repos = data
for repo in repos:
	print(repo["full_name"])
	repoNames.append(repo["full_name"])

print(os.system("pwd"))

for repo in repoNames:
	dirName = "docs/" + repo.replace("https123456789/", "")
	os.makedirs(dirName, exist_ok=True)
	os.system("python generate.py " + repo.replace("https123456789/", ""))

#os.system("python generate.py " + sys.argv[1])

# Write to README.md
readmeFile = open("README.md", "w")
readmeFile.write(str(readmeData))
readmeFile.close()
print(date)
