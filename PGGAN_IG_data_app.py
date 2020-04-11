import os
import sys
import time
import glob
from model import *
from config import *

from keras.models import load_model,save_model
from keras.layers import Input
from keras import optimizers

import dataset
import config

import misc

import time
from datetime import datetime

from PIL import Image
import gpt_2_simple as gpt2 # tensorflow should be at around 1.13.1
import streamlit as st


def load_G_weights(G, path, by_name = True):
    G_path = os.path.join(path,'Generator_tree.h5')
    G.load_weights(G_path, by_name = by_name)
    return G

def rampup(epoch, rampup_length):
    if epoch < rampup_length:
        p = max(0.0, float(epoch)) / float(rampup_length)
        p = 1.0 - p
        return math.exp(-p*p*5.0)
    else:
        return 1.0

def rampdown_linear(epoch, num_epochs, rampdown_length):
    if epoch >= num_epochs - rampdown_length:
        return float(num_epochs - epoch) / rampdown_length
    else:
        return 1.0

def create_result_subdir(result_dir, run_desc):

    # Select run ID and create subdir.
    while True:
        run_id = 0
        for fname in glob.glob(os.path.join(result_dir, '*')):
            try:
                fbase = os.path.basename(fname)
                ford = int(fbase[:fbase.find('-')])
                run_id = max(run_id, ford + 1)
            except ValueError:
                pass

        result_subdir = os.path.join(result_dir, '%03d-%s' % (run_id, run_desc))
        try:
            os.makedirs(result_subdir)
            break
        except OSError:
            if os.path.isdir(result_subdir):
                continue
            raise

    print ("Saving results to", result_subdir)
    return result_subdir

def random_latents(num_latents, G_input_shape):
    return np.random.randn(num_latents, *G_input_shape[1:]).astype(np.float32)

def random_labels(num_labels, training_set):
    return training_set.labels[np.random.randint(training_set.labels.shape[0], size=num_labels)]

# download a 124m GPT2 model (make sure it's ONLY downloaded if it doesn't exit)
model_name = "124M"
if not os.path.isdir(os.path.join("models", model_name)):
	print(f"Downloading {model_name} model...")
	gpt2.download_gpt2(model_name=model_name)   # model is saved into current directory under /models/124M/

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='tree_run1')


def predict_gan():
    separate_funcs          = False
    drange_net              = [-1,1]
    drange_viz              = [-1,1]
    image_grid_size         = (1 ,1)
    image_grid_type         = 'default'
    resume_network          = './pre-trained_weight' # adding the ./ to define the pre-trained-weight folder at root level
    
    np.random.seed(config.random_seed)

    if resume_network:
        print("Resuming weight from:"+resume_network)
        G = Generator(num_channels=3, resolution=128, label_size=0, **config.G)
        G = load_G_weights(G,resume_network,True)

    print(G.summary())

    # Misc init.

    if image_grid_type == 'default':
        if image_grid_size is None:
            w, h = G.output_shape[1], G.output_shape[2]
            print("w:%d,h:%d"%(w,h))
            image_grid_size = np.clip(int(1920 // w), 3, 16).astype('int'), np.clip(1080 / h, 2, 16).astype('int')
        
        print("image_grid_size:",image_grid_size)
    else:
        raise ValueError('Invalid image_grid_type', image_grid_type)

    result_subdir = misc.create_result_subdir('pre-trained_result', config.run_desc)

    for i in range(1,6):
        snapshot_fake_latents = random_latents(np.prod(image_grid_size), G.input_shape)
        snapshot_fake_images = G.predict_on_batch(snapshot_fake_latents)
        misc.save_image_grid(snapshot_fake_images, os.path.join(result_subdir, 'pre-trained_%03d.png'%i), drange=drange_viz, grid_size=image_grid_size)
        
        # use streamlit to show images generated
        # st.image(os.path.join(result_subdir, 'pre-trained_%03d.png'%i))
        st.header('IG Post #' + str(i))
        im = Image.open(os.path.join(result_subdir, 'pre-trained_%03d.png'%i))
        st.image(im.resize((1024, 1024), Image.ANTIALIAS)) # with gpt2, the images are generated too slow
        # call gpt2-simple on a pre-trained weight
        gen_file = os.path.join(result_subdir,'gpt2_gentext_{:%Y%m%d_%H%M%S}.txt'.format(datetime.utcnow()))
        
        gpt2.generate_to_file(sess, destination_path=gen_file, run_name='tree_run1')
        # read contents of generated text
        with open(gen_file, 'r') as content:
            st.write(content.read())


if __name__ == '__main__':
    st.title('Instagram Content Generator')
    st.write('The following are a list of 5 Instagram images along with their captions, all generated for mood boarding')
    
    predict_gan()
