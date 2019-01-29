---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---
{% assign matrix_table=site.data.matrix_table %}


<table>
    <caption>Table caption</caption>
    <thead>
    {% for theme in matrix_table %}
        <th>{{ theme[0] }}</th>
    {% endfor %}
    </thead>
    <tbody>
    {% for theme in matrix_table %}
        <tr>
        {% for technique in theme[1] %}
            <td>{{ theme[0] }}: {{ technique[0] }}</td>
        {% endfor %}
        </tr>
    {% endfor %}
    </tbody>
</table>