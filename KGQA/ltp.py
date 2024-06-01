# -*- coding: utf-8 -*-
import pyltp 
import os
LTP_DATA_DIR = 'D:\download\ltp_data_v3.4.0\ltp_data_v3.4.0'  # ltp模型目录的路径
seg_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')
# 这个函数实现了对文本进行分词的功能
def cut_words(words):
    segmentor = pyltp.Segmentor('D:\download\ltp_data_v3.4.0\ltp_data_v3.4.0\cws.model')
    # segmentor.load(seg_model_path)
    words = segmentor.segment(words)
    array_str="|".join(words)
    array=array_str.split("|")
    segmentor.release()#释放模型
    return array

# 这个函数实现了对分词结果进行词性标注的功能
def words_mark(array):

    # 词性标注模型路径，模型名称为`pos.model`
    pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')
    postagger = pyltp.Postagger(pos_model_path)  # 初始化实例
    # postagger.load(pos_model_path)  # 加载模型
    postags = postagger.postag(array)  # 词性标注
    pos_str=' '.join(postags)
    pos_array=pos_str.split(" ")
    postagger.release()  # 释放模型
    return pos_array
#这个函数实现了从词性标注结果中提取目标词性单词的功能
def get_target_array(words):#第三个函数实现获取目标词性单词
    target_pos=['nh','n']
    target_array=[]
    seg_array=cut_words(words)
    pos_array = words_mark(seg_array)
    for i in range(len(pos_array)):
        if pos_array[i] in target_pos:
            target_array.append(seg_array[i])
    target_array.append(seg_array[1])
    return target_array





