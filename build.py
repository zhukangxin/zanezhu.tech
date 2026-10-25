#!/usr/bin/env python3
"""
zanezhu.tech 网站生成器 / site generator

读取 data/ 里的简历、content/ 里的文章和动态，生成完整的静态网站到 dist/。
Netlify 每次检测到 GitHub 有更新时会自动运行:  python build.py

本地预览:
    pip install -r requirements.txt
    python build.py
    python -m http.server 8000 --directory dist     # 打开 http://localhost:8000
"""

import datetime as dt
import html
import json
import os
import re
import shutil
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
CONTENT = ROOT / "content"


# ---------------------------------------------------------------- helpers
def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def to_date(value):
    """Accept date, datetime or string from front matter."""
    if isinstance(value, dt.datetime):
        return value.date()
    if isinstance(value, dt.date):
        return value
    if isinstance(value, str) and value.strip():
        s = value.strip().replace("/", "-")
        for fmt in ("%Y-%m-%dT%H:%M:%S.%fZ", "%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M",
                    "%Y-%m-%d %H:%M", "%Y-%m-%d", "%Y-%m"):
            try:
                return dt.datetime.strptime(s, fmt).date()
            except ValueError:
                continue
    return dt.date.today()


def parse_markdown_file(path):
    text = path.read_text(encoding="utf-8")
    meta, body = {}, text
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.S)
    if m:
        meta = yaml.safe_load(m.group(1)) or {}
        body = m.group(2)
    return meta, body


def render_md(body):
    md = markdown.Markdown(extensions=["extra", "sane_lists", "toc"])
    return md.convert(body)


def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()


def excerpt(html_text, n=160):
    t = strip_tags(html_text)
    return t if len(t) <= n else t[:n].rstrip() + "…"


def fmt_date(d, lang):
    if lang == "zh":
        return "{}年{}月{}日".format(d.year, d.month, d.day)
    return d.strftime("%b ") + str(d.day) + d.strftime(", %Y")


def fmt_period(start, end, lang, present):
    end = end or present
    return "{} – {}".format(start, end)


# ---------------------------------------------------------------- loaders
def load_collection(kind, lang):
    folder = CONTENT / kind / lang
    items = []
    if not folder.exists():
        return items
    for path in sorted(folder.glob("*.md")):
        meta, body = parse_markdown_file(path)
        if meta.get("draft"):
            continue
        slug = path.stem
        body_html = render_md(body) if body.strip() else ""
        item = {
            "slug": slug,
            "title": str(meta.get("title", slug)),
            "date": to_date(meta.get("date")),
            "description": meta.get("description") or (excerpt(body_html) if body_html else ""),
            "tags": meta.get("tags") or [],
            "publication": meta.get("publication") or "",
            "external_url": meta.get("external_url") or "",
            "link": meta.get("link") or "",
            "cover": meta.get("cover") or "",
            "url": meta.get("url") or "",
            "repo": meta.get("repo") or "",
            "featured": bool(meta.get("featured")),
            "html": body_html,
            "lang": lang,
        }
        item["date_str"] = fmt_date(item["date"], lang)
        # 只填写了外部链接、没有正文的文章，直接跳转到原文
        item["has_page"] = bool(body_html) if kind == "articles" else False
        items.append(item)
    items.sort(key=lambda x: x["date"], reverse=True)
    return items


