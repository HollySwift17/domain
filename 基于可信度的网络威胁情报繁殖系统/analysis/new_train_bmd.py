# -*- coding: utf-8 -*

import domain
from linguistic_classifier import DGAClassifier, DGAClassifier_hmd
import pandas as pd
from publicsuffix import PublicSuffixList
from database import DatabaseInterface
from tools import clean_string
import string
from os import path   
d = path.dirname(__file__)     
parent_path = os.path.dirname(d)   


def feature_hmd():
        print("\t提取正规域名的特征值...")
        #数字占比
        file = open(parent_path+'/analysis/all.txt',"r")
        lines=0
        domains={}
        for line in file:
                lines += 1
                part=line.split('.',2)
                domain11 = part[1]
                if domain11 in domains.keys():
                        domains[domain11] += 1
                else:
                        domains[domain11] = 1

        file.close()
        file = open("bmd3.txt","r")
        for line in file:
                line1 = line.split('.')[0]
                do = domain.Domain(line,'False')
                DGA_classifier = DGAClassifier_bmd(do)
                distance = DGA_classifier.classify()

                #数字占比
                dig_sum = 0
                for num in line1:
                        if num.isdigit():
                                dig_sum += 1
                num_ratio=1.0*dig_sum/(len(line1))
                #不同字母占比
                alp_num=0
                alp=[]
                for num in line1:
                        if num.isalpha() and num not in alp:
                                alp.append(num)
                                alp_num += 1
                alp_ratio=1.0*alp_num/(len(line1))
                #不同数字占比
                num_num=0
                dig=[]
                for num in line1:
                        if num.isdigit() and num not in dig:
                                dig.append(num)
                                num_num += 1
                num_ratios=1.0*num_num/(len(line1))
                #长度
                lenth=len(line1)
                #元音对辅音的比例
                vowel=0
                cons=0
                vow=['a','e','i','o','u']
                for num in line1:
                        if num.isalpha():
                                if num in vow:
                                        vowel+=1
                                else:
                                        cons+=1
                ratio=1.0*vowel/(len(line1)+1)
                #新特征值
                value=0
                alp_flag=1
                num_flag=1
                part=list(line1)
                for i in range(0,len(part)):
                        if part[i].isdigit() and alp_flag==0:
                                value+=1
                                num_flag=0
                                alp_flag=1
                        elif part[i].isalpha() and num_flag==0:
                                value+=1
                                alp_flag=0
                                num_flag=1
                        elif part[i].isdigit():
                                alp_flag=1
                                num_flag=0
                        elif part[i].isalpha():
                                num_flag=1
                                alp_flag=0
                        else:
                                continue

                f=open(parent_path+"/trails/result_bmd.csv","a")
                f.write(str(num_ratio))#shuzi
                f.write('\t')
                f.write(str(alp_ratio))#butong zimu
                f.write('\t')
                f.write(str(num_ratios))#butong shuzi
                f.write('\t')
                f.write(str(lenth))#changdu
                f.write('\t')
                f.write(str(ratio))#yuanyin
                f.write('\t')
                f.write(str(value))#xintezhengzhi
                f.write('\t' + '1')
                f.write('\n')
                f.close()
        print ("\t提取完毕!\n")





