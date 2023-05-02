# ACA-Python DID Web plugin

## Developing

First-time initialization of the python environment:

```bash
poetry install
pre-commit install
```

You're all set !

To run aca-py with the plugin, include it in your config:

```yaml
plugin:
  - didweb
```

and run aca-py from the poetry environment:
```bash
poetry env
aca-py ....
```

## Creating a did:web

```bash
curl -X 'POST' \
  'http://localhost:7082/wallet/did/create' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "method": "web",
  "options": {
    "did": "did:web:adaptivespace.io",
    "key_type": "ed25519"
  }
}'
```

results in

```json
{
  "result": {
    "did": "did:web:adaptivespace.io",
    "verkey": "FLgVvRqfE1iATV315ySYojoz3SqQ2zJMGyvjDynyErm5",
    "posture": "wallet_only",
    "key_type": "ed25519",
    "method": "web"
  }
}
```
