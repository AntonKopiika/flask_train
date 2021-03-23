from jinja2 import Template
# cities = [{'id': 1, 'city': 'Москва'},
#           {'id': 5, 'city': 'Тверь'},
#           {'id': 7, 'city': 'Минск'},
#           {'id': 8, 'city': 'Смоленск'},
#           {'id': 11, 'city': 'Калуга'}]
#
# link = '''<select name="cities">
# {% for c in cities -%}
# {% if c.id > val -%}
# <optional value="{{c['id']}}">{{c['city']}}</option>
# {% endif -%}
# {% endfor -%}
# </select>'''
# tm = Template(link)
# msg = tm.render(cities=cities, val=3)

# cars = [
#     {'model': 'Ауди', 'price': 23000},
#     {'model': 'Шкода', 'price': 17300},
#     {'model': 'Вольво', 'price': 44300},
#     {'model': 'Фольксваген', 'price': 21300}
# ]
#
# tpl = "Автомобиль: {{ (cs | min(attribute='price')).model  }} : {{ (cs | min(attribute='price')).price  }}"
# tpl = 'Автомобиль: {{ cs | replace("о", "О") }}'
# tm = Template(tpl)
# msg = tm.render(cs=cars)

# persons = [
#     {"name": "Алексей", "old": 18, "weight": 78.5},
#     {"name": "Николай", "old": 28, "weight": 82.3},
#     {"name": "Иван", "old": 33, "weight": 94.0}
# ]
#
# tpl = """
# {%- for u in users -%}
# {% filter upper %}{{ u.name }}{% endfilter %}
# {% endfor -%}
# """
# tpl = '''
# {% macro input(name, value='', type='text', size=20) -%}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value|e }}" size="{{ size }}">
# {%- endmacro %}
#
# {{ input('username') }}
# {{ input('email') }}
# {{ input('password') }}'''
tpl = """
{%- macro list_users( list_of_users ) -%}
<ul>
{%- for u in list_of_users %}
    <li>{{u.name}} {{caller(u)}}
{%- endfor %}
</ul>
{%- endmacro -%}
{% call(user) list_users(users) %}
    <ul>
    <li>age: {{user.old}}
    <li>weight: {{user.weight}}
    </ul>
{% endcall -%}
"""
persons = [
    {"name": "Алексей", "old": 18, "weight": 78.5},
    {"name": "Николай", "old": 28, "weight": 82.3},
    {"name": "Иван", "old": 33, "weight": 94.0}
]
tm = Template(tpl)
msg = tm.render(users=persons)
print(msg)