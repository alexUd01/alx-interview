#!/usr/bin/env bash
# Initialize project repository

echo "# alx-interview" >> README.md
git init
git add README.md
git commit -m "project initialization"
git branch -M master
git remote add origin git@github.com:alexUd01/alx-interview.git
git push -u origin master
