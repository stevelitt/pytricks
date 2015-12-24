#!/usr/bin/python3
import sys

def relevant_lines(dic):
    if 'this_line_number' not in dic:
        dic['this_line_number'] = 0
    if 'this_line_text' not in dic:
        dic['this_line_text'] = 0
    if 'is_relevant' not in dic:
        def junkfcn():
            return dic['this_line_text'].strip() != ''
        dic['is_relevant'] = junkfcn
        del junkfcn

    def rtrnfcn():
        dic['this_line_text'] = sys.stdin.readline()
        dic['this_line_text'] = dic['this_line_text']
        dic['this_line_number'] += 1

        # Blow off any nonrelevant lines
        while dic['this_line_text'] and not dic['is_relevant']():
            dic['this_line_text'] = sys.stdin.readline()
            dic['this_line_number'] += 1

        # Return None if eof
        if dic['this_line_text'] == '':
            return -99, 'basura'

        else: # Run tweak procedure and then return the line number and text
            if 'tweak' in dic:
                dic['tweak']()
        return dic['this_line_number'], dic['this_line_text'].strip()
    return rtrnfcn 


mydict = {}
nextt = relevant_lines(mydict)
(lineno, txt) = nextt()
while lineno != -99:
    print('Line {}: {}'.format(str(lineno), txt))
    (lineno, txt) = nextt()



