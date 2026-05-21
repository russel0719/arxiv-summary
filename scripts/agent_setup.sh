#!/usr/bin/env bash
# Setup script for the scheduled Claude agent environment.
# Run this at the start of each agent session before fetching papers.
set -e

pip install feedparser -q
