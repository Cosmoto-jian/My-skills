#!/usr/bin/env python3
"""Read the latest 经验 (experience) Memory Log entries for the paper-reading project.

Run this BEFORE writing each interpretation: the entries capture what worked /
didn't about factual fidelity, readability, and wording, so the next run improves.

Config via environment:
    NOTION_API_KEY               Notion internal integration token
    NOTION_MEMLOG_DATA_SOURCE_ID Memory Log data source id
    NOTION_PROJECT_ID            paper-reading project page id (relation filter)
"""
import json
import os
import sys
import urllib.request
import urllib.error

NOTION_API_KEY = os.environ.get("NOTION_API_KEY", "")
MEMLOG_DS = os.environ.get("NOTION_MEMLOG_DATA_SOURCE_ID", "")
PROJ_ID = os.environ.get("NOTION_PROJECT_ID", "")

for name, val in [("NOTION_API_KEY", NOTION_API_KEY),
                  ("NOTION_MEMLOG_DATA_SOURCE_ID", MEMLOG_DS),
                  ("NOTION_PROJECT_ID", PROJ_ID)]:
    if not val:
        print(f"missing env var: {name}", file=sys.stderr)
        sys.exit(2)


def api_call(method, path, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(
        "https://api.notion.com/v1" + path, data=data, method=method,
        headers={"Content-Type": "application/json",
                 "Authorization": f"Bearer {NOTION_API_KEY}",
                 "Notion-Version": "2022-06-28"})
    try:
        resp = urllib.request.urlopen(req, timeout=30)
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.read().decode()[:500]}", file=sys.stderr)
        sys.exit(1)
    return json.loads(resp.read().decode())


def plain(rich):
    return "".join(x["plain_text"] for x in rich)


def main():
    res = api_call("POST", f"/data_sources/{MEMLOG_DS}/query", {
        "filter": {"and": [
            {"property": "项目", "relation": {"contains": PROJ_ID}},
            {"property": "类型", "select": {"equals": "经验"}},
            {"property": "状态", "select": {"equals": "有效"}},
        ]},
        "sorts": [{"property": "日期", "direction": "descending"}],
        "page_size": 8,
    })
    results = res.get("results", [])
    if not results:
        print("（暂无经验条目，直接生成）")
        return
    for r in results:
        p = r["properties"]
        title = plain(p["标题"]["title"])
        date = (p["日期"]["date"] or {}).get("start", "")
        content = plain(p["内容"]["rich_text"])
        print(f"### {title}（{date}）\n{content}\n")


if __name__ == "__main__":
    main()
