rm flop/*
#rm contrast/*

./flop.sh $1 flop
cp "${1}/*" flop/
./contrast.sh flop $2
rm flop/*
#./rotate.sh contrast $2

#rm contrast/*
