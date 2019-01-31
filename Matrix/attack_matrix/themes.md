---
layout: page
title: Themes
permalink: /themes/
---

{% assign matrix_table=site.data.matrix_table %}



<table>
    <tbody>
        <!-- Create column headings -->
        <tr>
            <th>Theme</th>
            <th>Description</th>
        </tr>

        
        <!-- Iterate themes and techniques in each theme defined in matrix_tabele.json -->
        {% for theme in matrix_table %}
            <!-- Skip theme if disabled values -->
            {% if theme[1]['enabled'] == true %}
                <tr>
                    <!-- Display theme name if it's enabled -->
                        <td>{{ theme[0] }}</td>
                        <td></td>
                </tr>
            {% endif %}
            
        {% endfor %}
        
    </tbody>
</table>
