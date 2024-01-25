#!/bin/bash

# Check if the file exists
if [ ! -f "words.txt" ]; then
  echo "File words.txt not found."
  exit 1
fi

# Read the file and calculate word frequencies
while read -r line; do
  # Remove punctuation and convert to lowercase
#   cleaned_line=$(echo "$line" | tr -d '[:punct:]' | tr '[:upper:]' '[:lower:]')
  cleaned_line=$(echo "$line")
  
  # Tokenize the line into words
  words=($cleaned_line)
  
  # Count the frequency of each word
  for word in "${words[@]}"; do
    ((word_frequency["$word"]++))
  done
done < words.txt

# Print the word frequencies
echo "Word Frequencies:"
for word in "${!word_frequency[@]}"; do
  echo "$word: ${word_frequency[$word]}"
done