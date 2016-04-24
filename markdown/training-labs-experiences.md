<!-- .slide: id="training-labs" data-background-transition="zoom" data-background-size="50%" data-background-image="images/openstack-fancy-image.png" -->
#Training Labs

<img data-src="images/OpenStack_logo.png" width="20%" style="position: absolute; left: 0; top: 480px" align="center"/>


<!-- .slide: data-state="normal" id="training-labs-overview" -->
## Training Labs

*   Initial blueprint was to automate VirtualBox based OpenStack deployment using Vagrant.
*   Starting as "labs" section under training-guides.
*   Eventually moved as a speciality team under Documentation Project.


<!-- .slide: data-state="normal" id="training-labs-challenges" -->
## Challenges of Training Labs

*   Very different from other OpenStack Projects:
    * Our aim is to have one click deployment system for training and Proof of Concepts
    * Minimal dependencies. (Big challenge).
* Speciality team under Documentation Project


<!-- .slide: data-state="normal" id="training-labs-challenges" -->
## Why speciality team under Documentation Project

* Working closely with install guides.
* Coming out of training-guides.
* Creating new project has a lot of overhead.
* No real benefit for added workload.
* Small team of 3 (+~2) regular contributors.
* Can take advantage of Documentation Project's resources.
* Easier to get help and guidance from the documentation team.


<!-- .slide: data-state="normal" id="training-labs-challenges" -->
## Release Cycle

* We have one major release every six months with rest of OpenStack projects.
* One minor release mid-cycle for adding new features and improving stability.


<!-- .slide: data-state="normal" id="training-labs-challenges" -->
## Training-Labs: Last six months.

* Mostly setting up the new project under Documentation team.
* Trying to figure out our sweet spot for training-labs in the OpenStack ecosystem.
* Technical Stuff:
    * Adding new features
        * Added KVM backend.
        * Refactoring code.
        * Repository boilderplate.
        * Catching up with OpenStack releases.
            * Released Liberty.
            * Released Mitaka.
        * Working with PXE support.


<!-- .slide: data-state="normal" id="training-labs-challenges" -->
## Training Labs: Future Roadmap

* Improving stability.
* Increasing flexibility of the existing system.
* Adding CentOS, openSUSE support.
* Improving visibility.
* Using it as a part of CI system.
* Moving to Python.
