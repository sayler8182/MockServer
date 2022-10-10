MockServer is easy and quic way to run mock APIs locally.
No remote deployment, no account required, free and open-source.

It's a web panel and a CLI that help you work faster with APIs by mocking them.
Integrate third-party APIs quicker, improve your integration tests, speed up your development, etc.

# Requirements

- python3
- tested only on macOS (12.5+)

# Installation

You can automatically install the tool by simply call

```bash
./scripts/init.sh
``` 

The script will:

- create and activate the venv
- install requirements from `requirements.txt` file
- init flask db
- migrate flask db

You can also do this steps manually.

### Creation of venv

```bash
pip3 install virtualenv
python3 -m venv venv
```

### Activation of venv

```bash
. venv/bin/activate
```

### Installation of the requirements

```bash
pip3 install -r requirements.txt
```

### Initialization of the database

```bash
flask db init
```

### Migration of the database

Migration is required after database initialization and when database structure was changed.

```bash
flask db migrate
flask db upgrade
```

or

```bash
./scripts/update.sh
```

## Launching the MockServer

In order to run MockServer You should call

```bash
./scripts/run.sh
```

By default, service is running on http://127.0.0.1:5012. You can change default setting by settings proper environment
variable:

```bash
export MOCK_SERVER_FLASK_HOST=127.0.0.1;
export MOCK_SERVER_FLASK_PORT=5012;
```

