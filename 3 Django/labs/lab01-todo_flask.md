

# Lab 1 Flask TODO


## Part 1

Create a folder called `lab01` to hold all the files for your lab. Inside that create `database.json` with the following content:

```json
{
  "todos":[
    {
      "text": "walk the dog",
      "priority": "high"
    },{
      "text":"butter the cat",
      "priority":"medium",
    },{
      "text":"wash dishes",
      "priority":"low"
    }
  ]
}
```

Create a flask app to load this data `with open...`, parse it using the `json` library, and render a template to display the data. Below is an example of parsing and encoding json:

```python
import json
data = '{"name": "bob"}'
data = json.loads(data) # json string -> python dictionary
print(data['name']) # bob
data = json.puts(data) # python dictionary -> json string
print(data)
```

The resulting HTML should look something like:

```html
<ul>
  <li>walk the dog</li>
  <li>butter the cat</li>
  <li>wash dishes</li>
</ul>
```

## Part 2


Using a `form`, allow the user to save data



