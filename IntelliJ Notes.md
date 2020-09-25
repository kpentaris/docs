**Notes regarding handling of IntelliJ projects and quirks**

**Toubleshooting**

 * Jars are not properly detected in the project tree and they cannot be expanded to view contents
   
   Source A: Seems like problems with the library classpath in the Project Structure might block jar indexing (or indexing takes time?). Fixing classpath problems seemed to fix issue.
   Source B: Sometimes intellij just fails to scan the configured dependencies folder. 
   Fix: One trick seems to be removing it, letting intellij scan post-removal and then adding it back and forcing intellij to rescan them.

 * Can't find own sources.
 
   Source A: Not sure where it comes from but sometimes it follows failure to detect jar dependencies.
   Fix A: Change the project wide syntax to Java 1.3 then back to 1.8 seems to fix it. It probably triggers a re-index of the whole project.
   Fix B: If only one class fails to be detected, removing it, letting it scan and adding it again and rescanning seems to help.
