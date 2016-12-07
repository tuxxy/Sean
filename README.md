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

## Why is it named 'Sean'?
Because Sean isn't Jason.
Also, because of https://www.youtube.com/watch?v=DAhG9D9UO7c
