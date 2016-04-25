<!-- .slide: data-state="section-break" id="setting-up-project" data-timing="30" -->
# Setting up your project


<!-- .slide: data-background-transition="zoom" data-background-image="images/Cavalia_Big_tent.jpg" data-background-size="100%" data-timing="5" -->
# <p class="bg-light-neutral"> to Big Tent or not to Big Tent?</p>


<!-- .slide: data-state="normal" id="design-goals" data-timing="120" -->
## <a href="http://docs.openstack.org/infra/manual/creators.html#decide-status-of-your-project" target="_blank">Decide Status of your Project</a>

* Have a clear project scope
* Select the right home for your project
    -   Sub-project
    -   Speciality Team
    -   Stackforge
    -   Big Tent
* Evaluate the scope/use-case/targeted audience?
* Impact of your project on the OpenStack ecosystem
* Solving a problem is more important than making it to the Big Tent!

Note:

- Quote openstack-resource-agents and training-labs as an example of Big Tent is not the primary target.
- Requirements for a project team with PTL
- Governance repository


<!-- .slide: data-state="normal" id="tech-choice" data-timing="120" -->
## Choose the right technologies

<img src="images/choose_righttool.jpg" style="position: absolute; right: 0%; width: 40%;"></img>
<br><br><br><br>
 * Choice of programming language
 * Choice of libraries/frameworks used
 * Technical facts for the Technical Committee!

Note:

* Quote training-labs here
* Technical Committee


<!-- .slide: data-state="normal" id="prepare-existing" data-timing="60" data-menu-title="Preparing an existing repo" -->
## Preparing an existing repository

* Repo layout
* Need working CI
* [Consistent Testing Interface: Python](https://governance.openstack.org/reference/cti/python_cti.html)


<!-- .slide: data-state="normal" data-timing="60" -->
## First steps

* Follow <a href="http://docs.openstack.org/project-team-guide/index.html" target="_blank"> OpenStack Project Team Guide</a>
* Get all the reviews merged for creating your project
* Verify if things are as expected:
    * Check repository
    * Check if the review system is setup correctly
    * Check the CI system
    * Give appropriate permissions (core approvers)

Note:

- Let's focus on things that are not documented for obvious reasons


<!-- .slide: data-state="normal" data-timing="60" data-menu-title="Choosing the right name" -->
## [Choose the right name for your project](http://docs.openstack.org/infra/manual/creators.html#choosing-a-good-name-for-your-project)

<img src="images/common-sense.jpg" style="position: absolute; right: 0%; width: 45%;"></img>

* Character Set
* Small Letters
* Unique:
    * Existing OpenStack Projects
    * OpenSource projects
* Of course common sense!


<!-- .slide: data-state="normal" data-timing="60" -->
## [cookiecutting your repository](http://docs.openstack.org/infra/manual/creators.html#preparing-a-new-git-repository-using-cookiecutter)

<img src="images/cookiecuttershark.jpg" style="position: absolute; right: 0%; width: 45%;"></img>

<br><br>
* Cookie cutter cuts the boilerplate
* Good way to avoid common pitfalls
* Easy starting point with a template

<br><br><br><br><br><br><br>

###Do you really need to use the common project template?

Note:

* Ofcourse, there is a lot more to do ...
* But before you get started ...


<!-- .slide: data-state="normal" data-timing="30" -->
## Other steps

* OpenStack Infra and infra team
* IRC, ML's, Meetings, Technical Committee
* Great documentation
    * `-specs` and `-docs` repos
* branch name/release strategy
* Jenkins jobs

Note:

- Skim through this.
- This should be covered later on.
