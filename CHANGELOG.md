# Release 0.4.4.1
## Bug fixes:

* Fixed #8

# Release 0.4.4
## Bug fixes:

* Fixed an issue where setup would wipe your credentials.


# Release 0.4.3
## New features:
* Russian language: LiuOS is now mutilingual! (or rather biingual but that's besides the point)

Known issues: 

Command line does not factor in case sensitivity (#8)

Webget does not work with any URLs (#7) 


# Release 0.4.2
API deprecations:
* allocate_memory; only worked on Windows and was redundant as you could just create a variable

Known issues: 

Command line does not factor in case sensitivity (#8)

Webget does not work with any URLs (#7) 

Bug fixes:

`changecred` can no longer set your password to `password`.

# Release 0.4.1
No new features this minor release.

Honorable mentions:
* Merged the `generate_confirm_msg` and `elevateSession` APIs
* LiuOS API is now on version 0.1.6

Bug fixes:
* Fixed an issue where the changelog wasn't Markdown
* Fixed an issue in the changelog where the 1st bug fix for 0.4.0 wasn't descriptive

# Release 0.4.0
Several new features that I've wanted since LiuOS development started
* Elevation (like UAC but for LiuOS)
* Authentication for the `changecred` command
* Crash handler for LiuOS Apps
* Changelog for each release

Bug fixes:
* Fixed an issue where running `core.py` without running `setup.py` would cause an exception, now it tells you to run `setup.py`
* Fixed an issue where missing modules would result in an exception, instead telling you what went wrong
