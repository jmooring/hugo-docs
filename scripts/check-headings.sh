#!/usr/bin/env bash
set -euo pipefail

# If run with no arguments, discover files and re-run this script with the file list
if [ "$#" -eq 0 ]; then
  find content/en/functions content/en/methods -type f -name "*.md" ! -name "_index.md" -print0 | xargs -0 "$0"
  exit $?
fi

errors=0
expected=$'Usage\nExamples'

for file in "$@"; do
  actual=$(grep -E '^## ' "$file" | sed 's/^## *//; s/ *$//' || true)
  if [ "$actual" != "$expected" ]; then
    echo "::error file=$file::Invalid headings. Expected ## Usage followed by ## Examples."
    errors=$((errors + 1))
  fi
done

[ "$errors" -eq 0 ]
