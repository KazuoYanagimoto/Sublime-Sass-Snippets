##Functions

###RGB Functions

######Creates a Color object from red, green, and blue values. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#rgb-instance_method)

```sass
rgb(${1:\$red}, ${2:\$green}, ${3:\$blue})
```

######Creates a Color from red, green, blue, and alpha values. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#rgba-instance_method)

```sass
rgba(${1:\$red}, ${2:\$green}, ${3:\$blue}, ${4:\$alpha})
```

######Sets the opacity of an existing color. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#rgba-instance_method)

```sass
rgba(${1:\$color}, ${2:\$alpha})
```

######Gets the red component of a color. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#red-instance_method)

```sass
red(${1:\$color})
```

######Gets the green component of a color. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#green-instance_method)

```sass
green(${1:\$color})
```

######Gets the blue component of a color. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#blue-instance_method)

```sass
blue(${1:\$color})
```

######Mixes two colors together. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#mix-instance_method)

```sass
mix(${1:\$color1}, ${2:\$color2}, ${3:\$weight:50%})
```

###HSL Functions

######Creates a Color from hue, saturation, and lightness values. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#hsl-instance_method)

```sass
hsl(${1:\$hue}, ${2:\$saturation}, ${3:\$lightness})
```

######Creates a Color from hue, saturation, lightness, and alpha values. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#hsla-instance_method)

```sass
hsla(${1:\$hue}, ${2:\$saturation}, ${3:\$lightness}, ${4:\$alpha})
```

######Gets the hue component of a color. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#hue-instance_method)

```sass
hue(${1:\$color})
```

######Gets the saturation component of a color. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#saturation-instance_method)

```sass
saturation(${1:\$color})
```

######Gets the lightness component of a color. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#lightness-instance_method)

```sass
lightness(${1:\$color})
```

######Changes the hue of a color. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#adjust_hue-instance_method)

```sass
adjust-hue(${1:\$color}, ${2:\$degrees})
```

######Makes a color lighter. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#lighten-instance_method)

```sass
lighten(${1:\$color}, ${2:\$amount})
```

######Makes a color darker. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#darken-instance_method)

```sass
darken(${1:\$color}, ${2:\$amount})
```

######Makes a color more saturated. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#saturate-instance_method)

```sass
saturate(${1:\$color}, ${2:\$amount})
```

######Makes a color less saturated. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#desaturate-instance_method)

```sass
desaturate(${1:\$color}, ${2:\$amount})
```

######Converts a color to grayscale. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#grayscale-instance_method)

```sass
grayscale(${1:\$color})
```

######Returns the complement of a color. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#complement-instance_method)

```sass
complement(${1:\$color})
```

######Returns the inverse of a color. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#invert-instance_method)

```sass
invert(${1:\$color})
```

###Opacity Functions

######Gets the alpha component (opacity) of a color. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#alpha-instance_method)

```sass
alpha(${1:\$color})
```

######Returns the alpha component (opacity) of a color. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#opacity-instance_method)

```sass
opacity(${1:\$color})
```

######Changes the alpha component for a color. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#rgba-instance_method)

```sass
rgba(${1:\$red}, ${2:\$green}, ${3:\$blue}, ${4:\$alpha})
```

```sass
rgba(${1:\$color}, ${2:\$alpha})
```

######Makes a color more opaque. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#opacify-instance_method)

```sass
opacify(${1:\$color}, ${2:\$amount})
```

```sass
fade-in(${1:\$color}, ${2:\$amount})
```

######Makes a color more transparent. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#transparentize-instance_method)

```sass
transparentize(${1:\$color}, ${2:\$amount})
```

```sass
fade-out(${1:\$color}, ${2:\$amount})
```

### Other Color Functions

######Increases or decreases one or more components of a color. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#adjust_color-instance_method)

```sass
adjust-color(${1:\$color}, ${2:[\$red]}, ${3:[\$green]}, ${4:[\$blue]}, ${5:[\$hue]}, ${6:[\$saturation]}, ${7:[\$lightness]}, ${8:[\$alpha]})
```

######Fluidly scales one or more properties of a color. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#scale_color-instance_method)

