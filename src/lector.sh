#! /usr/bin/env bash
# Script de Prueba
cd ~
mesosPossibles=("Gen" "Jan" "Feb" "Ene" "Mar" "May" "Mai" "Jun" "Jul" "Aug" "Ago" "Set" "Sep" "Oct" "Nov" "Des" "Dic" "Abr" "Apr")
while read line;
do 
	newLine=$(echo "$line" | tr -s " ")
	echo $newLine
	mes=$(echo $newLine | cut -d ' ' -f1)
	dia=$(echo $newLine | cut -d ' ' -f2)
	tempsCamps=$(echo $newLine | cut -d ' ' -f3)
	hores=$(echo $tempsCamps | cut -d ':' -f1)
	minuts=$(echo $tempsCamps | cut -d ':' -f2)
	segons=$(echo $tempsCamps | cut -d ':' -f3)
	
	if [ $dia -lt 1 -o $dia -gt 31 ]; then
		echo "Dia incorrecte"
		continue
	fi
	if [ $hores -lt 0 -o $dia -gt 23 ]; then
		echo "Hora incorrecte"
		continue
	fi
	if [ $minuts -lt 0 -o $minuts -gt 59 ]; then
		echo "Minuts incorrectes"
		continue
	fi
	if [ $segons -lt 0 -o $segons -gt 59 ]; then
		echo "Segons incorrectes"
		continue
	fi
	
done < dates.txt


