for file in $1/*.png
do
	name="${file##*/}"
	convert $file -flop "${2}/f$name"
done
