#!/usr/bin/env python

import urllib
from sgmllib import SGMLParser

class PageParser(SGMLParser):
  def reset(self):
    self.datas=[]
    SGMLParser.reset(self)
  def parse(self,data):
    self.feed(data)
    self.close()
  def handle_data(self,data):
    if not data.isspace(): 
      self.datas.append(data.strip())

class NodeMonitor:
  def __init__(self):
    self.node_stat = {}

  def fetch_page(self, url):
    response = urllib.urlopen(url)
    page = response.read() 
    return page
  
  def parse_page(self, page):
    parser = PageParser()
    parser.parse(page)
    return parser.datas
  
  def fetch_node_stat(self):
    page = self.fetch_page("http://www.nas.nasa.gov/monitoring/hud/realtime/pleiadespanel1.html")
    raw_data = self.parse_page(page)
    self.node_stat = {
      'har_in_use':raw_data[13],
      'har_available':raw_data[15],
      'har_free':raw_data[17],
      'neh_in_use':raw_data[20],
      'neh_available':raw_data[22],
      'neh_free':raw_data[24],
      'san_in_use':raw_data[27],
      'san_available':raw_data[29],
      'san_free':raw_data[31],
      'wes_in_use':raw_data[34],
      'wes_available':raw_data[36],
      'wes_free':raw_data[38],
    }

class NodeScheduler:
  def __init__(self):
    self.node_types = [
      {'model':'san', 'ncpus':16},
      {'model':'wes', 'ncpus':12},
      {'model':'neh', 'ncpus':8},
      {'model':'har', 'ncpus':8}]
    self.node_monitor = NodeMonitor()

  def reserve(self, node_type, num_req_cpus):
    num_available_nodes = int(self.node_monitor.node_stat[node_type['model']+'_available'])  
    model = node_type['model']
    ncpus = node_type['ncpus']
    select = 0
    while(num_req_cpus>0 and num_available_nodes>0):
      num_req_cpus -= ncpus
      num_available_nodes -= 1
      select += 1
    reserved_node = {'model':model, 'ncpus':ncpus, 'select':select}
    return (reserved_node, num_req_cpus)

  def schedule(self, mode, num_req_cpus):
    self.node_monitor.fetch_node_stat()
    if mode == 'performance':
      for t in self.node_types:
        if num_req_cpus <= 0:
          break
        reserved_node, num_req_cpus = self.reserve(t, num_req_cpus)
        return reserved_node
    elif mode == 'cost':
      for t in reversed(self.node_types):
        if num_req_cpus <= 0:
          break
        reserved_node, num_req_cpus = self.reserve(t, num_req_cpus)
        return reserved_node

    return None

if __name__ == "__main__":
  scheduler = NodeScheduler()
  print scheduler.schedule('performance', 5000)
  print scheduler.schedule('cost', 17)
