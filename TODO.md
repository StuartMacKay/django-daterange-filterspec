# TODO

This is a list of things to do. First is a list of tasks in the order they 
will be implemented. Following that is a scratchpad of ideas and things that
might be useful. These will either get fleshed out and turned into tasks or 
discarded.

## Tasks

Here is what is planned, roughly in the order it will be implemented:

### Upgrade the layout so it follows django-app-template

Status: In project

Freshen the project structure, so it matches the django-app-template where 
needed. For example move the demo code from apps into demo.

Leave out the Docker related files - an SQLite database is all that's needed
to demonstrate how the filter works.

## Ideas

This area is permanent work in progress. It's a collection of ideas, not all of 
them sensible, and things that might be useful some day or never.

### Discard the change_list.html template

Currently, you need to set the changelist template in a ModelAdmin to pick up 
the css and js files needed to display the daterange filter. That makes it a 
little more awkward to use, particularly if you use apps like django-suit to 
restyle the admin. Double check simplifying adding the css and js in a Media
class is enough to inject the elements need to style the filter correctly.
