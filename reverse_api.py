import requests


def find_video_ID(query_string):
    print(query_string)
    cookies = {
        'VISITOR_INFO1_LIVE': 'aaprLFuYbz0',
        'VISITOR_PRIVACY_METADATA': 'CgJDQRICGgA%3D',
        'NID': '511=sonQLgoBmW8Ha9SmprVAoaHhWNZjj94yWGO3HvfThSJ0XerrTzltuZkvsp6QtHTmEV-dEAH0fvudCBRYxVGWe6-RZWtDKXleM4vG6T-IS0z_f0w18ojUBiA7ArZAGblIAevM1Q1nSDtQgolf7-0EGLjki380O2u4EwCm5IiQjXSxV2m-DZZqIaQEU8he-kob',
        'LOGIN_INFO': 'AFmmF2swRQIgPP8RaEHYZhb-SoW4a49d1r3KufoDvpo6BokkUB2BUsACIQCXGgiQKUCQaSJhbVj5u191R3mXPFbxpYCZsr_7N2Vzxw:QUQ3MjNmeEd1X2tBNzgtbWRLOTRDRVRqMU85VmNjeGE5SU15SFRnQ2laVU5TbW1JZEpPcEVndWFBS2k2c3RRcmkyUC13ZUZfcGNweUYxZm9TeTNEWEh1TGI0X3FjWG9ONVFwX25La0hrdGxPQ0ZQSWFuMkJkaG9BcWE5RWJZRnZCTVcxVDNUWWE0VUtnazdPNDMweDduOEZqY1YxYXdvNlgxUnRreC1Gb3pmX2FKYmpEOEk3TFNYSkwzVGhxdFItUGZVdFc4RUd3U1lUNmNCMlhTSFdIVXAzUkloUHFRYWVUQQ==',
        'HSID': 'AQaAf33kyDwRgz204',
        'SSID': 'AvOAPWzpWW_5HyUys',
        'APISID': 'CCmXfgaBy4KgPHkf/Ayt8HeBX56AmbV9kr',
        'SAPISID': 'lYSoCdGi7qJo29dn/AcuKs-wfmCezUtsOG',
        '__Secure-1PAPISID': 'lYSoCdGi7qJo29dn/AcuKs-wfmCezUtsOG',
        '__Secure-3PAPISID': 'lYSoCdGi7qJo29dn/AcuKs-wfmCezUtsOG',
        'YSC': 'wZCaQ0PV0kw',
        'wide': '1',
        'SID': 'dQhxVc26CfNl03RLIoQ0dNHx4m5MBeyoRJuvmSJqlJ8KqezGqJGL_-Ah0zBH7H0F7Pw_bw.',
        '__Secure-1PSID': 'dQhxVc26CfNl03RLIoQ0dNHx4m5MBeyoRJuvmSJqlJ8KqezGWxYG8DNDSTKvwhz6BYpPCw.',
        '__Secure-3PSID': 'dQhxVc26CfNl03RLIoQ0dNHx4m5MBeyoRJuvmSJqlJ8KqezGMk42drac7PXfbBFmMk1xEQ.',
        '__Secure-1PSIDTS': 'sidts-CjEBNiGH7qGO9ge-qWhItlHFx5UIrRS97fL1iYFcmAg8FKSJxDQgHcJpqL4xAn6hx1NYEAA',
        '__Secure-3PSIDTS': 'sidts-CjEBNiGH7qGO9ge-qWhItlHFx5UIrRS97fL1iYFcmAg8FKSJxDQgHcJpqL4xAn6hx1NYEAA',
        'PREF': 'f6=40000480&f7=100&tz=America.Vancouver&f5=30000&autoplay=true',
        'SIDCC': 'ACA-OxPVEvZaSkzVTzZzo3fHNtjUCPs9Ry3Qz7lV7U6exo6NlCWK7ZEDanBKw3B5kIndVoTh4QQ',
        '__Secure-1PSIDCC': 'ACA-OxMaGRi0KfSWcj5Bbz-9XtGVKk53-VkvwS9Z4psR456WhCnacf4dtLD3wAKX9YV8lXDYgEg',
        '__Secure-3PSIDCC': 'ACA-OxN4pAhg6JaWoVIqPeXk9BYekPBlHAd2eLR6GiDQnqyg3rCPAocPL2lqpG7yGG75Z5EpQEYT',
    }

    headers = {
        'authority': 'music.youtube.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': 'SAPISIDHASH 1700551637_e7ede34abe2ab74fedf84ba78a86b317f659ef06',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        # 'cookie': 'VISITOR_INFO1_LIVE=aaprLFuYbz0; VISITOR_PRIVACY_METADATA=CgJDQRICGgA%3D; NID=511=sonQLgoBmW8Ha9SmprVAoaHhWNZjj94yWGO3HvfThSJ0XerrTzltuZkvsp6QtHTmEV-dEAH0fvudCBRYxVGWe6-RZWtDKXleM4vG6T-IS0z_f0w18ojUBiA7ArZAGblIAevM1Q1nSDtQgolf7-0EGLjki380O2u4EwCm5IiQjXSxV2m-DZZqIaQEU8he-kob; LOGIN_INFO=AFmmF2swRQIgPP8RaEHYZhb-SoW4a49d1r3KufoDvpo6BokkUB2BUsACIQCXGgiQKUCQaSJhbVj5u191R3mXPFbxpYCZsr_7N2Vzxw:QUQ3MjNmeEd1X2tBNzgtbWRLOTRDRVRqMU85VmNjeGE5SU15SFRnQ2laVU5TbW1JZEpPcEVndWFBS2k2c3RRcmkyUC13ZUZfcGNweUYxZm9TeTNEWEh1TGI0X3FjWG9ONVFwX25La0hrdGxPQ0ZQSWFuMkJkaG9BcWE5RWJZRnZCTVcxVDNUWWE0VUtnazdPNDMweDduOEZqY1YxYXdvNlgxUnRreC1Gb3pmX2FKYmpEOEk3TFNYSkwzVGhxdFItUGZVdFc4RUd3U1lUNmNCMlhTSFdIVXAzUkloUHFRYWVUQQ==; HSID=AQaAf33kyDwRgz204; SSID=AvOAPWzpWW_5HyUys; APISID=CCmXfgaBy4KgPHkf/Ayt8HeBX56AmbV9kr; SAPISID=lYSoCdGi7qJo29dn/AcuKs-wfmCezUtsOG; __Secure-1PAPISID=lYSoCdGi7qJo29dn/AcuKs-wfmCezUtsOG; __Secure-3PAPISID=lYSoCdGi7qJo29dn/AcuKs-wfmCezUtsOG; YSC=wZCaQ0PV0kw; wide=1; SID=dQhxVc26CfNl03RLIoQ0dNHx4m5MBeyoRJuvmSJqlJ8KqezGqJGL_-Ah0zBH7H0F7Pw_bw.; __Secure-1PSID=dQhxVc26CfNl03RLIoQ0dNHx4m5MBeyoRJuvmSJqlJ8KqezGWxYG8DNDSTKvwhz6BYpPCw.; __Secure-3PSID=dQhxVc26CfNl03RLIoQ0dNHx4m5MBeyoRJuvmSJqlJ8KqezGMk42drac7PXfbBFmMk1xEQ.; __Secure-1PSIDTS=sidts-CjEBNiGH7qGO9ge-qWhItlHFx5UIrRS97fL1iYFcmAg8FKSJxDQgHcJpqL4xAn6hx1NYEAA; __Secure-3PSIDTS=sidts-CjEBNiGH7qGO9ge-qWhItlHFx5UIrRS97fL1iYFcmAg8FKSJxDQgHcJpqL4xAn6hx1NYEAA; PREF=f6=40000480&f7=100&tz=America.Vancouver&f5=30000&autoplay=true; SIDCC=ACA-OxPVEvZaSkzVTzZzo3fHNtjUCPs9Ry3Qz7lV7U6exo6NlCWK7ZEDanBKw3B5kIndVoTh4QQ; __Secure-1PSIDCC=ACA-OxMaGRi0KfSWcj5Bbz-9XtGVKk53-VkvwS9Z4psR456WhCnacf4dtLD3wAKX9YV8lXDYgEg; __Secure-3PSIDCC=ACA-OxN4pAhg6JaWoVIqPeXk9BYekPBlHAd2eLR6GiDQnqyg3rCPAocPL2lqpG7yGG75Z5EpQEYT',
        'origin': 'https://music.youtube.com',
        'pragma': 'no-cache',
        'referer': 'https://music.youtube.com/',
        'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'same-origin',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
        'x-goog-authuser': '4',
        'x-goog-pageid': '100322064526774765897',
        'x-goog-visitor-id': 'CgthYXByTEZ1WWJ6MCjKt_GqBjIICgJDQRICGgA%3D',
        'x-origin': 'https://music.youtube.com',
        'x-youtube-bootstrap-logged-in': 'true',
        'x-youtube-client-name': '67',
        'x-youtube-client-version': '1.20231113.01.00',
    }

    params = {
        'key': 'AIzaSyC9XL3ZjWddXya6X74dJoCTL-WEYFDNX30',
        'prettyPrint': 'false',
    }

    json_data = {
        'context': {
            'client': {
                'hl': 'en',
                'gl': 'CA',
                'remoteHost': '2001:569:7664:c200:597a:dcd:f80e:41a',
                'deviceMake': '',
                'deviceModel': '',
                'visitorData': 'CgthYXByTEZ1WWJ6MCjKt_GqBjIICgJDQRICGgA%3D',
                'userAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0,gzip(gfe)',
                'clientName': 'WEB_REMIX',
                'clientVersion': '1.20231113.01.00',
                'osName': 'Windows',
                'osVersion': '10.0',
                'originalUrl': 'https://music.youtube.com/',
                'platform': 'DESKTOP',
                'clientFormFactor': 'UNKNOWN_FORM_FACTOR',
                'configInfo': {
                    'appInstallData': 'CMq38aoGEPX5rwUQqfevBRDQjbAFEKKSsAUQ3ej-EhCigbAFEOno_hIQzN-uBRCIh7AFENSSsAUQrtT-EhCWlbAFEMeDsAUQ0OKvBRC_968FEKf3rwUQlPr-EhC9tq4FELfvrwUQ1YiwBRCI468FENnJrwUQo5KwBRDrk64FELOSsAUQ9fv-EhC4i64FEMn3rwUQvPmvBRDm_f4SEOvo_hIQ4fKvBRCst68FEJrwrwUQpoGwBRDqw68FEL2KsAUQpcL-EhDT4a8FEL75rwUQzK7-EhCZlLAFEOe6rwUQ_IWwBRD9uP0SEKuCsAUQqIGwBRDks_4SEJ2LsAUQt-r-EhDaibAF',
                    'coldConfigData': 'CMq38aoGEO26rQUQ65OuBRC9tq4FEPzorgUQ_uiuBRDX7q4FEKTFrwUQ-sevBRCW7q8FEP7vrwUQ4fKvBRCigbAFEMeDsAUQsoiwBRDaibAFEL2KsAUQnYuwBRDQjbAFEKOPsAUQ-ZGwBRCekrAFEKKSsAUQo5KwBRCzkrAFENSSsAUQ7ZKwBRCZlLAFEJaVsAUQqJewBRoyQU9qRm94MGNrQ2QyeWNfb29jY2xxVnFmWkdUQzJvN2hkNTlVcGNQbnFBSEVjZ0d0TVEiMkFPakZveDFkOEk5NEIwQVFfRHozeVZ3UncwM1F2WFFDSG1lcGh5Z0V2SEttQ0l5VGtnKlxDQU1TUHcwZmdwYW9Bc2dXX2dXbUg5SVNfUWFQR2RVQV9BQ0VDUEFGRlNTU2d0QU0yX1lHamg2eVJ0NWluUy1EaEFXVjNBYWYwY3dMMnppNDdRWUVzWXVYRFE9PQ%3D%3D',
                    'coldHashData': 'CMq38aoGEhQxNzE1NzEzNDQ4NDg3NTc3NzgyNxjKt_GqBjIyQU9qRm94MGNrQ2QyeWNfb29jY2xxVnFmWkdUQzJvN2hkNTlVcGNQbnFBSEVjZ0d0TVE6MkFPakZveDFkOEk5NEIwQVFfRHozeVZ3UncwM1F2WFFDSG1lcGh5Z0V2SEttQ0l5VGtnQlxDQU1TUHcwZmdwYW9Bc2dXX2dXbUg5SVNfUWFQR2RVQV9BQ0VDUEFGRlNTU2d0QU0yX1lHamg2eVJ0NWluUy1EaEFXVjNBYWYwY3dMMnppNDdRWUVzWXVYRFE9PQ%3D%3D',
                    'hotHashData': 'CMq38aoGEhM2MTYzNzQ5Njk0OTkwOTc0NjE0GMq38aoGKJTk_BIo3JP9EijGsv0SKKq0_RIonpH-Eiiarf4SKMjK_hIo3c7-Eiio4f4SKOvn_hIoovX-Eiiy-f4SKOb7_hIo8vv-Eij1-_4SKN39_hIo5v3-Eij5_f4SKMX-_hIyMkFPakZveDBja0NkMnljX29vY2NscVZxZlpHVEMybzdoZDU5VXBjUG5xQUhFY2dHdE1ROjJBT2pGb3gxZDhJOTRCMEFRX0R6M3lWd1J3MDNRdlhRQ0htZXBoeWdFdkhLbUNJeVRrZ0IsQ0FNU0d3ME4ySV81RmNvQXFEbkFFUlVLamVMTkRJdnVBZkhnRHJXQUJBPT0%3D',
                },
                'userInterfaceTheme': 'USER_INTERFACE_THEME_DARK',
                'timeZone': 'America/Vancouver',
                'browserName': 'Edge Chromium',
                'browserVersion': '119.0.0.0',
                'acceptHeader': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'deviceExperimentId': 'ChxOek13TXpneE16WXlNRFkzTlRVME5qYzNOdz09EMq38aoGGMq38aoG',
                'screenWidthPoints': 1099,
                'screenHeightPoints': 932,
                'screenPixelDensity': 1,
                'screenDensityFloat': 1,
                'utcOffsetMinutes': -480,
                'musicAppInfo': {
                    'pwaInstallabilityStatus': 'PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED',
                    'webDisplayMode': 'WEB_DISPLAY_MODE_BROWSER',
                    'storeDigitalGoodsApiSupportStatus': {
                        'playStoreDigitalGoodsApiSupportStatus': 'DIGITAL_GOODS_API_SUPPORT_STATUS_UNSUPPORTED',
                    },
                },
            },
            'user': {
                'lockedSafetyMode': False,
            },
            'request': {
                'useSsl': True,
                'internalExperimentFlags': [],
                'consistencyTokenJars': [],
            },
            'adSignalsInfo': {
                'params': [
                    {
                        'key': 'dt',
                        'value': '1700551627217',
                    },
                    {
                        'key': 'flash',
                        'value': '0',
                    },
                    {
                        'key': 'frm',
                        'value': '0',
                    },
                    {
                        'key': 'u_tz',
                        'value': '-480',
                    },
                    {
                        'key': 'u_his',
                        'value': '8',
                    },
                    {
                        'key': 'u_h',
                        'value': '1080',
                    },
                    {
                        'key': 'u_w',
                        'value': '1920',
                    },
                    {
                        'key': 'u_ah',
                        'value': '1040',
                    },
                    {
                        'key': 'u_aw',
                        'value': '1920',
                    },
                    {
                        'key': 'u_cd',
                        'value': '24',
                    },
                    {
                        'key': 'bc',
                        'value': '31',
                    },
                    {
                        'key': 'bih',
                        'value': '932',
                    },
                    {
                        'key': 'biw',
                        'value': '1087',
                    },
                    {
                        'key': 'brdim',
                        'value': '0,0,0,0,1920,0,1920,1040,1099,932',
                    },
                    {
                        'key': 'vis',
                        'value': '1',
                    },
                    {
                        'key': 'wgl',
                        'value': 'true',
                    },
                    {
                        'key': 'ca_type',
                        'value': 'image',
                    },
                ],
            },
        },
        'query': f'{query_string}',
        'suggestStats': {
            'validationStatus': 'VALID',
            'parameterValidationStatus': 'VALID_PARAMETERS',
            'clientName': 'youtube-music',
            'searchMethod': 'ENTER_KEY',
            'inputMethods': [
                'KEYBOARD',
            ],
            'originalQuery': f'{query_string}',
            'availableSuggestions': [
                {
                    'index': 0,
                    'type': 0,
                },
                {
                    'index': 1,
                    'type': 0,
                },
                {
                    'index': 2,
                    'type': 0,
                },
                {
                    'index': 3,
                    'type': 0,
                },
                {
                    'index': 4,
                    'type': 0,
                },
                {
                    'index': 5,
                    'type': 0,
                },
                {
                    'index': 6,
                    'type': 0,
                },
            ],
            'zeroPrefixEnabled': True,
            'firstEditTimeMsec': 2956,
            'lastEditTimeMsec': 10448,
        },
    }

    response = requests.post(
        'https://music.youtube.com/youtubei/v1/search',
        params=params,
        cookies=cookies,
        headers=headers,
        json=json_data,
    )
    

    contents = response.json()['contents']['tabbedSearchResultsRenderer']['tabs'][0]['tabRenderer']['content']['sectionListRenderer']['contents']

    song_content = [content for content in contents if "musicShelfRenderer" in content]
    
    return song_content[0]['musicShelfRenderer']['contents'][0]['musicResponsiveListItemRenderer']['overlay']['musicItemThumbnailOverlayRenderer']['content']['musicPlayButtonRenderer']['playNavigationEndpoint']['watchEndpoint']['videoId']


# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"context":{"client":{"hl":"en","gl":"CA","remoteHost":"2001:569:7664:c200:597a:dcd:f80e:41a","deviceMake":"","deviceModel":"","visitorData":"CgthYXByTEZ1WWJ6MCjKt_GqBjIICgJDQRICGgA%3D","userAgent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0,gzip(gfe)","clientName":"WEB_REMIX","clientVersion":"1.20231113.01.00","osName":"Windows","osVersion":"10.0","originalUrl":"https://music.youtube.com/","platform":"DESKTOP","clientFormFactor":"UNKNOWN_FORM_FACTOR","configInfo":{"appInstallData":"CMq38aoGEPX5rwUQqfevBRDQjbAFEKKSsAUQ3ej-EhCigbAFEOno_hIQzN-uBRCIh7AFENSSsAUQrtT-EhCWlbAFEMeDsAUQ0OKvBRC_968FEKf3rwUQlPr-EhC9tq4FELfvrwUQ1YiwBRCI468FENnJrwUQo5KwBRDrk64FELOSsAUQ9fv-EhC4i64FEMn3rwUQvPmvBRDm_f4SEOvo_hIQ4fKvBRCst68FEJrwrwUQpoGwBRDqw68FEL2KsAUQpcL-EhDT4a8FEL75rwUQzK7-EhCZlLAFEOe6rwUQ_IWwBRD9uP0SEKuCsAUQqIGwBRDks_4SEJ2LsAUQt-r-EhDaibAF","coldConfigData":"CMq38aoGEO26rQUQ65OuBRC9tq4FEPzorgUQ_uiuBRDX7q4FEKTFrwUQ-sevBRCW7q8FEP7vrwUQ4fKvBRCigbAFEMeDsAUQsoiwBRDaibAFEL2KsAUQnYuwBRDQjbAFEKOPsAUQ-ZGwBRCekrAFEKKSsAUQo5KwBRCzkrAFENSSsAUQ7ZKwBRCZlLAFEJaVsAUQqJewBRoyQU9qRm94MGNrQ2QyeWNfb29jY2xxVnFmWkdUQzJvN2hkNTlVcGNQbnFBSEVjZ0d0TVEiMkFPakZveDFkOEk5NEIwQVFfRHozeVZ3UncwM1F2WFFDSG1lcGh5Z0V2SEttQ0l5VGtnKlxDQU1TUHcwZmdwYW9Bc2dXX2dXbUg5SVNfUWFQR2RVQV9BQ0VDUEFGRlNTU2d0QU0yX1lHamg2eVJ0NWluUy1EaEFXVjNBYWYwY3dMMnppNDdRWUVzWXVYRFE9PQ%3D%3D","coldHashData":"CMq38aoGEhQxNzE1NzEzNDQ4NDg3NTc3NzgyNxjKt_GqBjIyQU9qRm94MGNrQ2QyeWNfb29jY2xxVnFmWkdUQzJvN2hkNTlVcGNQbnFBSEVjZ0d0TVE6MkFPakZveDFkOEk5NEIwQVFfRHozeVZ3UncwM1F2WFFDSG1lcGh5Z0V2SEttQ0l5VGtnQlxDQU1TUHcwZmdwYW9Bc2dXX2dXbUg5SVNfUWFQR2RVQV9BQ0VDUEFGRlNTU2d0QU0yX1lHamg2eVJ0NWluUy1EaEFXVjNBYWYwY3dMMnppNDdRWUVzWXVYRFE9PQ%3D%3D","hotHashData":"CMq38aoGEhM2MTYzNzQ5Njk0OTkwOTc0NjE0GMq38aoGKJTk_BIo3JP9EijGsv0SKKq0_RIonpH-Eiiarf4SKMjK_hIo3c7-Eiio4f4SKOvn_hIoovX-Eiiy-f4SKOb7_hIo8vv-Eij1-_4SKN39_hIo5v3-Eij5_f4SKMX-_hIyMkFPakZveDBja0NkMnljX29vY2NscVZxZlpHVEMybzdoZDU5VXBjUG5xQUhFY2dHdE1ROjJBT2pGb3gxZDhJOTRCMEFRX0R6M3lWd1J3MDNRdlhRQ0htZXBoeWdFdkhLbUNJeVRrZ0IsQ0FNU0d3ME4ySV81RmNvQXFEbkFFUlVLamVMTkRJdnVBZkhnRHJXQUJBPT0%3D"},"userInterfaceTheme":"USER_INTERFACE_THEME_DARK","timeZone":"America/Vancouver","browserName":"Edge Chromium","browserVersion":"119.0.0.0","acceptHeader":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","deviceExperimentId":"ChxOek13TXpneE16WXlNRFkzTlRVME5qYzNOdz09EMq38aoGGMq38aoG","screenWidthPoints":1099,"screenHeightPoints":932,"screenPixelDensity":1,"screenDensityFloat":1,"utcOffsetMinutes":-480,"musicAppInfo":{"pwaInstallabilityStatus":"PWA_INSTALLABILITY_STATUS_CAN_BE_INSTALLED","webDisplayMode":"WEB_DISPLAY_MODE_BROWSER","storeDigitalGoodsApiSupportStatus":{"playStoreDigitalGoodsApiSupportStatus":"DIGITAL_GOODS_API_SUPPORT_STATUS_UNSUPPORTED"}}},"user":{"lockedSafetyMode":false},"request":{"useSsl":true,"internalExperimentFlags":[],"consistencyTokenJars":[]},"adSignalsInfo":{"params":[{"key":"dt","value":"1700551627217"},{"key":"flash","value":"0"},{"key":"frm","value":"0"},{"key":"u_tz","value":"-480"},{"key":"u_his","value":"8"},{"key":"u_h","value":"1080"},{"key":"u_w","value":"1920"},{"key":"u_ah","value":"1040"},{"key":"u_aw","value":"1920"},{"key":"u_cd","value":"24"},{"key":"bc","value":"31"},{"key":"bih","value":"932"},{"key":"biw","value":"1087"},{"key":"brdim","value":"0,0,0,0,1920,0,1920,1040,1099,932"},{"key":"vis","value":"1"},{"key":"wgl","value":"true"},{"key":"ca_type","value":"image"}]}},"query":"last surprice lyn","suggestStats":{"validationStatus":"VALID","parameterValidationStatus":"VALID_PARAMETERS","clientName":"youtube-music","searchMethod":"ENTER_KEY","inputMethods":["KEYBOARD"],"originalQuery":"last surprice lyn","availableSuggestions":[{"index":0,"type":0},{"index":1,"type":0},{"index":2,"type":0},{"index":3,"type":0},{"index":4,"type":0},{"index":5,"type":0},{"index":6,"type":0}],"zeroPrefixEnabled":true,"firstEditTimeMsec":2956,"lastEditTimeMsec":10448}}'
#response = requests.post('https://music.youtube.com/youtubei/v1/search', params=params, cookies=cookies, headers=headers, data=data)