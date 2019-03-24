# CNN Digit detector

## why
i needed a place to get started with ai/ml and get a feel for tensorflow
so i did the ML equivalent of a hello world. i'm aware that this app is terribly made.

## how to run
`cnn.h5` is a pre-trained model I found at [https://github.com/EN10/KerasMNIST]. Use it for good results.

`digits.h5` is the model that I trained using `train.py`. Althought during training the metrics said 98.76% accuracy I probably overfitted. So it performs worse than `cnn.h5`, because I have the midas touch except 
`s/gold/mediocrity`. If you understand that last sentence you're pretty cool.

To run the prediction program run `predict.py` and then draw a digit on the black canvas and then press predict.

#### notes
i'm slowly going crazy.
