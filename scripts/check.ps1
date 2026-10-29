$ErrorActionPreference = "Stop"
Push-Location (Split-Path -Parent $PSScriptRoot)
try {
    python -m unittest discover -s tests -v
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
    python -c "import json, pathlib; d=json.loads(pathlib.Path('data/services.json').read_text(encoding='utf-8')); print(f'{len(d[\"families\"])} families OK')"
} finally {
    Pop-Location
}
