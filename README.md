oai2pairtree
============

oai2pairtree.py harvests records from an [oai-pmh](http://www.openarchives.org/OAI/openarchivesprotocol.html) repository and stores them in a [pairtree](https://confluence.ucop.edu/display/Curation/PairTree) on the filesystem. 

Usage
-----

    oai2pairtree.py http://www.pubmedcentral.nih.gov/oai/oai.cgi 

or if you want to limit to a particular set:

    oai2pairtree.py http://www.pubmedcentral.nih.gov/oai/oai.cgi --set pmc-open

or if you want to also limit to a particular kind of record metadata:

    oai2pairtree.py http://www.pubmedcentral.nih.gov/oai/oai.cgi --set pmc-open --metadata_prefix pmc

Installation
------------

oai2pairtree requires that the [lxml](http://lxml.de/) and [ptree](http://pypi.python.org/pypi/ptree) to run.  The best way to get these is to:

    easy_install oai2pairtree

or:

    pip install oai2pairtree

or, if you prefer:

    git clone https://edsu@github.com/edsu/oai2pairtree.git
    cd oai2pairtree
    python setup.py install

License
-------

* CC0
