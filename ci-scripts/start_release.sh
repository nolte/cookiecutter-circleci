#!/bin/sh
export currentVersion=$(bumpversion --allow-dirty --dry-run --list release | grep new_version | sed -r s,"^.*=",,)

echo "Starting Release"
bumpversion --commit release
echo "Create Release Branch"
git checkout -b release/v$currentVersion-pre
echo "Update to next development version"
git checkout develop
bumpversion --commit minor
git push origin release/v$currentVersion-pre
