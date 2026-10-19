#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VENV="${GEO_VENV:-$HOME/.venvs/geo}"
if [ ! -x "$VENV/bin/python" ]; then
  python3 -m venv "$VENV"
  "$VENV/bin/pip" install -q 'requests>=2.32,<3' 'beautifulsoup4>=4.12,<5' 'lxml>=5,<7'
fi
mkdir -p "$ROOT/.geo/reports"
exec "$VENV/bin/python" "$ROOT/tools/geo-check.py" --json "$ROOT/.geo/reports/$(date +%F).json" "$@"
