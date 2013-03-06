In sublime text 2 when running ruby spec's
I want to copy the path of the spec to the clipboard.
Otherwise I just want to copy the whole path.

(On mac) Move the filename_to_clipboard_command.py into
~/Library/Application Support/Sublime Text 2/Packages/User

Add this to your Users Keybindings in preferences:

```javascript
{ "keys": ["ctrl+super+t"], "command": "filename_to_clipboard" },
```