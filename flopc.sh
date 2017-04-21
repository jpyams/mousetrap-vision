for file in $1/*.png
do
	name=${file##*/}
	convert $file -flop "dest/f$name"
	cp $file "dest/o$name"
done
