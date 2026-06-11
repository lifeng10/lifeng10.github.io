import re

with open('site/_layouts/bib.liquid', 'r') as f:
    content = f.read()

old = (
    '        {%- if author_is_self -%}\n'
    '          <em>\n'
    '            {{- author.first }}\n'
    '            {{ author_last_html -}}\n'
    '          </em>'
)
new = (
    '        {%- if author_is_self -%}\n'
    '          <em><strong>{{- author.first }} {{ author_last_html -}}</strong></em>'
    '{%- if entry.corresponding == "true" %}'
    ' <sup title="Corresponding Author" style="color:#b03a2e;">'
    '<i class="fas fa-envelope"></i></sup>'
    '{%- endif %}'
)

result = content.replace(old, new)
if result == content:
    print('WARNING: exact pattern not found, trying regex fallback')
    result = re.sub(
        r'(\{%-\s*if author_is_self\s*-%\}\s*)<em>(.*?)</em>',
        r'\1<em><strong>\2</strong></em>'
        r'{%- if entry.corresponding == "true" %}'
        r' <sup title="Corresponding Author" style="color:#b03a2e;">'
        r'<i class="fas fa-envelope"></i></sup>'
        r'{%- endif %}',
        result, flags=re.DOTALL
    )

# Color venue badges by publication type when venue metadata is absent.
# Journals (article) -> green, conferences (inproceedings/incollection) -> blue.
abbr_old = (
    '        {% else %}\n'
    '          <abbr class="badge rounded w-100">{{ entry.abbr }}</abbr>\n'
    '        {% endif %}'
)
abbr_new = (
    '        {% else %}\n'
    '          {% if entry.type == \'article\' %}\n'
    '            <abbr class="badge rounded w-100" style="background-color:#1b8a5a;">{{ entry.abbr }}</abbr>\n'
    '          {% elsif entry.type == \'inproceedings\' or entry.type == \'incollection\' %}\n'
    '            <abbr class="badge rounded w-100" style="background-color:#1f5fbf;">{{ entry.abbr }}</abbr>\n'
    '          {% else %}\n'
    '            <abbr class="badge rounded w-100">{{ entry.abbr }}</abbr>\n'
    '          {% endif %}\n'
    '        {% endif %}'
)

result2 = result.replace(abbr_old, abbr_new)
if result2 == result:
    print('WARNING: abbr exact pattern not found, trying regex fallback')
    result2 = re.sub(
        r'(\{\%\s*else\s*\%\}\s*)<abbr class="badge rounded w-100">\{\{\s*entry\.abbr\s*\}\}</abbr>(\s*\{\%\s*endif\s*\%\})',
        r'\1{% if entry.type == \'article\' %}\n'
        r'            <abbr class="badge rounded w-100" style="background-color:#1b8a5a;">{{ entry.abbr }}</abbr>\n'
        r'          {% elsif entry.type == \'inproceedings\' or entry.type == \'incollection\' %}\n'
        r'            <abbr class="badge rounded w-100" style="background-color:#1f5fbf;">{{ entry.abbr }}</abbr>\n'
        r'          {% else %}\n'
        r'            <abbr class="badge rounded w-100">{{ entry.abbr }}</abbr>\n'
        r'          {% endif %}\2',
        result2,
        flags=re.DOTALL,
    )

with open('site/_layouts/bib.liquid', 'w') as f:
    f.write(result2)
print('bib.liquid patched successfully')
