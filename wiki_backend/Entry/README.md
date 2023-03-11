# Views

## TagList

Return all the tags

| name | value|
| --- | --- |
| ViewName| TagList | 
| url | `entry/tags` | 
| Return Type| json |
| Return Example | [\{id : --, name: ---, number: ---, update_date: ---\}, ] |

usage:

```javascript
axios.get("entry/tags")
    .then(res=>{
        _this.taglist = res.data
    })
```

## CreateEntry

Receive Parameters:

```json
{"tag":[], "content":"", "title": ""  }
```

## detail

Return the detailed content of a post 

|name| value|
|---|---|
|ViewName| detail|
|url | `entry/entry/<:id>`|
|Return Type| json|
|Return Example| ['id' :10,'client' :\<Object: Client\>,'title','create_date','tag'] |

```javascript

```
