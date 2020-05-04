# RenameWithDict
This python code renames all files under a **specific directory** with a given **dictionary**.

Note: The dictionary has to be saved as Json-format.

Export Dictionary type to Json:

```python
f = codecs.open('dictionary', 'w', 'utf-8')
f.write(json.dumps(name_dict, ensure_ascii=False))
```

Import Json to Dictionary:

```python
name_dict = json.load(open('dictionary', encoding='utf-8'))
```