# FuckFakeGitHubStars

**NOTICE:** The results are for your reference only. 

## Usage

1. Fill your GitHub secret token in `fetchdata.py`
2. Set `SEARCH_NODE_ID` in `fetchdata.py`
3. Run `fetchdata.py`
4. Run `processingdata.py`
5. See log files in `data` folder

You can get repo or user's node ID via GitHub GraphQL API.

[GraphiQL](https://developer.github.com/v4/explorer/) example:

```
query {
  repository(owner: "CocoaDebug", name: "CocoaDebug") {
    id
  }
}
```

Result is `MDEwOlJlcG9zaXRvcnkxMTc1MTM4NTI=` 

```
{
  "data": {
    "repository": {
      "id": "MDEwOlJlcG9zaXRvcnkxMTc1MTM4NTI="
    }
  }
}
```

## Disclaimer

This is just some messy code. I really don't know what it is. Don't ask me!