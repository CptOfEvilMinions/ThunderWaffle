---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---
{% assign matrix_table=site.data.matrix_table %}


<div class="matrix">

{% for theme in matrix_table %}
<div class="theme">
    <p class="bold"> 
        {{ theme [0] }}
    </p>
    <div class="techniques">
        {% for technique in theme[1] %}
        <p>
            {{technique[0]}}
        <p>
        {{% endfor %}}
    </div>
</div>
{% endfor %}


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

