# attgan
[论文](https://arxiv.org/abs/1711.10678)：[Zhenliang He](https://github.com/LynnHo/AttGAN-Tensorflow), [Wangmeng Zuo](https://github.com/LynnHo/AttGAN-Tensorflow), [Meina Kan](https://github.com/LynnHo/AttGAN-Tensorflow), [Shiguang Shan](https://github.com/LynnHo/AttGAN-Tensorflow), [Xilin Chen](https://github.com/LynnHo/AttGAN-Tensorflow), et al. AttGAN: Facial Attribute Editing by Only Changing What You Want[C]// 2017 CVPR. IEEE

# Dataset
CelebFaces Attributes Dataset (CelebA) :[CelebA](<http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html>)

# Train
```python
  export DEVICE_ID=0
  export RANK_SIZE=1
  python train.py --experiment_name 128_shortcut1_inject1_none --data_path /path/data/img_align_celeba --attr_path /path/data/list_attr_celeba.txt
  OR
  bash run_single_train.sh experiment_name /path/data/img_align_celeba /path/data/list_attr_celeba.txt
```

# Eval
  ```bash
  export DEVICE_ID=0
  export RANK_SIZE=1
  python eval.py --experiment_name 128_shortcut1_inject1_none --test_int 1.0 --custom_data /path/data/custom/ --custom_attr /path/data/list_attr_custom.txt --custom_img --gen_ckpt_name generator-119_84999.ckpt
  ```