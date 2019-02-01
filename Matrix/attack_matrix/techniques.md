---
layout: page
title: Techniques
permalink: /techniques/

---
total {{site.posts | size}}

{% assign posts = site.posts}

{% for post in posts %}

<a href="{{site.baseurl}}{{post.url}}">yeet</a>

{{% endfor %}}