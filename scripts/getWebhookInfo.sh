#!/bin/sh

REPO_ROOT=$(git rev-parse --show-toplevel)
source $REPO_ROOT/.env.dev

curl \
    --request POST \
    --url https://api.telegram.org/bot$TG_TOKEN/getWebhookInfo