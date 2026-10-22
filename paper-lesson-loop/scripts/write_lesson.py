#!/usr/bin/env python3
"""Append one 经验 (or 决策/弃用/失败/待办...) Memory Log entry.

Run this AFTER each interpretation: distill what worked / didn't about
understanding, fidelity to the source paper, readability, and wording,
so the next run improves. One fact per entry.

Usage:
    python3 write_lesson.py --title "标题" --content "2-5句：是什么+为什么+关键细节" \\
        [--type 经验] [--keywords 论文解读]

Config via environment:
    NOTION_API_KEY               Notion internal integration token
    NOTION_MEMLOG_DATA_SOURCE_ID Memory Log data source id
    NOTION_PROJECT_ID            paper-reading project page id (relation target)
"""
import argparse
import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta

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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True)
    ap.add_argument("--content", required=True)
    ap.add_argument("--type", default="经验",
                    choices=["决策", "架构", "发布/里程碑", "经验",
                             "弃用/失败", "约束/偏好", "待办"])
    ap.add_argument("--keywords", default="论文解读")
    ap.add_argument("--recorder", default="Muse")
    ap.add_argument("--doer", default="Muse")
    args = ap.parse_args()

    beijing = (datetime.now(timezone.utc) + timedelta(hours=8)).strftime("%Y-%m-%d")
    props = {
        "标题": {"title": [{"text": {"content": args.title}}]},
        "项目": {"relation": [{"id": PROJ_ID}]},
        "类型": {"select": {"name": getattr(args, "type")}},
        "日期": {"date": {"start": beijing}},
        "内容": {"rich_text": [{"text": {"content": args.content}}]},
        "状态": {"select": {"name": "有效"}},
        "关键词": {"multi_select": [{"name": k.strip()} for k in args.keywords.split(",") if k.strip()]},
        "记录者": {"select": {"name": args.recorder}},
        "完成者": {"select": {"name": args.doer}},
    }
    res = api_call("POST", "/pages", {
        "parent": {"type": "data_source_id", "data_source_id": MEMLOG_DS},
        "properties": props,
    })
    print("lesson written:", res["id"])


if __name__ == "__main__":
    main()
