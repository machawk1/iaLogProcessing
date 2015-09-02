# To change this template, choose Tools | Templates
# and open the template in the editor.
import sys

import gzip
import os
import re
import zipfile

__author__ = "yasmin"
__date__ = "$Oct 17, 2012 10:10:37 AM$"

if __name__ == "__main__":
    count = 0
    w = open("z:\\log30_filter.txt", 'w');
    wr = open("z:\\log30_filter_rawFormat.txt", 'w');
    #fh = gzip.GzipFile("z:\\samplelog.txt", 'r')
    fh = open("z:\\filterlog_30min.txt", 'r')
    #0.129.220.44 - - [02/Feb/2012:00:01:03 +0000] "GET http://wayback.archive.org/web/jsp/Interstitial.jsp?seconds=5&date=1262392557000&url= HTTP/1.1" 200 2137 "http://www.fastpasstv.ms/movies/bolt-2008/" "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)"
    #   0         1 2        3                4      5                        6                                                                 7        8   9                 10                                     11
    for line in fh: #zf.read(filename).split("\n"):
        count = count + 1;
        if count % 10000 == 0:
            print count
        #print line
        list = line.split(' ');

        if len(list) <12:
       #     print line;
            continue;
        ip = list[0]
        if len(list[3]) < 2:
            continue;
        logtime = list[3][1:];
        #GET,http://wayback.archive.org/web/*/http://edutwist.com,HTTP/1.1
        uri = ""
        if list[5].endswith("GET"):
            uri = list[6];
        else:
            continue;

        if uri.endswith(".js") or uri.endswith(".png") or uri.endswith(".css") or uri.endswith(".jpg") or uri.endswith(".gif") or uri.endswith(".ico"):
                continue;
        #20101122150451cs_
        if uri.startswith("http://liveweb") or uri.startswith("http://static"):
                continue;
        if uri.find("jsp/graph.jsp")>0:
            continue;
        dateExpression = re.compile( r"\d\d\d\d\d\d\d\d\d\d\d\d\d\d(js_|cs_|im_|fw_)" )
        result = dateExpression.search( uri )
        if result:
            continue




        status = list[8]
        if status != "200":
            continue
        ref = list[10][1:len(list[10])-1];
        #if  ref == "\"-\"":
        #    continue
        agent = list[11][1:]
        agent = agent.lower()
        #print agent
        if agent.startswith("mozilla") or agent.startswith("firefox") or agent.startswith("opera") or agent.startswith("microsoft")  or agent.startswith("safari") or agent.startswith("chrome")  :
            w.write(ip + "\t" + logtime + "\t" + uri + "\t" + ref + "\t" + agent + "\n");
            w.flush();

            wr.write(line);
    w.close()
    wr.close()

#        except KeyError:
#            print 'ERROR: Did not find %s in zip file' % filename
#        else:
#            print filename, ':'
#            print repr(data)
#        print




     