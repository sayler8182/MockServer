# check requirements.txt to verify what third-part library can be imported
from faker import Faker
# request - request (ProxyRequest)
# mock - Mock object if found (Mock)
# mock_response - Mock response object if found (MockResponse)
# result - generated response

# return one of [str, dict, list] value must be json encodable
def run(request, mock, mock_response) -> any:
    fake = Faker()
    return {
        'name': fake.name(),
        'address': fake.address(),
        'date': '{{DATE}}',
        'host': '{{MOCK_SERVER_FLASK_HOST}}'
    }

# required to run action
# result needs to be stored in result['body']
result['body'] = run(request, mock, mock_response)