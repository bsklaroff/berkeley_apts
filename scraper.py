import urllib2

def parse_berk():
    url_list = []
    count = 0
    while True:
        f = urllib2.urlopen('http://sfbay.craigslist.org/search/apa/eby?nh=48&nh=49&s=' + str(count))
        url_line = ''
        while url_line == '':
            line = f.readline()
            if line.find('<!-- sphinx:') != -1:
                f.readline()
                url_line = f.readline()
        url_line = url_line.split('<a href="/search')[0]
        urls_split = url_line.split('<a href="')
        if len(urls_split) == 1:
            break
        for url_junk in urls_split:
            good_url = url_junk.split('">')
            if len(good_url) > 1:
                url_list.append(good_url[0])
        count += 100
    for url_str in url_list:
        parse_apt(url_str)
        
def parse_apt(url_str):
    f = urllib2.urlopen(url_str)
    post_title = ''
    post_time = ''
    while post_title == '':
        line = f.readline()
        if line.find('<h2>') != -1:
            post_title_split = line[4:].split('(berkeley')
            i = 0
            while i < len(post_title_split) - 1:
                post_title += post_title_split[i]
                i += 1
            break
    post_title = post_title.strip()
    if len(post_title) < 2:
        return
    print post_title

if __name__ == '__main__':
    parse_berk()
