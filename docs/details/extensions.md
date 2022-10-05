# Extensions

## Custom scripts

MockServer allows us to run the `bash / python / etc..` script remotely from API call.
It is possible to:

- start process in background
- stop process
- call script

The full API documentation can be found [here](./api.md)

### Starting process

In order to start the process You need to call MockServer API eg:

```bash
curl --location --request POST '$HOST:$PORT/api/process/start' \
--header 'Content-Type: application/json' \
--data-raw '{
    "key": "<process_key>",
    "file_path": "<process_script_absolute_path>"
}'
```

where:

- `key` is unique key for process. If proces with such key exist, the process will be stopped
- `file_path` is an absolute path to the `bash / python / etc..` script

eg: iOS script for recording iPhone simulator

```bash
curl --location --request POST '$HOST:$PORT/api/process/start' \
--header 'Content-Type: application/json' \
--data-raw '{
    "key": "ios_record",
    "file_path": "$DOCS_PATH/example/simulator_recording.sh"
}'
```

### Stopping process

Launched process may be stopped by calling:

```bash
curl --location --request DELETE '$HOST:$PORT/api/process/stop' \
--header 'Content-Type: application/json' \
--data-raw '{
    "key": "<process_key>"
}'
```

### Listing processes

You can list all started process:

```bash
curl --location --request GET '$HOST:$PORT/api/process'
```

### Calling process

In order to start the process and wait for the completion we should use `call` method:

```bash
curl --location --request POST '$HOST:$PORT/api/process/stop' \
--header 'Content-Type: application/json' \
--data-raw '{
    "file_path": "<process_script_absolute_path>"
}'
```

Notice that the key is not needed for this method. The process is not stored and data can't be retrieved.

## Custom response interceptor

In order to modify response in specific way, You may implement custom python script and connect them to the response
interceptor. For more information about interceptors check [Interceptors section](../docs.md).

- Create a custom interceptor (You can find example [here](../example/response_custom_interceptor.py)).
- Add `Custom` interceptor for mock response
- Configure `file_path` for custom interceptor:

```json
{
  "file_path": "<absolute_file_path>.py"
}
```

There is also possibility to pass additional parameters to custom interceptor:

```json
{
  "file_path": "<absolute_file_path>.py",
  "param1": "some param",
  "param2": 1234
}
```