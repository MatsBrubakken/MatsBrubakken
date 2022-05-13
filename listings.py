\usepackage{listings}

\usepackage{caption}
\renewcommand{\lstlistingname}{Kodeuddrag} % Listing -> Snippet
\lstloadlanguages{C,C++,csh,Java}

\definecolor{codegreen}{RGB}{0, 204, 122}
\definecolor{codered}{RGB}{204, 0, 0}
\definecolor{codeblue}{RGB}{0, 82, 204}
\definecolor{codeTurkey}{RGB}{97, 199, 210}
\definecolor{darkerBlue}{RGB}{61, 0, 204}
\definecolor{forestGreen}{RGB}{34,139,34}
\definecolor{codeorange}{RGB}{240, 161, 24}

\lstdefinestyle{Python}{
    language        = Python,
    numbers=left,
    numberstyle=\scalebox{.6},
    numbersep=5pt,
    tabsize=2,
    extendedchars=true,
    breaklines=true,
    frame=single,
    xleftmargin=17pt,
    framexleftmargin=17pt,
    framexrightmargin=5pt,
    framexbottommargin=4pt,
    showspaces=false,
    showtabs=false,
    morecomment=[l]{//}, %use comment-line-style!
    morecomment=[s]{/*}{*/}, %for multiline comments
    showstringspaces=false,
        basicstyle=\scriptsize\ttfamily,
    captionpos=b,
    classoffset=1, % starting new class,
    morestring=[b]',
    morestring=[b]"
    keywordstyle    = \color{codered},
    keywordstyle    = [2] \color{teal}, % just to check that it works
    stringstyle     = \color{codeorange},
    commentstyle    = \color{forestGreen}\ttfamily,
    emphstyle={\color{codeblue}},
    emph={True, False, None, and, or, not, in, is, if, elif, else, for, while, break, continue, else, def, class, with, as, pass, lambda, return, yield, import, from, try, except, raise, finally, assert, async, await, del, global, nonlocal}
}
