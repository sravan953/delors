# DeLorRS
---
#### Application of Deep Learning Neural Networks for Rapid Reconstruction of Spiral K-Space Data for Magnetic Resonance Imaging
---
Project submission for [`Intro to ML (EL-9123)`](https://github.com/sdrangan/introml) coursework.

### Setup
1. Clone repo
2. Download and generate data (read below)
3. Run network

### Downloading data
0. Clone repo
1. Download grayscale images from ImageNet: `python3 get_data_imagenet.py` in your terminal
2. Run `IterAddPhase.m` in Matlab on all the downloaded folders
3. [Download](http://gpilab.com/downloads/) GPI v1-beta, and install
4. Generate k-space data using samples from step 3 and `complex_spiral_traj280_58.mat` in the `gen_kspace.net`
5. Place all the k-space data (in their belonging folders) in `imagenet_64_kspace` and the original images (in their belonging folders) in `imagenet_64_orig`

### Contributing
Fork and PR!
