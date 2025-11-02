---
layout: page
title: "📰 All Posts"
permalink: /posts/
---

Welcome to the archive of **Ramblings**.  
Here you’ll find all my posts, notes, and experiments in chronological order.

---

{% for post in site.posts %}
## [{{ post.title }}]({{ post.url | relative_url }})
<small><em>{{ post.date | date: "%B %d, %Y" }}</em></small>

{{ post.excerpt | strip_html | truncate: 200 }}

[Read more →]({{ post.url | relative_url }})

---
{% endfor %}

> Tip: You can also browse the most recent posts on the [home page](/).
