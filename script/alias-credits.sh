#!/bin/bash
# Replace links in output of mkimgcreds.py with available aliases
# Aliases are defined in /data/aliases

data_file="../data/aliases"
mkcred_script="mkimgcreds.py"
alias wc="/usr/bin/wc"
alias sed="/usr/bin/sed"
alias head="/usr/bin/head"
alias tail="/usr/bin/tail"

pipes=""
i=0
while [[ $i -ne $(wc --lines $data_file | cut -d " " -f 1) ]]
do
    i=$(( $i + 1 ))
    ln=$(head -$i $data_file | tail -1)
    org=$(echo $ln | cut -d "|" -f 2 | sed "s/\//\\\\\//g")
    als=$(echo $ln | cut -d "|" -f 1)
    pipes="$pipes | sed \"s/($org)/[$als]/g\""
done

eval "./$mkcred_script $pipes" | sed "s/$mkcred_script/$(basename $0)/"
