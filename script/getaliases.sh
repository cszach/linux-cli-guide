#!/bin/bash
# Generate alias definitions in Markdown format.
# Aliases are defined in /data/aliases.
# Copy and paste the output of this program at the
# desired location in CREDITS.md

data_file="../data/aliases"
alias echo=/usr/bin/echo

for line in $(cat $data_file)
do
    echo "[$(echo -n $line | cut -d "|" -f 1)]: $(echo -n $line | cut -d "|" -f 2)"
done
