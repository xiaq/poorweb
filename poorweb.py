"""
poorweb is a poor man's literate programming tool.
"""

import sys

code_begin = '>>'
code_end = '<<'
code_begin_tex = r'\begin{verbatim}'
code_end_tex = r'\end{verbatim}'

def main(argv):
    if len(argv) != 3:
        print 'Usage: poorweb.py <src> <tex dst> <default code dst>'
        return 1
    src_name, tex_dst_name, code_dst_name = argv
    src = open(src_name, 'r')
    tex_dst = open(tex_dst_name, 'w')
    code_dsts = {'': open(code_dst_name, 'w')}

    code_dst = None
    for line in src:
        if line.startswith(code_begin):
            name = line[len(code_begin):].rstrip('\n')
            if name not in code_dsts:
                code_dsts[name] = open(name, 'w')
            code_dst = code_dsts[name]
            tex_dst.write(code_begin_tex + '\n')
        elif line.startswith(code_end):
            code_dst = None
            tex_dst.write(code_end_tex + '\n')
        else:
            tex_dst.write(line)
            if code_dst is not None:
                code_dst.write(line)

    for f in [src, tex_dst] + code_dsts.values():
        f.close()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
