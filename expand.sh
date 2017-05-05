rm flop/*
#rm contrast1/*

./flop.sh $1 flop
cp $2/* flop/
./contrast.sh flop $3 #contrast1
rm flop/*
#./rotate.sh contrast1 $3

#rm contrast1/*
