for file in $1/*.png
do
	name=${file##*/}
	for ((i=-5; i<=5; i++))
	do
		convert $file -rotate $i "${2}/${i}$name"
	done
done
