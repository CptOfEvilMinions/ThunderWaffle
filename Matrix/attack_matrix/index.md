---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---
{% assign matrix_table=site.data.matrix_table %}

<table>
    <tbody>
        <!-- Iterate themes and techniques in each theme defined in matrix_tabele.json -->
        {% for theme in matrix_table %}
            <tr>
            <!-- Obtain attack theme which is the key -->
            <td>{{ theme [0] }}</td>
                <!-- Iterate techniques in each theme -->
                {% for technique in theme[1] %}
                    <!-- Display technique name if it's enabled -->
                    {% if technique[1]['enabled'] == true %}
                        <td>
                            <a href="/{{ technique[1]['file_loc'] }}">{{ technique[0] }}</a>
                        </td>
                    {% endif %}
                {% endfor %}
            </tr>
        {% endfor %}
    </tbody>
</table>
<p><a href="#">Rotate table</a></p>

<style>
    table, caption, thead, tbody, td, tr{
        border: 1px solid black;
        padding: 1rem;
    }

</style>

<script src="jquery-3.3.1.min.js"></script>
<script>

    $("a").click(function(){
    $("table").each(function() {
        var $this = $(this);
        var newrows = [];
        $this.find("tr").each(function(){
            var i = 0;
            $(this).find("td").each(function(){
                i++;
                if(newrows[i] === undefined) { newrows[i] = $("<tr></tr>"); }
                newrows[i].append($(this));
            });
        });
        $this.find("tr").remove();
        $.each(newrows, function(){
            $this.append(this);
        });
    });
    
    return false;
});
</script>