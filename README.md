# DanitonAPI
A global Artificial Intelligence Network called Daniton

API endpoint: api.daniton999.ml

### Currently Available
ChatBot

### Use
`` pip install danitonapi ``

```python
from danitonapi import api
api.token = <TOKEN>
```

#### ChatBot
#### Normal
```python
cb = api.ChatBot(id, username, language)
cb.getAnswer(message)
cb.reset()
```
#### Async
```python
cb = api.ChatBot(id, username, language)
await cb.getAsyncAnswer(message)
cb.reset()
```
