#! /bin/bash
# download from google drive
# Written by someone else, but I cannot find the source now.

download_from_gdrive() {
    file_id=$1
    file_name=$2

    # first stage to get the warning html
    curl -c /tmp/cookies \
    "https://drive.google.com/uc?export=download&id=$file_id" > \
    /tmp/intermezzo.html

    # second stage to extract the download link from html above
    download_link=$(cat /tmp/intermezzo.html | \
    grep -Po 'uc-download-link" [^>]* href="\K[^"]*' | \
    sed 's/\&amp;/\&/g')
    curl -L -b /tmp/cookies \
    "https://drive.google.com$download_link" > $file_name
}

printf "File ID: "
read ID
printf "Output File Name: "
read out

download_from_gdrive $ID $out
