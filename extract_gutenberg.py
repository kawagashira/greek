#!/usr/bin/env python
#
#   Extract lines from literature

def extract(i_file):

    main_text_yn = 0
    with open(i_file) as i_handle:
        for line in i_handle:
            line = line.rstrip()
            print (main_text_yn, line)
            ### FIND THE FIRST LINE ###
            if not main_text_yn:
                if line=='Ραψωδία Τ':
                    main_text_yn = 1    # entered main text
                else:
                    continue

            ### MAIN TEXT ###
            if main_text_yn == 1:
                if len(line) == 0:
                    print ('SKIP SPACE')
                    continue
                elif line == 'Τ Ε Λ Ο Σ':
                    break
                else:
                    print ('#', line)

###
if __name__ == '__main__':

    extract('data/odysseia_a.txt')
