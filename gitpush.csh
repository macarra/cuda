#!/bin/env csh

set message = $1

git add --all
git commit -m \$message
git push

