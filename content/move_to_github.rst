Moving Back to Github
#####################

:date: 2014-12-20
:modified: 2015-04-17
:slug: moving-back-to-github
:authors: Steven E. Lamberson Jr.
:tags: archlinux, centos, cgit, debian, git, github, gitolite, jenkins, nginx, redmine, travis-ci, uwsgi, wordpress
:category: Computing
:summary: After a long hiatus I am back to github.

.. contents::

.. figure:: {filename}/images/Octocat.png
    :alt: The Github octopus.
    :align: left

    The Github octocat_.

Once Upon A Time
----------------

Once upon a time, a long time ago, I was a happy github_ user.  However these
were the days before github pages, travis-ci_, and readthedocs_ (or, if they
existed, I didn't know about them).  I needed to have some other service to
host my blog, do my continuous integration testing, and host my software's
built documentation.  After looking around for options I decided that I was
just going to host them myself using wordpress_, jenkins_, and some home-grown
post-commit hooks to build and move the documentation to my web server.

Since I was going to be hosting some of my own applications anyway, I started
wondering if I should replace github with my own git repository mirror and
issue tracker.  I don't remember all my thoughts that went into that decision,
but I do remember holding many of the opinions expressed here_.  Particularly I
remember being disatisifed with github's pull requests being incompatible with
git's pull requests (an opinion shared by others, including `Linus Torvalds`_).  I also remember seeing a few features in redmine_ that were not available in github's issue tracker, but I don't remember now what those features were.

I also suffer from the affliction of being fiercly independent.  Why let
someone else host my stuff when I am perfectly capable of doing it on my own?

Self-hosted Solution
--------------------

So, I decided to move to an entirely self-hosted solution.  Well, not
"entirely".  I had it all set up on a linode, not my own hardware, but apart
from that I did it all myself.  I hosted the git repositories using gitolite_
and provided a browser view to them using cgit_.  I set up a redmine_ issue
tracker and had a jenkins_ continuous integration server, that were both
tightly coupled to the git repositories containing the code they were
interested in.  I had my own wordpress_ instance to host my blog (which I
eventually ditched for pelican_).  I even eventually had my own instance of
readthedocs_ to automatically build the documentation.  And all of this was
hosted using nginx_ and uwsgi_.

It was a pretty sweet setup.  It took several months to get setup, but by the
end it was awesome.  But it was also fragile.

I initially tried to set it up on centos_ and debian_, but I couldn't get
redmine to work in uwsgi on either of those.  I finally tried again using
archlinux_ and was able to get it working.  This worked great for a while, but
the redmine/uwsgi setup would break about once a month after updating the box,
even when updating packages that didn't seem like they'd matter to the setup.


Reflecting on the Choice
------------------------

I had just finished fixing the redmine/uwsgi setup again after an update from
archlinux when I realized something.  I had just spent all of my free time for
the day fixing my software infrastructure instead of doing what I really wanted
to do, which was work on one of my software applications.  I pondered the
situation over the next few days, and eventually decided to abandon my setup
and move to a less self-hosted plan.  I do not regret my earlier decision to go
self-hosted because I learned a lot about various technologies and about
myself, but I am definitely ready for something else.

Here are some of the things I learned, in no particular order.  Maybe they will
help other people make their own decision, but at least they will remind me of
how I felt when I get the itch to do it myself in a few months or years.

- **I would much rather spend my time developing my software applications than
  maintaining my software infrastructure.** I had come to this conclusion
  before when it came to Linux distributions and window managers vs. desktop
  environments, but it applies to this as well.

- **I hate deploying ruby/rails apps.**  The php and C applications I deployed
  were all very simple to setup, but the ruby/rails applications were much
  harder to do and much more fragile.  The python applications I tried were
  also a challenge, but they didn't seem near as bad as the ruby ones.  Maybe I
  just need more experience, but my current thinking is I will never host my
  own ruby application ever again.

Back to Github
--------------

So, here I am, moving back to github_.  I'll do everything I can on github,
like issue tracking and git hosting, and I'll use readthedocs_ to host my
documentation and travis-ci_ to host my continuous integration testing.  I've
even moved my blog to using github pages.  Hopefully this will be a good
solution for me.  At a minimum it will leave me more time to actually work in
my applications.

.. _archlinux: https://www.archlinux.org/
.. _centos: http://centos.org/
.. _cgit: http://git.zx2c4.com/cgit/about/
.. _debian: https://www.debian.org/
.. _github: https://github.com
.. _gitolite: http://gitolite.com/gitolite/
.. _here: http://bytbox.net/blog/2012/08/leaving-github.html
.. _jenkins: http://jenkins-ci.org/
.. _Linus Torvalds: https://github.com/torvalds/linux/pull/17#issuecomment-5654674
.. _nginx: http://nginx.org/en/
.. _octocat: https://github.com/logos
.. _pelican: http://blog.getpelican.com/
.. _readthedocs: https://readthedocs.org/
.. _redmine: http://www.redmine.org/
.. _travis-ci: https://travis-ci.org/
.. _uwsgi: https://uwsgi-docs.readthedocs.org/en/latest/
.. _wordpress: https://wordpress.org/
