# Deep-Video-Understanding

## Dataset
We provide link to dataset used for evaluating our proposed frameworks at https://archive.org/download/gt_20200215 .

The critical frames dataset is labelled as `Sports Dataset.zip`. It (Version 2) contains approx 200 football highlights in the form of short clips (with extracted frames). If `clip-x` contains any critical frames, they are extracted and stored in a seprate folder under `Critical Frames` directory.

The `Dog-Birds Dataset.zip` contains frames extracted from video clips of different breeds of dogs and birds used in the paper for fine-grained retrieval.

## Citation
 If you use the dataset and research from our papers for further research, consider citing:
```
@inproceedings{gupta2018pentuplet,
  title =  {Pentuplet Loss for Simultaneous Shots and Critical Points Detection in a Video},
  author  = {Gupta, Nitin and Jain, Abhinav and Agarwal, Prerna and Mujumdar, Shashank and Mehta, Sameep},
  booktitle = {2018 24th International Conference on Pattern Recognition (ICPR)},
  pages =  {2392--2397},
  year  = {2018},
  organization  = {IEEE}
}

@inproceedings{jain2019radial,
  title={Radial Loss for Learning Fine-grained Video Similarity Metric},
  author={Jain, Abhinav and Agarwal, Prerna and Mujumdar, Shashank and Gupta, Nitin and Mehta, Sameep and Chattopadhyay, Chiranjoy},
  booktitle={ICASSP 2019-2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  pages={1652--1656},
  year={2019},
  organization={IEEE}
}
```
