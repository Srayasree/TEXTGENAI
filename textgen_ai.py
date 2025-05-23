# -*- coding: utf-8 -*-
"""textgen AI.ipynb

Original file is located at
    https://colab.research.google.com/drive/10Q9pokC6aRy47d2JClJQZrEnf5C9YGv6
"""

##Libraries required
!pip install langchain_huggingface
## for API Calls
!pip install huggingface_hub
!pip install transformers
!pip install accelerate
!pip install bitsandbytes
!pip install langchain

##Enviornment for secret keys
from google.colab import userdata
sec_key = userdata.get('HF_TOKEN')
print(sec_key)

"""HUGGING FACE **ENDPOINT**"""

from langchain_huggingface import HuggingFaceEndpoint

from google.colab import userdata
sec_key = userdata.get('HF_TOKEN')
print(sec_key)

import os
os.environ['HF_TOKEN']=sec_key

repo_id="mistralai/Mistral-7B-Instruct-v0.2"
llm=HuggingFaceEndpoint(repo_id=repo_id,max_length=128,temperature=0.7,token=sec_key)

llm

repo_id="mistralai/Mistral-7B-Instruct-v0.3"
llm=HuggingFaceEndpoint(repo_id=repo_id,max_length=128,temperature=0.7,token=sec_key)

llm

"""HUGGING FACE **PIPELINE**"""

from langchain_huggingface import HuggingFacePipeline
from transformers import AutoTokenizer, pipeline,AutoModelForCausalLM

model_id="gpt2"
model=AutoModelForCausalLM.from_pretrained(model_id)
tokenizer=AutoTokenizer.from_pretrained(model_id)

pipe=pipeline("text-generation",model=model,tokenizer=tokenizer,max_new_tokens=100)
hf=HuggingFacePipeline(pipeline=pipe)

hf

hf.invoke("langchain is a company")
