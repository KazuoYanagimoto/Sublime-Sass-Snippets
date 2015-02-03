# Sublime-Sass-Snippets
A collection of Sass Snippets for Sublime Text 2/3

##Install
Download ZIP and un-zip the file under Sublime Text 2(3) > Packages directory.

###Usage
Auto-complete: Sass Snippets automatically suggest snippets as you type..
Command Palette: Open Command Palette, and type sass, sassf, saf, or function to show all the sass snippets.
Completions: To bring up all the available completions list, press "Ctrl+spacebar" as default settings.
I recommend adding following lines to your preferences: Preferences >Settings - User

```json
"auto_complete_triggers": {"characters": "", "selector": "source.scss"},
"tab_completion": false
```

####Limitation
There is a confliction for using sass.sublime-completions when you set syntax .scss/
+ As walkaround, set syntax .sass instead if you want activate sass.sublime-complications.