You can also send additional parameter with path to the zip which will be imported during first launch. The zip will be
decompressed and json files will be imported. See [Import section](#importing-and-exporting)

```bash
./scripts/run.sh ./docs/example/init_configuration.zip
```

## Admin panel

In order to manage mocks and configuration You can use [web panel](http://127.0.0.1:5012).

[**More info**](./details/admin_panel.md)

## Testing outside the localhost

In order to use the MockServer and run app on device (not simulator) You need to use tunnel application, for
example [ngrok](https://www.ngrok.com/download).

The binary must be downloaded and placed somewhere on disk. The next commands need to be run in when inside the
directory containing ngrok binary.

```bash
./ngrok http 5012
```

Next, You should copy the **Forwarding https** url and use it as the server url in project. From now on, all requests
from device should call MockServer through ngrok service.

On macOS, we've seen issues that ngrok returns 403 and request don't reach MockServer. In this case You can disable '
AirPlay Receiver' in 'System Preferences' or try a different port.

# Mocking mechanism

Mocks allow you to return some predefined value instead of calling API endpoint. You can define one or more responses
for mock ([see mock](./details/admin_panel.md)). Mock is applied only when allow
criteria are meet:

- mock is enabled
- methods are equal
- full requests paths are equal
- at least one defined mock is enabled

For multiple mocks there are a few method to calculate which response will be mocked:

- rotate - rotation order [1, 2, 3, 1, 2, 3, 1, 2] (for three mocks)
- sequential - sequential order [1, 2, 3, 3, 3, 3] (for three mocks)

You can also force response to be mocked ([see mocks](./details/admin_panel.md)).

# Response interceptors

Mock and proxy response can be modified in some specific way. You can define an interceptor which transform the response
or do some work without change.

## Predefined interceptors

### Templating interceptor

Apply templating mechanism for response. By default, templating is enabled for all responses, but You can use this
interceptor if You want to change default settings and apply templating only for one
response. [See templating](#templating).

### Update environment interceptor

Using [jsonpath_ng](https://github.com/h2non/jsonpath-ng) finds a value for key and store it in
environment. [See environment)](./details/admin_panel.md).

### Replace value interceptor

Using [jsonpath_ng](https://github.com/h2non/jsonpath-ng) finds a value for key and replace it with a new value. Can be
templated ([see templating](#templating)).

### Custom interceptor

Links external interceptor defined outside the mock server. [See extensions](#extensions).

# Templating

JSON body can be templated with simple tag mechanism `{{VARIABLE}}`. During processing the response, the body is
analysed and tags are replaced with `static` or `dynamic` variables. Eg:

```json
{
  "data": "{{DATA}}"
}
```

will be transformed into:

```json
{
  "data": "2022-10-07T19:38:43.049640"
}
```

By default, templating is enabled in
proxy ([see settings](./details/admin_panel.md)), but may be disabled, so if You want to use templating in only for
specific response, You should disable templating in proxy and use [Templating interceptor](#response-interceptors).

## Static variables

Predefined variables or computed properties:

| key  | description                | example                    |
|------|----------------------------|----------------------------|
| date | current date in iso format | 2022-10-07T19:38:43.049640 |

## Dynamic variable

Dynamic variables can be defined in environment tab ([see admin panel](./details/admin_panel.md)) or set in
interceptor ([see interceptors](#response-interceptors)).

# Importing and exporting

It is possible to import and export mocks and configuration in order to share environment in the team or store cases for
future use.

[**More info**](./details/importing_exporting.md)

# Extensions

It is possible to extend mock server behaviour. You can add:

- custom scripts launched via MockServer
- custom interceptors which modifies the response

[**More info**](./details/extensions.md)

# Env

| key                                    | default value | details                                                                                                                                          |
|----------------------------------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| MOCK_SERVER_FLASK_HOST                 | 127.0.0.1     | MockServer host                                                                                                                                  |
| MOCK_SERVER_FLASK_PORT                 | 5012          | MockServer proxy                                                                                                                                 |
| MOCK_SERVER_FLASK_DATABASE_INITIALIZED |               | Use only if is not running with ./run.sh script. Needs to be set only before running mock server. For database initialisation should not be set. |
| MOCK_SERVER_RESOURCES                  | /app/static/  | Default resource path                                                                                                                            |
| MOCK_SERVER_AUTO_IMPORT                |               | Path to the file which will be imported during first launch. Use only if is not running with ./run.sh script.                                    |

# API

I suggest You to import the postman collection - `./docs/postman_collection.json`.

[**More info**](./details/api.md)

# Use case

In order to check the real use case, check [use_case directory](./example/use_case/use_case.md).

- import [postman collection](./example/use_case/postman_collection.json) in postman.
- import [mocks and configuration](./example/use_case/use_case.zip) in web panel (any import button).
- check [use case documentation](./example/use_case/use_case.md).

# FAQ

**Q:** How to change host / port?
<br>
**A:** Yes, just set `MOCK_SERVER_FLASK_HOST` and `MOCK_SERVER_FLASK_PORT` envs.
See [Launching the MockServer](#launching-the-mockserver) section.

**Q:** How to run the tool with specific configuration set?
<br>
**A:** Yes, You can import configuration during first launch. See [Launching the MockServer](#launching-the-mockserver)
section.

**Q:** I have problem with incorrect migration between version. What to do?
<br>
**A:** Try to run `./scripts/reinit.sh` script - **notice that this scripts clear the database**.

**Q:** I have problem with mocks, the server doesn't mock my request. What to do?
<br>
**A:** You should check whether:

- the proxy is correctly set end enabled - pay attention on `/` at the end (the slash depends on Your app configuration)
- the mock is enabled
- the mock has proper path and method set
- the logs history recognize the request
- the request call correct host and port
- the MockServer doesn't catch an error in logs
- the port is already in use (try different port)

**Q:** Where can I find the API documentation?
<br>
**A:** See [API section](#api). You can also import the postman collection - `./docs/postman_collection.json`.

**Q:** Is it possible to deploy it on the server?
<br>
**A:** Probably yes, but is not recommended, this tool is dedicated to run locally.

**Q:** Is want to use mocks on real device - not a simulator or emulator. What to do?
<br>
**A:** See [Testing outside the localhost](#testing-outside-the-localhost).

**Q:** Is it possible to run external bash scripts?
<br>
**A:** Yes. See [Extensions section](#extensions).

**Q:** Is it possible to run in container (docker, etc..)?
<br>
**A:** Yes, but You should prepare image yourself.

**Q:** I have other problem. What to do?
<br>
**A:** Fell free to create PR / issue or contact the author `konradpiekos93@gmail.com`.

**Q:** I want to deep into source code of MockServer. What to do?
<br>
**A:** Fell free. I suggest You to use PyCharm IDE.