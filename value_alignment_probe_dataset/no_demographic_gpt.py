#!/usr/bin/env python
# coding: utf-8

# In[7]:


import openai
openai.api_key = "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" # add your openai key here.


# In[8]:


from gptinference.base_prompt import Prompt
from gptinference.openai_wrapper import OpenAIWrapper
import json
from typing import Dict, Tuple, List, Any
from dataclasses import dataclass
from tqdm import tqdm
import csv

    
def call_gpt(openai_wrapper: OpenAIWrapper, prompt: str, max_tokens: int= 256) -> str:
    """
    :param claim:
    :param abstracts: can be empty -- defaults to ungrounded gpt baseline if empty abstracts.
    :return:
    """
    generation_query = prompt
    generated_str = openai_wrapper.call(
        prompt=generation_query,
        engine="gpt-3.5-turbo",
        max_tokens=max_tokens,
        temperature=0.0
    )

    return generated_str
    


# In[12]:


openai_wrapper = OpenAIWrapper(cache_path='cache.jsonl')


with open('no_demogrpahics_prompt.jsonl', 'r') as f, open('no_demogrpahics_prompt_out.jsonl', 'w+') as out:
    for line in f:
        js = json.loads(line)
        prompt = js['prompt']
        question = js['question_id']
#         generated_str = call_gpt(openai_wrapper, prompt)
        output_js = { 'output': '', 'question_id': question }
        out.write(json.dumps(output_js))
        out.write('\n')
        
    


# In[ ]:




