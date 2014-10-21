# A poor man's literate programming tool

Write your documentation and code in one file. Usage:

    poorweb.py <src> <tex dst> <default code dst>

# How it works

poorweb looks for code chunks enclosed by a line beginning with `>>` and a
line beginning with `<<`. It then collects those code chunks into the file
named after the starting `>>` (the name after `<<` is ignored). When no file
is named, it collects them into the default code file.

# An example

Write the following in `hello.web`:

    \documentclass{article}
    \begin{document}
    Hello world in \textsf{Python}:

    >>
    print 'Hello world!'
    <<

    Hello world in \textsf{PHP}:

    >>hello.php
    <?php
    echo 'Hello world!'
    ?>
    <<hello.php

    To make our python say another hello, simply append:

    >>
    print 'Hello world again!'
    <<
    \end{document}

Run:

    python twoweb.py hello.web hello.tex hello.py

`hello.php`, which is named in the source, will also be created.
