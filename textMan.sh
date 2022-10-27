#!/bin/bash

EMAIL_REGEX='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$'
DIGIT_REGEX='^[0-9]+$'
RECORDS=`cat file.txt`
IFS=$'\n'
for record in $RECORDS;
do
    email=`echo $record | cut -d " " -f 2`
    id=`echo $record | grep -o '[^ ]*$'`
    if [[ "$email" =~ $EMAIL_REGEX ]]
    then
        if [[ "$id" =~ $DIGIT_REGEX ]]
        then
            if [[ $(( id % 2 )) -eq 0 ]]
            then
                echo "the id $id of the email $email is an even number."
            else
                echo "the id $id of the email $email is an odd number."
            fi
        fi
    fi
done
