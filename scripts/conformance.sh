#!/usr/bin/env bash
# Run the shared Gauge conformance suite against this SDK.
#   CONFORMANCE_SPECS  path to couchdb-sdk-generator/conformance/specs
#                      (default: ../couchdb-sdk-generator/conformance/specs)
#   extra args are passed to `gauge run`, e.g. --tags documents
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
specs="${CONFORMANCE_SPECS:-$root/../couchdb-sdk-generator/conformance/specs}"
[[ -d "$specs" ]] || { echo "conformance specs not found at $specs" >&2; exit 1; }

cd "$root/conformance"
rm -rf specs && cp -r "$specs" specs

# Use the project venv's python (with getgauge + this SDK) when there is one.
for bin in "$root/.venv/Scripts" "$root/.venv/bin"; do
  [[ -d "$bin" ]] && export PATH="$bin:$PATH"
done

gauge() { npx --yes @getgauge/cli@1.6.38 "$@"; }
gauge install python >/dev/null 2>&1 || true
gauge install html-report >/dev/null 2>&1 || true
gauge run specs "$@"
