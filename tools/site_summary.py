"""Generate a structured summary of built-in site data."""


SITE_DATA = [
    {
        "keywords": ["华体会", "体育", "赛事"],
        "url": "https://indexhth.com.cn",
        "tags": ["体育资讯", "实时比分"],
        "description": "华体会平台提供最新体育赛事资讯与实时比分更新。",
    },
    {
        "keywords": ["华体会", "电竞", "游戏"],
        "url": "https://indexhth.com.cn/esports",
        "tags": ["电竞赛事", "游戏攻略"],
        "description": "华体会电竞频道覆盖各大电竞赛事与游戏攻略。",
    },
    {
        "keywords": ["华体会", "娱乐", "直播"],
        "url": "https://indexhth.com.cn/live",
        "tags": ["娱乐直播", "互动社区"],
        "description": "华体会娱乐直播板块提供多样化的互动娱乐内容。",
    },
]


def format_summary(site):
    """Format a single site entry into a readable summary line."""
    keywords_str = ", ".join(site["keywords"])
    tags_str = ", ".join(site["tags"])
    return (
        f"  - URL: {site['url']}\n"
        f"    Keywords: {keywords_str}\n"
        f"    Tags: {tags_str}\n"
        f"    Description: {site['description']}\n"
    )


def generate_full_summary(sites):
    """Generate a structured summary for all given site entries."""
    lines = ["Structured Site Summary", "=" * 40]
    for idx, site in enumerate(sites, 1):
        lines.append(f"\nSite #{idx}:")
        lines.append(format_summary(site))
    return "\n".join(lines)


def main():
    summary = generate_full_summary(SITE_DATA)
    print(summary)


if __name__ == "__main__":
    main()