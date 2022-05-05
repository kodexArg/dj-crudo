#!/bin/bash
dc down && sudo rm -rf data && dc build && dc up -d && dc logs -f web
