# Network matrix

## Matrix outline

| Recon and Weaponization | Delivery | Initial access | Command and Control | Lateral movement | Actions on objective | Masquerade| Evasion | DOS |
| :--: | :--: | :--: | :--: |  :--: | :--: |  :--: | :--: | :--: |
|  -  |  -  |  -  |  -  |   -  |  -  |   -  |  -  |  -  |
|  -  |  -  |  -  |  -  |   -  |  -  |   -  |  -  |  -  |


## Jekyll

## Install Jekyll on Mac OSX MoJave

1. `cd ~`
1. `gem install --user-install bundler jekyll`
1. `jekyll new attack_matrix`
1. `cd attack_matrix`

## Building site

1. `jekyll build`

## Adding technique/theme

```json
"attack-theme-template": {
    "enabled": false,
    "file_loc": "themes/template.md",
    "technique-template":
    {
        "Id": "0X",
        "file_loc": "techniques/template.md",
        "enabled": true
    }
}
```


## Adding column


## To do

* dos/udp_flood - Resize photo
* Make matrix pretty
* Make each technique/theme page pretty
* Render threat actor table for each technique
* Theme and technique pages in top right

## Resources/Sources

* [Youtube - Introduction | Jekyll - Static Site Generator | Tutorial 1](https://www.youtube.com/watch?v=T1itpPvFWHI&list=PLLAZ4kZ9dFpOPV5C5Ay0pHaa0RJFhcmcB&index=1)