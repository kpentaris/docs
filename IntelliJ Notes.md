**Notes regarding handling of IntelliJ projects and quirks**

**Toubleshooting**

* Jars are not properly detected in the project tree and they cannot be expanded to view contents

    - Source A: Seems like problems with the library classpath in the Project Structure might block jar indexing (or indexing takes time?). Fixing classpath problems seemed to fix issue.
    - Source B: Sometimes intellij just fails to scan the configured dependencies folder.
    - Fix: One trick seems to be removing it, letting intellij scan post-removal and then adding it back and forcing intellij to rescan them.

* Can't find own sources

    - Source A: Not sure where it comes from but sometimes it follows failure to detect jar dependencies.
    - Fix A: Change the project wide syntax to Java 1.3 then back to 1.8 seems to fix it. It probably triggers a re-index of the whole project.
    - Fix B: If only one class fails to be detected, removing it, letting it scan and adding it again and rescanning seems to help.

* Address already in use

    - Source: Not sure why but it seems that intellij some times (maybe after pc sleep?) caches the fact that a web service is in use and improperly logs that its port is already in use when trying to redeploy. Before trying to troubleshoot this run `netstat -aob | grep <debug-port>` in the command line to check if the port is indeed in use.
    - Fix A: Try to debug what exactly is cached. This usually happens when we are trying a debug deployment which can be checked by trying to deploy the application in Run mode. Additionally, if the application is successfully deployed in Run mode then IntelliJ seems to purge its cache and it can be started in Debug mode as well.
    - Fix B: Invalidate caches and restart
    - Fix C: Create a new server configuration
###Gradle
**When using Gradle with IntelliJ always remember to set the Gradle tool to the one you have installed on the machine. The options is under Settings > Build Tools > Gradle**

* Using IntelliJ Build engine in a Gradle project can't find other project dependencies

    - Issue: The issue appears when trying to build a multimodule project using the IntelliJ Build system. What happens is that although IntelliJ properly detects dependent *modules* in the *editor* (i.e. they are not marked as compilation errors) when trying to build the project it fails to detect the dependent modules.
    - Source: Not sure but it seems it is another IntelliJ caching issue.
    - Fix A: Try the SDK/Language level fix.
    - Fix B: Another potential issue is that the *compilation output* directory of the project does not match the directory from which the project is run from. For example, if the IntelliJ Build produces the output under *out/production/classes* but we run the project from *build/classes* due to the Gradle script then this issue appears. The *same* compiled directory structure must be used for *all* dependent projects as well! A dependency's compiled files can't be under *out/production/classes* while the main project is under *build/classes* for example.
    - Fix C: If all directories are properly set up but the issue persists, it seems a caching issue is at work. Deleting the build directory (e.g. *build/...*) and rebuilding seems to fix the issue.
    - Fix D: Revert the compilation output to *out/production* or whatever the default is and issue an IntelliJ Build System compilation of the module (e.g. server.main). If done properly then IntelliJ should compile the whole module under *out/production/server*. Revert back to the *build/classes* output directory from within the Gradle script and this seems to reset the behavior, even if the *out* directory is deleted afterwards.

* Using IntelliJ Build engine with a Gradle project and IntelliJ deployment

    - Goal: Using a Gradle based project but with the IntelliJ build system for recompiling updated class files and combining the Gradle and IntelliJ-Build results in order to deploy them with the IntelliJ deployment system.
    - How to: The IntelliJ deployment system works best if an Artifact is provided for deployment. If a webapp directory is given for deployment then IntelliJ won't provide hot reload functionality. This means that an Artifact must be defined. The easiest way to do this is to define an empty artifact (i.e. we provide no output to it) but its *output* directory should be the webapp directory that gradle generates when creating an explodedWar. With this we can have gradle generate the exploded war and still deploy it with the IntelliJ system by deploying the artifact that points there.
    - Hot reload: In order to properly do hot reload with the IntelliJ build system the compilation output of classes must be the explodedWar/WEB-INF/classes directory (since this is the directory that the deployment system listens to for changes in order to issue a hot reload). In order to set the output path there we must go through the Gradle script, *not* the IntelliJ project setup because it is overridden by the gradle script. The **idea** plugin must be used and the following configuration must be provided:
      ```
      idea {
         module {
           inheritOutputDirs = false
           outputDir = file(explodedWarWebDir + "/WEB-INF/classes")
         }
       }
       ```
        By providing the `outputDir` directly, we change the *compile output path* which is under Project Structure > Modules > <module-name> > main. This means that a recompilation command like Ctrl + Shift + F9 will recompile the class and the .class file will be saved under the exploded war classes directory, ready for deployment.
