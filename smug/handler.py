"""
"""

import json
import re

from smug import log, WD,TIMESTAMP

#!/usr/bin/env python

class Handler:
    def __init__(self):
        pass

    def verify_fastq(self, fn):
        #Check suffix
        hit = re.search("fastq.gz$",fn)
        if not hit:
            raise Exception("File {0} is not a zipped fastq".format(fn))
        log.debug('Verified that {0} is a zipped fastq'.format(fn))
 
        #Check contents
        nuc = set("ATCG\n")
        lineno = 0
        for line in open(fn):
            lineno = lineno + 1 
            if lineno == 1:
                corr = re.match("^@",line)
            elif lineno == 2:
                corr = set(line) <= nuc
            elif lineno == 3:
                corr = re.match("^\+",line)
            elif lineno == 4:
                lineno = 0

            if not corr:
                raise Exception("File {0} does not look like a fastq at line {1}: {2}".format(fn, lineno, line))

        if lineno % 4 != 0:
            raise Exception("File {0} is missing data".format(fn))
        log.debug('Verified that {0} resembles a fastq'.format(fn))
 
    def gen_metadata(self, fn, tag):
        mdict = dict()
        mdict[fn] = {'tag':tag}
        md = open("meta-{}.json".format(TIMESTAMP), "a")
        md.write(json.dumps(mdict, indent=4))
        md.close()
        log.debug('Generated metadata file meta-{}.json'.format(TIMESTAMP)) 
