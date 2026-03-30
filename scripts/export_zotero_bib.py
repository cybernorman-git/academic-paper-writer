#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyzotero>=1.6.0"]
# ///
"""
Export a Zotero collection to a .bib file for use in LaTeX.

Usage:
    ZOTERO_CREDENTIALS="userID:apiKey" uv run export_zotero_bib.py \
        --collection COLLECTION_KEY \
        --output project/refs.bib

Find collection key by listing all collections:
    ZOTERO_CREDENTIALS="userID:apiKey" uv run export_zotero_bib.py --list-collections
"""

import argparse
import os
import re
import sys

def get_zotero_client():
    creds = os.environ.get("ZOTERO_CREDENTIALS", "")
    if ":" not in creds:
        print("ERROR: Set ZOTERO_CREDENTIALS='userID:apiKey'", file=sys.stderr)
        sys.exit(1)
    uid, key = creds.strip().split(":", 1)
    # Resolve numeric user ID via API if non-numeric
    if not uid.isdigit():
        import urllib.request, json
        url = f"https://api.zotero.org/keys/{key}"
        with urllib.request.urlopen(url) as r:
            data = json.loads(r.read())
        uid = str(data["userID"])
    from pyzotero import zotero
    return zotero.Zotero(uid, "user", key), uid


def list_collections(zot):
    cols = zot.collections()
    print(f"{'Key':<12} {'Name':<30} {'Parent'}")
    print("-" * 60)
    for c in sorted(cols, key=lambda x: x["data"]["name"]):
        print(f"{c['key']:<12} {c['data']['name']:<30} {c['data'].get('parentCollection','ROOT')}")


def make_citekey(item):
    """Generate a cite key: LastName + Year + FirstTitleWord"""
    data = item.get("data", {})
    creators = data.get("creators", [])
    last = creators[0].get("lastName", "Unknown") if creators else "Unknown"
    last = re.sub(r"[^A-Za-z]", "", last)
    year = data.get("date", "")[:4] or "0000"
    title_words = re.findall(r"\b[A-Z][a-z]+\b", data.get("title", ""))
    word = title_words[0] if title_words else "Paper"
    return f"{last}{year}{word}"


def item_to_bibtex(item, citekey):
    data = item.get("data", {})
    itype = data.get("itemType", "journalArticle")

    bib_type = {
        "journalArticle": "article",
        "bookSection": "incollection",
        "book": "book",
        "conferencePaper": "inproceedings",
        "preprint": "misc",
        "thesis": "phdthesis",
    }.get(itype, "misc")

    def fmt_authors(creators):
        parts = []
        for c in creators:
            if c.get("creatorType") not in ("author", "editor"):
                continue
            if c.get("lastName"):
                name = c["lastName"]
                if c.get("firstName"):
                    name += ", " + c["firstName"]
            else:
                name = c.get("name", "Anonymous")
            parts.append(name)
        return " and ".join(parts)

    fields = {}
    fields["author"] = fmt_authors(data.get("creators", []))
    fields["title"] = "{" + data.get("title", "") + "}"
    fields["year"] = data.get("date", "")[:4] or ""
    fields["journal"] = data.get("publicationTitle", "") or data.get("bookTitle", "")
    fields["volume"] = data.get("volume", "")
    fields["number"] = data.get("issue", "")
    fields["pages"] = data.get("pages", "")
    fields["doi"] = data.get("DOI", "")
    fields["url"] = data.get("url", "")
    fields["abstract"] = data.get("abstractNote", "")[:300]  # truncate

    lines = [f"@{bib_type}{{{citekey},"]
    for k, v in fields.items():
        if v:
            lines.append(f"  {k} = {{{v}}},")
    lines.append("}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Export Zotero collection to .bib")
    parser.add_argument("--collection", help="Collection key (e.g. 4V9WZTGV)")
    parser.add_argument("--output", default="refs.bib", help="Output .bib filename")
    parser.add_argument("--list-collections", action="store_true")
    args = parser.parse_args()

    zot, uid = get_zotero_client()

    if args.list_collections:
        list_collections(zot)
        return

    if not args.collection:
        print("ERROR: --collection COLLECTION_KEY required", file=sys.stderr)
        sys.exit(1)

    print(f"Fetching items from collection {args.collection}...")
    items = zot.collection_items(args.collection, itemType="journalArticle || conferencePaper || preprint || book")
    
    seen_keys = set()
    entries = []
    for item in items:
        if item["data"].get("itemType") == "note":
            continue
        key = make_citekey(item)
        # Deduplicate keys
        orig = key
        i = 2
        while key in seen_keys:
            key = f"{orig}{i}"
            i += 1
        seen_keys.add(key)
        entries.append(item_to_bibtex(item, key))

    output = "\n\n".join(entries)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"Exported {len(entries)} entries to {args.output}")


if __name__ == "__main__":
    main()