```sass
scale-color(${1:\$color}, ${2:[\$red]}, ${3:[\$green]}, ${4:[\$blue]}, ${5:[\$saturation]}, ${6:[\$lightness]}, ${7:[\$alpha]})
```

######Changes one or more properties of a color. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#change_color-instance_method)

```sass
change-color(${1:\$color}, ${2:[\$red]}, ${3:[\$green]}, ${4:[\$blue]}, ${5:[\$hue]}, ${6:[\$saturation]}, ${7:[\$lightness]}, ${8:[\$alpha]})
```

######Converts a color into the format understood by IE filters. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#ie_hex_str-instance_method)

```sass
ie-hex_str(${1:\$color})
```

### String Functions

######Removes quotes from a string. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#unquote-instance_method)

```sass
unquote(${1:\$string})
```

######Adds quotes to a string. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#quote-instance_method)

```sass
quote(${1:\$string})
```

######Returns the number of characters in a string. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#str_length-instance_method)

```sass
str-length(${1:\$string})
```

######Inserts $insert into $string at $index. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#str_insert-instance_method)

```sass
str-insert(${1:\$string}, ${2:\$insert}, ${3:\$index})
```

######Returns the index of the first occurance of $substring in $string. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#str_index-instance_method)

```sass
str-index(${1:\$string}, ${2:\$substring})
```

######Extracts a substring from $string. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#str_slice-instance_method)

```sass
str-slice(${1:\$string}, ${2:\$start-at}, ${3:\$end-at:-1})
```

######Converts a string to upper case. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#to_upper_case-instance_method)

```sass
to-upper-case(${1:\$string})
```

######Converts a string to lower case. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#to_lower_case-instance_method)

```sass
to-lower-case(${1:\$string})
```

### Number Functions

######Converts a unitless number to a percentage. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#percentage-instance_method)

```sass
percentage(${1:\$number})
```

######Rounds a number to the nearest whole number. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#round-instance_method)

```sass
round(${1:\$number})
```

######Rounds a number up to the next whole number. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#ceil-instance_method)

```sass
ceil(${1:\$number})
```

######Rounds a number down to the previous whole number. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#floor-instance_method)

```sass
floor(${1:\$number})
```

######Returns the absolute value of a number. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#abs-instance_method)

```sass
abs(${1:\$number})
```

######Finds the minimum of several numbers. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#min-instance_method)

```sass
min(${1:\$numbers...})
```

######Finds the maximum of several numbers. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#max-instance_method)

```sass
max(${1:\$numbers...})
```

######Returns a random number. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#random-instance_method)

```sass
random(${1:\$limit})
```

### List Functions

>All list functions work for maps as well, treating them as lists of pairs.

######Returns the length of a list. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#length-instance_method)

```sass
length(${1:\$list})
```

######Returns a specific item in a list. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#nth-instance_method)

```sass
nth(${1:\$list}, ${2:\$n})
```

######Replaces the nth item in a list.

```sass
set-nth(${1:\$list}, ${2:\$n}, ${3:\$value})
```

######Joins together two lists into one. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#join-instance_method)

```sass
join(${1:\$list1}, ${2:\$list2}, ${3:\$separator:auto})
```

######Appends a single value onto the end of a list. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#append-instance_method)

```sass
append(${1:\$list}, ${2:\$val}, ${3:\$separator:auto})
```

######Combines several lists into a single multidimensional list. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#zip-instance_method)

```sass
zip(${1:\$lists...})
```

######Returns the position of a value within a list. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#index-instance_method)

```sass
index(${1:\$list}, ${2:\$value})
```

######Returns the separator of a list. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#list_separator-instance_method)

```sass
list-separator(${1:\$list})
```

### Map Functions

######Returns the value in a map associated with a given key. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#map_get-instance_method)

```sass
map-get(${1:\$map}, ${2:\$key})
```

######Merges two maps together into a new map. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#map_merge-instance_method)

```sass
map-merge(${1:\$map1}, ${2:\$map2})
```

######Returns a new map with keys removed. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#map_remove-instance_method)

```sass
map-remove(${1:\$map}, ${2:\$keys...})
```

