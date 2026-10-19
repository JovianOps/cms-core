# Tests for cms-core
import pytest
from pathlib import Path

from cms import _parse_frontmatter, load_config, find_root, init_project


class TestFrontmatter:
    def test_parse_with_frontmatter(self):
        text = """---
title: Home
author: Me
---
Hello world"""
        fm, body = _parse_frontmatter(text)
        assert fm["title"] == "Home"
        assert fm["author"] == "Me"
        assert "Hello world" in body

    def test_parse_without_frontmatter(self):
        text = "Just content"
        fm, body = _parse_frontmatter(text)
        assert fm == {}
        assert body == "Just content"

    def test_parse_empty_frontmatter(self):
        text = """---
---
Content here"""
        fm, body = _parse_frontmatter(text)
        assert fm == {}
        assert "Content here" in body


class TestConfig:
    def test_load_default(self, tmp_path):
        config = load_config(tmp_path)
        assert config["site"]["title"] == "My Site"
        assert config["theme"] == "default"

    def test_load_custom(self, tmp_path):
        (tmp_path / "cms.yaml").write_text("""
site:
  title: Blog
theme: bootstrap
""")
        config = load_config(tmp_path)
        assert config["site"]["title"] == "Blog"
        assert config["theme"] == "bootstrap"


class TestInit:
    def test_init_creates_structure(self, tmp_path):
        init_project(tmp_path)
        assert (tmp_path / ".cms").is_dir()
        assert (tmp_path / "cms.yaml").exists()
        assert (tmp_path / "content" / "index.md").exists()
        assert (tmp_path / "themes" / "default" / "base.html").exists()

    def test_find_root(self, tmp_path):
        init_project(tmp_path)
        subdir = tmp_path / "src"
        subdir.mkdir()
        assert find_root(subdir) == tmp_path
