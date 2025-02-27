
import os


def to_head(projectpath):
    pathlayers = os.path.join(projectpath, 'layers/').replace('\\', '/')
    return r"""
\documentclass[border=8pt, multi, tikz]{standalone} 
\usepackage{tkz-graph}

% Preambule to match presentation 
\usepackage{amsmath,amsthm,amssymb,amsfonts}
\usepackage{color}
\usepackage[scaled]{beramono}
\usepackage[sfdefault]{AlegreyaSans}
\usepackage[italic]{mathastext}

\usepackage{graphicx}
\usepackage{import}
\subimport{""" + pathlayers + r"""}{init}
\usetikzlibrary{positioning}
\usetikzlibrary{3d} %for including external image 
"""


def to_cor():
    return r"""
\def\ConvColor{rgb:yellow,5;red,2.5;white,5}
\def\ConvReluColor{rgb:yellow,5;red,5;white,5}
\def\PoolColor{rgb:red,1;black,0.3}
\def\UnpoolColor{rgb:blue,2;green,1;black,0.3}
\def\FcColor{rgb:blue,5;red,2.5;white,5}
\def\FcReluColor{rgb:blue,5;red,5;white,4}
\def\SoftmaxColor{rgb:magenta,5;black,7}   
\def\SumColor{rgb:blue,5;green,15}
"""


def to_begin():
    return r"""
\newcommand{\copymidarrow}{\tikz \draw[-Stealth,line width=0.8mm,draw={rgb:blue,4;red,1;green,1;black,3}] (-0.3,0) -- ++(0.3,0);}

\begin{document}
\begin{tikzpicture}[
  convnode/.style={shape=rectangle, opacity=0.8, fill=\ConvReluColor, minimum width = 2cm, 
    minimum height = 1cm},
  poolnode/.style={shape=rectangle, opacity=0.5, fill=\PoolColor, minimum width = 2cm, 
    minimum height = 1cm},
  fcnode/.style={shape=rectangle, opacity=0.8, fill=\FcColor, minimum width = 2cm, 
    minimum height = 1cm},
  softmaxnode/.style={shape=rectangle, opacity=0.8, fill=\SoftmaxColor, minimum width = 2cm, 
    minimum height = 1cm}
]
\tikzstyle{connection}=[ultra thick,every node/.style={sloped,allow upside down},draw=\edgecolor,opacity=0.7]
\tikzstyle{copyconnection}=[ultra thick,every node/.style={sloped,allow upside down},draw={rgb:blue,4;red,1;green,1;black,3},opacity=0.7]
"""

# layers definition


def to_input(pathfile, to='(-3,0,0)', width=8, height=8, name="temp"):
    return r"""\node[canvas is zy plane at x=0,font=\Huge] ("""+name+r""") at (-3, -5, 0) {\reflectbox{\textbf{"""+str(name)+r"""}}};
    \node[canvas is zy plane at x=0] (""" + name + """) at """ + to + """ {\includegraphics[width=""" + str(width)+"cm"+""",height=""" + str(height)+"cm"+"""]{""" + pathfile + """}};"""

# Conv


def to_Conv(name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=40, caption=" "):
    return r"""
\pic[shift={""" + offset + """}] at """ + to + """ 
    {Box={
        name =""" + name + """,
        caption = """ + caption + r""",
        xlabel = {{""" + str(n_filer) + """, }},
        zlabel = """ + str(s_filer) + """,
        fill=\ConvColor,
        height = """ + str(height) + """,
        width = """ + str(width) + """,
        depth = """ + str(depth) + """
        }
    };
"""

# Conv,Conv,relu
# Bottleneck


def to_ConvConvRelu(name, s_filer=256, n_filer=(64, 64), offset="(0,0,0)", to="(0,0,0)", width=(2, 2), height=40, depth=40, caption=" "):
    return r"""
\pic[shift={ """ + offset + """ }] at """ + to + """ 
    {RightBandedBox={
        name = """ + name + """,
        caption = """ + caption + """,
        xlabel = {{ """ + (','.join(['"'+str(filer)+'"' for filer in n_filer])) + """ }},
        zlabel = """ + str(s_filer) + """,
        fill=\ConvColor,
        bandfill=\ConvReluColor,
        height = """ + str(height) + """,
        width ={ """ + (','.join([str(w) for w in width])) + """ },
        depth = """ + str(depth) + """
        }
    };
"""


def to_FullyConnected(name, s_filer=" ", n_filer=" ", offset="(0,0,0)", to="(0,0,0)", width=1.5, height=3, depth=25, opacity=0.8, caption=" ", zlabelposition='midway'):
    return r"""
\pic[shift={""" + offset + """}] at """ + to + """ 
    {Box={
        name =""" + name + """,
        caption =""" + caption + """,
        xlabel = {{ """ + '"'+str(n_filer) + '", "dummy"' + """ }},
        zlabel = """ + str(s_filer) + """,
        fill=\FcColor,
        opacity = """ + str(opacity) + """,
        height = """ + str(height) + """,
        width = """ + str(width) + """,
        depth = """ + str(depth) + """
        }
    };
"""


