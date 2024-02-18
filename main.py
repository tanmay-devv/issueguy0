#!/usr/bin/env python3

from github import Github  

resultno = int(input("Enter the number of Results To Fetch:  "))

# Replace 'YOUR_PERSONAL_ACCESS_TOKEN' with your actual personal access token
g = Github("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")

query = "is:issue is:open"
issues = g.search_issues(query)
for issue in issues:
    print(issue.title)
    print(issue.labels)
    print(issue.html_url)
    print()
    
    resultno -= 1
    if resultno == 0:
        break

