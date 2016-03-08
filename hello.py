def app (environ, start_response):
  status = '200 OK'
  response_headers = [('Content-Type','text/plain')]
  start_response(status, response_headers)
  response = environ['QUERY_STRING'].split("&")
  response = [item+"\r\n" for item in response]
  return response