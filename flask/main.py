import os
from flask import Flask, render_template, redirect
from xml.dom import minidom
from requests import get

storage_name = "storagee1"
container_name = "container1"


def bring_xml(url):
    artifact_list = []

    req = get(url, allow_redirects=True)
    open('test.xml', 'wb').write(req.content)
    xmldoc = minidom.parse('test.xml')
    itemlist = xmldoc.getElementsByTagName('Name')
    max_count = len(itemlist)
    current_count = 0
    for current_count in range(max_count):
        artifact_list.append(itemlist[current_count].childNodes[0].nodeValue)
        print(itemlist[current_count].childNodes[0].nodeValue)
    return artifact_list


app = Flask(__name__)

@app.route('/')
def dirtree():
    xml_url = 'https://%s.blob.core.windows.net/%s?restype=container&comp=list' % (storage_name, container_name)
    return render_template('dirtree.html', tree=bring_xml(xml_url))


@app.route('/<uri>')
def redirect_to_blob(uri):
    download_link = 'https://%s.blob.core.windows.net/%s/%s' % (storage_name, container_name, uri)
    return redirect(download_link, 301)

if __name__=="__main__":
    app.run()
