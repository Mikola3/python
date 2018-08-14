import time
start_time = time.time()

from sys import path
from xml.dom import minidom
import urllib2
import os
import re
import json

path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'myenv/Lib/site-packages'))) # name of pyenv virt.env
from jinja2 import Environment, FileSystemLoader


#ignored = ['.bzr', '$RECYCLE.BIN', '.DAV', '.DS_Store', '.git', '.hg', '.htaccess', '.htpasswd', '.Spotlight-V100', '.svn', '__MACOSX', 'ehthumbs.db', 'robots.txt', 'Thumbs.db', 'thumbs.tps']
#datatypes = {'audio': 'm4a,mp3,oga,ogg,webma,wav', 'archive': '7z,zip,rar,gz,tar', 'image': 'gif,ico,jpe,jpeg,jpg,png,svg,webp', 'pdf': 'pdf', 'quicktime': '3g2,3gp,3gp2,3gpp,mov,qt', 'source': 'atom,bat,bash,c,cmd,coffee,css,hml,js,json,java,less,markdown,md,php,pl,py,rb,rss,sass,scpt,swift,scss,sh,xml,yml,plist', 'text': 'txt', 'video': 'mp4,m4v,ogv,webm', 'website': 'htm,html,mhtm,mhtml,xhtm,xhtml'}
#icontypes = {'fa-music': 'm4a,mp3,oga,ogg,webma,wav', 'fa-archive': '7z,zip,rar,gz,tar', 'fa-picture-o': 'gif,ico,jpe,jpeg,jpg,png,svg,webp', 'fa-file-text': 'pdf', 'fa-film': '3g2,3gp,3gp2,3gpp,mov,qt', 'fa-code': 'atom,plist,bat,bash,c,cmd,coffee,css,hml,js,json,java,less,markdown,md,php,pl,py,rb,rss,sass,scpt,swift,scss,sh,xml,yml', 'fa-file-text-o': 'txt', 'fa-film': 'mp4,m4v,ogv,webm', 'fa-globe': 'htm,html,mhtm,mhtml,xhtm,xhtml'}

storage_name = "pkfunction"
container_name = "test"

xml_url = 'https://%s.blob.core.windows.net/%s?restype=container&comp=list' % (storage_name, container_name) # link to url where we can see in xml file all files in blob storage


def xml_bring_names(link):
    """Parse Blob Storage xml in order to get list of all names of artifacts."""
    artifact_list = []
    xmldoc = minidom.parse(urllib2.urlopen(link))
    itemlist = xmldoc.getElementsByTagName('Name')

    max_count = len(itemlist)
    current_count = 0
    for current_count in range(max_count):
        file = str(itemlist[current_count].childNodes[0].nodeValue)
        artifact_list.append(file)
    return artifact_list


def get_all_folders(somelist):
    """Generate a list of all folders, based on xml"""
    dirlist = []
    for elem in somelist:
        folder = os.path.dirname(elem) + "/"
        dirlist.append(folder)
    unique = list(set(dirlist))
    updated = ["" if elem == "/" else elem for elem in unique]
    return updated


def get_files_list(filelist, dir=''):
    """Return all files and folders from $dir."""
    file_list = []
    dir_list = []
    my_regex = re.compile(r"%s(\w+\/)" % (dir + "/"))

    dir_corrected = dir + "/"

    for elem in filelist:
        if dir_corrected in elem or dir_corrected == "/":
            if os.path.dirname(elem) == dir:
                file_list.append(os.path.basename(elem))
            else:
                if dir == "":
                    elem = "/" + elem
                result = my_regex.match(elem)
                dir_list.append(result.group(1))

    dir_list = list(set(dir_list))

    for x in dir_list:
        file_list.append(x)
    return file_list


def dir_or_file(somestring):
    """Simple function to determine whether argument is a file of dir"""
    if somestring[-1] == "/":
        return "dir"
    else:
        return "file"


def out_of_azure_function(some_html="no_body"):
    """Output of azure function in temp variable $res, that was specified in settings"""
    returnData = {
        #HTTP Status Code:
        "status": 200,        
        # Send any number of HTTP headers
        "headers": {
            "Content-Type": "text/html",
            "X-Awesome-Header": "YesItIs"
            }
        }
    
    if some_html != "no_body":
        returnData["body"] = some_html

    if "blob.core.windows.net" in some_html:
#        returnData["body"] = some_html
        returnData["status"] = 301
        returnData["headers"]["Location"] = some_html

    output = open(os.environ['res'], 'w')
    result = output.write(json.dumps(returnData))
    print("--- %s seconds ---" % (time.time() - start_time))
    return result


def gimme_page(p=''):
    """Render HTML-page or return a redirect link depending of URI given."""
    root = os.path.expanduser('')

    path = os.path.join(root, p)
    files = xml_bring_names(xml_url)

    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('index.html')

    if path in get_all_folders(files):
        contents = []
        for filename in get_files_list(files, path[:-1]):
            info = {}
            info['type'] = dir_or_file(filename)
            if info['type'] == "dir":
                info['name'] = filename[:-1]
            else:
                info['name'] = filename
            contents.append(info)
        page = template.render(path=p, contents=contents)
    elif path in files:
        print("i'm in elif")
        page = 'https://%s.blob.core.windows.net/%s/%s' % (storage_name, container_name, path)
    else:
#        pass
        page = "<h1>Something went wrong. You shouldn't have seen it.</h1>"
    out_of_azure_function(page)


def get_uri_from_trigger():
    """Obtain URI from GET Request."""
    uri = os.environ["REQ_HEADERS_X-ORIGINAL-URL"][1:] # get uri from environment variable
    gimme_page(uri)


def get_or_head():
    """Define further logic of work depending on what kind of request has been triggered."""
    if os.environ['REQ_METHOD'] == "GET":
        get_uri_from_trigger()
    elif os.environ['REQ_METHOD'] == "HEAD":
        out_of_azure_function()


if __name__ == "__main__":
    """Kind of entry point."""
#    print(os.environ['REQ_METHOD'])
    get_or_head()
