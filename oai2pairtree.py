#!/usr/bin/env python

import os
import optparse

from lxml import etree
from ptree import id2ptree

ns = {'oai': 'http://www.openarchives.org/OAI/2.0/'}

def harvest(base_url, metadata_prefix='oai_dc', set_name=None):
    url = "%s?verb=ListRecords&metadataPrefix=%s" % (base_url, metadata_prefix)
    if set_name:
        url += "&set=%s" % set_name

    while True:
        doc = etree.parse(url)
        for record in doc.xpath('oai:ListRecords/oai:record', namespaces=ns):
            # determine the record identifier
            id = record.xpath('string(oai:header/oai:identifier)', namespaces=ns)

            # write out the record to a pair tree
            d = "data" + id2ptree(id)

            if not os.path.isdir(d):
                os.makedirs(d)

            p = os.path.join(d, "%s-%s.xml" % (id, metadata_prefix))
            open(p, "w").write(etree.tostring(record))

            print "saved %s as %s" % (id, p)

        # handle resumption token
        t = doc.xpath('string(oai:ListRecords/oai:resumptionToken)', namespaces=ns)
        if not t:
            break
        url = "%s?verb=ListRecords&resumptionToken=%s" % (base_url, t)


def main():
    parser = optparse.OptionParser(usage="oai2pairtree.py [oai-pmh base URL]")
    parser.add_option('-m', '--metadata_prefix', dest='metadata_prefix', default='oai_dc')
    parser.add_option('-s', '--set', dest='set')
        
    (opts, args) = parser.parse_args()
    if len(args) != 1:
        parser.error("must supply base URL for oai-pmh repository")
    harvest(args[0], metadata_prefix=opts.metadata_prefix, set_name=opts.set)


if __name__ == "__main__":
    main()
