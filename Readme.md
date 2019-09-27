#DtwSom

##Dynamic Time Warping Self Organizing Map

DtwSom is a python implementation of Dynamic Time Warping Self Organizing Map (DTW-SOM).DTW-SOM substitutes the original SOM distance measurement to dynamic time warping distance, moreover it uses the dynamic time warping alignment in training other than the original element-wise alignment. These changes will allow DTW-SOM to outperform SOM in time series clustering. A multi-variate DTW-SOM has also been developed.

##Installation

Just use pip:

    pip install dtwsom

or download DtwSom to a directory of your choice and use the setup script:

    git clone https://github.com/Kenan-Li/dtwsom.git
    python setup.py install

##Compatibility notes

DtwSom has been tested under Python 3.6.4.

##License

DtwSom by Kenan Li is licensed under the Creative Commons Attribution 3.0 Unported License. To view a copy of this license, visit [http://creativecommons.org/licenses/by/3.0/](http://creativecommons.org/licenses/by/3.0/ "http://creativecommons.org/licenses/by/3.0/").

![License]( http://i.creativecommons.org/l/by/3.0/88x31.png "Creative Commons Attribution 3.0 Unported License")
