#!/bin/bash

python3 lexer.py test1.java
mv output.csv test1.csv

python3 lexer.py test2.java
mv output.csv test2.csv

python3 lexer.py test3.java
mv output.csv test3.csv

python3 lexer.py test4.java
mv output.csv test4.csv
