import random
import string
from django.conf import settings
from urllib.request import urlopen
from bs4 import BeautifulSoup


SHORT_CODE_MIN = getattr(settings, 'SHORT_CODE_MIN', 8)

def code_generator(size=SHORT_CODE_MIN , chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_short_code(clazz, size=SHORT_CODE_MIN):
    new_code = code_generator(size=size)
    qs_exists = clazz.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_short_code(clazz, size=size)
    return new_code

def is_exist_url(url):
    try:
      return urlopen(url).read()
    except:
        return None

def get_description_text_from_html(data):
    try:
       soup = BeautifulSoup(data, 'html.parser')
       sorted_html = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span'], limit=1)
       if len(sorted_html):
          return sorted_html[0].text
    except:
        return None

def initialize_url(clazz, protocol, domain, sh_url=None):
    if sh_url:
        sh_url = sh_url.replace('/', '')
        return '{}://{}/{}/'.format(protocol, domain, sh_url)
    return '{}://{}/{}/'.format(protocol, domain, create_short_code(clazz))



