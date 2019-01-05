#!/bin/sh
export currentVersion=$(bumpversion --allow-dirty --dry-run --list release | grep new_version | sed -r s,"^.*=",,)
echo "Starting Release"
git checkout -b release/v$currentVersion-pre
git checkout develop
git commit --allow-empty -m "[GradeUP] grade up the branch"
git push origin
