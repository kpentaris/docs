**Notes regarding handling of IntelliJ projects and quirks**

**Toubleshooting**

 * Jars are not properly detected in the project tree and they cannot be expanded to view contents
   
   Source A: Seems like problems with the library classpath in the Project Structure might block jar indexing (or indexing takes time?). Fixing classpath problems seemed to fix issue.
   Source B: Sometimes intellij just fails to scan the configured dependencies folder. 
   Fix: One trick seems to be removing it, letting intellij scan post-removal and then adding it back and forcing intellij to rescan them.

 * Can't find own sources
 
   Source A: Not sure where it comes from but sometimes it follows failure to detect jar dependencies.
   Fix A: Change the project wide syntax to Java 1.3 then back to 1.8 seems to fix it. It probably triggers a re-index of the whole project.
   Fix B: If only one class fails to be detected, removing it, letting it scan and adding it again and rescanning seems to help.

* Address already in use

   Source: Not sure why but it seems that intellij some times (maybe after pc sleep?) caches the fact that a web service is in use and improperly logs that its port is already in use when trying to redeploy. Before trying to troubleshoot this run `netstat -aob | grep <debug-port>` in the command line to check if the port is indeed in use.
   Fix A: Try to debug what exactly is cached. This usually happens when we are trying a debug deployment which can be checked by trying to deploy the application in Run mode. Additionally, if the application is successfully deployed in Run mode then IntelliJ seems to purge its cache and it can be started in Debug mode as well.
   Fix B: Invalidate caches and restart
   Fix C: Create a new server configuration

* Using IntelliJ Build engine in a Gradle project can't find other project dependencies

  Issue: The issue appears when trying to build a multimodule project using the IntelliJ Build system. What happens is that although IntelliJ properly detects dependent *modules* in the *editor* (i.e. they are not marked as compilation errors) when trying to build the project it fails to detect the dependent modules.
  Source: Not sure but it seems it is another IntelliJ caching issue.
  Fix A: Try the SDK/Language level fix.
  Fix B: Another potential issue is that the *compilation output* directory of the project does not match the directory from which the project is run from. For example, if the IntelliJ Build produces the output under *out/production/classes* but we run the project from *build/classes* then this issue appears.
  Fix C: If all directories are properly set up but the issue persists, it seems a caching issue is at work. Deleting the build directory (e.g. *build/...*) and rebuilding seems to fix the issue.
