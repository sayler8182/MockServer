class StatusCode(object):
    def __init__(self,
                 code: int,
                 name: str,
                 description: str):
        self.code = code
        self.name = name
        self.description = description

    @staticmethod
    def supported_codes():
        return [
            StatusCode(100, 'Continue',
                       'Only a part of the request has been received by the server, but as long as it has not been '
                       'rejected, the client should continue with the request.'),
            StatusCode(101, 'Switching Protocols', 'The server switches protocol.'),
            StatusCode(200, 'OK', 'The request is OK.'),
            StatusCode(201, 'Created', 'The request is complete, and a new resource is created.'),
            StatusCode(202, 'Accepted', 'The request is accepted for processing, but the processing is not complete.'),
            StatusCode(203, 'Non-authoritative Information',
                       'The information in the entity header is from a local or third-party copy, not from the '
                       'original server.'),
            StatusCode(204, 'No Content',
                       'A status code and a header are given in the response, but there is no entity-body in the reply.'),
            StatusCode(205, 'Reset Content',
                       'The browser should clear the form used for this transaction for additional input.'),
            StatusCode(206, 'Partial Content',
                       'The server is returning partial data of the size requested. Used in response to a request '
                       'specifying a Range header. The server must specify the range included in the response with '
                       'the Content-Range header.'),
            StatusCode(300, 'Multiple Choices',
                       'A link list. The user can select a link and go to that location. Maximum five addresses.'),
            StatusCode(301, 'Moved Permanently', 'The requested page has moved to a new url.'),
            StatusCode(302, 'Found', 'The requested page has moved temporarily to a new url.'),
            StatusCode(303, 'See Other', 'The requested page can be found under a different url.'),
            StatusCode(304, 'Not Modified',
                       'This is the response code to an If-Modified-Since or If-None-Match header, where the URL has '
                       'not been modified since the specified date.'),
            StatusCode(305, 'Use Proxy',
                       'The requested URL must be accessed through the proxy mentioned in the Location header.'),
            StatusCode(306, 'Unused',
                       'This code was used in a previous version. It is no longer used, but the code is reserved.'),
            StatusCode(307, 'Temporary Redirect', 'The requested page has moved temporarily to a new url.'),
            StatusCode(400, 'Bad Request', 'The server did not understand the request.'),
            StatusCode(401, 'Unauthorized', 'The requested page needs a username and a password.'),
            StatusCode(402, 'Payment Required', 'You can not use this code yet.'),
            StatusCode(403, 'Forbidden', 'Access is forbidden to the requested page.'),
            StatusCode(404, 'Not Found', 'The server can not find the requested page.'),
            StatusCode(405, 'Method Not Allowed', 'The method specified in the request is not allowed.'),
            StatusCode(406, 'Not Acceptable',
                       'The server can only generate a response that is not accepted by the client.'),
            StatusCode(407, 'Proxy Authentication Required',
                       'You must authenticate with a proxy server before this request can be served.'),
            StatusCode(408, 'Request Timeout', 'The request took longer than the server was prepared to wait.'),
            StatusCode(409, 'Conflict', 'The request could not be completed because of a conflict.'),
            StatusCode(410, 'Gone', 'The requested page is no longer available.'),
            StatusCode(411, 'Length Required',
                       'The "Content-Length" is not defined. The server will not accept the request without it.'),
            StatusCode(412, 'Precondition Failed',
                       'The pre condition given in the request evaluated to false by the server.'),
            StatusCode(413, 'Request Entity Too Large',
                       'The server will not accept the request, because the request entity is too large.'),
            StatusCode(414, 'Request-url Too Long',
                       'The server will not accept the request, because the url is too long. Occurs when you convert '
                       'a "post" request to a "get" request with a long query information.'),
            StatusCode(415, 'Unsupported Media Type',
                       'The server will not accept the request, because the mediatype is not supported.'),
            StatusCode(416, 'Requested Range Not Satisfiable',
                       'The requested byte range is not available and is out of bounds.'),
            StatusCode(417, 'Expectation Failed',
                       'The expectation given in an Expect request-header field could not be met by this server.'),
            StatusCode(500, 'Internal Server Error',
                       'The request was not completed. The server met an unexpected condition.'),
            StatusCode(501, 'Not Implemented',
                       'The request was not completed. The server did not support the functionality required.'),
            StatusCode(502, 'Bad Gateway',
                       'The request was not completed. The server received an invalid response from the upstream '
                       'server.'),
            StatusCode(503, 'Service Unavailable',
                       'The request was not completed. The server is temporarily overloading or down.'),
            StatusCode(504, 'Gateway Timeout', 'The gateway has timed out.'),
            StatusCode(505, 'HTTP Version Not Supported', 'The server does not support the "http protocol" version.')
        ]
