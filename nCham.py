from urllib.request import urlopen
from urllib.parse import urlencode

from time import sleep

def randfline(fpath):
  from random import randint
  with open(fpath, encoding='euc-kr') as f:
    i=0
    for l in f:
      i += 1
    r=randint(1,i)
    f.seek(0)
    i=0
    for l in f:
      i += 1
      if i == r:
        return l
  return ''

if __name__ == '__main__':
  from subprocess import Popen, PIPE
  from random import uniform
  cnt=0
  logf = open('log.txt', 'a')
  while True:
    try:
      #if '만료'.encode('euc-kr') in Popen(['ping', '-n', '1', 'korcham.net'], stdout=PIPE).stdout.read():
      #  print('server closed')
      #  sleep(30)
      #  continue
      name = randfline('fuckers.txt').rstrip()
      addr = randfline('si-gu.txt').split()
      addr1 = addr[0]
      addr2 = '' if len(addr) == 1 else ' '.join(addr[1:])
      cnt += 1
      data=urlencode({'NM':name, 'POS':'', 'tmp_addr01':addr1,'tmp_addr02':addr2}, encoding='euc-kr')
      r=urlopen('http://www.korcham.net/main_pop.jsp', data.encode())
      log=' '.join(list(map(str, (cnt, name, addr1, addr2, r.msg, b'signconfirm4_2.asp' in r.read()))))
      print(log)
      print(log, file=logf)
      sleep(uniform(1,5))
    except KeyboardInterrupt:
      exit()
