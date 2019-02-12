# Network matrix

## Matrix outline

| Recon and Weaponization | Delivery | Initial access | Internal recon | Command and Control | Lateral movement | Actions on objective | Masquerade| Evasion | DOS |
| :--: | :--: | :--: | :--: |  :--: | :--: | :--: |  :--: | :--: | :--: |
|  -  |  -  |  -  |  -  |   -  |  -  |   -  |  -  |  -  | -  |
|  -  |  -  |  -  |  -  |   -  |  -  |   -  |  -  |  -  | -  |

## Jekyll

### Install Jekyll on Mac OSX MoJave

1. `cd ~`
1. `gem install --user-install bundler jekyll`
1. `jekyll new attack_matrix`
1. `cd attack_matrix`

### Building Jekyll site

1. `bundle exec Jekyll build`

### Local testing

1. `jekyll s`

## Adding technique/theme to matrix

### Creating new technique

1. `cp _posts/techniques/2019-02-01-template.md _posts/techniques/<theme>/<technique name>.md`
1. `vim _posts/techniques/<theme>/<technique name>.md` and add:

```yaml
---
layout: post
enabled: <true/false>
title: "<technique name>"
category: techniques
theme: "<theme>"
Id: <0X>
description: "<description>"
---
```

```markdown
{{ page.description }}

## Malware/Threat actors
{% assign malwares = '<List of threat actors(comma seperated) in threat_actors.json>' | split: ',' %}

{% include threat_actor_table.html %}
```

### Creating new theme

1. `cp _posts/themes/2019-02-01-template.md _posts/themes/<theme name>.md`
1. `vim _posts/themes/<theme name>.md` and add:

```yaml
---
layout: post
enabled: <true/false>
title: <theme name>
category: themes
description: "<description>"
---
```

```markdown
{{ page.description }}
```

## Adding threat actor

1. `vim _data/threat_actors.json` and add:

```json
"<threat actor/malware name>": {
        "type": "< threat actor/malware >",
        "description": "< Description of threat actor or malware >",
        "years": "< Known years active >",
        "sources": [
            "<URL to resource>"
        ]
    }
```

## To do

* Make matrix pretty

## Resources/Sources

* [Youtube - Introduction | Jekyll - Static Site Generator | Tutorial 1](https://www.youtube.com/watch?v=T1itpPvFWHI&list=PLLAZ4kZ9dFpOPV5C5Ay0pHaa0RJFhcmcB&index=1)
* [Setting up your GitHub Pages site locally with Jekyll](https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/)
* [Jekyll Includes](https://jekyllrb.com/docs/includes/)