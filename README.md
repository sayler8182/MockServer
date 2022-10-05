# MockServer

MockServer is easy and quic way to run mock APIs locally. 
No remote deployment, no account required, free and open-source.

It's a web panel and a CLI that help you work faster with APIs by mocking them. 
Integrate third-party APIs quicker, improve your integration tests, speed up your development, etc.

You can find full documentation [here](./docs/docs.md).

## Features
- unlimited number of mock local servers and routes
- proxy forwarding
- complete control on routes definition: HTTP methods and statuses, regex paths, file serving, custom headers, etc.
- JSON templating
- store state between requests
- modify proxy response
- API for integration in external services
- multiple responses per route
- importing / exporting 
- simulated latency
- running external scripts
- ... and many more - see the [documentation](./docs/docs.md)

# TODO

## Panel
- random mock rotation
- mock connection errors
- conditional mocks
- faker for mocking response
- write docs

## API
- proxy.is_templating_enabled - API
- response_interceptors - API
- environment - API
- proxy delay - API
- mock response delay - API
- is_single_use - API
- mock response order - API
- mocks conflict - API
- mock raw file - API
- logs - API

## Long time features
- Open api converter