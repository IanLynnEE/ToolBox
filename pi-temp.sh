#!/bin/bash
# Script: my-pi-temp.sh
# Purpose: Display the ARM CPU and GPU  temperature of Raspberry Pi 2/3 
# Author: Vivek Gite <www.cyberciti.biz> under GPL v2.x+
# -------------------------------------------------------
cpu=$(</sys/class/thermal/thermal_zone0/temp)
path="${HOME}/piTempLog.txt"
echo "" >> $path
echo "$(date) @ $(hostname)" >> $path
echo "-------------------------------------------" >> $path
echo "GPU => $(/opt/vc/bin/vcgencmd measure_temp)" >> $path
echo "CPU => $((cpu/1000))'C" >> $path
tail -4 $path
