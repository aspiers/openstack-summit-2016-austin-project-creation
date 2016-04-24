<!-- .slide: data-state="section-break" id="setting-up-project" -->
# Setting up your project


<!-- .slide: data-background-transition="zoom" data-background-image="images/Cavalia_Big_tent.jpg" data-background-size="100%" -->
# <p class="bg-light-neutral"> to Big Tent or not to Big Tent?</p>


<!-- .slide: data-state="normal" id="design-goals" -->
## [Decide Status of your Project](http://docs.openstack.org/infra/manual/creators.html#decide-status-of-your-project)

* Be clear about scope of project
* Project may be better off as a sub-project/speciality team
    * Identify the right place for your project
* How important is it to be in big tent?
    * Depends on your project.
        * What is the scope/use-case/targeted audience?
        * More ...
* Requirements for a project team with PTL
* Quote openstack-resource-agents and training-labs as an example of Big Tent is not the primary target.
* Governance Repository
* Tags
    * Release cycles ... more


<!-- .slide: data-state="normal" id="tech-choice" -->
## Choose the right technologies

 *    Choice of programming language
 *    Choice of libraries/frameworks used (quote training-labs here)
 *    How this impacts whether a project will be approved (TC)


<!-- .slide: data-state="normal" -->
## First steps

* Follow <a href="http://docs.openstack.org/project-team-guide/index.html" target="_blank"> OpenStack Project Team Guide</a>
* Get all the reviews merged for creating your project.
* Verify if things are as expected:
    * Check repository.
    * Check if the review system is setup correctly.
    * Check the CI system.
    * Give appropriate permissions (core approvers).

Note:
Let's focus on things that are not documented for obvious reasons.


<!-- .slide: data-state="normal" -->
## [Choose the right name for your project](http://docs.openstack.org/infra/manual/creators.html#choosing-a-good-name-for-your-project)


<!-- .slide: data-state="normal" -->
## [Preparing a New Git Repository using cookiecutter](http://docs.openstack.org/infra/manual/creators.html#preparing-a-new-git-repository-using-cookiecutter)


<!-- .slide: data-state="normal" -->
# Other steps

* OpenStack Infra and infra team
* IRC, ML's, Meetings, Technical Committee
* Mention great documentation
* -specs and -docs repos
* branch name/release strategy
* Jenkins jobs
    * building tarballs
    * https://github.com/openstack/gerrit-dash-creator
* Focus on unique properties of our projects and show the differences from standard openstack python based projects.
