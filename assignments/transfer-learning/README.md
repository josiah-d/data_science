# Transfer Learning
Transfer learning is a technique for building neural networks based on previously trained neural networks.  We have explored that in order to build deep and/or wide neural networks from scratch, large amounts of training data is needed.  Transfer learning reduces the burden of data volumes by allowing us to base new networks on exiting networks, and have made extremely accurate neural nets more practical than ever.

## Examples
### Image Classification
The most robustly developed area of transfer learning is in the field of CNNs.  Every year, researchers compete in the [ImageNet](http://image-net.org/challenges/LSVRC/) competition to try to create the best image classifier on a very large set of labeled data.  The images in the set tend to be both large differences (e.g. people, animals, landscapes), and small differences (e.g. cheetahs vs jaguars).  The [VGG](https://arxiv.org/pdf/1409.1556.pdf) network is an example of one that publishes the weights of their trained networks.

### NLP
Hoping to reproduce the benefits seen with images, transfer NLP models have recently emerged.  Starting with [ELMo](https://allennlp.org/elmo) and expanded upon with [BERT](https://ai.googleblog.com/2018/11/open-sourcing-bert-state-of-art-pre.html), natural language tasks seem to be benefitting from similar open sourced advances. 

