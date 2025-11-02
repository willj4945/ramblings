---
layout: home
title: "Ramblings"
permalink: /
---

# 🌀 Ramblings

> Notes, ideas, and experiments — a place to ramble about what I’m building and learning.

Welcome to **Ramblings** — my little corner of the web where I write about technology, code, privacy, hacking, and anything else that catches my attention.  
This is a place for in-progress thoughts, personal experiments, and lessons I pick up along the way.

I don’t promise polished tutorials or perfect answers — just honest notes and ideas from my own learning process.

---

## 🧩 Recent Posts

{% for post in site.posts limit:5 %}

- [{{ post.title }}]({{ post.url | relative_url }})  
  <small><em>{{ post.date | date: "%B %d, %Y" }}</em> — {{ post.excerpt | strip_html | truncate: 160 }}</small>
{% endfor %}

[**Browse all posts →**](/posts)

---

## 🧠 About This Site

**Ramblings** is built with [Jekyll](https://jekyllrb.com/) and hosted on [GitHub Pages](https://pages.github.com/).  
The site is intentionally minimal — it’s more notebook than magazine, a space to think out loud and track what I’m learning.

If you’d like to follow along, check out my work on [GitHub](https://github.com/yourusername) or drop by occasionally to see what’s new.

---

> “The best way to learn is to write it down — even if it’s messy.”