# Pool
def to_Pool(name, offset="(0,0,0)", to="(0,0,0)", width=1, height=32, depth=32, opacity=0.5, caption=" "):
    return r"""
\pic[shift={ """ + offset + """ }] at """ + to + """ 
    {Box={
        name="""+name+""",
        caption = """ + caption + r""",
        fill=\PoolColor,
        opacity = """ + str(opacity) + """,
        height = """ + str(height) + """,
        width = """ + str(width) + """,
        depth = """ + str(depth) + """
        }
    };
"""

# unpool4,


def to_UnPool(name, offset="(0,0,0)", to="(0,0,0)", width=1, height=32, depth=32, opacity=0.5, caption=" "):
    return r"""
\pic[shift={ """ + offset + """ }] at """ + to + """ 
    {Box={
        name = """ + name + r""",
        caption = """ + caption + r""",
        fill=\UnpoolColor,
        opacity = """ + str(opacity) + """,
        height = """ + str(height) + """,
        width = """ + str(width) + """,
        depth = """ + str(depth) + """
        }
    };
"""


def to_ConvRes(name, s_filer=256, n_filer=64, offset="(0,0,0)", to="(0,0,0)", width=6, height=40, depth=40, opacity=0.2, caption=" "):
    return r"""
\pic[shift={ """ + offset + """ }] at """ + to + """ 
    {RightBandedBox={
        name =""" + name + """,
        caption =""" + caption + """,
        xlabel ={{ """ + str(n_filer) + """, }},
        zlabel = """ + str(s_filer) + r""",
        fill={rgb:white,1;black,3},
        bandfill={rgb:white,1;black,2},
        opacity = """ + str(opacity) + """,
        height = """ + str(height) + """,
        width = """ + str(width) + """,
        depth = """ + str(depth) + """
        }
    };
"""


# ConvSoftMax
def to_ConvSoftMax(name, s_filer=40, offset="(0,0,0)", to="(0,0,0)", width=1, height=40, depth=40, caption=" "):
    return r"""
\pic[shift={""" + offset + """}] at """ + to + """ 
    {Box={
        name =""" + name + """,
        caption = """ + caption + """,
        zlabel = """ + str(s_filer) + """,
        fill=\SoftmaxColor,
        height = """ + str(height) + """,
        width = """ + str(width) + """,
        depth = """ + str(depth) + """
        }
    };
"""

# SoftMax


def to_SoftMax(name, s_filer=" ", n_filer=" ", offset="(0,0,0)", to="(0,0,0)", width=1.5, height=3, depth=25, opacity=0.8, caption=" "):
    return r"""
\pic[shift={""" + offset + """}] at """ + to + """ 
    {Box={
        name =""" + name + """,
        caption = """ + caption + """,
        xlabel = {{ """ + '"'+str(n_filer) + '", "dummy"' + """ }},
        zlabel = """ + str(s_filer) + """,
        fill=\SoftmaxColor,
        opacity = """ + str(opacity) + """,
        height = """ + str(height) + """,
        width = """ + str(width) + """,
        depth = """ + str(depth) + """
        }
    };
"""


def to_Sum(name, offset="(0,0,0)", to="(0,0,0)", radius=2.5, opacity=0.6):
    return r"""
\pic[shift={""" + offset + """}] at """ + to + """ 
    {Ball={
        name =""" + name + """,
        fill=\SumColor,
        opacity = """ + str(opacity) + """,
        radius = """ + str(radius) + """,
        logo=$+$
        }
    };
"""


def to_connection(of, to, of_dir='east', to_dir='west'):
    if of_dir:
        of = '(' + of + '-' + of_dir + ')'
    if to_dir:
        to = '(' + to + '-' + to_dir + ')'

    return r"""
\draw [connection]  """+of+"""    -- node {\midarrow} """+to+""";
"""


def to_skip(of, to, pos=1.25):
    return r"""
\path (""" + of + """-southeast) -- (""" + of + """-northeast) coordinate[pos=""" + str(pos) + """] (""" + of + """-top) ;
\path (""" + to + """-south)  -- (""" + to + """-north)  coordinate[pos=""" + str(pos) + """] (""" + to + """-top) ;
\draw [copyconnection]  ("""+of+"""-northeast)  
-- node {\copymidarrow}("""+of+"""-top)
-- node {\copymidarrow}("""+to+"""-top)
-- node {\copymidarrow} ("""+to+"""-north);
"""


def to_legend():
    return r"""
  \matrix [draw,below left, column sep=1cm, row sep=0.3cm, nodes={font=\huge}] at (current bounding box.south east) {
  \node [convnode,label=right:Conv ($3 \times 3$) + ReLu] {}; &
  \node [poolnode,label=right:Max. Pooling ($2 \times 2$)] {}; &\\
  \node [fcnode,label=right:Fully Connected] {}; &
  \node [softmaxnode,label=right:Softmax] {}; \\
};
"""


def to_end():
    return r"""
\end{tikzpicture}
\end{document}
"""


def to_generate(arch, pathname="file.tex"):
    with open(pathname, "w") as f:
        for c in arch:
            print(c)
            f.write(c)