######Returns a list of all keys in a map. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#map_keys-instance_method)

```sass
map-keys(${1:\$map})
```

######Returns a list of all values in a map. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#map_values-instance_method)

```sass
map-values(${1:\$map})
```

######Returns whether a map has a value associated with a given key. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#map_has_key-instance_method)

```sass
map-has-key(${1:\$map}, ${2:\$key})
```

######Returns the keywords passed to a function that takes variable arguments. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#keywords-instance_method)

```sass
keywords(${1:\$args})
```

### Selector Functions

>Selector functions are very liberal in the formats they support for selector arguments. They can take a plain string, a list of lists as returned by & or anything in between:

* A plain sring, such as ".foo .bar, .baz .bang".
* A space-separated list of strings such as (".foo" ".bar").
* A comma-separated list of strings such as (".foo .bar", ".baz .bang").
* A comma-separated list of space-separated lists of strings such as ((".foo" ".bar"), (".baz" ".bang")).

In general, selector functions allow placeholder selectors (%foo) but disallow parent-reference selectors (&).

######Nests selector beneath one another like they would be nested in the stylesheet. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#selector_nest-instance_method)

```sass
selector-nest(${1:\$selectors...})
```

######Appends selectors to one another without spaces in between. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#selector_append-instance_method)

```sass
selector-append(${1:\$selectors...})
```

######Extends $extendee with $extender within $selector. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#selector_extend-instance_method)

```sass
selector-extend(${1:\$selector}, ${2:\$extendee}, ${3:\$extender})
```

######Replaces $original with $replacement within $selector. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#selector_replace-instance_method)

```sass
selector-replace(${1:\$selector}, ${2:\$original}, ${3:\$replacement})
```

######Unifies two selectors to produce a selector that matches elements matched by both. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#selector_unify-instance_method)

```sass
selector-unify(${1:\$selector1}, ${2:\$selector2})
```

######Returns whether $super matches all the elements $sub does, and possibly more. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#is_superselector-instance_method)

```sass
is-superselector(${1:\$super}, ${2:\$sub})
```

######Returns the simple selectors that comprise a compound selector. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#simple_selectors-instance_method)

```sass
simple-selectors(${1:\$selector})
```

######Parses a selector into the format returned by &. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#selector_parse-instance_method)

```sass
selector-parse(${1:\$selector})
```

### Introspection Functions

###### Returns whether a feature exists in the current Sass runtime. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#feature_exists-instance_method)

```sass
feature-exists(${1:\$feature})
```

###### Returns whether a variable with the given name exists in the current scope. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#variable_exists-instance_method)

```sass
variable-exists(${1:\$name})
```

###### Returns whether a variable with the given name exists in the global scope. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#global_variable_exists-instance_method)

```sass
global-variable-exists(${1:\$name})
```

###### Returns whether a function with the given name exists. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#function_exists-instance_method)

```sass
function-exists(${1:\$name})
```

###### Returns whether a mixin with the given name exists. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#mixin_exists-instance_method)

```sass
mixin-exists(${1:\$name})
```

###### Returns the string representation of a value as it would be represented in Sass. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#inspect-instance_method)

```sass
inspect(${1:\$value})
```

###### Returns the type of a value. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#type_of-instance_method)

```sass
type-of(${1:\$value})
```

###### Returns the unit(s) associated with a number. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#unit-instance_method)

```sass
unit(${1:\$number})
```

###### Returns whether a number has units. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#unitless-instance_method)

```sass
unitless(${1:\$number})
```

###### Returns whether two numbers can be added, subtracted, or compared. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#comparable-instance_method)

```sass
comparable(${1:\$number1}, ${2:\$number2})
```

###### Dynamically calls a Sass function. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#call-instance_method)

```sass
call(${1:\$name}, ${2:\$args...})
```

### Miscellaneous Functions

######Returns one of two values, depending on whether or not $condition is true. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#if-instance_method)

```sass
if(${1:\$condition}, ${2:\$if-true}, ${3:\$if-false})
```

######Returns a unique CSS identifier. [>>](http://sass-lang.com/documentation/Sass/Script/Functions.html#unique_id-instance_method)

```sass
unique-id(${1:})
```
