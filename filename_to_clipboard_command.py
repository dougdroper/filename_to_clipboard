#Add this to the User Keybindings
#{ "keys": ["ctrl+super+t"], "command": "filename_to_clipboard" },

import sublime, sublime_plugin, os

class FilenameToClipboardCommand(sublime_plugin.TextCommand):
   def run(self, edit):
      s = str(self.view.file_name())
      s = s if s.find("spec") == -1 else s[s.find('spec'):]
      sublime.set_clipboard(s)