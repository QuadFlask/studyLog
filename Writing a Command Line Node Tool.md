Writing a Command Line Node Tool
---------------

http://blog.npmjs.org/post/118810260230/building-a-simple-command-line-tool-with-npm
http://javascriptplayground.com/blog/2015/03/node-command-line-tool/
http://javascriptplayground.com/blog/2012/08/writing-a-command-line-node-tool/

`mkdir myTool`

`cd myTool`

`npm init` 

```
his utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help json` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg> --save` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
name: (color-darker)
version: (1.0.0)
description:
entry point: (index.js)
test command:
git repository:
keywords:
author: flask
license: (ISC) MIT
About to write to /Users/flask/Documents/workspace_js/color-darker/package.json:

{
  "name": "color-darker",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "flask",
  "license": "MIT"
}
```

`vi package.json`

```
  "bin": "index.js"
```

`npm install --save shelljs`

`vi index.js`

```
#! /usr/bin/env node
var shell = require("shelljs");

shell.exec("echo shell.exec works");
```

`npm link`

done!


