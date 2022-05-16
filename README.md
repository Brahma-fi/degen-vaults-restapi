# Degen Vaults REST API

This is the backend for getting various data related to Brahma's Degen Vaults.

**Deployed to**: [this url](https://vault-api.brahma.fi/)

## Endpoints include -

- /historic_rewards
- /latest_buffer
- /open_timestamps
- /:vault_name/share_price
- /:vault_name/apr
- /tvl

## Setup

- Install dependencies

```
pip3 install -r requirements.txt
```

- Create .env as

```
DB_SECRET_ARN =
DB_ARN =
AWS_SECRET_ACCESS_KEY =
AWS_ACCESS_KEY_ID =

PRODUCTION=

MAINNET_RPC =
```

- Create shell environment variables
  - PM_API_IMAGE_NAME
  - AWS_URL
  - AWS_REGION
