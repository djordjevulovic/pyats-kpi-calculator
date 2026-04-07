# BOOTSTRAP_TEMPLATE.py
# pyats-kpi-calculator -- Template for AI update sessions
#
# INSTRUCTIONS FOR AI:
#   1. Start from latest bootstrap_project.py
#   2. Apply requested changes to relevant FILE variables
#   3. Update feature_description
#   4. Return complete updated bootstrap_project.py
#   5. Use only generic names: n7k, cat9k, asr9k

from ai_bootstrap import Bootstrap

PYPROJECT_TOML     = """<content>"""
KPI_CALCULATOR_PY  = """<content>"""
KPI_MODELS_YAML    = """<content>"""
TEST_SCHEMA_PY     = """<content>"""
TEST_CALCULATOR_PY = """<content>"""
TEST_PARSER_PY     = """<content>"""
README_MD               = "<content>"
GITIGNORE               = """<content>"""
TESTS_INIT_PY           = ""
INPUT_FILES_GITKEEP     = ""
AI_SESSION_GUIDE_MD     = "<content>"
BOOTSTRAP_TEMPLATE_PY   = "<content>"

FILES = {
    "pyproject.toml":           PYPROJECT_TOML,
    "README.md":                README_MD,
    ".gitignore":               GITIGNORE,
    "kpi_calculator.py":        KPI_CALCULATOR_PY,
    "kpi_models.yaml":          KPI_MODELS_YAML,
    "tests/__init__.py":        TESTS_INIT_PY,
    "tests/test_schema.py":     TEST_SCHEMA_PY,
    "tests/test_calculator.py": TEST_CALCULATOR_PY,
    "tests/test_parser.py":     TEST_PARSER_PY,
    "input_files/.gitkeep":     INPUT_FILES_GITKEEP,
    "AI_SESSION_GUIDE.md":      AI_SESSION_GUIDE_MD,
    "BOOTSTRAP_TEMPLATE.py":    BOOTSTRAP_TEMPLATE_PY,
}

if __name__ == "__main__":
    Bootstrap(project_path=".").run(
        feature_description = "<describe what changed>",
        files               = FILES,
        push                = True,
        remote              = "origin",
        branch              = "main"
    )
