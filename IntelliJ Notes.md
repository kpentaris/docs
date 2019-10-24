**Notes regarding handling of IntelliJ projects and quirks**

**Toubleshooting**

 * Jars are not properly detected in the project tree and they cannot be expanded to view contents
   
   Source: Seems like problems with the library classpath in the Project Structure might block jar indexing (or indexing takes time?). Fixing classpath problems seemed to fix issue.
