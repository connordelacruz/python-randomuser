#!/usr/bin/env bash
# Update gh-pages branch using docs/build/html/

git subtree push --prefix docs/build/html origin gh-pages
