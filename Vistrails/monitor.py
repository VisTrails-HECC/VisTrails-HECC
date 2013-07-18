'''
Created on Nov 29, 2012

@author: normanxin
'''

def get_page(url):
    import urllib
    response = urllib.urlopen(url)
    page = response.read() 
    return page

def get_cpu_use():
    page = get_page("http://www.nas.nasa.gov/monitoring/hud/realtime/pleiadespanel1.html")
    return page

def get_pbs_jobs():
    page = get_page("http://www.nas.nasa.gov/monitoring/hud/realtime/pleiadespanel2.html")
    return page

def get_filesystem_usage():
    page = get_page("http://www.nas.nasa.gov/monitoring/hud/realtime/pleiadespanel3.html")
    return page

def get_status_datas(page):
    from StatusParser import StatusParser
    parser=StatusParser()
    parser.parse(page)
    return parser.datas

def get_cpu_used():
    d = get_status_datas(get_cpu_use())
    return d[4]

def get_cpu_total():
    d = get_status_datas(get_cpu_use())
    return d[6]

def get_cpu_percent():
    d = get_status_datas(get_cpu_use())
    return d[7]

def get_harpertown_in_use():
    d = get_status_datas(get_cpu_use())
    return d[13]

def get_harpertown_available():
    d = get_status_datas(get_cpu_use())
    return d[15]

def get_harpertown_free():
    d = get_status_datas(get_cpu_use())
    return d[17]

def get_nehalem_in_use():
    d = get_status_datas(get_cpu_use())
    return d[20]

def get_nehalem_available():
    d = get_status_datas(get_cpu_use())
    return d[22]

def get_nehalem_free():
    d = get_status_datas(get_cpu_use())
    return d[24]

def get_sandy_bridge_in_use():
    d = get_status_datas(get_cpu_use())
    return d[27]

def get_sandy_bridge_available():
    d = get_status_datas(get_cpu_use())
    return d[29]

def get_sandy_bridge_free():
    d = get_status_datas(get_cpu_use())
    return d[31]

def get_westmere_in_use():
    d = get_status_datas(get_cpu_use())
    return d[34]

def get_westmere_available():
    d = get_status_datas(get_cpu_use())
    return d[36]

def get_westmere_free():
    d = get_status_datas(get_cpu_use())
    return d[38]

def get_held_jobs():
    d = get_status_datas(get_pbs_jobs())
    return d[4]

def get_queued_jobs():
    d = get_status_datas(get_pbs_jobs())
    return d[6]

def get_running_jobs():
    d = get_status_datas(get_pbs_jobs())
    return d[8]

def get_total_jobs():
    d = get_status_datas(get_pbs_jobs())
    return d[10]

def get_efficiency():
    d = get_status_datas(get_pbs_jobs())
    return d[13]

def get_stalled_jobs():
    d = get_status_datas(get_pbs_jobs())
    return d[16]

def get_most_nodes_used_per_job():
    d = get_status_datas(get_pbs_jobs())
    return d[18]

def get_most_cpus_used_per_job():
    d = get_status_datas(get_pbs_jobs())
    return d[20]

def get_longest_held_job():
    d = get_status_datas(get_pbs_jobs())
    return d[22]

def get_longest_queued_job():
    d = get_status_datas(get_pbs_jobs())
    return d[24]

def get_longest_running_job():
    d = get_status_datas(get_pbs_jobs())
    return d[26]

def get_nbp1_free():
    d = get_status_datas(get_filesystem_usage())
    return d[5]

def get_nbp1_used_percent():
    d = get_status_datas(get_filesystem_usage())
    return d[6][1:]

def get_nbp1_used():
    d = get_status_datas(get_filesystem_usage())
    return d[8]

def get_nbp2_free():
    d = get_status_datas(get_filesystem_usage())
    return d[11]

def get_nbp2_used_percent():
    d = get_status_datas(get_filesystem_usage())
    return d[12][1:]

def get_nbp2_used():
    d = get_status_datas(get_filesystem_usage())
    return d[14]

def get_nbp3_free():
    d = get_status_datas(get_filesystem_usage())
    return d[17]

def get_nbp3_used_percent():
    d = get_status_datas(get_filesystem_usage())
    return d[18][1:]

def get_nbp3_used():
    d = get_status_datas(get_filesystem_usage())
    return d[20]

def get_nbp4_free():
    d = get_status_datas(get_filesystem_usage())
    return d[23]

def get_nbp4_used_percent():
    d = get_status_datas(get_filesystem_usage())
    return d[24][1:]

def get_nbp4_used():
    d = get_status_datas(get_filesystem_usage())
    return d[26]

def get_nbp5_free():
    d = get_status_datas(get_filesystem_usage())
    return d[29]

def get_nbp5_used_percent():
    d = get_status_datas(get_filesystem_usage())
    return d[30][1:]

def get_nbp5_used():
    d = get_status_datas(get_filesystem_usage())
    return d[32] 

def get_nbp6_free():
    d = get_status_datas(get_filesystem_usage())
    return d[35]

def get_nbp6_used_percent():
    d = get_status_datas(get_filesystem_usage())
    return d[36][1:]

def get_nbp6_used():
    d = get_status_datas(get_filesystem_usage())
    return d[38]
