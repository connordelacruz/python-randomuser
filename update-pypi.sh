#!/usr/bin/env bash
# Update PyPI package
python setup.py sdist
twine upload dist/*
rm dist/*

