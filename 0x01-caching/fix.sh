#!/usr/bin/env bash
for file in *.py
do 
    vi +':w ++ff=unix' +':q' "$file"
done
