def intercept(response, mock, mock_response, interceptor):
    response.headers['custom_interceptor_from_file'] = 'intercepted'
    return response

intercept(response, mock, mock_response, interceptor)