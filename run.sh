#!/bin/bash

source .venv/bin/activate
cd backend
uvicorn server:app
