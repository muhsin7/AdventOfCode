#!/bin/bash

# alias newaoc='source ~/AdventOfCode/newday.sh'
# chmod +x ~/AdventOfCode/newday.sh
# (adjust paths as needed)
# 
# usage with above alias:
# 	newaoc		      -> creates next day in 2024 (current default)
#	newaoc -d 2           -> creates day 2 in 2024 folder
#	newaoc -d 2 -y 2025   -> creates day 2 in 2025 folder

# Use $0 for filename, not positional arguments in sourced mode
if [[ "${BASH_SOURCE[0]}" != "$0" ]]; then
    ARGS=("$@")
else
    ARGS=("$@")
fi

# Default values
YEAR=2024
DAY=""

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    -y) YEAR=$2; shift 2 ;;
    -d) DAY=$2; shift 2 ;;
    *) echo "Usage: $0 [-y year] [-d day]" >&2; return 1 ;;
  esac
done

# Create the year directory if it doesn't exist
if [ ! -d "$YEAR" ]; then
  echo "Creating directory for year $YEAR..."
  mkdir -p "$YEAR"
fi

# Determine the day directory
if [ -z "$DAY" ]; then
  # Get the number of existing directories and set DAY as N+1
  N=$(ls -l "$YEAR" | grep -c '^d')
  DAY=$((N + 1))
  echo "No day specified. Using default day: $DAY"
else
  echo "Using specified day: $DAY"
fi

DAY_DIR="./$YEAR/day$DAY"

# Check if the day directory exists
if [ -d "$DAY_DIR" ]; then
  echo "Directory $DAY_DIR already exists. Changing to it..."
else
  echo "Creating directory $DAY_DIR..."
  mkdir -p "$DAY_DIR"
  echo "Copying template.py into $DAY_DIR..."
  cp ./template.py "$DAY_DIR/day$DAY.py" 2>/dev/null || echo "No template.py found to copy."
  echo "Creating input.txt in $DAY_DIR..."
  touch "$DAY_DIR/input.txt"
fi

# Change to the day directory
if cd "$DAY_DIR"; then
  echo "Successfully changed directory to $DAY_DIR"
  echo "Current working directory: $(pwd)"
else
  echo "Failed to change directory to $DAY_DIR"
  exit 1
fi
