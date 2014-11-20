#! /bin/sh
#
# testUniEmo.sh
# Copyright (C) 2014 server2103 <server2103@2103>
#
# Distributed under terms of the MIT license.
#

TYPE="uniemo"
Emotions=('admir' 'amaze' 'anger' 'ecsta' 'grief' 'loath' 'terrr' 'vigil')

fileSuffix='.txt'
modelSuffix='.model'
inputDirPrefix='/home/server2103/tweetEmotion/emojiOutput/feautre_'$TYPE'_'
modelPrefix='/home/server2103/tweetEmotion/Compare_Output/svm_'$TYPE'_'
outputDirPrefix='/home/server2103/tweetEmotion/Compare_Output/predict_'$TYPE'_'
testDirPrefix='/home/server2103/tweetEmotion/emojiOutput/test_feautre_'$TYPE'_'

function fun()
{
    echo "$1 $2 $3 $4 $5"
    echo "./svm-train -s $1 -t $2 -q $3 $4_$1_$2 &"
    ./svm-train -s $1 -t $2 $3 $4_$1_$2 
    wait
    echo "./svm-predict $6 $4_$1_$2 $5_$1_$2"
    ./svm-predict $6 $4_$1_$2 $5_$1_$2
}

function fun_all()
{
    TRAIN_ALL="feautre_"$TYPE"_all"
    TEST_ALL="test_feautre_"$TYPE"_all"
    MODEL_ALL="svm_"$TYPE"_all.model"
    PREDICT_ALL="predict_"$TYPE"_all"
    ANS_ALL="test_ans_"$TYPE"_all"
    echo "./svm-train -s $1 -t $2 -q /home/server2103/tweetEmotion/emojiOutput/$TRAIN_ALL /home/server2103/tweetEmotion/"$MODEL_ALL"_"$1"_"$2
    ./svm-train -s $1 -t $2 -q /home/server2103/tweetEmotion/emojiOutput/$TRAIN_ALL /home/server2103/tweetEmotion/$MODEL_ALL"_"$1"_"$2
    wait
    echo "./svm-predict /home/server2103/tweetEmotion/emojiOutput/$TEST_ALL /home/server2103/tweetEmotion/Compare_Output/"$MODEL_ALL"_"$1"_"$2" /home/server2103/tweetEmotion/Compare_Output/"$PREDICT_ALL"_"$1"_"$2
    ./svm-predict /home/server2103/tweetEmotion/emojiOutput/$TEST_ALL /home/server2103/tweetEmotion/Compare_Output/$MODEL_ALL"_"$1"_"$2 /home/server2103/tweetEmotion/Compare_Output/$PREDICT_ALL"_"$1"_"$2
}

# for each emotion 8
for emo in ${Emotions[@]}
do
    ifilename=$inputDirPrefix$emo$fileSuffix
    modelname=$modelPrefix$emo$modelSuffix
    outputname=$outputDirPrefix$emo$fileSuffix
    tfilename=$testDirPrefix$emo$fileSuffix
    echo "$ifilename $modelname $outputname"

    fun $1 $2 $ifilename $modelname $outputname $tfilename&
    # for the svm -s -t
#    for ((ss=0;ss<2;++ss))
#    do
#        for tt in {0..2..2}
#        do
#            fun $ss $tt $ifilename $modelname $outputname &
#        done
#    done
done

#fun_all $1 $2&
fun_all $1 $2&

wait

