The Master Algorithm  
####################

:date: 2018-05-01
:summary: A low-tech, cheerleading explainer of much of what machine learning is about, by Pedro Domingos
:category: books
:tags: algorithm, ai, machine learning, pedro domingos, popular

An interesting overview and cheerleading explainer of much of what machine learning is about.  At the moment I think it is at too high a conceptual level for students to read it directly, and it is also too generally positive -- though that may change as I get farther in.

Perceptron: 

A connectionist model of something like a neuron.  A perceptron is a function that outputs 0 or 1 if its input is below or above a certain threshold.  The input is the weighted sum of the values coming from some number of inputs, each of which is in the domain [0,1] in R.  Training a perceptron consists of determining the weights for each input, and perhaps determining the threshold value above which the output will be one.  So for n inputs, there are n+1 parameters for the model (the n weights plus the threshold).  So does that mean that one needs at least n+1 labeled data points to be able to determine the weights?  Looks like the training is done starting from a random set of weights, then the weights are adjusted after each input is tested to see if the output is correct (so yes, you do need labeled data)

Criticism from Minsky and Papert:  a perceptron cannot learn the function XOR, because the perceptron can only learn lines (hyperplanes) as dividers between the positive and negative examples.  XOR requires two boundaries so you can exclude the examples that are BOTH.  XOR is a universal gate, so perceptrons cannot be universal computers

This criticism caused funders and researchers to conclude that neural networks were a dead-end, and thus machine learning was a dead end -- so they focused on knowledge engineering for 15 years.

Domingos calls Minsky the evil queen in Snow White.... (and Papert is the huntsman)


Spin glasses:

A model of brain network connections, in that Ising models are kind of like neurons by firing together and wiring together with neighbors, and that spin glasses can be trapped in local minima.  The analogy is that a "memory" is a local minimum energy state of the network.  Different in that Ising models are symmetric while neurons are directional, and that real neurons are stochastic.  By adding a probability distribution to describe the likelihood of a neural network spin flip given the set of inputs, the model gives the Boltzmann distribution of states

Boltzmann machine:

They can dream?


Phase transitions:

Sigmoid curves describe phase transitions, and a lot of phenomena are or can be thought of as phase transitions.  And apparently sigmoid curves are complete in the same sense that Fourier series are complete.

Backpropagation:

The master algorithm for connectionism, a form of gradient descent. Finding global optima in hyperspace is really hard, and there are LOTS of local optima.  Domingos argues that most of the time a local is just fine, and often the local is a saddle because there are lots of ways out of a valley in hyperspace, so one is not necessarily trapped in a local optimum.  

I don't understand the disdain for Marvin Minsky.

Autoencoder:

A multilayer perceptron that performs the identity function -- given an input, it produces an identical output.  BUT, it does so through a hidden layer that is *smaller* than the input and output layers, so the task of the network optimization is to figure out how to compress and then decompress the input. (this prevents the network function from being "copy").  But they were hard to train because there isn't much space -- it's basically a compression engine.  A *sparse autoencoder* does the same task, with a larger hidden layer that has most of the hidden units turned off at any given time, so it can learn using the dual signal of which bits are on and what is encoded in them.

*Stacked* sparse autoencoders combine multiple layers of sparse autoencoders, with each layer responsible for compressing one aspect of the input, and the final output given by some combination of the compressed versions.  Thus an image of a face becomes a set of compressed names for qualities of the face, and the final output is the recognized name of the person.  Gestalt-y.

This is a kind of deep learner.






   
