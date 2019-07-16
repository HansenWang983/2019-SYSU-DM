# Original Version: Taehoon Kim (http://carpedm20.github.io)
#   + Source: https://github.com/carpedm20/DCGAN-tensorflow/blob/e30539fb5e20d5a0fed40935853da97e9e55eee8/main.py
#   + License: MIT
# [2016-08-05] Modifications for Inpainting: Brandon Amos (http://bamos.github.io)
#   + License: MIT
# [2017-07] Modifications for sText2Image: Shangzhe Wu
#   + License: MIT

import os
import scipy.misc
import numpy as np
import tensorflow as tf

from model import GAN

flags = tf.app.flags
flags.DEFINE_integer("epoch", 25, "Epoch to train [25]")
flags.DEFINE_float("learning_rate", 0.0002, "Learning rate of for adam [0.0002]")
flags.DEFINE_float("beta1", 0.5, "Momentum term of adam [0.5]")
flags.DEFINE_integer("train_size", np.inf, "The size of train images [np.inf]")
flags.DEFINE_integer("batch_size", 64, "The size of batch images [64]")
flags.DEFINE_integer("image_size", 64, "The size of image to use [64]")
flags.DEFINE_string("dataset", "datasets/celeba/train", "Dataset directory.")
flags.DEFINE_string("checkpoint_dir", "checkpoint", "Directory name to save the checkpoints [checkpoint]")
flags.DEFINE_string("sample_dir", "samples", "Directory name to save the image samples [samples]")
flags.DEFINE_string("log_dir", "logs", "Directory name to save the logs [logs]")
#flags.DEFINE_float("lam1", 0.1, "Hyperparameter for contextual loss [0.1]")
#flags.DEFINE_float("lam2", 0.1, "Hyperparameter for perceptual loss [0.1]")
FLAGS = flags.FLAGS

if not os.path.exists(FLAGS.checkpoint_dir):
    os.makedirs(FLAGS.checkpoint_dir)
if not os.path.exists(FLAGS.sample_dir):
    os.makedirs(FLAGS.sample_dir)

config = tf.ConfigProto()
config.gpu_options.allow_growth = True
with tf.Session(config=config) as sess:
    model = GAN(sess, 
                  image_size=FLAGS.image_size, 
                  batch_size=FLAGS.batch_size, 
                  checkpoint_dir=FLAGS.checkpoint_dir, 
                  sample_dir=FLAGS.sample_dir, 
                  log_dir=FLAGS.log_dir, 
                  is_crop=False
                 )

    model.train(FLAGS)
