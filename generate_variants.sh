#!/bin/bash

rm output
touch output

for i in $(seq 0 56); do
    python modulos.py >> output
    if [ "$(expr $i % 6)" -eq 5 ]
    then
        echo -e "\f" >> output
    fi
done
