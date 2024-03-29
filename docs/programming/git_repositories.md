---
layout: default
title: Git Repositories
---
Git Repositories
================

We strongly recommend that you develop your code within the IDE.  However, we appreciate that this can be limiting for some users.  Therefore, we provide access to the git repositories that the IDE stores your code in.  You can access your git repository by pointing your git client at a URL of the form:

<pre class="not-code">
https://USERNAME@www.studentrobotics.org/robogit/TEAMTLA/PROJNAME.git
</pre>

Replace:

 * `USERNAME` with your Student Robotics username.
 * `TEAMTLA` with the TLA of your team.  (You can find this out by logging into the IDE and looking at the team id displayed at the top)
 * `PROJNAME` with the name of the project that you've already created within the IDE.

When you clone the repository, your client will prompt you for your Student Robotics password.  When you've done some things, go ahead and push your commits back into the repository.  To get your code onto your robot, you will need to use the IDE's export feature as usual.

Example
-------

If dave from team SRZ has a project called "armadillo", then one of their team members might clone it like so:

<pre class="not-code">
git clone https://dave@www.studentrobotics.org/robogit/SRZ/armadillo.git
</pre>

*[TLA]: Three Letter Acronym
