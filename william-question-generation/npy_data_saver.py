'''
Module for preparing data from json-format into a numpy array format (npy). 
'''

import json
import numpy as np

def to_npy(data_att, from_path, to_path):
    '''
    Reads content of a json file and saves it in npy format.
    param data_att: The name of the attribute holding the data in
    the json file
    param from_path: The path of the json file to convert to npy
    param to_path: The location of the new npy file to create
    from the json file
    '''
    with open(from_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)[data_att]
        
        question_data = np.empty(len(data), dtype=np.ndarray)

        for idx, d in enumerate(data):
            paragraphs = d['paragraphs']
            for p in paragraphs:
                qs = p['qas']
                context_question = np.empty(len(qs)+1, dtype=np.ndarray)
                context_question[0] = p['context']
                
                for i, q in enumerate(qs):
                    context_question[i+1] = q['question'] #+1 because first index is context

                question_data[idx] = context_question

        np.save(to_path, question_data)

if __name__ == '__main__':
    to_npy('data', './data/squad_v2.json', './data/squad_v2.npy')