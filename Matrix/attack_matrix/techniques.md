---
layout: page
title: Techniques
permalink: /techniques/
---

{% assign matrix_table=site.data.matrix_table %}



<table>
    <tbody>
        <!-- Create column headings -->
        <tr>
            <th>Technique</th>
            <th>Id</th>
            <th>Description</th>
        </tr>

        
        <!-- Iterate themes and techniques in each theme defined in matrix_tabele.json -->
        {% for theme in matrix_table %}
            <!-- Skip theme if disabled values -->
            {% if theme[1]['enabled'] == true %}

                <!-- Iterate techniques in each theme -->
                {% for technique in theme[1] %}
                    
                    <tr>
                    <!-- Display technique name if it's enabled -->
                    {% if technique[1]['enabled'] == true %}
                        <td>{{ technique[0] }}</td>
                        <td>{{ technique[1]['Id'] }}</td>
                        <td>{{ technique[1] }}</td>
                    {% endif %}
                    </tr>     

                {% endfor %}

            {% endif %}
            
        {% endfor %}
        
    </tbody>
</table>
