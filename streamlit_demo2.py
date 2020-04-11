#import streamlit as st

import gpt_2_simple as gpt2
import os
import time
from datetime import datetime

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess, run_name='IG_run1')

gen_file = os.path.join('results','gpt2_gentext_{:%Y%m%d_%H%M%S}.txt'.format(datetime.utcnow()))

gpt2.generate_to_file(sess, destination_path=gen_file, run_name='IG_run1')
#print(type(generated_text))
#print(generated_text)

#st.write("hi there")

#st.write(gpt2.generate(sess, run_name='IG_run1'))