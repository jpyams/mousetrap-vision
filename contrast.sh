for file in $1/*.png
do
	name=${file##*/}
	convert $file -contrast "${2}/-$name"
	convert $file +contrast "${2}/+$name"
	cp $file "${2}/0$name"
done
