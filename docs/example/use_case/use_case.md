# Use case

Preconditions:

- remove all mocks and logs
- import [postman collection](./postman_collection.json) in postman
- import [mocks and configuration](./use_case.zip) in web panel (any import button).

## Mock1

| Action                 | Result              | Details                                                                                                     |
|------------------------|---------------------|-------------------------------------------------------------------------------------------------------------|
| Send TestCase1 request | Standard response   | {{DATE}} tag has been replaced with current date.                                                           |
| Send TestCase1 request | Single use response | Mock is disabled after usage.                                                                               |
| Send TestCase1 request | Error response      | Error response with different status code and response.                                                     |
| Send TestCase1 request | Standard response   | Again {{DATE}} tag has been replaced with current date.                                                     |
| Send TestCase1 request | Error response      | Single use response is skipped because is disabled. Error response with different status code and response. |
| ...                    | ...                 | ...                                                                                                         |

## Mock2

| Action                 | Result                      | Details                                                                                         |
|------------------------|-----------------------------|-------------------------------------------------------------------------------------------------|
| Send TestCase2 request | Standard response           | {{DATE}} tag has been replaced with current date.                                               |
| Send TestCase2 request | Replace value response      | Mock uses interceptor. Returned response is modified and is different than defined.             |
| Send TestCase2 request | File response               | File is returned.                                                                               |
| Send TestCase2 request | Set value response response | Mock uses interceptor. Check Environment tab. New environment is now defined based on response. |
| Send TestCase2 request | Environment value response  | Mock uses interceptor. Response is modified based on Environment variable.                      |
| Send TestCase2 request | Environment value response  | Mock uses interceptor. Response is modified based on Environment variable.                      |
| ...                    | ...                         | ...                                                                                             |

## Proxy1

| Action                 | Result                 | Details                                                       |
|------------------------|------------------------|---------------------------------------------------------------|
| Send TestCase3 request | Proxy response         | Response from remote server is returned.                      |
| Send TestCase3 request | Proxy updated response | Response from remote server is returned but name is modified. |
| Send TestCase3 request | Proxy response         | Response from remote server is returned.                      |
| ...                    | ...                    | ...                                                           |