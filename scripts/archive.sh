#!/bin/sh

zip -r archive.zip . \
    -x "scripts" \
    -x "scripts/*" \
    -x ".vscode" \
    -x ".vscode/*" \
    -x ".venv" \
    -x ".venv/*" \
    -x "__pycache__" \
    -x "__pycache__/*" \
    -x "tmp" \
    -x "tmp/*" \
    -x ".git" \
    -x ".git/*" \
    -x ".env.dev" \
    -x ".gitignore"