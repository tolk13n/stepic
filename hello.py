def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type','text/plain')]
    body = str()
    for i in environ['QUERY_STRING'].split('&'):
        body += i+'\r\n'
   # body = bytes(body, encoding = 'utf-8')
    start_response(status, headers)
    return [body]
