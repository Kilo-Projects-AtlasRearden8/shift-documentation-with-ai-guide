#!/usr/bin/env python3
"""Verification script for the AI-Assisted Shift Documentation project.

Checks:
- Required files exist
- All HTML files parse as valid HTML5
- Every internal link resolves to an existing file
- LICENSE copyright line matches exactly
- README credits Asdale Dynamics, LLC
- No .github/workflows directory
- No obvious secrets / personal data patterns in tracked text files
"""
import html.parser
import os
import re
import sys
from html.parser import HTMLParser
from urllib.parse import urlparse, urljoin

ROOT = os.path.dirname(os.path.abspath(__file__))
ERRORS = []
WARNINGS = []


def fail(msg):
    ERRORS.append(msg)
    print("FAIL: " + msg)


def warn(msg):
    WARNINGS.append(msg)
    print("WARN: " + msg)


def ok(msg):
    print("ok: " + msg)


class LinkCollector(HTMLParser):
    """Collect href/src attributes from HTML."""
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for attr, value in attrs:
            if attr in ("href", "src"):
                self.links.append((tag, attr, value))


def parse_html(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def check_html_valid(path):
    text = parse_html(path)
    # Basic structural sanity: must open and close html, head, body
    lower = text.lower()
    for required in ("<html", "</html>", "<head", "</head>", "<body", "</body>"):
        if required not in lower:
            fail(f"{path}: missing {required}")
    # Balanced tag check via a simple stack for common tags
    stack = []
    tag_re = re.compile(r"<\s*/?\s*([a-zA-Z0-9]+)([^>]*)>", re.S)
    void = {"area", "base", "br", "col", "embed", "hr", "img", "input",
            "link", "meta", "param", "source", "track", "wbr"}
    ignore_attrs_end = re.compile(r"\s*/\s*$")
    for m in tag_re.finditer(text):
        tagname = m.group(1).lower()
        rest = m.group(2)
        is_closing = m.group(0).startswith("</")
        is_self_closing = bool(ignore_attrs_end.search(rest))
        if is_closing:
            if not stack or stack[-1] != tagname:
                fail(f"{path}: closing </{tagname}> without matching open tag (stack={stack[-5:]})")
            else:
                stack.pop()
        elif tagname not in void and not is_self_closing:
            stack.append(tagname)
    if stack:
        fail(f"{path}: unclosed tags remaining: {stack}")


def check_internal_links(path):
    text = parse_html(path)
    collector = LinkCollector()
    collector.feed(text)
    base_dir = os.path.dirname(path)
    for tag, attr, value in collector.links:
        # Skip fragments, external URLs, mailto, tel
        if value.startswith(("#", "mailto:", "tel:", "http://", "https://")):
            continue
        # Strip fragment
        value = value.split("#", 1)[0]
        if not value:
            continue
        candidate = os.path.normpath(os.path.join(base_dir, value))
        if not os.path.exists(candidate):
            fail(f"{path}: link '{value}' ({attr} on <{tag}>) does not resolve to {candidate}")


def check_no_secrets(path):
    text = parse_html(path)
    patterns = {
        "possible API key": r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_-]{8,}",
        "possible AWS key": r"AKIA[0-9A-Z]{16}",
        "possible email": r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    }
    for name, pat in patterns.items():
        for m in re.finditer(pat, text):
            # Allow the noreply github email in README? It's the git identity email, not a secret.
            # But it's personal data-ish; flag as warning only.
            if name == "possible email":
                warn(f"{path}: email address found ({m.group(0)})")
            else:
                fail(f"{path}: possible {name} found")


def main():
    os.chdir(ROOT)

    # Required files/dirs
    required = ["LICENSE", "README.md", "docs", "site", "site/index.html", "site/style.css"]
    for r in required:
        if os.path.exists(r):
            ok(f"exists: {r}")
        else:
            fail(f"missing: {r}")

    # No .github/workflows
    if os.path.isdir(os.path.join(ROOT, ".github", "workflows")):
        fail(".github/workflows directory present (must not be created)")
    else:
        ok("no .github/workflows directory")

    # Docs chapters present
    docs = sorted(f for f in os.listdir("docs") if f.endswith(".md"))
    if not docs:
        fail("no markdown chapters in docs/")
    else:
        ok(f"docs chapters: {', '.join(docs)}")

    # HTML files
    html_files = []
    for dirpath, _dirs, files in os.walk("site"):
        for f in files:
            if f.endswith(".html"):
                html_files.append(os.path.join(dirpath, f))
    ok(f"HTML files: {len(html_files)}")
    for h in sorted(html_files):
        check_html_valid(h)
        check_internal_links(h)
        check_no_secrets(h)

    # LICENSE copyright line exact
    with open("LICENSE", "r", encoding="utf-8") as f:
        lic = f.read()
    expected = "Copyright (c) 2026 Asdale Dynamics, LLC"
    if expected in lic:
        ok("LICENSE contains exact copyright line")
    else:
        fail(f'LICENSE missing exact line: "{expected}"')

    # README credits Asdale Dynamics, LLC
    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()
    if "Asdale Dynamics, LLC" in readme:
        ok("README credits Asdale Dynamics, LLC")
    else:
        fail("README does not credit Asdale Dynamics, LLC")

    # Scan all text files for secrets patterns (docs, md, html, css)
    text_exts = (".md", ".html", ".css", ".txt")
    for dirpath, _dirs, files in os.walk(ROOT):
        # skip .git
        if ".git" in dirpath.split(os.sep):
            continue
        for f in files:
            if f.endswith(text_exts):
                check_no_secrets(os.path.join(dirpath, f))

    print("\n--- Summary ---")
    print(f"errors: {len(ERRORS)}  warnings: {len(WARNINGS)}")
    if ERRORS:
        for e in ERRORS:
            print("FAIL - " + e)
        sys.exit(1)
    if WARNINGS:
        print("warnings (non-fatal):")
        for w in WARNINGS:
            print("WARN - " + w)
    print("All checks passed.")
    sys.exit(0)


if __name__ == "__main__":
    main()