# ---------------------------------------------------------------- build
def main():
    site = load_yaml(ROOT / "data" / "site.yaml")
    profile = load_yaml(ROOT / "data" / "profile.yaml")
    base_url = site["site_url"].rstrip("/")
    langs = site["languages"]
    default = site["default_lang"]

    if DIST.exists():
        shutil.rmtree(DIST)
    shutil.copytree(ROOT / "static", DIST)

    env = Environment(loader=FileSystemLoader(str(ROOT / "templates")),
                      autoescape=select_autoescape(["html", "xml"]),
                      trim_blocks=True, lstrip_blocks=True)
    env.filters["tojson_raw"] = lambda v: json.dumps(v, ensure_ascii=False)

    def prefix(lang):
        return "" if lang == default else "/" + lang

    def other_lang(lang):
        return [l for l in langs if l != lang][0]

    articles = {l: load_collection("articles", l) for l in langs}
    updates = {l: load_collection("updates", l) for l in langs}
    projects = {}
    for l in langs:
        items = load_collection("projects", l)
        items.sort(key=lambda x: (not x["featured"], -x["date"].toordinal()))
        projects[l] = items

    sitemap = []  # (path, {lang: path}, lastmod)
    build_date = dt.date.today()

    def write(path, content):
        out = DIST / path.lstrip("/")
        if path.endswith("/"):
            out = out / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(content, encoding="utf-8")

    def p(obj, key, lang):
        """Pick the bilingual field, e.g. p(job, 'role', 'zh') -> job['role_zh']."""
        v = obj.get("{}_{}".format(key, lang))
        if v in (None, "", []):
            v = obj.get("{}_{}".format(key, default))
        if v in (None, "", []):
            v = obj.get(key, "")
        return v

    env.globals.update(p=p, fmt_period=fmt_period)

    for lang in langs:
        ui = site["ui"][lang]
        pre = prefix(lang)
        alt = other_lang(lang)
        alt_pre = prefix(alt)

        person_ld = {
            "@context": "https://schema.org",
            "@type": "Person",
            "name": profile["name_en"].replace("(", "").replace(")", "").replace("  ", " "),
            "alternateName": [profile["name_zh"], "Zane Zhu", "Kangxin Zhu"],
            "url": base_url + "/",
            "email": "mailto:" + profile["email"],
            "jobTitle": p(profile, "headline", lang),
            "description": ui["site_description"],
            "sameAs": [profile["linkedin"]],
            "alumniOf": [
                {"@type": "CollegeOrUniversity", "name": "Shanghai Jiao Tong University"},
                {"@type": "CollegeOrUniversity", "name": "Cheung Kong Graduate School of Business"},
            ],
            "knowsLanguage": ["zh-CN", "en"],
            "knowsAbout": ["Digital strategy", "Cross-border payments", "Fintech",
                           "Product management", "Corporate strategy", "AI applications"],
        }
        if profile.get("avatar"):
            person_ld["image"] = base_url + profile["avatar"]

        def ctx(page_path, alt_path, title, description, extra=None, page_type="website"):
            c = {
                "lang": lang, "ui": ui, "site": site, "profile": profile,
                "pre": pre, "alt_lang": alt, "alt_ui": site["ui"][alt],
                "page_path": page_path, "alt_path": alt_path,
                "canonical": base_url + page_path,
                "alternates": {lang: base_url + page_path, alt: base_url + alt_path}
                if alt_path else {lang: base_url + page_path},
                "x_default": base_url + (page_path if lang == default else alt_path)
                if alt_path else None,
                "title": title, "description": description,
                "base_url": base_url, "page_type": page_type,
                "year": build_date.year,
            }
            if extra:
                c.update(extra)
            return c

        name = p(profile, "name", lang)

        # Home
        path, apath = pre + "/", alt_pre + "/"
        write(path, env.get_template("home.html").render(**ctx(
            path, apath, ui["site_title"] + " · " + p(profile, "headline", lang).split("·")[0].strip(),
            ui["site_description"],
            {"articles": articles[lang][:3], "updates": updates[lang][:3],
             "projects": projects[lang][:3],
             "json_ld": [person_ld], "nav": "home"})))
        sitemap.append((path, {lang: path, alt: apath}, build_date))

        # Résumé
        path, apath = pre + "/resume/", alt_pre + "/resume/"
        write(path, env.get_template("resume.html").render(**ctx(
            path, apath, ui["resume_title"] + " · " + name, ui["site_description"],
            {"json_ld": [person_ld], "nav": "resume"})))
        sitemap.append((path, {lang: path, alt: apath}, build_date))

        # Articles list
        path, apath = pre + "/articles/", alt_pre + "/articles/"
        write(path, env.get_template("articles.html").render(**ctx(
            path, apath, ui["articles_title"] + " · " + name, ui["articles_intro"],
            {"articles": articles[lang], "nav": "articles"})))
        last = articles[lang][0]["date"] if articles[lang] else build_date
        sitemap.append((path, {lang: path, alt: apath}, last))

        # Article pages
        alt_slugs = {a["slug"] for a in articles[alt] if a["has_page"]}
        for a in articles[lang]:
            if not a["has_page"]:
                continue
            path = "{}/articles/{}/".format(pre, a["slug"])
            apath = "{}/articles/{}/".format(alt_pre, a["slug"]) if a["slug"] in alt_slugs else None
            article_ld = {
                "@context": "https://schema.org", "@type": "BlogPosting",
                "headline": a["title"], "description": a["description"],
                "datePublished": a["date"].isoformat(), "inLanguage": ui["html_lang"],
                "mainEntityOfPage": base_url + path,
                "author": {"@type": "Person", "name": "Kangxin (Zane) Zhu",
                           "alternateName": profile["name_zh"], "url": base_url + "/"},
            }
            if a["cover"]:
                article_ld["image"] = base_url + a["cover"]
            write(path, env.get_template("article.html").render(**ctx(
                path, apath or (alt_pre + "/articles/"), a["title"] + " · " + name,
                a["description"], {"a": a, "json_ld": [article_ld], "nav": "articles",
                                   "has_translation": bool(apath)}, page_type="article")))
            sitemap.append((path, {lang: path, alt: apath} if apath else {lang: path}, a["date"]))

        # Projects
        path, apath = pre + "/projects/", alt_pre + "/projects/"
        write(path, env.get_template("projects.html").render(**ctx(
            path, apath, ui["projects_title"] + " · " + name, ui["projects_intro"],
            {"projects": projects[lang], "nav": "projects"})))
        last = max([x["date"] for x in projects[lang]] or [build_date])
        sitemap.append((path, {lang: path, alt: apath}, last))

        # Updates
        path, apath = pre + "/updates/", alt_pre + "/updates/"
        years = []
        for u in updates[lang]:
            if not years or years[-1][0] != u["date"].year:
                years.append((u["date"].year, []))
            years[-1][1].append(u)
        write(path, env.get_template("updates.html").render(**ctx(
            path, apath, ui["updates_title"] + " · " + name, ui["updates_intro"],
            {"years": years, "nav": "updates"})))
        last = updates[lang][0]["date"] if updates[lang] else build_date
        sitemap.append((path, {lang: path, alt: apath}, last))

        # RSS (articles + updates)
        feed_items = []
        for a in articles[lang]:
            link = base_url + "{}/articles/{}/".format(pre, a["slug"]) if a["has_page"] else a["external_url"]
            if link:
                feed_items.append({"title": a["title"], "link": link, "date": a["date"],
                                   "description": a["description"]})
        for u in updates[lang]:
            feed_items.append({"title": u["title"], "link": base_url + pre + "/updates/#" + u["slug"],
                               "date": u["date"], "description": strip_tags(u["html"])})
        feed_items.sort(key=lambda x: x["date"], reverse=True)
        write(pre + "/rss.xml", env.get_template("rss.xml").render(
            ui=ui, base_url=base_url, pre=pre, items=feed_items[:30], lang=lang,
            rfc=lambda d: dt.datetime(d.year, d.month, d.day, 12).strftime("%a, %d %b %Y %H:%M:%S +0000"),
            now=dt.datetime.now(dt.timezone.utc).strftime("%a, %d %b %Y %H:%M:%S +0000")))

    # 404 (bilingual)
    ui = site["ui"][default]
    write("/404.html", env.get_template("404.html").render(
        lang=default, ui=ui, ui_zh=site["ui"]["zh"], site=site, profile=profile, pre="",
        alt_lang="zh", alt_ui=site["ui"]["zh"], page_path="/404.html", alt_path="/zh/",
        canonical=base_url + "/404.html", alternates={}, x_default=None,
        title=ui["not_found_title"], description=ui["not_found_text"], base_url=base_url,
        page_type="website", year=build_date.year, nav="", noindex=True))

    # sitemap.xml with hreflang
    hreflang = {l: site["ui"][l]["html_lang"] for l in langs}
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
             'xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for path, alts, lastmod in sitemap:
        lines.append("  <url>")
        lines.append("    <loc>{}</loc>".format(html.escape(base_url + path)))
        lines.append("    <lastmod>{}</lastmod>".format(lastmod.isoformat()))
        for l, ap in alts.items():
            if ap:
                lines.append('    <xhtml:link rel="alternate" hreflang="{}" href="{}"/>'.format(
                    hreflang[l], html.escape(base_url + ap)))
        if len([a for a in alts.values() if a]) > 1:
            lines.append('    <xhtml:link rel="alternate" hreflang="x-default" href="{}"/>'.format(
                html.escape(base_url + alts[default])))
        lines.append("  </url>")
    lines.append("</urlset>")
    (DIST / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")

    (DIST / "robots.txt").write_text(
        "User-agent: *\nAllow: /\nDisallow: /admin/\n\nSitemap: {}/sitemap.xml\n".format(base_url),
        encoding="utf-8")

    n_pages = len(sitemap)
    print("Built {} pages, {} articles, {} updates -> {}".format(
        n_pages, sum(len(v) for v in articles.values()),
        sum(len(v) for v in updates.values()), DIST))


if __name__ == "__main__":
    main()
