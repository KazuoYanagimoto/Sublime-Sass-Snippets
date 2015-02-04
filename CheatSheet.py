import sublime_plugin

import webbrowser

# available commands
# open_cheat_sheet

def browse(happy):
	url = 'https://' + happy
	webbrowser.open_new_tab(url)

class OpenCheatSheetCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		happy = 'github.com/KazuoYanagimoto/sublime-sass-snippets/blob/master/CheatSheet.md'
		browse(happy)
