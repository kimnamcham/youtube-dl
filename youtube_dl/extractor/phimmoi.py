# coding: utf-8
from __future__ import unicode_literals

import re

from .common import InfoExtractor
from ..utils import (
    ExtractorError,
    int_or_none,
    update_url_query,
)

class PHIMMOIIE(InfoExtractor):
    # _VALID_URL = r'https?://khoai\.tv/phim/(?:[^/]+-)(?P<id>[0-9]+)'
    # _VALID_URL = r'https?://(?:www\.)?khoai\.tv/(?:[^/]+/)*.*?-(?P<id>)'
    # _VALID_URL = r'https?://(?:www\.)?phimmoi\.net/phim/(?P<id>([^/]+/)*[^/?#]+)/xem-phim.html'
    _VALID_URL = r'https?://wwww\.phimmoi\.net/phim/(?P<id>[^/]+)/xem-phim\.html'
    _TEST = {
        'url':'http://www.phimmoi.net/phim/toa-thap-choc-troi-6751/xem-phim.html',
        'md5': '344558ccfea74d33b7adbce22e577f54',
        'info_dict': {
            'id': 'toa-thap-choc-troi-6751',
            'ext': 'mp4',
            'title': 'Xem phim Tòa Tháp Chọc Trời-Skyscraper (2018) [Full HD-Vietsub+Thuyết minh]',
            'thumbnail': r're:https?://.*\.(?:jpg|png)',
        }
    }
    

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)

        # TODO more code goes here, for example ...
        title = self._html_search_meta('title', webpage, 'title', fatal=True)
        description = self._html_search_meta('description', webpage, 'description')

        media_urls = re.findall(r'data-contenturl="([^"]+)"', webpage)
        media_urls.extend(re.findall(r'var\s+filePath\s*=\s*"([^"]+)"', webpage))
        media_urls.extend(re.findall(r'\'file\'\s*:\s*["\']([^"\']+)["\'],', webpage))
        return {
            'id': video_id,
            'title': title,
            'description': description,
            'urls':media_urls
        }