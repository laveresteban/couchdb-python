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
# Gauge passes a run whose scenarios were skipped for missing steps. Treat
# that as a failure so a new spec can't go unimplemented unnoticed.
log="$(mktemp)"
trap 'rm -f "$log"' EXIT
gauge run specs "$@" | tee "$log"
status=${PIPESTATUS[0]}
[[ $status -eq 0 ]] || exit "$status"
if ! grep -Eq '^Scenarios:.*[^0-9]0 skipped' "$log"; then
  echo "conformance: scenarios were skipped (unimplemented steps?)" >&2
  exit 1
fi
