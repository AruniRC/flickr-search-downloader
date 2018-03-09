import os
import os.path as osp


KEYWORD_LIST = './keyword-small.txt'

with open(KEYWORD_LIST, 'r') as fid:
    for line in fid:
        line = line.rstrip()
        if line is not None:
            print 'Running keyword: %s' % line
            os.system('python download_keyword.py -k "%s" &' % line)
