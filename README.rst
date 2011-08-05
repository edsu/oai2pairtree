oai2pairtree.py harvests records from an `oai-pmh <http://www.openarchives.org/OAI/openarchivesprotocol.html>`_ repository and stores them in a `pairtree <https://confluence.ucop.edu/display/Curation/PairTree>`_ on the filesystem. 

For example:

    oai2pairtree.py http://www.pubmedcentral.nih.gov/oai/oai.cgi 

or if you want to limit to a particular set:

    oai2pairtree.py http://www.pubmedcentral.nih.gov/oai/oai.cgi --set pmc-open

or if you want to also limit to a particular kind of record metadata:

    oai2pairtree.py http://www.pubmedcentral.nih.gov/oai/oai.cgi --set pmc-open --metadata_prefix pmc

Installation:

    easy_install oai2pairtree

or:

    python setup.py install

