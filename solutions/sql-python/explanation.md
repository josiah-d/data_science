# Python-SQL

When writing SQL commands as strings there's no great way to avoid
having big, multi-line strings. It's not ideal, but with SQL it sometimes
happens. One way to avoid this would be to use an ORM like SQLAlchemy to automatically
write your SQL queries. Both approaches are in use. For more formal scenarios
an ORM would be used, but for quick and dirty approaches with fewer modules to import
writing queries as strings would be more likely to be used.

This solution takes some pains to avoid repetitive code, but given the verbosity
of the SQL commands themselves, we can't avoid having a pretty long solution.

# Why use a `__main__` block?

When writing a script, it's always a good practice to use a `__main__` block.
When looking at a `.py` file, experienced users will search for a `__main__`
block to understand what happens when this file is executed as a script.

In this case, we _only_ have a main block, so the effect would be the same
with or without a `__main__` block. So using the `__main__` block essentially
just protects anybody who inadvertently tried to import from `make_users_snapshot.py`
from accidentally running the script.

# Why are the queries, connection and dates defined in `__main__`?

In the case of the pipeline, these essentially constitute _data_ (rather than
execution logic) related
to our pipeline. In other words, the pipeline needs this information
to run properly. Since that information is what defines our pipeline,
we set those in the `__main__` block. You could imagine modifying this script
to take command-line arguments to change the date, for example, or to specify
a different database to run against. If we implemented command line args,
we could use argument parsing inside the main block, and set these variables
based on the parsed args.

# Why is some code in a separate file?

We could define our `Pipeline` class inside the make_users_snapshot.py file.
If we wanted to do this, we would move the `Pipeline` class code above the `__main__`
block and it would work equivalently.

Separating the two files would make most sense if we were going to have many pipelines
each of which defined different queries. In that case, though we could have 
the pipeline code in `make_users_snapshot.py` and import it to other pipelines from
there, it doesn't really belong with that _particular_ pipeline more than any
other one, so it seems like it makes sense to put that piece of reusable code in its
own file and import it everywhere it's needed. Then we can have nice descriptive
names for the script files that will help us remember what they do.

# Why use a class for `Pipeline`?

We could easily just call `c.execute` on each of ours steps inside our
`__main__` script. The pipeline class allows us to clean up our code a little
by removing the duplication that would require. It also allows us to 
hide the creation of the cursor and the `conn.commit` step. Overall,
these are very small optimizations, and doing this with a function
or as a script would be roughly the same for the purposes of this sprint.

In the long run, if we wanted to do more complex tasks with our pipelines,
for example we might want to do some kind of dependency resolution, or automatically
trigger required tasks before another task runs. Extending the functionality in these 
ways would likely be much easier using classes.

# Why didn't you make more tmp tables in SQL instead of using subqueries?

Temporary sql tables used as they are above are largely a way of breaking what 
would otherwise be a very complex query into easier to grasp logical components of 
that query. In this case, I broke the queries into the friends component, the logins
component and the final join step. Further breakdowns are possible, but contribute
less in terms of clarity. This is simlar to using `def` or `lambda`, for 
short functions; for long definitions, `def` probably is clearer, but for very
short definitions `lambda` can still be used clearly and is a little bit more
terse.

# What's COALESCE?

`COALESCE` takes the first non-missing value from a series of columns. This is a
way to address the problem of missing values. In this example we use it to fill `NULL`
values with 0.
