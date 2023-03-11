# response - flask response (ProxyResponse)
# mock - Mock object if found (Mock)
# mock_response - Mock response object if found (MockResponse)
# interceptor - Interceptor object  which can send json configuration (MockResponseInterceptor)
def intercept(response, mock, mock_response, interceptor):
    # custom behaviour

    # mutating object is allowed
    # response.headers['custom_interceptor_from_file'] = 'intercepted'

    # handling parameters
    # from app.utils.utils import to_list
    # configuration = json.loads(interceptor.configuration)
    # param1 = configuration.get('param1', None)
    # param2 = configuration.get('param2', None)

    return response

# required to intercept action
intercept(response, mock, mock_response, interceptor)