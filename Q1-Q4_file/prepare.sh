#!/bin/bash
python generate_dirty_data.py
#remove comment empty,extra commas
sed '/^#/d' ms_data_dirty.csv | sed '/^$/d' | sed 's/,,*/,/g' > cleaned_data.csv

#Extract columns
cut -d ',' -f 1,2,4,5,6 cleaned_data.csv > filtered_data.csv

#Filter rows
awk -F ',' 'NR==1 || ($5 >= 2.0 && $5 <= 8.0)' OFS=',' filtered_data.csv > ms_data.csv
rm cleaned_data.csv filtered_data.csv
#Create insurance file
echo -e "insurance_type\nBronze\nSilver\nGold\nPlatinum" > insurance.lst

# Summarize
echo "Summary for Question 1" > readme.md
tail -n +2 ms_data.csv | wc -l >> readme.md
head -n 10 ms_data.csv >> readme.md

