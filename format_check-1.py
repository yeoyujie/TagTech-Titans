import os
import codecs



def check_submission_format(filename):
    #supposed to be two cols, and 15972 lines (15185 tokens, and 787 empty rows)
    readfile = codecs.open(filename, 'r', 'ISO-8859-1')
    word2tag = []
    empty=0
    for line in readfile:
        if len(line.strip())>0:
            parts = line.strip().split()
            if len(parts)==2:
                word2tag.append((parts[0].strip(), parts[1].strip()))
            else:
                print('wrong line:', line.strip(), ' with length:', len(line.strip().split()))
        else:
            empty+=1
    readfile.close()
    if len(word2tag)==15185 and empty==787:
        print('correct format')
    else:
        print('incorrect format')






if __name__ == "__main__":
    check_submission_format("./TagTech Titans.test.txt")
