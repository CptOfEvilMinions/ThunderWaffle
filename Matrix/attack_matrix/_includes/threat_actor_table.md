{% assign threat_actors = site.data.threat_actors %}
| Name | Type | Description | Year(s) | Source |
| --- | --- | --- | --- | - |
{%- for malware in malwares %}
    {% assign tmp = threat_actors[0][malware] -%}
    | {{ malware }} | {{ tmp.type }} | {{ tmp.description }} | {{ tmp.years }} |
    {%- for source in tmp.sources -%}
        {%- assign source1 = source | split:'/' -%}
            <a href="{{ source }}">{{ source1[-1] }}</a><br>
    {%- endfor -%}
    |
{%- endfor %}