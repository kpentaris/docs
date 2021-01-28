### Bash
#### Find filtered files and execute delete on them
`find ./ -maxdepth 10 -name "*.js.map" -delete`

#### Find processes
`ps -ef`<br>
Optionally pipe through a grep for filtering specific processes e.g. `ps -ef | grep java`

#### Terminate process
Find the process id (PID) via `ps -ef` and then run<br>
`kill <PID>`<br>
Running `kill -9 <PID>` actually instructs the OS itself to stop running the process not giving it
time to run its shutdown logic and should not be used except if it seems the process is stuck during shutdown.

### View running process under port
`netstat -aob | grep <port-number>`

### POWERSHELL
`Set the network to Private`
`Set-NetConnectionProfile -name "Unidentified network" -networkcategory private`
