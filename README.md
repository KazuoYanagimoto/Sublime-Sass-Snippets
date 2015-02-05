# Sublime-Sass-Snippets
A collection of Sass Snippets for Sublime Text 2/3

##Install
Download ZIP and un-zip the file under Sublime Text 2(3) > Packages directory.

###Usage
___
+ Auto-complete: Sass Snippets automatically bring up snippets as you type..
+ Command Palette: Open Command Palette, and type "sass", "sassf", "saf", or "function" to show all the sass snippets.
+ Completions: To bring up all the available completions list, press "Ctrl+spacebar" (by default).

> I recommend adding following lines to your preferences: Preferences >Settings - User

```json
"auto_complete_triggers": {"characters": "", "selector": "source.scss, source.sass"},
"tab_completion": false
```

+ Cheat Sheet: You can find from Tools > Sass Snippets > Open CheatSheet/  
or from Tools > Command Palette, and type "open cheat", there will be "Sass Snippets: Open CheatSheet" to open url.

> Tips: You can also access it by right click and go to Sass Snippets > Open CheatSheet/

####Limitation
___
There is a technical conflict between .scss syntax and sass.sublime-completions/  
> As walkaround, set syntax .sass instead if you want to activate sass.sublime-complications.
