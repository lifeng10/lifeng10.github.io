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

with open('site/_layouts/bib.liquid', 'w') as f:
    f.write(result)
print('bib.liquid patched successfully')
