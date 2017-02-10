# Sean
Sean is a JSON value factory. It takes a provided schema and outputs values
that match that schema for testing and whatnot.

## The Sean syntax
Sean syntax is valid JSON which means that it can be read with any JSON parser.

The two primary gotchas are iterables. In the Sean syntax, an iterable's data
is declared with the `_val` keyword. See the example below:

```
{
    "family": {
        "_type": "list",
        "_len": 3,
        "_val": {
            "_type": "dict",
            "_val": {
                "name": {"_type": "name"},
                "age": {"_type": "int", "_len": 2},
                "email": {"_type": "email"},
                "current_residence": {"_type": "bool"},
                "description": {"_type": "text"},
                "room_name": ["Room 1", "Room 2", "Room 3"],
                "time_added": {"_type": "timestamp"}
            }
        }
    }
}
```

In the above example, `family` is a key that points to a list-of-dicts. The
`_len` keyword declares how many times the `_val` will be repeated when using a
Sean `list`. This `_len` must be a value greater than 0.

When using Sean, a JSON list becomes a random choice! In the above example,
look at `room_name`. This declares that Sean must pick one of the three values
at random.

In Sean, a `timestamp` will be a unix timestamp and will always be within the
current month.

## Using Sean
Sean is pretty easy to use. First, you will need a Sean schema. This isn't
shown in the creation, so for this we'll assume that the example above was used
and it was named 'family.sean'.

After you've made the Sean schema file, read it and create your Sean factory
like this:
```
import Sean

with open('family.sean') as f:
    sean_data = f.read()

sean_factory = Sean.Sean(sean_data)
```

After you have your factory, you are good to generate your JSON! Sean reads
your schema and creates an in-memory copy of it that replaces the values
with `SeanType` objects. These are able to be executed in place and generate
the values you want. This allows you to generate files really quickly!
Generating is simple, too:
```
values = sean_factory.seanify()
```

Once generated, `values` will be a JSON string that you are free to use
however.

### Custom Handlers
In Sean, a handler is a function that a `SeanType` executes to render your
value in place. These are called by declaring a `_type` in your schema. For
example:
```
"foobar": {"_type": "string", "_len": 10}
```
will generate a random string 10 chars long.

This actually calls a function (`sean.handlers.sean_string`).

Sean allows for the creation of custom handlers in the event that you need
your own datatype in your schema. We'll make a test one that always generates
a string of "foobar" for `_len` times. Let's call the type `foobar`!
```
def sean_foobar(**kwargs):
    _len = kwargs.get('_len', 1)
    return ''.join('foobar' for i in range(_len))
```

Do you see how we passed in the `_len` param? You can name this whatever you
want and use it in the schema. In Sean, the schema type is passed as a dict,
that's what is used for the `**kwargs` argument.

To add this handler to Sean, you use the `override_handlers` argument.
```
my_handlers = {
    'foobar': sean_foobar,
}

sean_factory = Sean.Sean(sean_data, override_handlers=my_handlers)
```

In the `my_handlers` example, we declared a key of `foobar` to `sean_foobar`.
This is what sets the `_type`. You can now use `"_type": "foobar"` in your
schema!

#### Override Default Handlers
Sean allows you to override a default handler exactly like the above. If you
wanted to replace the `string` default type, you would replace the `foobar` key
in the previous example with `string`:
```
my_handlers = {
    'string': sean_foobar,
}
```

It's that easy!
        
## Why is it named 'Sean'?
Because Sean isn't Jason.
Also, because of https://www.youtube.com/watch?v=DAhG9D9UO7c
