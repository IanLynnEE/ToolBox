#!/bin/zsh
# Download the best quality of YouTube video by youtube-dl.
set -e

dir="/Users/ian/Documents/youtube-dl"
[ -d ${dir} ] || mkdir -p ${dir}

declare -i videoQ=22
declare -i audioQ=140

printf "Please enter url: "
read website
printf "Please enter file name: "
read name

youtube-dl -F ${website}

printf "Video Quality (22->default, 0->audio): "
read videoQ

if [ ${videoQ} = 22 ]
then
	youtube-dl ${website} -o ${dir}/${name}.mp4
	exit 0

else
	printf "Audio Quality (0->No audio): "
	read audioQ
	
	if [ ${videoQ} = 0 ]; then
		youtube-dl -f ${audioQ} ${website} -o ${dir}/${name}.m4a
		exit 0
	elif [ ${audioQ} = 0 ]; then
		if [ ${videoQ} -lt 150 -o ${videoQ} -gt 400 ]; then
			youtube-dl -f ${videoQ} ${website} -o ${dir}/${name}.mp4
			exit 0
		else
			youtube-dl -f ${videoQ} ${website} -o ${dir}/${name}.webm
			exit 0
		fi
	else
		youtube-dl -f ${audioQ} ${website} -o ${name}-a
		youtube-dl -f ${videoQ} ${website} -o ${name}-v
		if [ ${videoQ} -lt 150 -o ${videoQ} -gt 400 ]; then
			ffmpeg -i ${name}-a -i ${name}-v -c copy ${name}.mp4
			mv ${name}.mp4 ${dir}
		else
			ffmpeg -i ${name}-a -i ${name}-v -c copy ${name}.webm
			mv ${name}.webm ${dir}
		fi
		rm ${name}-a
		rm ${name}-v
	fi
fi

