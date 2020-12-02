# Deep-Video-Understanding

## Dataset
We provide link to dataset used for evaluating our proposed frameworks at https://archive.org/download/gt_20200215 .

The critical frames dataset is labelled as `Sports Dataset.zip`. It (Version 2) contains approx 200 football highlights in the form of short clips (with extracted frames). If `clip-x` contains any critical frames, they are extracted and stored in a seprate folder under `Critical Frames` directory.

The `Dog-Birds Dataset.zip` contains frames extracted from video clips of different breeds of dogs and birds used in the paper for fine-grained retrieval.

## Additional Experiments and Results
||CnD|FcP|FtW||
||---|---|---||
||QP%|NDCG|TP%|MAP| QP%|NDCG|TP%|MAP| QP%|NDCG|TP%|MAP|
|Triplet|69.19|0.95|86.69|0.80|70.45|0.89|85.32|0.54|42.75|0.88|75.91|0.65 |
|Quadruplet-1|78.14|0.95|90.99|0.84|79.77|0.90|88.78|0.64|37.12|0.86|71.92|0.59|
|Quadruplet-2a|76.90|0.94|89.91|0.85|77.65|0.90|88.52|0.61|45.88|0.87|76.13|0.66|
|Quadruplet-2b|51.83|0.92|87.38|0.82|78.42|0.90|87.06|0.60|38.64|0.84|74.77|0.61|
|Quadlet(Ours) |81.82|0.97|93.92|0.91|83.74|0.91|91.74|0.66|53.93|0.89|80.56|0.67|
|Radial(Ours) |84.39|0.98|95.86|0.93|87.21|0.92|92.64| 0.70|55.18|0.90| 81.91|0.68|

        
Table 3: Quantitative metrics for order-preserving image ranking task (QP, NDCG) and coarse-grained ranking task (TP, MAP).

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
