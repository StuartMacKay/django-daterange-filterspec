django-daterange-filterspec
---------------------------

Allows a form with AdminDateWidgets to be used to select a range of dates for
filtering the list of records displayed in the admin.

The forms for each date field to be filtered are displayed in a panel displayed
at the top of the page, which gives plenty of space for the fields and allows
better styling, see the screenshot.

Usage
-----

1. Copy the filterspecs.py file to your project.

2. Edit your model to specify which fields will use the date range filter by
   adding an attribute 'date_range_filter' and set it to any suitable value:

   ::

       date_added.date_range_filter = True

   The test to determine whether to display the date range or the regular
   date filterspec is performed by testing for the presence of the attribute
   rather than testing for a given value.

   The first field to use to the date range filterspec must also set an
   attribute to load the javascript and stylesheet for the calendar widget:

   ::

       date_added.show_media = True

   This ensures that the javascript used to display the calendar widget next
   to each date field is only executed once.

3. Edit the model admin to specify which fields will be filtered:

   ::

       list_filter = ['date_added', 'date_modified']

   Then register the daterange filterspec:

   ::

       FilterSpec.filter_specs.insert(0,
           (lambda f: hasattr(f, 'date_range_filter'), DateRangeFilterSpec))

   Registration could be performed in the filterspecs.py file but this ensures
   that the import is not flagged as unused.

4. Add the templates to your project:

   ::

       admin/change_list.html
       admin/daterange/date_range_form.html

   If you have not already done so, in your settings file, set the directory
   where templates will be loaded from so that the the local templates are
   found first rather than the ones from the INSTALLED_APPS.

5. Add the stylesheet to your project.

   ::

       static/css/admin.css

   This file is references on line 7 of the change_list.html template so be
   sure to update this if you move the file somewhere else or simply add the
   styles to your main stylesheet.

6. Start filtering...


Project
-------

This project comes with a basic Django project so you can quickly see the
filters in action. The model contains two date fields, date_added and
date_modified. Only the date_added field uses the date range filterspec,
the date_modified field uses the built-in DateFilterSpec so you can see how
the two differ.

Create a media directory in the root directory of the project and create 
a link to (or copy) the media files (images, stylesheets and javascript) 
from the django admin.

To start the project run the following commands:

::

    python manage.py syncdb
    python manage.py loaddata daterange
    python manage.py runserver
    
