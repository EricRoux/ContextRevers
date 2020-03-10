from urllib.parse import urlparse, quote, unquote


def encode(text):
    '''
    URL Encoder
    Replace special characters in string using the %xx escape.

    example:
        In[1]: print(quote('https://context.reverso.net/перевод/английский-русский/times'))
        Out[1]: 'https://context.reverso.net/%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4/%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9-%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9/times'

    :param text:    Decoded URL
    :return:        Encoded URL
    '''
    url = urlparse(text)
    return url._replace(path=quote(url.path)).geturl()


def decode(text):
    '''
        URL Encoder
        Replace %xx escapes by their single-character equivalent

        example:
            In[1]: print(quote('https://context.reverso.net/%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4/%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9-%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9/times'))
            Out[1]: 'https://context.reverso.net/перевод/английский-русский/times'

        :param text:    Encoded URL
        :return:        Decoded URL
        '''
    url = urlparse(text)
    return url._replace(path=unquote(url.path)).geturl()
