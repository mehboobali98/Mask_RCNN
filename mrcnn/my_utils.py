import operator
import numpy as np

'''
list1: class ids
list2: confidence scores
The function returns sorted lists based on the confidence scores
'''
def sort_lists(list1, list2):
  list1, list2 = zip(*sorted(zip(list1, list2), reverse=True)) 
  list1, list2 = (list(t) for t in zip(*sorted(zip(list1, list2))))

  return list1, list2
  
'''
Append score to boundary boxes
'''
def append_scores(bbx, scores):
  if isinstance(bbx,np.ndarray):
    bbx = bbx.tolist()
  for i in range(len(scores)):
    score = scores[i]
    bbx[i].append(score)
  return bbx

'''
Sort b boxes based on scores
'''
def sort_bbx(bbx):
  index = len(bbx[0])
  sorted_list = sorted(bbx, key=lambda x: (x[index-2], x[index-1]))
  return sorted_list
  
'''
list containing indices of duplicate c_ids are returned
'''
def duplicate_rois_indx(c_ids):
  c_ids_ = list() 
  dup_indexes = []
  
  for index, val in enumerate(c_ids): 
      if val not in c_ids_: 
          c_ids_.append(val)       
      else: 
          dup_indexes.append(index)
  
  # decrement indices        
  indexes = [x - 1 for x in dup_indexes]
  return indexes
  
'''
takes in: lists of c_ids, scores, duplicate indexes
out: c_ids and scores without duplicates
'''
def rm_duplicate_rois(c_ids, scores, bbx, indexes):
  for ele in sorted(indexes, reverse=True):
    del c_ids[ele]
    del scores[ele]
    del bbx[ele]
  return c_ids, scores, bbx
  
'''
Remove class ids and scores from bboxes
'''
def clean_bbx(bbxs):
  for bbx in bbxs:
    del bbx[-2:]
  return bbxs
  
